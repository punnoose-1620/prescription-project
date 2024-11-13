import csv
import json
import pickle
import random
from tqdm import tqdm
from datetime import datetime

condition_map = ['none', 'addict', 'tolerance', 'ph_dependence', 'ps_dependence', 'abuse', 'misuse', 'od', 'rebound', 'poly_drug', 'illicit_use', 'self_medication', 'impaired', 'wd_cycle', 'relapse']
prescription_classes = []
prescription_classes_file = "prescription_classes.pkl"
medicine_types = []
medicine_types_file = "medicine_types.pkl"
medicine_names = []
medicine_names_file = "medicine_names.pkl"
json_file_path = "medical_data_250000.json"

def insert_commas_to_number(num):
    rev_num = ''
    count = 0
    for digit in str(num)[::-1]:
        rev_num = rev_num + digit
        count = count+1
        if count%3==0:
            rev_num = rev_num+','
    ori_num = rev_num[::-1]
    if(len(ori_num)==1):
        ori_num = '0' + ori_num
    if rev_num[-1]==',':
        return ori_num[1:]
    return ori_num

def print_list(list_of_items, title):
    print(title,' (', insert_commas_to_number(len(list_of_items)),') : ')
    for item in list_of_items:
        index = list_of_items.index(item)+1
        if index<10:
            print(index,'. ', item)
        else:
            print(index,'. ', item)

def get_item_names(entry, key):
    if key=='prescription_name':
        item = str(entry[key])
        if item not in medicine_names:
            medicine_names.append(item)
    else:
        class_list = list(entry[key])
        for item in class_list:
            if (key=='medicine_type'):
                if item not in medicine_types:
                    medicine_types.append(item)
            else:
                if item not in prescription_classes:
                    prescription_classes.append(item)

def write_list_to_pickle(data_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data_list, file)
    print(f"List written to {filename} successfully.")

def read_list_from_pickle(filename):
    with open(filename, 'rb') as file:
        data_list = pickle.load(file)
    return data_list

def add_type_flags(entry, key, comparator):
    types_list = list(entry[key])
    for item in comparator:
        if item in types_list:
            entry[item] = 1
        else:
            entry[item] = 0
    del entry[key]
    return entry

def calculate_BMI(entry):
    weight = float(entry['user_weight'])
    height = float(entry['user_height'])
    bmi = height/weight
    entry['user_bmi'] = bmi
    del entry['user_height']
    del entry['user_weight']
    return entry

def calculate_usage(entry):
    prescriptions_fillings = list(entry['prescription_collections'])
    last_refill = str(datetime.now().date())
    previous_refill = str(datetime.now().date())
    before_refill = str(datetime.now().date())
    amount = 0
    prev_amount = 0
    if len(prescriptions_fillings)>=1:
        last_refill = str(prescriptions_fillings[-1]['date'])
        amount = prescriptions_fillings[-1]['quantity']
        if len(prescriptions_fillings)>1:
            previous_refill = str(prescriptions_fillings[-2]['date'])
            prev_amount = prescriptions_fillings[-2]['quantity']
        if len(prescriptions_fillings)>2:
            before_refill = str(prescriptions_fillings[-3]['date'])

    date_format = "%Y-%m-%d"
    # Parse the given date string into a datetime object
    old_date = datetime.strptime(before_refill, date_format)

    # Parse the given date string into a datetime object
    given_date = datetime.strptime(previous_refill, date_format)
    
    # Get today's date
    today = datetime.strptime(last_refill, date_format)
    
    # Calculate the difference in days
    difference = today - given_date
    count_for_days = difference.days
    usage = 0
    if count_for_days>0:
        usage = amount/count_for_days
        
    entry['daily_usage'] = usage

    # Calculate difference in days for previous usage
    old_difference = given_date-old_date
    old_count_for__days = old_difference.days
    old_usage = 0
    if old_count_for__days>0:
        usage = prev_amount/old_count_for__days

    entry['prev_daily_usage'] = usage
    del entry['prescription_collections']

    return entry

def convert_str_to_dt_to_epoch(cur_date):
    date_format = "%Y-%m-%d"
    split_date_space = str(cur_date).split(' ')
    split_date_t = str(cur_date).split('T')
    if len(split_date_space)>1:
        cur_date = split_date_space[0]
    if(len(split_date_t)>1):
        cur_date = split_date_t[0]
    dt = datetime.strptime(str(cur_date), date_format)
    return int(dt.timestamp())

def open_and_process_file(file_path, type='other'):
    try:
        # Open the JSON file
        with open(file_path, 'r') as file:
            # Load the data
            data = json.load(file)

            # from graph_plotter import plot_sunburst
            # plot_sunburst(data,"Initial Sunburst.png")

            progress_title = "Pre-Processing Data"
            if type=='self':
                progress_title = 'Converting to new Data'

            for entry in tqdm(data, desc="Logging unique entry types...."):
                # First note all existing prescription classes and type classes and write them to pickle files for later reference
                get_item_names(entry, 'prescription_classes')
                entry['medicine_type'] = [entry['medicine_type']]
                get_item_names(entry, 'medicine_type')
                get_item_names(entry, 'prescription_name')
            if type=='self':
                print_list(prescription_classes, 'Prescriptions')
                print_list(medicine_types, 'Medicine Types')
                print_list(medicine_names, 'Medicine Names')
            write_list_to_pickle(prescription_classes, prescription_classes_file)
            write_list_to_pickle(prescription_classes, medicine_types_file)
            write_list_to_pickle(medicine_names, medicine_names_file)
            
            # Print the parsed data
            print("Begin Data Processing....\n")
            for entry in tqdm(data, desc=progress_title):                
                # Add User Id only for internal function calls
                if type=='self':
                    entry['user_id'] = entry['user_id']
                else:
                    del entry['user_id']
                
                if type=='self':
                    entry['user_weight'] = entry['user_weight']
                    entry['user_height'] = entry['user_height']
                else:
                    entry = calculate_BMI(entry)
                
                # Convert medicine names to numeric equivalents
                if type!='self':
                    name = str(entry['prescription_name']).strip()
                    if name not in medicine_names:
                        medicine_names.append(name)
                    entry['prescription_name'] = int(medicine_names.index(name))
                else:
                    entry['prescription_name'] = entry['prescription_name']

                # Convert prescription date into epoch time
                if type!='self':
                    entry['prescription_date'] = convert_str_to_dt_to_epoch(str(entry['prescription_date']))
                else:
                    entry['prescription_date'] = entry['prescription_date']

                entry['prescribed_daily_dose'] = entry['prescribed_daily_dose']

                # Remove Risk factor from data prepared for model
                if(type=='self'):
                    entry['risk_factor'] = entry['risk_factor']
                else:
                    del entry['risk_factor']

                entry['risk_dosage'] = entry['risk_dosage']
                entry['maximum_daily_dosage'] = entry['maximum_daily_dosage']

                # Calculate average usage since last prescription
                entry = calculate_usage(entry)
                
                # Replace risk condition with numbers
                if type!='self':
                    entry['risk_condition'] = condition_map.index(str(entry['risk_condition']))
                else:
                    entry['risk_condition'] = str(entry['risk_condition'])

                # Add flags based on prescription classes
                if type=='self':
                    entry = add_type_flags(entry, 'prescription_classes', prescription_classes)
                else:
                    class_names = list(entry['prescription_classes'])
                    sum = 0
                    for item in class_names:
                        if item not in prescription_classes:
                            prescription_classes.append(item)
                        sum = sum + prescription_classes.index(item)
                    entry['prescription_class_sum'] = sum
                    del entry['prescription_classes']

                # Add flags based on medicine types
                if type=='self':
                    entry = add_type_flags(entry, 'medicine_type', medicine_types)
                else:
                    class_names = list(entry['medicine_type'])
                    sum = 0
                    for item in class_names:
                        if item not in medicine_types:
                            medicine_types.append(item)
                        sum = sum + medicine_types.index(item)
                    entry['medicine_types_sum'] = sum
                    del entry['medicine_type']

                # Convert last consultation into epoch time
                if type!='self':
                    entry['last_consultation'] = convert_str_to_dt_to_epoch(entry['last_consultation'])
                else:
                    entry['last_consultation'] = entry['last_consultation']

                if type=='self':
                    entry['med_details_url'] = entry['med_details_url']
                else:
                    del entry['med_details_url']

                # entry = new_entry

            print("\nData Processing Completed....")
            # Shuffle the processed data to avoid order based bias
            random.shuffle(data)
            print("Data Shuffling Complete....\n")
            if type!='self':
                keys_to_remove = ['prescription_date']
                for entry in data:
                    for key in keys_to_remove:
                        del entry[key]
                data = normalize_0_to_10(data)
                print("Sample Data keys : ", list(data[0].keys()))

            return data

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {file_path}.")

def write_to_csv(data, filename):
    headers = data[0].keys()
    print_list(list(headers), 'Headers to CSV')
    print("Content size : ",insert_commas_to_number(len(data)))
    flag = True
    for item in data : 
        new_h = item.keys()
        for key in new_h:
            if key not in headers:
                item[key] = False
                # headers.append(key)
                # print('Updated header count : ',insert_commas_to_number(len(headers)))
                flag = False
                # print(key, 'not in ', headers)

    if flag:
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()  # Write the header
            writer.writerows(data) # Write the data

def get_list_of_vals_from_json(filename, key):
    try:
        # Open the JSON file
        with open(filename, 'r') as file:
            # Load the data
            data = json.load(file)
            values = []
            for entry in data:
                value = entry[key]
                if isinstance(value, list):
                    for item in value:
                        values.append(item)
                else:
                    values.append(str(value))
            return values

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")

def get_item_type_from_json(filename, key1, key2):
    try:
        # Open the JSON file
        with open(filename, 'r') as file:
            # Load the data
            data = json.load(file)
            items = []
            types = []
            for entry in data:
                value = entry[key1]
                type_of_value = entry[key2]
                items.append(str(value))
                types.append(str(type_of_value))
            return items,types

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")

def get_daily_usage_stats_for_param(filename, key):
    try:
        # Open the JSON file
        with open(filename, 'r') as file:
            # Load the data
            data = json.load(file)
            items = []
            types = []
            for entry in data:
                entry = calculate_usage(entry)
                value = entry[key]
                type_of_value = entry['daily_usage']
                items.append(str(value))
                types.append(str(type_of_value))
            return items,types

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file {filename}.")

def normalize_0_to_10(entries):
    maxes = {}
    mins = {}
    keys = list(entries[0].keys())
    # keys.remove('risk_condition')
    #Find the max and min value for each key
    for entry in entries:
        for key in keys:
            max_keys = maxes.keys()
            min_keys = mins.keys()
            if key not in max_keys:
                maxes[key] = 0
            elif float(maxes[key])<float(entry[key]):
                maxes[key] = entry[key]
            if key not in min_keys:
                mins[key] = 200
            elif float(mins[key])>float(entry[key]):
                mins[key] = entry[key]
    # min-max normalize each value
    for entry in tqdm(entries, desc="Normalizing data...."):
        for key in keys:
            numerator = maxes[key] - float(entry[key])
            denominator = maxes[key] - mins[key]
            entry[key] = numerator * 10 / denominator
    # Print min and max for each value
    for key in keys:
        print("Range of ",key," : (",mins[key],",",maxes[key],")")
    return entries

def read_data_from_csv(key, filename):
    values = []
    with open(filename, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        # Iterate over each row in the CSV
        for row in csv_reader:
            if 'user_weights' in row:
                values.append(float(row['user_weights']))  # Convert to float, if needed

# Example usage:
# jsondata = open_and_process_file(json_file_path,'self')
# write_to_csv(jsondata, 'medical_data_250000.csv')
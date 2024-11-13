import pickle
import pandas as pd
from pre_processor import *
from model_creations import *
from graph_plotter import *
from sklearn.model_selection import train_test_split

def correct_inputs(key, value):
    if key=='prescription_name':
        if value not in medicine_names:
            medicine_names.append(value)
        value = int(medicine_names.index(str(value)))
    elif key=='prescription_date':
        value = convert_str_to_dt_to_epoch(str(value))
    print("Input Corrected. New value : ",value)

def check_inputs(data):
    for entry in tqdm(data, desc="Checking Data for Anomalies"):
        for key in entry.keys():
            value = entry[key]
            if str(value).strip().lower()=='null':
                del entry
                break
            if not isinstance(value, (int, float)):
                print('Nan value found. Key (',key,'), Value (',value,')')
                entry[key] = correct_inputs(key, value)

def get_x_data(data, type='Training'):
    values = []
    for entry in tqdm(data, desc='Getting X Data for '+type):
        item = {}
        for key in entry.keys():
            if(key!='risk_condition'):
                try:
                    item[key] = float(str(entry[key]))
                except ValueError or TypeError:
                    print('Index Check : ', data.index(entry))
                    print("Exception Value : ", json.dumps(entry),'\n')
        values.append(item)
    return values

def get_y_data(data, type='Training'):
    values = []
    for entry in tqdm(data, desc='Getting Y Data for '+type):
        values.append(int(entry['risk_condition']))
    return values

def save_model(fileName, model):
    with open('./saved_models/'+fileName+'.pkl', 'wb') as file:
        pickle.dump(model, file)

processed_data = open_and_process_file(json_file_path)
check_inputs(processed_data)

# plot_connection_graphs()

# print("Sample Entry : ",json.dumps(processed_data[0], indent=4))
print("Data Count after processing : ",insert_commas_to_number(len(processed_data)),'\n')

# Assuming processed_data is a list of dictionaries from your JSON
train_data, test_data = train_test_split(processed_data, test_size=0.3, random_state=42)

# Split the training data into X_train and y_train
X_train = pd.DataFrame(get_x_data(train_data, 'Training'))
y_train = pd.DataFrame(get_y_data(train_data, 'Training'))
print('\n')

# Split the testing data into X_test and y_test
X_test = get_x_data(test_data, 'Testing')
y_test = get_y_data(test_data, 'Testing')

X_test_pd = pd.DataFrame(X_test)
y_test_pd = pd.DataFrame(y_test)

print("\nTrain count : (",len(X_train),' : ',len(y_train),')')
print("Test count : (",len(X_test),' : ',len(y_test),')')

input_param_size = len(X_test[0].keys())

logistic_regression_model, lt_accuracy = logistic_regression(X_train, X_test_pd, y_train, y_test_pd)
save_model('logistic_regression_model', logistic_regression_model)
print("\nAccuracy of Logistic Model : ",lt_accuracy*100,'\n')

decision_tree_model, dt_accuracy = decision_tree(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
save_model('decision_tree_model', decision_tree_model)
print("\nAccuracy of Decision Tree Model : ",dt_accuracy*100,'\n')

random_forest_model, rf_accuracy = random_forest(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
save_model('random_forest_model', random_forest_model)
print("\nAccuracy of Random Forest Model : ",rf_accuracy*100,'\n')

gradient_boosting_model, gb_accuracy = gradient_boosting(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
save_model('gradient_boosting_model', gradient_boosting_model)
print("\nAccuracy of Gradient Boosting Model : ",gb_accuracy*100,'\n')

# support_vector_machine_model, svm_accuracy = support_vector_machine(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
# save_model('svm_model', support_vector_machine_model)
# print("\nAccuracy of Support Vector Machine Model : ",svm_accuracy*100,'\n')

neural_network_model, nn_accuracy = neural_network(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
save_model('neural_network_model', neural_network_model)
print("\nAccuracy of Neural Network Model : ",nn_accuracy*100,'\n')

xg_boost_model, xgb_accuracy = xgboost_classifier(X_train, X_test_pd, y_train, y_test_pd, input_param_size)
save_model('xg_boost_model', xg_boost_model)
print("\nAccuracy of XG Boost Model : ",xgb_accuracy*100,'\n')
import json
import random
from datetime import datetime, timedelta

# Function to generate random prescription data
def generate_prescriptions(num_entries):
    medicines = [
    {"name": "Amoxicillin", "type": "tablet", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 90, "max_dose_per_kg_per_day": 4000},
    {"name": "Ibuprofen", "type": "tablet", "classes": ["NSAID"], "risk_factor": 15, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 1200},
    {"name": "Citalopram", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 40, "max_dose_per_kg_per_day": 60},
    {"name": "Metformin", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 200, "max_dose_per_kg_per_day": 3000},
    {"name": "Insulin", "type": "injection", "classes": ["hormone"], "risk_factor": 25, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 200},
    {"name": "Atorvastatin", "type": "tablet", "classes": ["lipid-lowering agent"], "risk_factor": 15, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 80},
    {"name": "Lisinopril", "type": "tablet", "classes": ["antihypertensive"], "risk_factor": 10, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 80},
    {"name": "Amlodipine", "type": "tablet", "classes": ["antihypertensive"], "risk_factor": 10, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 10},
    {"name": "Sertraline", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 200},
    {"name": "Gabapentin", "type": "capsule", "classes": ["anticonvulsant"], "risk_factor": 15, "risk_dose_per_kg_per_day": 20, "max_dose_per_kg_per_day": 3600},
    {"name": "Omeprazole", "type": "tablet", "classes": ["PPI"], "risk_factor": 5, "risk_dose_per_kg_per_day": 40, "max_dose_per_kg_per_day": 120},
    {"name": "Furosemide", "type": "tablet", "classes": ["diuretic"], "risk_factor": 20, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 200},
    {"name": "Warfarin", "type": "tablet", "classes": ["anticoagulant"], "risk_factor": 30, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 10},
    {"name": "Alprazolam", "type": "tablet", "classes": ["benzodiazepine"], "risk_factor": 40, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 4},
    {"name": "Clonazepam", "type": "tablet", "classes": ["benzodiazepine"], "risk_factor": 35, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 20},
    {"name": "Fluoxetine", "type": "capsule", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 30, "max_dose_per_kg_per_day": 80},
    {"name": "Simvastatin", "type": "tablet", "classes": ["lipid-lowering agent"], "risk_factor": 10, "risk_dose_per_kg_per_day": 20, "max_dose_per_kg_per_day": 80},
    {"name": "Ciprofloxacin", "type": "tablet", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 20, "max_dose_per_kg_per_day": 1500},
    {"name": "Dexamethasone", "type": "tablet", "classes": ["corticosteroid"], "risk_factor": 25, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 30},
    {"name": "Levothyroxine", "type": "tablet", "classes": ["thyroid hormone"], "risk_factor": 5, "risk_dose_per_kg_per_day": 1.6, "max_dose_per_kg_per_day": 0.3},
    {"name": "Tamsulosin", "type": "capsule", "classes": ["alpha blocker"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.4, "max_dose_per_kg_per_day": 0.8},
    {"name": "Lansoprazole", "type": "capsule", "classes": ["PPI"], "risk_factor": 5, "risk_dose_per_kg_per_day": 30, "max_dose_per_kg_per_day": 120},
    {"name": "Montelukast", "type": "tablet", "classes": ["leukotriene receptor antagonist"], "risk_factor": 5, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 10},
    {"name": "Cetirizine", "type": "tablet", "classes": ["antihistamine"], "risk_factor": 5, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 20},
    {"name": "Azithromycin", "type": "tablet", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 500},
    {"name": "Ranitidine", "type": "tablet", "classes": ["H2 antagonist"], "risk_factor": 5, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 300},
    {"name": "Sildenafil", "type": "tablet", "classes": ["erectile dysfunction"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 0.5},
    {"name": "Bupropion", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 15, "risk_dose_per_kg_per_day": 75, "max_dose_per_kg_per_day": 400},
    {"name": "Tramadol", "type": "tablet", "classes": ["opioid analgesic"], "risk_factor": 40, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 400},
    {"name": "Mirtazapine", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 30, "max_dose_per_kg_per_day": 45},
    {"name": "Hydrochlorothiazide", "type": "tablet", "classes": ["diuretic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 50},
    {"name": "Nitroglycerin", "type": "sublingual tablet", "classes": ["vasodilator"], "risk_factor": 15, "risk_dose_per_kg_per_day": 0.3, "max_dose_per_kg_per_day": 1.2},
    {"name": "Prednisone", "type": "tablet", "classes": ["corticosteroid"], "risk_factor": 25, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 60},
    {"name": "Clopidogrel", "type": "tablet", "classes": ["antiplatelet"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 10},
    {"name": "Fentanyl", "type": "patch", "classes": ["opioid analgesic"], "risk_factor": 50, "risk_dose_per_kg_per_day": 0.05, "max_dose_per_kg_per_day": 0.1},
    {"name": "Risperidone", "type": "tablet", "classes": ["antipsychotic"], "risk_factor": 30, "risk_dose_per_kg_per_day": 0.02, "max_dose_per_kg_per_day": 6},
    {"name": "Quetiapine", "type": "tablet", "classes": ["antipsychotic"], "risk_factor": 25, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 800},
    {"name": "Oxycodone", "type": "tablet", "classes": ["opioid analgesic"], "risk_factor": 50, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 80},
    {"name": "Candesartan", "type": "tablet", "classes": ["antihypertensive"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.2, "max_dose_per_kg_per_day": 32},
    {"name": "Labetalol", "type": "tablet", "classes": ["antihypertensive"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.3, "max_dose_per_kg_per_day": 1200},
    {"name": "Venlafaxine", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 75, "max_dose_per_kg_per_day": 375},
    {"name": "Duloxetine", "type": "capsule", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 60, "max_dose_per_kg_per_day": 120},
    {"name": "Topiramate", "type": "tablet", "classes": ["anticonvulsant"], "risk_factor": 15, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 400},
    {"name": "Lithium", "type": "tablet", "classes": ["mood stabilizer"], "risk_factor": 25, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 2.5},
    {"name": "Nitrofurantoin", "type": "capsule", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 7, "max_dose_per_kg_per_day": 600},
    {"name": "Spironolactone", "type": "tablet", "classes": ["diuretic"], "risk_factor": 15, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 400},
    {"name": "Valproate", "type": "tablet", "classes": ["anticonvulsant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 20, "max_dose_per_kg_per_day": 60},
    {"name": "Buspirone", "type": "tablet", "classes": ["anxiolytic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 60, "max_dose_per_kg_per_day": 120},
    {"name": "Dapagliflozin", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 100},
    {"name": "Glimepiride", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 3, "max_dose_per_kg_per_day": 8},
    {"name": "Canagliflozin", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 300},
    {"name": "Pregabalin", "type": "capsule", "classes": ["anticonvulsant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 600},
    {"name": "Methotrexate", "type": "tablet", "classes": ["antimetabolite"], "risk_factor": 30, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 25},
    {"name": "Esomeprazole", "type": "tablet", "classes": ["PPI"], "risk_factor": 5, "risk_dose_per_kg_per_day": 30, "max_dose_per_kg_per_day": 120},
    {"name": "Rivastigmine", "type": "capsule", "classes": ["cholinesterase inhibitor"], "risk_factor": 15, "risk_dose_per_kg_per_day": 3, "max_dose_per_kg_per_day": 12},
    {"name": "Moxifloxacin", "type": "tablet", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 400},
    {"name": "Codeine", "type": "tablet", "classes": ["opioid analgesic"], "risk_factor": 40, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 360},
    {"name": "Trazodone", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 100, "max_dose_per_kg_per_day": 600},
    {"name": "Sodium Valproate", "type": "tablet", "classes": ["anticonvulsant"], "risk_factor": 25, "risk_dose_per_kg_per_day": 20, "max_dose_per_kg_per_day": 60},
    {"name": "Bromhexine", "type": "tablet", "classes": ["mucolytic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 36},
    {"name": "Budesonide", "type": "inhaler", "classes": ["corticosteroid"], "risk_factor": 15, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 800},
    {"name": "Fluticasone", "type": "inhaler", "classes": ["corticosteroid"], "risk_factor": 15, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 400},
    {"name": "Aspirin", "type": "tablet", "classes": ["NSAID"], "risk_factor": 10, "risk_dose_per_kg_per_day": 10, "max_dose_per_kg_per_day": 4000},
    {"name": "Corticosteroid", "type": "tablet", "classes": ["corticosteroid"], "risk_factor": 30, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 60},
    {"name": "Cholecalciferol", "type": "tablet", "classes": ["vitamin D"], "risk_factor": 5, "risk_dose_per_kg_per_day": 400, "max_dose_per_kg_per_day": 10000},
    {"name": "Folic Acid", "type": "tablet", "classes": ["vitamin"], "risk_factor": 5, "risk_dose_per_kg_per_day": 0.4, "max_dose_per_kg_per_day": 5},
    {"name": "Naproxen", "type": "tablet", "classes": ["NSAID"], "risk_factor": 15, "risk_dose_per_kg_per_day": 15, "max_dose_per_kg_per_day": 1000},
    {"name": "Dexamethasone", "type": "injection", "classes": ["corticosteroid"], "risk_factor": 25, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 30},
    {"name": "Cefalexin", "type": "capsule", "classes": ["antibiotic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 4000},
    {"name": "Varenicline", "type": "tablet", "classes": ["smoking cessation"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 2},
    {"name": "Sitagliptin", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 100, "max_dose_per_kg_per_day": 100},
    {"name": "Duloxetine", "type": "capsule", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 60, "max_dose_per_kg_per_day": 120},
    {"name": "Rizatriptan", "type": "tablet", "classes": ["migraine medication"], "risk_factor": 15, "risk_dose_per_kg_per_day": 0.2, "max_dose_per_kg_per_day": 5},
    {"name": "Topiramate", "type": "tablet", "classes": ["anticonvulsant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 400},
    {"name": "Tamsulosin", "type": "capsule", "classes": ["alpha blocker"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.4, "max_dose_per_kg_per_day": 0.8},
    {"name": "Montelukast", "type": "tablet", "classes": ["leukotriene receptor antagonist"], "risk_factor": 5, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 10},
    {"name": "Ropinirole", "type": "tablet", "classes": ["dopamine agonist"], "risk_factor": 15, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 24},
    {"name": "Baclofen", "type": "tablet", "classes": ["muscle relaxant"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 80},
    {"name": "Finasteride", "type": "tablet", "classes": ["5-alpha reductase inhibitor"], "risk_factor": 5, "risk_dose_per_kg_per_day": 1, "max_dose_per_kg_per_day": 5},
    {"name": "Cimetidine", "type": "tablet", "classes": ["H2 antagonist"], "risk_factor": 10, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 1600},
    {"name": "Metoclopramide", "type": "tablet", "classes": ["antiemetic"], "risk_factor": 15, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 30},
    {"name": "Fentanyl", "type": "injection", "classes": ["opioid analgesic"], "risk_factor": 50, "risk_dose_per_kg_per_day": 0.01, "max_dose_per_kg_per_day": 0.1},
    {"name": "Atenolol", "type": "tablet", "classes": ["beta blocker"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 100},
    {"name": "Clozapine", "type": "tablet", "classes": ["antipsychotic"], "risk_factor": 30, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 900},
    {"name": "Oxcarbazepine", "type": "tablet", "classes": ["anticonvulsant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 30, "max_dose_per_kg_per_day": 2400},
    {"name": "Levocetirizine", "type": "tablet", "classes": ["antihistamine"], "risk_factor": 5, "risk_dose_per_kg_per_day": 5, "max_dose_per_kg_per_day": 10},
    {"name": "Epinephrine", "type": "injection", "classes": ["adrenergic agonist"], "risk_factor": 25, "risk_dose_per_kg_per_day": 0.01, "max_dose_per_kg_per_day": 0.5},
    {"name": "Dexamethasone", "type": "inhaler", "classes": ["corticosteroid"], "risk_factor": 25, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 1.2},
    {"name": "Sumatriptan", "type": "tablet", "classes": ["migraine medication"], "risk_factor": 15, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 200},
    {"name": "Pramipexole", "type": "tablet", "classes": ["dopamine agonist"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.25, "max_dose_per_kg_per_day": 4.5},
    {"name": "Verapamil", "type": "tablet", "classes": ["calcium channel blocker"], "risk_factor": 15, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 480},
    {"name": "Olmesartan", "type": "tablet", "classes": ["antihypertensive"], "risk_factor": 10, "risk_dose_per_kg_per_day": 0.4, "max_dose_per_kg_per_day": 40},
    {"name": "Tizanidine", "type": "tablet", "classes": ["muscle relaxant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 36},
    {"name": "Desvenlafaxine", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 400},
    {"name": "Sodium Bicarbonate", "type": "tablet", "classes": ["alkalinizing agent"], "risk_factor": 5, "risk_dose_per_kg_per_day": 15, "max_dose_per_kg_per_day": 600},
    {"name": "Chlorpheniramine", "type": "tablet", "classes": ["antihistamine"], "risk_factor": 5, "risk_dose_per_kg_per_day": 4, "max_dose_per_kg_per_day": 24},
    {"name": "Imipramine", "type": "tablet", "classes": ["antidepressant"], "risk_factor": 20, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 300},
    {"name": "Zolpidem", "type": "tablet", "classes": ["sedative"], "risk_factor": 35, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 10},
    {"name": "Diazepam", "type": "tablet", "classes": ["benzodiazepine"], "risk_factor": 40, "risk_dose_per_kg_per_day": 0.1, "max_dose_per_kg_per_day": 60},
    {"name": "Glyburide", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 3, "max_dose_per_kg_per_day": 20},
    {"name": "Acarbose", "type": "tablet", "classes": ["antidiabetic"], "risk_factor": 5, "risk_dose_per_kg_per_day": 50, "max_dose_per_kg_per_day": 300},
    {"name": "Fentanyl", "type": "sublingual tablet", "classes": ["opioid analgesic"], "risk_factor": 50, "risk_dose_per_kg_per_day": 0.01, "max_dose_per_kg_per_day": 0.1},
    {"name": "Tolterodine", "type": "tablet", "classes": ["anticholinergic"], "risk_factor": 10, "risk_dose_per_kg_per_day": 2, "max_dose_per_kg_per_day": 4},
    {"name": "Prasugrel", "type": "tablet", "classes": ["antiplatelet"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 10},
    {"name": "Ticagrelor", "type": "tablet", "classes": ["antiplatelet"], "risk_factor": 20, "risk_dose_per_kg_per_day": 0.5, "max_dose_per_kg_per_day": 90}
  ]
    
    prescriptions = []
    
    for user_id in range(1, num_entries + 1):
        medicine = random.choice(medicines)
        prescription_date = datetime.now() - timedelta(days=random.randint(1, 365))
        collection_dates = []
        
        for _ in range(random.randint(1, 5)):
            collection_dates.append({
                "date": (prescription_date + timedelta(days=random.randint(5, 30))).strftime('%Y-%m-%d'),
                "quantity": random.randint(15, 90)
            })
        
        random_weight = random.randint(40, 100)
        prescription = {
            "user_id": user_id,
            "user_weight": random_weight,
            "user_height": random.randint(150, 200),
            "prescription_name": medicine["name"],
            "prescription_date": prescription_date.strftime('%Y-%m-%d'),
            "prescribed_daily_dose": random.uniform(0.001, medicine['risk_dose_per_kg_per_day'])*random_weight,
            "medicine_type": medicine["type"],
            "prescription_classes": medicine["classes"],
            "risk_factor": medicine["risk_factor"],
            "maximum_daily_dosage": medicine['max_dose_per_kg_per_day']*random_weight,
            "risk_dosage": medicine['risk_dose_per_kg_per_day']*random_weight,
            "risk_condition": random.choice(['none', 'addict', 'tolerance', 'ph_dependence', 'ps_dependence', 'abuse', 'misuse', 'od', 'rebound', 'poly_drug', 'illicit_use', 'self_medication', 'impaired', 'wd_cycle', 'relapse']),
            "prescription_collections": collection_dates,
            "last_consultation": (prescription_date - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%dT%H:%M:%S'),
            "med_details_url": f"https://www.example.com/{medicine['name'].lower()}"
        }
        
        prescriptions.append(prescription)
        print('generated_prescription : ',prescription['user_id'])
    
    return prescriptions

# Generate 25000 entries
data = generate_prescriptions(250000)

# Save to JSON file
with open('medical_data_250000.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# prescription-project# Medical Risk Prediction from Prescription Data

This project involves the generation and analysis of a synthetic dataset to predict various medical risks associated with prescription drugs. The dataset was created with ChatGPT, containing 250,000 entries of dummy medical data. The goal is to predict medical risks—such as overdose, abuse, misuse, addiction, and other adverse conditions—based on patients' prescription collection patterns, the types and brands of medicines prescribed, and related parameters.
Dataset Details

The dataset contains records of patient prescriptions with fields detailing:

    Prescription type and brand
    Prescription collection dates
    Patient demographics (e.g., height, weight)
    Prescription classes and risk factors associated with each medicine

This synthetic data was created with predictive modeling in mind, focusing on exploring patient behavior patterns and tendencies that could indicate potential risk conditions.
Project Objectives

    Predictive Modeling: Train and compare the performance of various machine learning models in predicting medical risks associated with prescriptions.
    Model Comparison: Evaluate models to identify which performs best in identifying high-risk behaviors or patterns.
    Visualization: Generate insightful graphs to understand data distributions and model performance.

# Models Implemented

We have implemented and trained the following models:

    Logistic Regression
    Decision Tree
    Random Forest
    Gradient Boosting
    Neural Network
    XGBoost

Each model’s output metrics, confusion matrix, and ROC curve have been evaluated for performance and comparison.
Results and Outputs

    medical_data_250000.json: This file contains 250000 entries of generated medical data based on 200 different varieties of medicines. This is generated using the dummy_data_generator.py which was in turn created with the help of chatGPT.

    PrescriptionTrainOutput.txt: This file contains the terminal output generated during the model training phase, including accuracy metrics, training logs, and general performance statistics.

    ./saved_models/: Contains various different models trained in a similar fashion on the exact same data and has been saved as pickle binary files

    Generated Graphs:
        ./generated_graphs/: Contains various visualizations that represent the dataset, such as distributions, feature importance, and class imbalance.
        ./generated_graphs/model_stats/: Contains confusion matrix and ROC curve graphs for each model, providing detailed insights into each model’s performance in identifying risk conditions.

# Directory Structure

bash

.
├── medical_data_250000.json      # Generated Dummy Data
├── PrescriptionTrainOutput.txt   # Training and evaluation logs for each model
├── generated_graphs/
│   ├── ...                       # Visualizations of the dataset and model features
│   └── model_stats/              # Confusion matrix and ROC curve graphs for each model
├── saved_models                  # Trained models saved as pickle files
└── README.md                     # Project documentation

# Usage

To reproduce this work, you may follow these steps:

    Generate a similar dataset or use the provided structure for your own data.
    Implement the predictive models as outlined above.
    Generate visualizations to analyze and interpret the results.

This project serves as a foundational framework for developing machine learning applications to identify and manage medical risks based on patient behavior patterns.

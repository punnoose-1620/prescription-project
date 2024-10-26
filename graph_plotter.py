import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from pre_processor import *
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix, ConfusionMatrixDisplay

roc_curves = {}
confusion_matrices = {}

def plot_confusion_matrix(y_true, y_pred, title="Confusion Matrix", save_path="confusion_matrix.png"):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title(title)
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    
    # Call your graph_plot() if it's custom for plotting
    # graph_plot(data=cm, ...)  # Example if graph_plot is a custom function
    plt.savefig('./generated_graphs/model_stats/'+save_path)
    # plt.show()
    # confusion_matrices[title] = cm_figure

def plot_roc_curve(y_true, y_prob, num_classes, title="ROC Curve", save_path="roc_curve.png"):
    plt.figure(figsize=(10, 8))
    for i in range(num_classes):
        fpr, tpr, _ = roc_curve(y_true, y_prob[:, i], pos_label=i)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f"Class {i} (area = {roc_auc:.2f})")

    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.title(title)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    
    # Call your graph_plot() if you have custom functionality
    # graph_plot(...)  # Example if graph_plot is a custom function
    plt.savefig('./generated_graphs/model_stats/'+save_path)
    # plt.show()
    # roc_curves[title] = roc_figure

def plot_and_save_bargraph(item_list, output_file='bargraph.png', x_title='Items', y_title='Count'):
    # Count occurrences of each unique item in the list
    item_counts = Counter(item_list)
    
    # Extract the items (x-axis) and their counts (y-axis)
    items = list(item_counts.keys())
    counts = list(item_counts.values())
    
    # Create a bar plot
    item_len = len(items)
    if item_len<350:
        plt.figure(figsize=(item_len*2, item_len))  # Optional: Set figure size
    plt.bar(items, counts, color='skyblue')
    
    # Labeling the axes and the title
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(output_file.split('.')[0])
    
    # Rotate x-axis labels for better readability (if needed)
    plt.xticks(rotation=90, ha='right')
    
    # Save the plot to a file
    plt.tight_layout()  # Adjusts plot to ensure everything fits
    plt.savefig('./generated_graphs/'+output_file)
    # plt.show()  # Optional: Show the plot

def plot_color_coded_bargraph(item_list, category_list, output_file='item_category_bargraph.png', x_title='Items', y_title='Count'):
    """
    Plots and saves a bar graph that shows the count of each item and color-codes the categories.
    
    Parameters:
        item_list (list): A list of item names.
        category_list (list): A list of categories corresponding to each item in item_list.
        output_file (str): The filename to save the bar graph image.
    """
    # Create a DataFrame from the provided item and category lists
    df = pd.DataFrame({'item': item_list, 'category': category_list})
    
    # Create a crosstab (pivot table) to get the count of each category for each item
    item_category_counts = pd.crosstab(df['item'], df['category'])
    
    # Plot the stacked bar graph
    item_category_counts.plot(kind='bar', stacked=True, figsize=(10, 6), color=plt.cm.Paired.colors)
    
    # Adding labels and title
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(output_file)

    # Place the legend outside the graph area
    plt.legend(title='Risk Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Save the plot to a file
    plt.tight_layout()  # Adjust layout for better appearance
    plt.savefig('./generated_graphs/'+output_file)
    # plt.show()

def plot_connection_graphs():
    medicine_names_counter_list = get_list_of_vals_from_json(json_file_path,'prescription_name')
    medicine_types_counter_list = get_list_of_vals_from_json(json_file_path,'medicine_type')
    prescription_classes_counter_list = get_list_of_vals_from_json(json_file_path,'prescription_classes')
    weights_counter = get_list_of_vals_from_json(json_file_path,'user_weight')
    heights_counter = get_list_of_vals_from_json(json_file_path,'user_height')
    prescription_dates_counter = get_list_of_vals_from_json(json_file_path,'prescription_date')
    risk_condition_counter = get_list_of_vals_from_json(json_file_path,'risk_condition')

    plot_and_save_bargraph(prescription_classes_counter_list,"Count of Categories of Prescriptions", "Prescription Types", "Prescriptions")
    plot_and_save_bargraph(medicine_types_counter_list,"Count of Medicine Categories", "Medicine Types", "Count")
    plot_and_save_bargraph(risk_condition_counter,"Count of Categories of Risks", "Risk Categories", "Count")
    plot_and_save_bargraph(medicine_names_counter_list,"Count of Medicine Names", "Medicine Names", "Count")
    plot_and_save_bargraph(weights_counter,"Count of User Weights", "Weight Classes", "Users")
    plot_and_save_bargraph(heights_counter,"Count of User Heights", "Height Names", "Users")
    plot_and_save_bargraph(prescription_dates_counter,"Count of Dates of Prescription")
    print("Category Count Bar Graphs Plotted")

    medicine_names_labelled, labels1 = get_item_type_from_json(json_file_path,'prescription_name','risk_condition')
    medicine_types_labelled, labels2 = get_item_type_from_json(json_file_path,'medicine_type','risk_condition')
    prescription_dates_labelled, labels3 = get_item_type_from_json(json_file_path,'prescription_date','risk_condition')

    plot_color_coded_bargraph(medicine_names_labelled, labels1, 'Labelled Medicine Name Counts', 'Medicine Name', 'Count')
    plot_color_coded_bargraph(medicine_types_labelled, labels2, 'Labelled Medicine Type Counts', 'Medicine Type', 'Count')
    plot_color_coded_bargraph(prescription_dates_labelled, labels3, 'Labelled Prescription Date Counts', 'Prescription Date', 'Count')
    print("Labelled Category Count Bar Graphs Plotted")

    # risk_types, usage_stats1 = get_daily_usage_stats_for_param(json_file_path,'risk_condition')
    # medicine_names, usage_stats2 = get_daily_usage_stats_for_param(json_file_path,'prescription_name')
    # medicine_types, usage_stats3 = get_daily_usage_stats_for_param(json_file_path,'medicine_type')

    # plot_color_coded_bargraph(risk_types, usage_stats1, 'Risk Cases', 'Daily Usage', 'Count')
    # plot_color_coded_bargraph(medicine_names, usage_stats2, 'Medicine Names', 'Daily Usage', 'Count')
    # plot_color_coded_bargraph(medicine_types, usage_stats3, 'Medicine Types', 'Daily Usage', 'Count')
    # print("Daily Usage Bar Graphs Plotted")

def plot_sunburst(json_data, output_file="sunburst_plot.png", required_columns = ['risk_condition', 'prescription_classes', 'medicine_type', 'user_weight', 'user_height']):
    # Convert JSON data to a DataFrame
    df = pd.DataFrame(json_data)
    
    # Ensure required columns are present
    if not all(col in df.columns for col in required_columns):
        raise ValueError("JSON data must contain all required fields: ", required_columns)
    
    # Convert `prescription_classes` to a string representation if it's a list
    df['prescription_classes'] = df['prescription_classes'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    
    # Create the sunburst plot
    fig = px.sunburst(
        df,
        path=required_columns,
        color=required_columns[0],  # color by risk_condition to differentiate segments
        title="Sunburst Plot of Medical Data",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    
    # Save as HTML file
    fig.write_image('./generated_graphs/'+output_file)
    print(f"Sunburst plot saved as {output_file}")

# Example usage
# json_data = [...]  # Replace with actual JSON data
# plot_sunburst(json_data)

# Example usage:
# plot_item_category_bargraph(items, categories)

# Assuming y_train and y_train_prob are available and num_classes is 15
# plot_roc_curve(y_train, y_train_prob, num_classes=15, title="Train ROC Curve", save_path="train_roc_curve.png")

# Plot ROC curve for test data
# plot_roc_curve(y_test, y_test_prob, num_classes=15, title="Test ROC Curve", save_path="test_roc_curve.png")

# Plot confusion matrix for train data
# plot_confusion_matrix(y_train, y_train_pred, title="Train Data Confusion Matrix", save_path="train_confusion_matrix.png")

# Plot confusion matrix for test data
# plot_confusion_matrix(y_test, y_test_pred, title="Test Data Confusion Matrix", save_path="test_confusion_matrix.png")

# Plot Bar Graph for Item Count
# plot_and_save_bargraph(sample_list, 'fruits_count.png')
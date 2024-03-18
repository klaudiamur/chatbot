#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets


#%%

#data = pd.read_csv('Iris.csv')
data = pd.read_csv('weatherHistory.csv')

#%%
def find_response(data, user_input):
    if "line" in user_input or "bar" in user_input:
        column = find_column_from_input_text(user_input, data.columns)
        if "line" in user_input:
            plot_function = plot_line_graph
        elif "bar" in user_input:
            plot_function = plot_bar_graph
        if column:
            return plot_function(data, column)
        else:
            
            all_columns = data.select_dtypes(include=[np.number]).columns.tolist()  
            return plot_function(data, all_columns)
    elif "columns" in user_input:
        return "The available columns are: " + ", ".join(data.columns)
    elif "info" in user_input:
        return data.head().to_string()
    else:
        return "I'm sorry, I didn't understand. Please try again."

def plot_line_graph(data, columns, filter=None):
    if filter:
        data = data[data[columns] == filter]
    if isinstance(columns, list):
        for column in columns:
            plt.plot(data[column], label=column)
        plt.legend()
    else:
        plt.plot(data[columns])
    plt.show()

def plot_bar_graph(data, columns, filter=None):
    if filter:
        data = data[data[columns] == filter]
    if isinstance(columns, list):
        data[columns].plot(kind='bar')
    else:
        data[columns].plot(kind='bar')
    plt.show()

def find_column_from_input_text(text, columns):
    for column in columns:
        if column.lower() in text.lower():
            return column
    return None


print("Hello! What can I visualize for you? type 'quit' to exit")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    
    response = find_response(data, user_input)
    print("Chatbot:", response)    


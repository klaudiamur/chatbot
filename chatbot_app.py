import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define the function to handle chatbot responses
def get_chatbot_response(user_input):
    """
    A simple function to return a response to user inputs.
    This function now includes a trigger for generating a plot.
    """
    if user_input.lower() == "show plot":
        # Generate and display a plot when the user asks for it
        generate_plot()
        return "Here's your plot!"
    
    # Predefined responses for the chatbot
    responses = {
        "hello": "Hello! How can I help you today?",
        "help": "You can ask me any question, and I'll try my best to answer.",
        "bye": "Goodbye! Have a nice day!"
    }
    
    # Convert user input to lowercase to ensure case-insensitive matching
    user_input = user_input.lower()
    
    # Return the corresponding response if one exists
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you try asking something else?")

def generate_plot():
    """
    Generates a simple line plot using Matplotlib and displays it in Streamlit.
    """
    # Sample data for the plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create the plot
    plt.figure()
    plt.plot(x, y)
    plt.title("Sample Sin Wave")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    
    # Display the plot in Streamlit
    st.pyplot(plt)

# Streamlit app layout setup
st.title('Data viz Chatbot v. 1')

# Input field for user messages
user_input = st.text_input("Talk to the chatbot:")

# Handling the chat interaction
if st.button('Send') or user_input:
    response = get_chatbot_response(user_input)
    if response:
        st.write(response)

## add more functionalities to your chatbot!
## run the code with streamlit run chatbot_app.py

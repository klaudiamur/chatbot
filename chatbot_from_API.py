import time
import requests

def generate_chatbot_response_via_api(input_text, api_key):
    
    #API_URL = "https://api-inference.huggingface.co/models/AI-Sweden-Models/gpt-sw3-1.3b"
    API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
    #API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-7b-hf"

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "inputs": input_text,
        "parameters": {"temperature": 0.7, "max_tokens": 100},
        "options": {"use_cache": False}
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return result[0]['generated_text']
    elif response.status_code == 503:
        error_info = response.json()
        wait_time = error_info.get("estimated_time", 30)  # Default to 30 seconds if not specified
        print(f"Model is loading, waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        # Retry the request once after waiting
        response = requests.post(API_URL, headers=headers, json={"inputs": input_text})
        if response.status_code == 200:
            result = response.json()
            return result[0]['generated_text']
        else:
            return f"Error after retrying: {response.status_code} - {response.text}"
    else:
        return f"Error calling the API: {response.status_code} - {response.text}"


def chat_loop(api_key):
    print("Chatbot is ready to talk! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        response = generate_chatbot_response_via_api(user_input, api_key)
        print("Chatbot:", response)

def main():
    api_key = "your_api_key"  # Replace this with your Hugging Face API key
    chat_loop(api_key)

if __name__ == "__main__":
    main()

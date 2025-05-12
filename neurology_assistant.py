import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# System prompt for the neurology assistant
SYSTEM_PROMPT = """You are a professional AI medical assistant trained specifically in the field of neurology. 
Your primary role is to assist users with accurate, helpful, and easy-to-understand answers related to neurological health, 
diseases, treatments, and brain functions.

Guidelines:
1. Provide clear, friendly, and respectful responses
2. Base answers on credible medical knowledge up to 2024
3. Clearly state that you are not a substitute for a real doctor
4. Offer general guidance, explain symptoms, and provide educational information
5. Suggest when to consult a medical professional
6. If a question is outside your scope or requires personal diagnosis, politely ask the user to consult a certified neurologist
7. If asked about non-neurological topics, gently redirect to neurology-related subjects

Remember: Always prioritize user safety and encourage professional medical consultation when appropriate."""

def get_neurology_response(user_input):
    try:
        # Combine system prompt with user input
        prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_input}\n\nPlease provide a helpful response:"
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again or consult a medical professional for immediate assistance."

def main():
    print("Welcome to the Neurology Assistant!")
    print("I can help you with questions about neurological health, diseases, treatments, and brain functions.")
    print("Type 'exit' to quit.")
    print("\nPlease note: I am an AI assistant and not a substitute for professional medical advice.")
    print("Always consult with a qualified healthcare provider for medical decisions.\n")

    while True:
        user_input = input("\nYour question: ").strip()
        
        if user_input.lower() == 'exit':
            print("\nThank you for using the Neurology Assistant. Take care!")
            break
            
        if not user_input:
            print("Please enter a question.")
            continue
            
        response = get_neurology_response(user_input)
        print("\nResponse:", response)

if __name__ == "__main__":
    main() 
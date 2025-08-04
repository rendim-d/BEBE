import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize the model, e.g., 'gemini-pro' or 'gemini-1.5-flash'
model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    """Main function to run the interactive chatbot."""
    print("🤖 Gemini AI Chat Bot")
    print("Ketik 'exit' untuk keluar\\n")

    # Start a chat session with an empty history
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("Anda: ")
        
        if user_input.lower() == 'exit':
            print("Terima kasih! Sampai jumpa!")
            break
            
        try:
            # Send the user's message to the chat session and get the response
            # The chat object now remembers the history automatically
            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}\\n")
        except Exception as e:
            print(f"Terjadi error: {e}\\n")

if __name__ == "__main__":
    main()
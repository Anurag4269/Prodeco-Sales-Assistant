import os
from groq import Groq
from product_database import load_products
from embedding import setup_embedding_and_index
from conversation import run_conversation

# Load environment variables
from config import load_environment_variables
load_environment_variables()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.1-70b-versatile"

# Load products
products = load_products()

# Setup embedding and index
embedding_model, index, product_names, product_descriptions = setup_embedding_and_index(products)

def main():
    conversation_history = []
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        _, conversation_history = run_conversation(user_input, conversation_history, client, MODEL, products, embedding_model, index, product_names)
        print()

if __name__ == "__main__":
    main()
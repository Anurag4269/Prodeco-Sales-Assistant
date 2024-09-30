# Electronics Store Sales Assistant

This project implements a conversational AI assistant for an electronics store using the Llama 3.1 model on Groq, with RAG (Retrieval-Augmented Generation) capabilities.

## Features

- Product search functionality
- Product comparison
- Detailed product information retrieval
- Natural language interaction with customers

## Project Structure

- `main.py`: The main script to run the conversation agent
- `product_database.py`: Functions related to product database and search
- `embedding.py`: Embedding model and FAISS index setup
- `conversation.py`: The conversation logic and Groq API interaction
- `config.py`: Configuration settings

## Technologies Used

- Python 3.10
- Groq API for LLM inference
- FAISS for efficient similarity search
- Sentence Transformers for text embedding

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY='your_api_key_here'
   ```
4. Ensure you have a `products.json` file in the correct location with your product database.

## Usage

Run the main script to start the interactive sales assistant:

```
python main.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)
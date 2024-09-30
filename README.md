# Prodeco-Sales-Assistant

# Electronics Store Sales Assistant

This project implements a conversational AI assistant for an electronics store using the Llama 3.1 model on Groq, with RAG (Retrieval-Augmented Generation) capabilities.

## Features

- Product search functionality
- Product comparison
- Detailed product information retrieval
- Natural language interaction with customers

## Technologies Used

- Python 3.10
- Groq API for LLM inference
- FAISS for efficient similarity search
- Sentence Transformers for text embedding
- Jupyter Notebook for development and demonstration

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install groq faiss-cpu sentence-transformers langtrace-python-sdk opentelemetry-exporter-otlp
   ```
3. Set up your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY='your_api_key_here'
   ```
4. Ensure you have a `products.json` file in the correct location with your product database.

## Usage

Run the Jupyter notebook `conversation-agent.ipynb` to start the interactive sales assistant.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

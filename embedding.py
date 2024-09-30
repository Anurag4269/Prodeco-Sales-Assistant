from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def setup_embedding_and_index(products):
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    product_names = list(products.keys())
    product_descriptions = [f"{name}: {data['specs']} Best for {data['best_for']}" for name, data in products.items()]

    # Create embeddings
    embeddings = embedding_model.encode(product_descriptions)

    # Create a FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))

    return embedding_model, index, product_names, product_descriptions
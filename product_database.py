import json

def load_products(file_path='/kaggle/input/prodeco/products.json'):
    with open(file_path, 'r') as file:
        products_raw = json.load(file)
    
    products = {product['name']: {
        'price': product['price'],
        'specs': product['description'],
        'best_for': product['best_for']
    } for product in products_raw}
    
    return products

def search_products(query, top_k, index, embedding_model, product_names, products):
    query_embedding = embedding_model.encode([query])
    distances, indices = index.search(query_embedding.astype('float32'), top_k)
    results = []
    for i in indices[0]:
        product_name = product_names[i]
        results.append({
            "name": product_name,
            "price": products[product_name]["price"],
            "specs": products[product_name]["specs"],
            "best_for": products[product_name]["best_for"]
        })
    return results

def get_product_details(product_name, products):
    if product_name in products:
        return products[product_name]
    return None

def compare_products(product_names, products):
    comparison = []
    for name in product_names:
        if name in products:
            comparison.append({
                "name": name,
                **products[name]
            })
    return comparison
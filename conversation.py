import json
from product_database import search_products, get_product_details, compare_products

def run_conversation(user_prompt, conversation_history, client, MODEL, products, embedding_model, index, product_names):
    if not conversation_history:
        conversation_history = [
            {
                "role": "system",
                "content": "You are an electronics store assistant. Help customers find products, compare options, and make informed decisions based on the information retrieved from the product database."
            }
        ]
    
    conversation_history.append({"role": "user", "content": user_prompt})
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_products",
                "description": "Search for products in the store",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"},
                        "top_k": {"type": "integer", "description": "Number of results to return"}
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get detailed information about a specific product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {"type": "string", "description": "Name of the product"},
                    },
                    "required": ["product_name"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "compare_products",
                "description": "Compare multiple products",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_names": {"type": "array", "items": {"type": "string"}, "description": "List of product names to compare"},
                    },
                    "required": ["product_names"],
                },
            },
        },
    ]

    while True:
        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation_history,
            tools=tools,
            tool_choice="auto",
            max_tokens=4096
        )

        response_message = response.choices[0].message
        conversation_history.append(response_message)

        print("Assistant:", response_message.content)
        print("----------------------------------------")

        if not response_message.tool_calls:
            return response_message.content, conversation_history

        available_functions = {
            "search_products": lambda query, top_k=3: search_products(query, top_k, index, embedding_model, product_names, products),
            "get_product_details": lambda product_name: get_product_details(product_name, products),
            "compare_products": lambda product_names: compare_products(product_names, products),
        }

        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)
            conversation_history.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(function_response),
                }
            )

    return response_message.content, conversation_history
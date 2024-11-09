import ollama

# Initialize the Ollama client
client = ollama.Client()

def generate_response(prompt, model_name='llama2'):
    """
    Generate a response from the Ollama model based on the provided prompt.
    Args:
        prompt (str): The input prompt for the model.
        model_name (str): The name of the Ollama model to use (default: 'llama2').
    Returns:
        str: The generated text response from Ollama.
    """
    response = client.chat(
        model=model_name,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']
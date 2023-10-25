import string
import requests

def query(payload):
    """
    Query the API with the given payload and return the generated text.

    Parameters:
        payload (dict): The payload containing the input data for the API.

    Returns:
        str: The generated text from the API response.
    """
    api_token = "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"
    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

    headers = {"Authorization": f"Bearer {api_token}"}

    response = requests.post(api_url, headers=headers, json=payload)
    output = response.json()[0]

    return output
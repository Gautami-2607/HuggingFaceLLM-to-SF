import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# Load environment variables
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")

# Validate API key
if not HUGGINGFACE_API_KEY:
    raise ValueError("HUGGINGFACE_API_KEY is not set in environment variables")

# Initialize Hugging Face client with token
hf_client = InferenceClient(model=MODEL_NAME, token=HUGGINGFACE_API_KEY)


def generate_text(prompt: str, max_tokens: int = 100, temperature: float = 0.7, top_p: float = 0.95) -> str:
    """
    Generate text using Hugging Face Inference API
    
    Args:
        prompt: The input prompt for text generation
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature (0-1)
        top_p: Nucleus sampling parameter
        
    Returns:
        Generated text from the model
    """
    try:
        response = hf_client.text_generation(
            prompt=prompt,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
        return response
    except Exception as e:
        raise RuntimeError(f"Error calling Hugging Face API: {str(e)}")

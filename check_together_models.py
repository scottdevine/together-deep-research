import os
from dotenv import load_dotenv
from together import Together

# Load environment variables from .env file
load_dotenv()

# Get API key
together_key = os.environ.get("TOGETHER_API_KEY", "")

# Initialize Together client
client = Together(api_key=together_key)

# List models
models = client.models.list()

# Print all model IDs
print("Available Together AI models:")
for model in models:
    print(f"- {model.id}")

# Check for specific models
print("\nChecking for specific models:")
model_prefixes = ["qwen", "llama", "deepseek"]
for prefix in model_prefixes:
    matching_models = [model.id for model in models if prefix.lower() in model.id.lower()]
    print(f"\nModels containing '{prefix}':")
    for model_id in matching_models:
        print(f"- {model_id}")

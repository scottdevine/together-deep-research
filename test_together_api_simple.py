import os
from dotenv import load_dotenv
from together import Together

# Load environment variables
load_dotenv()

# Get API key
together_key = os.environ.get("TOGETHER_API_KEY", "")

print(f"TOGETHER_API_KEY set: {'Yes' if together_key else 'No'}")

# Initialize Together client
client = Together(api_key=together_key)

# Test a simple completion
print("\nTesting simple completion...")
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is artificial intelligence?"}
    ],
    temperature=0.0,
    max_tokens=100
)

print(f"Success! Response: {response.choices[0].message.content}")

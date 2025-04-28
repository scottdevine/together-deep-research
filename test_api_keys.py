import os
import sys
import traceback
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys
together_key = os.environ.get("TOGETHER_API_KEY", "")
tavily_key = os.environ.get("TAVILY_API_KEY", "")
huggingface_token = os.environ.get("HUGGINGFACE_TOKEN", "")

print(f"TOGETHER_API_KEY set: {'Yes' if together_key else 'No'}")
print(f"TAVILY_API_KEY set: {'Yes' if tavily_key else 'No'}")
print(f"HUGGINGFACE_TOKEN set: {'Yes' if huggingface_token else 'No'}")

# Test Together API
print("\nTesting Together API...")
try:
    from together import Together
    
    client = Together(api_key=together_key)
    response = client.models.list()
    print("Together API test: SUCCESS")
    print(f"Found {len(response.data)} models")
except Exception as e:
    print(f"Together API test: FAILED")
    print(f"Error: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

# Test Tavily API
print("\nTesting Tavily API...")
try:
    from tavily import TavilyClient
    
    client = TavilyClient(api_key=tavily_key)
    response = client.search(query="What is artificial intelligence?", search_depth="basic", max_results=1)
    print("Tavily API test: SUCCESS")
    print(f"Found {len(response.get('results', []))} results")
except Exception as e:
    print(f"Tavily API test: FAILED")
    print(f"Error: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

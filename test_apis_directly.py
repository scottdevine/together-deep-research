import os
import sys
import traceback
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys
together_key = os.environ.get("TOGETHER_API_KEY", "")
tavily_key = os.environ.get("TAVILY_API_KEY", "")

print(f"TOGETHER_API_KEY set: {'Yes' if together_key else 'No'}")
print(f"TAVILY_API_KEY set: {'Yes' if tavily_key else 'No'}")

# Test Together API directly
print("\n=== Testing Together API Directly ===")
try:
    from together import Together
    
    client = Together(api_key=together_key)
    
    # Test 1: List models
    print("\nTest 1: Listing models...")
    models = client.models.list()
    print(f"Success! Found {len(models)} models")
    
    # Test 2: Simple completion without response_format
    print("\nTest 2: Simple completion without response_format...")
    response = client.chat.completions.create(
        model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is artificial intelligence?"}
        ],
        temperature=0.0,
        max_tokens=100
    )
    print(f"Success! Response: {response.choices[0].message.content[:100]}...")
    
    # Test 3: Completion with JSON response format in system prompt
    print("\nTest 3: Completion with JSON response format in system prompt...")
    schema = {
        "type": "object",
        "properties": {
            "definition": {"type": "string"},
            "examples": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["definition", "examples"]
    }
    
    system_prompt = f"""You are a helpful assistant.
    
Your response must be a valid JSON object that conforms to this schema:
{json.dumps(schema, indent=2)}

Ensure your response is properly formatted JSON with no additional text."""
    
    response = client.chat.completions.create(
        model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "What is artificial intelligence?"}
        ],
        temperature=0.0,
        max_tokens=500
    )
    print(f"Success! Response: {response.choices[0].message.content[:100]}...")
    
    # Test 4: Try with response_format parameter (this might fail)
    print("\nTest 4: Completion with response_format parameter (might fail)...")
    try:
        response = client.chat.completions.create(
            model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is artificial intelligence?"}
            ],
            temperature=0.0,
            max_tokens=100,
            response_format={"type": "json_object"}
        )
        print(f"Success! Response: {response.choices[0].message.content[:100]}...")
    except Exception as e:
        print(f"Failed as expected: {str(e)}")
        print("This confirms that Together AI doesn't support the response_format parameter")
    
except Exception as e:
    print(f"Together API test failed: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

# Test Tavily API directly
print("\n=== Testing Tavily API Directly ===")
try:
    from tavily import TavilyClient
    
    client = TavilyClient(api_key=tavily_key)
    
    # Test 1: Simple search
    print("\nTest 1: Simple search...")
    response = client.search(query="What is artificial intelligence?", search_depth="basic", max_results=3)
    print(f"Success! Found {len(response.get('results', []))} results")
    print(f"First result title: {response.get('results', [])[0].get('title', 'No title')}")
    
except Exception as e:
    print(f"Tavily API test failed: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

# Test litellm directly
print("\n=== Testing litellm Directly ===")
try:
    import litellm
    
    print(f"litellm version: {litellm.__version__}")
    
    # Test 1: Simple completion with Together AI
    print("\nTest 1: Simple completion with Together AI...")
    response = litellm.completion(
        model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is artificial intelligence?"}
        ],
        temperature=0.0,
        max_tokens=100
    )
    print(f"Success! Response: {response.choices[0].message['content'][:100]}...")
    
    # Test 2: Completion with JSON response format in system prompt
    print("\nTest 2: Completion with JSON response format in system prompt...")
    schema = {
        "type": "object",
        "properties": {
            "definition": {"type": "string"},
            "examples": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["definition", "examples"]
    }
    
    system_prompt = f"""You are a helpful assistant.
    
Your response must be a valid JSON object that conforms to this schema:
{json.dumps(schema, indent=2)}

Ensure your response is properly formatted JSON with no additional text."""
    
    response = litellm.completion(
        model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "What is artificial intelligence?"}
        ],
        temperature=0.0,
        max_tokens=500
    )
    print(f"Success! Response: {response.choices[0].message['content'][:100]}...")
    
    # Test 3: Try with response_format parameter (this might fail)
    print("\nTest 3: Completion with response_format parameter (might fail)...")
    try:
        response = litellm.completion(
            model="together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is artificial intelligence?"}
            ],
            temperature=0.0,
            max_tokens=100,
            response_format={"type": "json_object"}
        )
        print(f"Success! Response: {response.choices[0].message['content'][:100]}...")
    except Exception as e:
        print(f"Failed as expected: {str(e)}")
        print("This confirms that litellm with Together AI doesn't support the response_format parameter")
    
except Exception as e:
    print(f"litellm test failed: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

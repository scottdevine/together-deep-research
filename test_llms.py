import os
import sys
from dotenv import load_dotenv
from src.libs.utils.llms import single_shot_llm_call

# Load environment variables
load_dotenv()

# Check if API keys are set
if not os.environ.get("TOGETHER_API_KEY"):
    print("Error: TOGETHER_API_KEY is not set.")
    sys.exit(1)

# Test the single_shot_llm_call function
try:
    print("Testing single_shot_llm_call function...")
    response = single_shot_llm_call(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        system_prompt="You are a helpful assistant.",
        message="What is artificial intelligence?",
        max_completion_tokens=100
    )
    print("Success! Response:", response[:100] + "...")
except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()

# Test with JSON response format
try:
    print("\nTesting with JSON response format...")
    schema = {
        "type": "object",
        "properties": {
            "definition": {"type": "string"},
            "examples": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["definition", "examples"]
    }
    
    response = single_shot_llm_call(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        system_prompt="You are a helpful assistant.",
        message="What is artificial intelligence?",
        response_format={"type": "json_object", "schema": schema},
        max_completion_tokens=500
    )
    print("Success! Response:", response[:100] + "...")
except Exception as e:
    print("Error:", str(e))
    import traceback
    traceback.print_exc()

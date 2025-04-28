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

try:
    print("Importing DeepResearcher...")
    from src.together_open_deep_research import DeepResearcher
    print("Import successful!")

    # Create a researcher instance with minimal settings
    print("Creating DeepResearcher instance...")
    researcher = DeepResearcher(
        budget=1,
        max_queries=1,
        max_sources=5,
        planning_model="Qwen/Qwen2.5-72B-Instruct-Turbo",
        summarization_model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        json_model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        answer_model="deepseek-ai/DeepSeek-V3"
    )
    print("DeepResearcher instance created successfully!")

    # Try a simple query
    query = "What is artificial intelligence?"
    print(f"Running query: {query}")

    # Run the query
    answer = researcher(query)

    print("Query successful!")
    print("First 200 characters of answer:", answer[:200] + "...")

except Exception as e:
    print(f"Error: {str(e)}")
    print("Traceback:")
    traceback.print_exc()

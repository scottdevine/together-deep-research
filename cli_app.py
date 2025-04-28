import os
import sys
from dotenv import load_dotenv
from src.together_open_deep_research import DeepResearcher

# Load environment variables
load_dotenv()

# Check if API keys are set
if not os.environ.get("TOGETHER_API_KEY") or not os.environ.get("TAVILY_API_KEY"):
    missing_keys = []
    if not os.environ.get("TOGETHER_API_KEY"):
        missing_keys.append("TOGETHER_API_KEY")
    if not os.environ.get("TAVILY_API_KEY"):
        missing_keys.append("TAVILY_API_KEY")
    
    print(f"Error: Missing API keys in environment variables: {', '.join(missing_keys)}.")
    sys.exit(1)

# Create a researcher instance
researcher = DeepResearcher(
    budget=1,  # Use a small budget for testing
    max_queries=1,
    max_sources=5,
    planning_model="Qwen/Qwen2.5-72B-Instruct-Turbo",
    summarization_model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    json_model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
    answer_model="deepseek-ai/DeepSeek-V3"
)

# Get the query from the user
query = input("Enter your research topic: ")

# Run the research
print(f"Researching: {query}")
answer = researcher(query)

# Print the answer
print("\n\nRESEARCH RESULTS:\n")
print(answer)

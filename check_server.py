import requests
import time
import sys

def check_server(url="http://localhost:7860", max_attempts=5, delay=2):
    print(f"Checking if server is running at {url}...")
    
    for attempt in range(max_attempts):
        try:
            print(f"Attempt {attempt + 1}/{max_attempts}...")
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Server is running! Status code: {response.status_code}")
                print(f"Response content length: {len(response.text)} bytes")
                print(f"First 100 characters of response: {response.text[:100]}...")
                return True
        except requests.exceptions.ConnectionError:
            print(f"Server not responding on attempt {attempt + 1}. Waiting {delay} seconds...")
            time.sleep(delay)
    
    print("Server is not running or not accessible.")
    return False

if __name__ == "__main__":
    url = "http://localhost:7860"
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    check_server(url)

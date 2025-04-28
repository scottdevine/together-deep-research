import requests
import json

def test_gradio_api():
    """Test if we can make a direct API call to the Gradio server."""
    try:
        # Get the API endpoints
        response = requests.get("http://localhost:7860/")
        print(f"Server response status: {response.status_code}")
        
        if response.status_code == 200:
            print("Server is running!")
            return True
        else:
            print(f"Server returned status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {str(e)}")
        return False

if __name__ == "__main__":
    test_gradio_api()

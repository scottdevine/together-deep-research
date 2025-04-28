import os
import sys
import traceback

# Add the project root to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Set up environment variables
os.environ["PYTHONPATH"] = project_root

try:
    print(f"Starting webapp with PYTHONPATH={project_root}")
    print(f"Python version: {sys.version}")

    # Import gradio and check version
    import gradio as gr
    print(f"Gradio version: {gr.__version__}")

    # Now import the webapp module
    from src.webapp import demo

    print("Starting Gradio server...")
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False, debug=True)
    print("Gradio server started!")
except Exception as e:
    print(f"Error: {str(e)}")
    print(traceback.format_exc())

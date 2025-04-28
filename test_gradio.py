import gradio as gr
import os

print("Python version:", os.sys.version)
print("Current working directory:", os.getcwd())
print("Gradio version:", gr.__version__)

def greet(name):
    return "Hello " + name + "!"

# Create a simple Gradio interface
demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Test Gradio App"
)

# Launch the app with explicit server settings and verbose output
if __name__ == "__main__":
    print("Starting Gradio server...")
    demo.launch(
        server_name="127.0.0.1",  # Listen on localhost only
        server_port=7860,
        share=False,
        debug=True,
        show_error=True
    )
    print("Gradio server started!")

import os
import sys
import traceback

try:
    print("Python version:", sys.version)
    print("Current working directory:", os.getcwd())
    print("PYTHONPATH:", sys.path)
    
    print("Importing gradio...")
    import gradio as gr
    print("Gradio version:", gr.__version__)
    
    print("Creating a simple test interface...")
    
    def greet(name):
        return "Hello " + name + "!"

    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
    print("Launching Gradio interface...")
    demo.launch(server_name="127.0.0.1", server_port=8000, share=True, inbrowser=True)
    print("Gradio interface launched!")
    
except Exception as e:
    print("Error:", str(e))
    print("Traceback:", traceback.format_exc())

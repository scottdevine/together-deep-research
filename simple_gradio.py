import gradio as gr
import os
import sys

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())
print("Gradio version:", gr.__version__)

def greet(name):
    return "Hello " + name + "!"

print("Creating Gradio interface...")
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

print("Launching Gradio interface...")
demo.launch(server_name="127.0.0.1", server_port=7860)
print("Gradio interface launched!")

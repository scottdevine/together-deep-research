import gradio as gr

def greet(name):
    return "Hello " + name + "!"

# Create a simple Gradio interface
demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Test Gradio App"
)

# Launch the app with explicit server settings
if __name__ == "__main__":
    print("Starting Gradio server...")
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
    print("Gradio server started!")

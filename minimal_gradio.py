import gradio as gr

def hello(name):
    return f"Hello, {name}!"

demo = gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text",
    title="Minimal Gradio App"
)

if __name__ == "__main__":
    print("Starting minimal Gradio app...")
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
    print("Gradio server started!")

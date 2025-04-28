import os
import gradio as gr
from src.together_open_deep_research import DeepResearcher

def research_topic(query, budget=1):
    """Simple function to research a topic."""
    try:
        # Create a researcher instance
        researcher = DeepResearcher(
            budget=budget,
            max_queries=1,
            max_sources=5,
            planning_model="Qwen/Qwen2.5-72B-Instruct-Turbo",
            summarization_model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            json_model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            answer_model="deepseek-ai/DeepSeek-V3"
        )
        
        # Run the research
        answer = researcher(query)
        
        return answer
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{error_traceback}"
        print(f"ERROR: {error_message}")
        return f"Error: {str(e)}"

# Create a simple Gradio interface
demo = gr.Interface(
    fn=research_topic,
    inputs=[
        gr.Textbox(placeholder="Enter your research topic...", label="Research Topic"),
        gr.Slider(minimum=1, maximum=3, value=1, step=1, label="Research Budget (iterations)")
    ],
    outputs=gr.Textbox(label="Research Results"),
    title="Simple Together Open Deep Research",
    description="Enter a research topic to get started."
)

# Launch the app
if __name__ == "__main__":
    print("Starting Gradio server...")
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False, debug=True, show_error=True)
    print("Gradio server started!")

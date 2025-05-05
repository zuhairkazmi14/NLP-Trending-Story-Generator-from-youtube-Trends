# frontend.py
import gradio as gr
import grpc
import trendstory_pb2
import trendstory_pb2_grpc
from googleapiclient.discovery import build

# Replace with your own API key
API_KEY = "AIzaSyBDgmFQctKDB9WXvIIXHTw_ZiPu49_oKuA"

# --- Get YouTube Trending Titles ---
def get_trending_titles(max_results=10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode='PK',
        maxResults=max_results
    )
    response = request.execute()
    return [item['snippet']['title'] for item in response['items']]

# --- Generate Story via gRPC ---
def generate_story(title, theme):
    channel = grpc.insecure_channel('localhost:50051')
    stub = trendstory_pb2_grpc.TrendStoryServiceStub(channel)
    try:
        response = stub.GenerateStory(trendstory_pb2.TrendRequest(title=title, theme=theme))
        return response.story
    except grpc.RpcError as e:
        return f"❌ gRPC error: {e.details()}"

# --- Refresh titles ---
def refresh_titles():
    return gr.update(choices=get_trending_titles())

# --- Gradio UI ---
def launch_gradio():
    trending_titles = get_trending_titles()

    with gr.Blocks(css="""
body {
    background: linear-gradient(to right top, #ffecd2, #fcb69f);
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
}
.main-title {
    font-size: 3rem;
    font-weight: bold;
    color: #1e3a8a;
    text-align: center;
    margin-top: 1rem;
    text-shadow: 1px 1px 2px #94a3b8;
}
.subtitle {
    font-size: 1.2rem;
    color: #334155;
    text-align: center;
    margin-bottom: 2rem;
    font-style: italic;
}
.dropdown, .textbox {
    border-radius: 12px;
    padding: 12px;
    font-size: 1rem;
    background-color: #f8fafc;
    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    border: 1px solid #e2e8f0;
}
.generate-button {
    background: linear-gradient(135deg, #a855f7, #ec4899);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px 25px;
    font-weight: bold;
    font-size: 1rem;
    box-shadow: 0 6px 12px rgba(172, 69, 255, 0.4);
    transition: all 0.3s ease;
}
.generate-button:hover {
    background: linear-gradient(135deg, #ec4899, #a855f7);
    transform: scale(1.08);
    box-shadow: 0 8px 14px rgba(236, 72, 153, 0.5);
}
.refresh-button {
    background: linear-gradient(135deg, #22c55e, #10b981);
    color: white;
    border-radius: 14px;
    padding: 12px 25px;
    font-weight: bold;
    font-size: 1rem;
    box-shadow: 0 6px 12px rgba(16, 185, 129, 0.4);
    transition: all 0.3s ease;
}
.refresh-button:hover {
    background: linear-gradient(135deg, #10b981, #22c55e);
    transform: scale(1.08);
    box-shadow: 0 8px 14px rgba(34, 197, 94, 0.5);
}
.gr-button {
    margin-top: 12px;
}
"""
) as demo:

        gr.HTML("<div class='main-title'>📺 TrendStory Generator</div>")
        gr.HTML("<div class='subtitle'>Turn YouTube trends into magical stories powered by AI 🎭✍️</div>")

        with gr.Row(equal_height=True):
            title_dropdown = gr.Dropdown(
                choices=trending_titles,
                label="🔥 Select a Trending Title",
                elem_classes=["dropdown"],
                interactive=True
            )
            refresh_btn = gr.Button("🔁 Refresh Trends", elem_classes=["refresh-button"])

        theme_dropdown = gr.Dropdown(
            choices=["comedy", "sarcasm", "tragedy", "satire", "fantasy"],
            label="🎭 Choose a Story Theme",
            elem_classes=["dropdown"]
        )

        generate_btn = gr.Button("✨ Generate Story", elem_classes=["generate-button"])

        output_box = gr.Textbox(
            label="📖 Your Generated Story",
            lines=16,
            placeholder="Your story will appear here...",
            elem_classes=["textbox"]
        )

        # --- Actions ---
        refresh_btn.click(fn=refresh_titles, outputs=title_dropdown)
        generate_btn.click(fn=generate_story, inputs=[title_dropdown, theme_dropdown], outputs=output_box)

    demo.launch()

if __name__ == "__main__":
    launch_gradio()

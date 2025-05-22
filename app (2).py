import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model

# Load model (adjust filename and path)
model = load_model('best_lstm_model.keras')

def predict(stock_features):
    try:
        features = list(map(float, stock_features.split(',')))
    except:
        return "⚠️ Please enter valid comma-separated numbers."

    arr = np.array(features).reshape(1, -1, 1)
    pred = model.predict(arr)[0][0]
    return f"${pred:.2f}"
# Custom CSS for glassmorphism & smooth style
css = """
body, .gradio-container {
    background: linear-gradient(135deg, #667eea, #764ba2);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
}
h1 {
    color: white;
    text-shadow: 0 0 10px rgba(255,255,255,0.7);
    margin-bottom: 1rem;
}
.gradio-container > div {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    padding: 2rem;
    max-width: 600px;
    width: 100%;
    transition: box-shadow 0.3s ease;
}
.gradio-container > div:hover {
    box-shadow: 0 12px 48px rgba(0,0,0,0.45);
}
input[type="text"], textarea {
    background: rgba(255, 255, 255, 0.25) !important;
    border: none !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    border-radius: 30px !important;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
    transition: all 0.3s ease !important;
    font-size: 1rem !important;
}
input[type="text"]:focus, textarea:focus {
    outline: none !important;
    background: rgba(255, 255, 255, 0.4) !important;
    box-shadow: 0 8px 25px rgba(255, 255, 255, 0.45);
    transform: scale(1.03);
}
.gr-button {
    background: rgba(255, 255, 255, 0.25) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    padding: 14px 36px !important;
    border-radius: 30px !important;
    box-shadow: 0 6px 20px rgba(255, 255, 255, 0.25);
    transition: all 0.3s ease !important;
    cursor: pointer;
    font-size: 1.1rem !important;
}
.gr-button:hover {
    background: rgba(255, 255, 255, 0.45) !important;
    box-shadow: 0 10px 35px rgba(255, 255, 255, 0.55);
    transform: scale(1.08);
}
.output-text {
    font-size: 2.2rem;
    font-weight: 700;
    color: #fff;
    text-shadow: 0 0 15px rgba(255,255,255,0.9);
    margin-top: 1rem;
    text-align: center;
}
"""

with gr.Blocks(css=css) as demo:
    gr.Markdown("<h1>📈 Stock Price Predictor</h1>", elem_id="title")

    inp = gr.Textbox(
        label="Enter comma-separated stock features",
        placeholder="Example: 0.12, 0.15, 0.17, 0.19",
        lines=1,
        interactive=True
    )
    btn = gr.Button("Predict")
    out = gr.Textbox(label="Predicted Stock Price", interactive=False, lines=1, elem_classes="output-text")

    btn.click(fn=predict, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch()

import gradio as gr
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from safetensors.torch import load_file

# Load tokenizer và mô hình
model_path = "./bertrcnn_checkpoints"
tokenizer = BertTokenizer.from_pretrained(
    pretrained_model_name_or_path=model_path
)  # Khởi tạo tokenizer


# Khởi tạo mô hình từ Hugging Face và nạp trọng số từ safetensors
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=2)
# Tải trọng số mô hình từ safetensors
safetensor_model = load_file(f"./bertrcnn_checkpoints/model.safetensors")
model.load_state_dict(safetensor_model, strict=False)
model.eval()  # Chuyển mô hình sang chế độ đánh giá


# Hàm phân tích cảm xúc
def predict_sentiment(text):
    # Tokenize input text
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, padding=True, max_length=512
    )
    # Dự đoán với mô hình
    with torch.no_grad():
        outputs = model(**inputs)

    # Xử lý kết quả
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()  # Dự đoán nhãn
    confidence = probs[0][pred].item()  # Độ tin cậy của dự đoán
    label_name = "Tích cực" if pred == 1 else "Tiêu cực"
    return label_name, f"{confidence:.2%}"


def handle_prediction(input_text):
    if not input_text.strip():
        raise gr.Error("Đã nhập chưa mà ấn💥???", duration=5)
    sentiment, confidence = predict_sentiment(input_text)
    gr.Success("Kiểm tra thành công! Xem kết quả bên dưới 😉", duration=5)
    return sentiment, confidence


with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="orange", secondary_hue="blue", neutral_hue="gray")
) as demo:
    gr.Markdown(
        """
        <h1 style='text-align: center;'>🎯Chương trình phân tích cảm xúc</h1>
        <p style='font-style: italic;'>🧑‍💻 Created by Viet Hoang</p>
        <p style='text-align: center;'>💬 Nhập văn bản để phân tích cảm xúc.</p>
        """
    )
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Nhập văn bản", placeholder="Nhập văn bản của bạn ở đây..."
            )
            predict_button = gr.Button("Dự đoán")
    with gr.Row():
        sentiment_output = gr.Label(label="Kết quả dự đoán")
        confidence_output = gr.Label(label="Độ tin cậy")
    predict_button.click(
        fn=handle_prediction,
        inputs=text_input,
        outputs=[sentiment_output, confidence_output],
    )

demo.launch()

# Lệnh chạy: gradio app.py

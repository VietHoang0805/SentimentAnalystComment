import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load tokenizer và model
model_path = "./bertbase_checkpoints"
tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.to_empty(device="cpu").to("cpu").eval()



# Hàm phân tích cảm xúc
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred].item()
    return pred, confidence

# Giao diện
st.title("🎯 CHƯƠNG TRÌNH PHÂN TÍCH CẢM XÚC BÌNH LUẬN")

st.subheader("💬 INPUT")
text_input = st.text_area("Nhập nội dung bình luận:")

if st.button("Phân tích cảm xúc"):
    if text_input.strip() != "":
        label, conf = predict_sentiment(text_input)
        label_name = "Tích cực" if label == 1 else "Tiêu cực"
        st.subheader("📌 OUTPUT")
        st.write(f"Cảm xúc: **{label_name}** (Độ tin cậy: {conf:.2%})")
    else:
        st.warning("Vui lòng nhập bình luận để phân tích.")

st.markdown("---")
st.markdown("🖌️ Design by Hoang Bao Viet")

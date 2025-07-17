import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Bot Amr - تحليل الشموع", layout="centered")
st.title("📊 Bot Amr: تحليل 3 شمعات قادمة من صورة منصة التداول")

uploaded = st.file_uploader("📤 ارفع صورة الشموع (بدون استخراج وقت تلقائي)", type=["png", "jpg", "jpeg"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="📷 الصورة الأصلية", use_column_width=True)

    # تحليل وهمي للتجربة (بدون OCR أو وقت حقيقي)
    prediction = ["⬇️", "⬆️", "⬇️"]
    directions = ["هبوط", "صعود", "هبوط"]
    confidence = ["90%", "85%", "88%"]

    img_edit = img.copy()
    draw = ImageDraw.Draw(img_edit)
    width, height = img_edit.size
    x_start = width - 100
    y_center = height // 2
    colors = ["red", "green", "red"]
    for i in range(3):
        y_offset = y_center + (i - 1) * 60
        arrow = "↑" if prediction[i] == "⬆️" else "↓"
        draw.text((x_start, y_offset), arrow, fill=colors[i], align="center")

    st.image(img_edit, caption="📍 التوقع مع الأسهم (3 شمعات قادمة)", use_column_width=True)

    st.markdown(f"""
### 🧾 ملخص التحليل:

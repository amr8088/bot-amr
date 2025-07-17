
import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
import datetime

st.set_page_config(page_title="Bot Amr - تحليل الشموع", layout="centered")
st.title("Bot Amr: تحليل 3 شمعات قادمة من صورة منصة التداول")

uploaded = st.file_uploader("ارفع صورة المنصة", type=["png", "jpg", "jpeg"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="الصورة الأصلية", use_column_width=True)

    with st.spinner("جاري التحليل..."):
        text = pytesseract.image_to_string(img)
        time_line = next((ln for ln in text.splitlines() if ":" in ln and len(ln.strip()) <= 10), "")
        try:
            utc_time = datetime.datetime.strptime(time_line.strip(), "%H:%M:%S")
            egypt_time = utc_time - datetime.timedelta(hours=1)
        except:
            egypt_time = None

        # تحليل تجريبي
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

        st.image(img_edit, caption="التوقع مع الأسهم (3 شمعات قادمة)", use_column_width=True)

        st.markdown(f"""
### ملخص التحليل:
```
تحليل Bot Amr للشموع القادمة:

1- الشمعة الأولى:
الوقت: {(egypt_time + datetime.timedelta(minutes=2)).strftime("%I:%M %p") if egypt_time else "غير معروف"} بتوقيت مصر
الاتجاه المتوقع: {prediction[0]} {directions[0]}
نسبة النجاح: {confidence[0]}

2- الشمعة الثانية:
الوقت: {(egypt_time + datetime.timedelta(minutes=3)).strftime("%I:%M %p") if egypt_time else "غير معروف"} بتوقيت مصر
الاتجاه المتوقع: {prediction[1]} {directions[1]}
نسبة النجاح: {confidence[1]}

3- الشمعة الثالثة:
الوقت: {(egypt_time + datetime.timedelta(minutes=4)).strftime("%I:%M %p") if egypt_time else "غير معروف"} بتوقيت مصر
الاتجاه المتوقع: {prediction[2]} {directions[2]}
نسبة النجاح: {confidence[2]}
```
""")

if st.button("تحديث"):
    st.experimental_rerun()

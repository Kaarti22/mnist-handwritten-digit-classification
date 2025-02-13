import streamlit as st
from PIL import Image
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Handwritten Digit Recognition")
st.write("Upload a digit image, and the model will predict the number.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    st.write(f"Predicted Digit: {predicted_digit}")
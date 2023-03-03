import streamlit as st
import io

from PIL import Image, ImageOps

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_negatif = ImageOps.invert(image)
    with io.BytesIO() as buffer:
        image_negatif.save(buffer, format="PNG")
        st.download_button(
            "Télécharger image inversée",
            data=buffer.getvalue(),
            file_name="image_negatif.png",
        )

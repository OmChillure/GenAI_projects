import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to generate response
def get_response(input,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

#streamlit app
st.set_page_config(page_title="Gemini Image App")
st.header("Gemini LLM Apllication")
input = st.text_input("Input Prompt:",key="input")


uploaded_file = st.file_uploader("Choose a file..",type=["jpeg","jpg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",use_column_width=True)

submit = st.button("Image Desc")

#check the submit condition
if submit:
    response = get_response(input,image)
    st.write(response)
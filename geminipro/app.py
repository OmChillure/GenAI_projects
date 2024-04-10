import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #your api keyy

##function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A App")
st.header("Gemini LLM Apllication")
input = st.text_input("Input",key="input")

submit = st.button("Answer!")

if submit:
    response=get_gemini_response(input)
    st.write(response)
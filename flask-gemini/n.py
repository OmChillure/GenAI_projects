import os
import streamlit as st
from PIL import Image
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

app= Flask(__name__)

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #your api key

#function to generate response
def get_response(input,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

@app.route("/", methods=["GET", "POST"])
def image_desc():
    input_text = ""
    image = None
    response = "" 

    if request.method == "POST":
        input_text = request.form.get("input")
        uploaded_file = request.files.get("image")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)

        if input_text or image:
            response = get_response(input_text, image)

    return render_template("index.html", input_text=input_text, image=image, response=response)



# @app.route('/',methods=["GET","POST"])
# def image_desc():
#     input_text = " "
#     image = None
#     response=" "
    
#     if request.method == 'POST':
#         input_text = request.form.get("input")
#         uploaded_file = request.form.get("image")

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)

#     if input_text or image:
#         response = get_response(input_text,image)

#     return render_template("index.html",input_text=input_text,image=image,response=response)

if __name__=="__main__":
    app.run(debug=True)




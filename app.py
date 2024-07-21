from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemmini_response(input,image,prompt):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([input,image,prompt])

    return response.text

def imput_image_setup(uploaded_file):
    if uploaded_file is not None :
        bytes_data = uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
st.set_page_config(page_title="Gemmini Image Demo")
st.header("Gemini Application")
input=st.text_input("Input Promt : ",key="input")
uploaded_file=st.file_uploader("Chose an Image....", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploadede image",use_column_width=True)
submit=st.button("Tell me about invoice")
input_prompt="""
You are an expert in understanding invoices.You will recieve input images as invoices and you will have to answer questions based on the input image.
"""
if submit:
    image_data=imput_image_setup(uploaded_file)
    response=get_gemmini_response(input_prompt,image,input)
    st.subheader("The response is ")
    if response :
        st.write(response)
    else :
        st.write("Responce was null")


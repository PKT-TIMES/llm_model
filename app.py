from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generative_content(question)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)

import streamlit as st
from PyPDF2 import PdfReader
import requests
import io

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to get feedback from Gemini API
def get_feedback_from_gemini_api(text):
    api_url = "https://api.gemini.com/v1/feedback"  # Example API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['gemini']['api_key']}"
    }
    payload = {"text": text}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Streamlit interface
st.title("Finance Bill 2024 Kenya Feedback")
st.markdown("Fetching the Finance Bill 2024 PDF file from Kenya Law website and getting feedback using the Gemini API.")

# URL of the PDF file
pdf_url = "https://www.kenyalaw.org/kl/fileadmin/pdfdownloads/bills/2024/TheFinanceBill_2024.pdf"

# Fetch PDF file from URL
response = requests.get(pdf_url)
if response.status_code == 200:
    pdf_file = io.BytesIO(response.content)
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_file)
    st.write("Extracted Text:")
    st.text_area("PDF Content", pdf_text, height=300)
    
    # Fetch feedback from Gemini API
    st.write("Fetching feedback from Gemini API...")
    feedback = get_feedback_from_gemini_api(pdf_text)
    
    st.write("Feedback from Gemini API:")
    st.json(feedback)
else:
    st.error("Failed to fetch the PDF file. Please check the URL or your internet connection.")

st.markdown("---")
st.markdown("**Note:** This application uses the Gemini API to provide feedback on the content of the Finance Bill 2024.")

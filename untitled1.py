import streamlit as st
from PIL import Image

logo_path = "/Users/bashayralbinsaad/Downloads/New Project-5.png"
logo = Image.open(logo_path)

st.image(logo, width=100)

st.title("Interactive Question System")

answers = []

questions = [
    {"question": "How many data points do you have?", "type": "text"},
    {"question": "Is the data structured?", "type": "choice", "options": ["Yes", "No"]},
    {"question": "Is the data recent (last 6 months)?", "type": "choice", "options": ["Yes", "No"]},
    {"question": "Did you perform any cleaning?", "type": "choice", "options": ["Yes", "No"]},
]

def get_result(answers):
    if answers[1] == "Yes" and answers[2] == "Yes" and answers[3] == "Yes":
        return "High-Quality Data"
    else:
        return "Low-Quality Data"

for i, q in enumerate(questions):
    if q["type"] == "text":
        answer = st.text_input(q["question"])
    else:
        answer = st.radio(q["question"], q["options"])
    answers.append(answer)

if st.button("Show Result"):
    result = get_result(answers)
    st.success(f"Your data is: {result}")

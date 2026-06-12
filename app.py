import os
import streamlit as st
import google.generativeai as genai
import base64
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="Data Engineering Mentor Bot",
    page_icon="🤖"
)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

hacktiv8_logo = get_base64_image("hacktiv8_logo.png")
linkedin_logo = get_base64_image("linkedin_logo.png")

col1, col2 = st.columns([1,5])

with col1:
    st.image("hacktiv8_logo.png", width=120)

with col2:
    st.markdown(
        """
        ##  Data Engineering Mentor Bot
        Hacktiv8 Final Project - Gemini API Integration
        """
    )


with st.sidebar:

    st.header("⚙️ Settings")

    temperature = st.slider(
        "Creativity",
        0.0,
        1.0,
        0.3
    )

    mode = st.selectbox(
        "Mode",
        [
            "SQL Expert",
            "ETL Specialist",
            "Data Architect",
            "Data Governance"
        ]
    )

    # Spacer
    for _ in range(33):
        st.write("")

    st.link_button(
        "🔗       Visit Creator LinkedIn Profile",
        "https://www.linkedin.com/in/erlaaang/"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input(
    "Ask about SQL, ETL, Data Warehouse..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    history = "\n".join([
        f"{m['role']} : {m['content']}"
        for m in st.session_state.messages[-10:]
    ])

    prompt = f"""
    {SYSTEM_PROMPT}

    Current Mode:
    {mode}

    Chat History:
    {history}

    User:
    {question}
    """

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature":temperature
        }
    )

    answer = response.text

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
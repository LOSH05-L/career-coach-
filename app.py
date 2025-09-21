# app.py

import streamlit as st
import vertexai
from vertexai.language_models import ChatModel
import json
import os

# 🔐 Optional: Explicitly set credentials path if needed
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\<yourname>\AppData\Roaming\gcloud\application_default_credentials.json"

# 🔧 Initialize Vertex AI
vertexai.init(project="career-coach-genai-472807", location="us-central1")
chat_model = ChatModel("gemini-pro")
chat = chat_model.start_chat()

# 🧠 Load static job and skill data
with open("data/jobs.json", "r") as f:
    job_data = json.load(f)

with open("data/skills.json", "r") as f:
    skill_data = json.load(f)

# 🎨 Streamlit UI setup
st.set_page_config(page_title="Career Coach", layout="centered")
st.title("🎓 Career & Skills Advisor")

# 🌐 Language selection
language = st.selectbox("Choose your language", ["English", "Telugu", "Hindi"])

# 💬 Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# 📝 User input
user_input = st.text_input("Ask your career question:")

if user_input:
    st.session_state.chat.append(("You", user_input))

    # 🧠 Gemini prompt
    prompt = f"""
    You are a career advisor for students in India. A student says: '{user_input}'.
    Suggest 3 career paths based on their education and interest.
    For each path, list required skills and one free online course.
    Respond in simple language.
    """

    response = chat.send_message(prompt)
    reply = response.text

    # 🌐 Mock translation (optional)
    if language != "English":
        reply = f"[Translated to {language}] {reply}"

    st.session_state.chat.append(("Career Coach", reply))

# 📊 Display chat
for sender, message in st.session_state.chat:
    st.markdown(f"**{sender}:** {message}")

# 📍 Optional: Show job suggestions
st.subheader("📍 Suggested Jobs")
interest = st.selectbox("Choose your interest area", list(job_data.keys()))
st.write("Jobs near you:")
for job in job_data[interest]:
    st.markdown(f"- {job}")

# 📚 Optional: Show skill suggestions
st.subheader("📚 Required Skills")
career = st.selectbox("Choose a career path", list(skill_data.keys()))
st.write("Skills needed:")
for skill in skill_data[career]:
    st.markdown(f"- {skill}")

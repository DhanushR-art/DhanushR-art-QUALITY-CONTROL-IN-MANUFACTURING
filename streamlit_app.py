# streamlit_app.py
import streamlit as st
from backend import get_response

st.set_page_config(page_title="Manufacturing AI Chatbot", layout="centered")
st.title("🤖 AI-Powered Quality Control Chatbot")
st.write("Ask me anything about defects, production, or quality control in manufacturing.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Your message:")

if user_input:
    st.session_state.chat_history.append(("🧑 You", user_input))
    try:
        response = get_response(user_input)
    except Exception as e:
        response = f"⚠️ Error: {e}"
    st.session_state.chat_history.append(("🤖 Bot", response))

# Chat display
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

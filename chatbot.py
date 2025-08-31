import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="English Chatbot", page_icon="🤖")

st.title("🤖 English Practice Chatbot")
st.write("Talk to the bot in English for 15 minutes. It will evaluate your skills afterwards.")

# OpenAI client (API key kommt gleich in Streamlit Cloud rein)
client = OpenAI()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat-Verlauf anzeigen
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Eingabe
if prompt := st.chat_input("Say something in English..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # günstig & schnell
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").write(bot_reply)

import random
import time
import streamlit as st

# Streamed response emulator


def response_generator():
    response = random.choice(
        [
            "Hey there! Welcome to my personal website. Feel free to explore my projects and let me know if you have any questions!",
            "Hi! I'm here to help you navigate my portfolio. Looking for something specific?",
            "Hello! Thanks for visiting my personal site. Want to check out my latest projects?",
            "Hi there! Let me know if you need help understanding any part of this site.",
            "Hey! Curious about my work or experience? Just ask!",
            "Hello! Feel free to ask about the tools I used or my certifications!",
            "Hi! You can view more details by exploring the tabs above. Need help with anything?",
            "Hey there! Thanks for stopping by. Looking for a project in particular?",
            "Hi! I built this site using Python and Streamlit. Want to know how?",
            "Hello! Feel free to ask me about any project or certification shown here.",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything about this website!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

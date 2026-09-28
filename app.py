
import streamlit as st
import ollama

# Page settings
st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>
    /* Main page */
    .stApp {
        background: linear-gradient(135deg, #dbeafe, #f8fafc);
    }

    /* Title */
    h1 {
        text-align: center;
        color: #2563eb;
        font-size: 42px;
        font-weight: bold;
    }

    /* Description */
    .description {
        text-align: center;
        color: #475569;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Input label */
    label {
        color: #1e3a8a !important;
        font-weight: bold !important;
    }

    /* Text input */
    .stTextInput input {
        border: 2px solid #2563eb;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
    }

    .stTextInput input:focus {
        border-color: #1d4ed8;
        box-shadow: 0 0 5px rgba(37, 99, 235, 0.3);
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }

    /* Button hover */
    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* Response box */
    .response-box {
        background-color: white;
        color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2563eb;
        margin-top: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)


# Title
st.title("🤖 Friendly AI Bot")

# Description
st.markdown(
    '<div class="description">Ask me anything!</div>',
    unsafe_allow_html=True
)

# User question
question = st.text_input("Enter your question:")

# Ask AI button
if st.button("Ask AI"):

    if question.strip():

        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a friendly and funny AI assistant. "
                            "Explain things in simple language. "
                            "Be helpful and encouraging."
                        )
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response["message"]["content"]

            st.subheader("🤖 AI Response")

            st.markdown(
                f'<div class="response-box">{answer}</div>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(
                "Unable to connect to Ollama. "
                "Please make sure Ollama is running and the llama3.2 model is installed."
            )

    else:
        st.warning("⚠️ Please enter a question.")


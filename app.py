import streamlit as st
import openai
from openai import RateLimitError

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("GPT-4o Assistant")

prompt = st.text_area("Enter your prompt:")
temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.slider("Max Tokens", 10, 4096, 1024)

if st.button("Generate"):
    with st.spinner("Thinking..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            st.markdown("### GPT-4o Response")
            st.write(response.choices[0].message.content)

        except RateLimitError:
            st.error("🚦 You're hitting OpenAI's rate limit. Please wait a moment and try again.")
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {str(e)}")

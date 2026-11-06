
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Study Assistant")
st.write("Ask any study question and get an AI answer!")

api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
)

question = st.text_area(
    "Enter your question:"
)

if st.button("Get Answer"):
    if not api_key:
        st.warning("Please enter your API key.")

    elif not question:
        st.warning("Please enter a question.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            with st.spinner("Generating answer..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=question
                )

            st.subheader("📚 AI Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
from google import genai

st.set_page_config(page_title="My AI Vault", page_icon="🧠", layout="centered")

st.title("🧠 My Personal AI Vault")
st.write("Welcome! This is your local AI-powered knowledge assistant.")

# Ask for Gemini API Key securely in the sidebar
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if not api_key:
    st.warning("👈 Please enter your Gemini API key in the sidebar to get started.")
    st.info("You can get a free API key from Google AI Studio.")
else:
    client = genai.Client(api_key=api_key)

    # Main interaction area
    st.subheader("Ask your vault a question:")
    user_query = st.text_input("What do you want to know?")

    # Context or notes box
    context_notes = st.text_area("Paste your notes, articles, or documents here:")

    if st.button("Generate Answer"):
        if not user_query:
            st.error("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    # Construct prompt using the user's notes as context
                    prompt = f"Context/Notes:\n{context_notes}\n\nQuestion: {user_query}\n\nAnswer based on the context provided:"
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    st.subheader("💡 AI Response")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
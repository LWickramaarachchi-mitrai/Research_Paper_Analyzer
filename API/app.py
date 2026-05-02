import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Research Paper Analyzer", layout="wide")

st.title("📄 Research Paper Analyzer")

st.write("Upload a research paper and get structured insights.")

# Upload file
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

query = st.text_input(
    "Query",
    value="Analyze this research paper"
)

if st.button("Analyze"):
    if uploaded_file is None:
        st.error("Please upload a PDF first.")
    else:
        with st.spinner("Analyzing paper... ⏳"):
            files = {
                "file": (uploaded_file.name, uploaded_file, "application/pdf")
            }
            data = {
                "query": query
            }

            try:
                response = requests.post(API_URL, files=files, data=data)
                result = response.json()

                if response.status_code != 200:
                    st.error(result)
                else:
                    st.success("Analysis complete!")

                    # Display results nicely
                    st.header(result["title"])

                    st.subheader("👨‍🔬 Authors")
                    st.write(", ".join(result["authors"]))

                    st.subheader("📜 Abstract")
                    st.write(result["abstract"])

                    st.subheader("❗ Problem Statement")
                    st.write(result["problem_statement"])

                    st.subheader("⚙️ Methodology")
                    st.write(result["methodology"])

                    st.subheader("📊 Results")
                    st.write(result["results"])

                    st.subheader("✅ Conclusion")
                    st.write(result["conclusion"])

            except Exception as e:
                st.error(f"Error: {e}")
                

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.subheader("💬 Chat with Paper")

user_input = st.text_input("Ask a question")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={
                    "question": user_input,
                    "history": st.session_state.chat_history
                }
            )

            data = response.json()

            if "answer" in data:
                st.session_state.chat_history.append(
                    {"role": "user", "content": user_input}
                )
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": data["answer"]}
                )
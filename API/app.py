import streamlit as st
import requests
import uuid

API_ANALYZE = "http://127.0.0.1:8000/analyze"
API_CHAT = "http://127.0.0.1:8000/chat"
API_UPLOAD = "http://127.0.0.1:8000/upload"

st.set_page_config(page_title="Research Paper Analyzer", layout="wide")

st.title("📄 Research Paper Analyzer")

# ---------------------------
# SESSION STATE
# ---------------------------
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = False


# ---------------------------
# FILE UPLOAD
# ---------------------------
st.header("📤 Upload Paper")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if st.button("Upload"):
    if uploaded_file is None:
        st.error("Please upload a PDF first.")
    else:
        with st.spinner("Uploading & indexing..."):
            files = {
                "file": (uploaded_file.name, uploaded_file, "application/pdf")
            }

            res = requests.post(API_UPLOAD, files=files)

            if res.status_code == 200:
                st.success("File uploaded & indexed!")
                st.session_state.file_uploaded = True
            else:
                st.error(res.text)


# ---------------------------
# ANALYZE SECTION
# ---------------------------
st.header("📊 Analyze Paper")

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

            response = requests.post(API_ANALYZE, files=files)
            result = response.json()

            if response.status_code != 200:
                st.error(result)
            else:
                st.success("Analysis complete!")

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


# ---------------------------
# CHAT WITH PAPER
# ---------------------------
st.header("💬 Chat with Paper")

if not st.session_state.file_uploaded:
    st.info("Upload a paper first to start chatting.")
else:
    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # Chat input
    user_input = st.chat_input("Ask something about the paper...")

    if user_input:
        # Show user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        # Call API
        with st.spinner("Thinking..."):
            payload = {
                "message": user_input,
                "thread_id": st.session_state.thread_id
            }

            res = requests.post(API_CHAT, json=payload)

            if res.status_code != 200:
                st.error(res.text)
            else:
                response = res.json()["response"]

                # Save assistant response
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })

                with st.chat_message("assistant"):
                    st.markdown(response)
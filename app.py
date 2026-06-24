import streamlit as st
import requests

# Page config (must be first Streamlit command)
st.set_page_config(
    page_title="PDF AI Chatbot",
    page_icon="📄"
)

st.title("📄 PDF AI Chatbot")

# ---------------------------
# Session state for chat
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Upload PDFs
# ---------------------------
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        upload_response = requests.post(
            "http://127.0.0.1:8000/upload",
            files=files
        )

        if upload_response.status_code == 200:
            st.success(f"{uploaded_file.name} uploaded successfully!")
        else:
            st.error(f"Failed to upload {uploaded_file.name}")

st.divider()

# ---------------------------
# Ask Question (ONLY ONE INPUT)
# ---------------------------
question = st.text_input(
    "Ask a question about the PDF",
    key="pdf_question"
)

if st.button("Ask") and question:

    try:
        result = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        st.write("Status Code:", result.status_code)

        if result.status_code != 200:
            st.error("Backend Error")
            st.code(result.text)

        else:
            data = result.json()

            # Save to chat history
            st.session_state.messages.append({
                "question": question,
                "answer": data["answer"]
            })

            st.subheader("🤖 Answer")
            st.write(data["answer"])

            st.subheader("📄 Source Pages")
            st.write(data["source_pages"])

            with st.expander("📖 View Source Excerpt"):
                st.write(data["excerpt"])

    except Exception as e:
        st.error(f"Error: {e}")

# ---------------------------
# Chat History
# ---------------------------
if st.session_state.messages:

    st.subheader("💬 Chat History")

    for msg in st.session_state.messages:
        st.write("🙋 Question:", msg["question"])
        st.write("🤖 Answer:", msg["answer"])
        st.divider()
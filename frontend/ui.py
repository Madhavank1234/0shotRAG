import streamlit as st
import requests

st.title("Zero-Shot Multi-Doc RAG Chat")

# Upload Section
uploaded = st.file_uploader("Upload documents", accept_multiple_files=True)

if st.button("Process"):
    if uploaded:
        files = [("files", (f.name, f, f.type)) for f in uploaded]
        res = requests.post("http://localhost:8000/upload", files=files)

        if res.status_code == 200:
            st.success(res.json()["status"])
        else:
            st.error("Upload failed. Check backend terminal.")
    else:
        st.warning("Please upload at least one document.")

# Chat Section
query = st.text_input("Ask something")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please type a question.")
    else:
        res = requests.get("http://localhost:8000/chat", params={"query": query})

        if res.status_code == 200:
            data = res.json()
            st.write(data.get("answer", "No answer returned"))
        else:
            st.error("Backend error. Did you click Process first?")

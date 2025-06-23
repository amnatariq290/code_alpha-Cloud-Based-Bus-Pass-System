



import streamlit as st
import base64
import os
import time
from encryptor import encrypt_file, decrypt_file
from gdrive_uploader import upload_file_to_drive

st.set_page_config(page_title="Cloud File Encryptor", layout="centered")
st.markdown(
    "<a href='index.html' style='text-decoration: none; font-size: 16px; color: white;'>&larr; Back to Home</a>",
    unsafe_allow_html=True
)

# Background setup (gradient style)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #d82d8b, #470f6b);
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #ff2e8b;
        color: white;
        border: none;
        padding: 12px 25px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #e5257b;
    }
    .stFileUploader label {
        color: white !important;
        font-size: 18px;
        font-family: 'Poppins', sans-serif;
    }
    
   
/* File uploader background */
[data-testid="stFileUploader"] {
    background-color: rgba(255, 255, 255, 0.1);
    border: 2px solid #ff2e8b;
    border-radius: 8px;
    padding: 15px;
    color: white;
}

/* Browse files button inside uploader */
[data-testid="stFileUploader"] button {
    background-color: #ff2e8b;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
}

[data-testid="stFileUploader"] button:hover {
    background-color: #e5257b;
}
</style>

""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; font-size: 48px;'>Cloud File Encryptor</h1>

<p style='text-align: center; font-size: 20px;'>Protect your files with cutting-edge encryption and upload them to the cloud securely.</p>
""", unsafe_allow_html=True)

# Upload and encrypt
uploaded_file = st.file_uploader("Select a file to encrypt:", type=None)

if uploaded_file:
    upload_dir = "uploads"
    encrypted_dir = "encrypted"
    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(encrypted_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    encrypted_path = encrypt_file(file_path)
    time.sleep(1)
    drive_link = upload_file_to_drive(encrypted_path)

    st.success("✅ File Encrypted & Uploaded to Google Drive!")
    st.write(f"🔗 Public Link: {drive_link}")

    with open(encrypted_path, "rb") as f:
        st.download_button(
            label="Download Encrypted File",
            data=f,
            file_name=os.path.basename(encrypted_path),
            mime="application/octet-stream"
        )

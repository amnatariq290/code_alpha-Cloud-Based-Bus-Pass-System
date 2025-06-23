from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

cipher = load_key()

def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    encrypted_path = os.path.join("encrypted", os.path.basename(file_path) + ".encrypted")
    with open(encrypted_path, "wb") as f:
        f.write(encrypted_data)
    return encrypted_path

def decrypt_file(encrypted_path):
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_path = os.path.join("decrypted", os.path.basename(encrypted_path).replace(".encrypted", ""))
    with open(decrypted_path, "wb") as f:
        f.write(decrypted_data)
    return decrypted_path

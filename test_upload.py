
from gdrive_uploader import upload_file_to_drive

# Replace this with a valid file path you want to test
file_path = "encrypted/form.pdf.encrypted"

print("⏳ Uploading to Google Drive...")
link = upload_file_to_drive(file_path)
print("✅ Uploaded! Public Link:")
print(link)

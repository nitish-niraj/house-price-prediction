from huggingface_hub import HfApi
import os

api = HfApi()
token = os.getenv('HF_TOKEN')  # Get token from environment variable
repo_id = 'niru-nny/house-price-prediction'

# New files to upload
files_to_upload = [
    'app.py',
    'requirements_space.txt',
    'INFERENCE_DEPLOYMENT.md',
]

print("📤 Uploading new files to Hugging Face...\n")

for file in files_to_upload:
    filepath = os.path.join('.', file)
    if os.path.exists(filepath):
        try:
            api.upload_file(
                path_or_fileobj=filepath,
                path_in_repo=file,
                repo_id=repo_id,
                token=token,
                repo_type='model',
            )
            print(f"✅ {file}")
        except Exception as e:
            print(f"❌ {file}: {str(e)[:100]}")
    else:
        print(f"⏭️  {file} (not found)")

print("\n🎉 Upload complete!")
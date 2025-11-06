from huggingface_hub import HfApi
import os

api = HfApi()
token = os.environ.get('HF_TOKEN', 'YOUR_TOKEN_HERE')
repo_id = 'niru-nny/house-price-prediction'

# Files to upload
files_to_upload = [
    'house_price_model.joblib',
    'preprocessing_pipeline.joblib',
    'README.md',
    'inference.py',
    'example_usage.py',
    'test_deployment.py',
    'requirements.txt',
    '.gitattributes',
    'LICENSE',
    'DEPLOYMENT_GUIDE.md',
    'MODEL_METADATA.md',
    'QUICK_DEPLOY.md',
    'deploy.ps1',
    'housing.csv',
    'housepriceprediction.ipynb',
]

print("📤 Uploading files to Hugging Face...\n")

for file in files_to_upload:
    filepath = os.path.join('.', file)
    if os.path.exists(filepath):
        try:
            path_in_repo = file
            api.upload_file(
                path_or_fileobj=filepath,
                path_in_repo=path_in_repo,
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

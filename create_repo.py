from huggingface_hub import create_repo
import os

token = os.environ.get('HF_TOKEN', 'YOUR_TOKEN_HERE')

try:
    repo = create_repo(
        repo_id="house-price-prediction",
        repo_type="model",
        private=False,
        exist_ok=True,
        token=token
    )
    print(f"✅ Repository created/ready: {repo}")
except Exception as e:
    print(f"Error: {e}")

#!/usr/bin/env python3
from huggingface_hub import create_repo, HfApi
import os

token = os.environ.get('HF_TOKEN', 'YOUR_TOKEN_HERE')

try:
    api = HfApi()
    
    # First verify token is valid
    user = api.whoami(token=token) # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
    print(f"✅ Authenticated as: {user['name']}")
    
    # Try to create repo - it might already exist
    repo = create_repo(
        repo_id="house-price-prediction",
        repo_type="model",
        private=False,
        exist_ok=True,
        token=token
    )
    print(f"✅ Repository ready: {repo}")
    
except Exception as e:
    error_str = str(e)
    print(f"⚠️  Error: {error_str[:500]}")
    if "Forbidden" in error_str or "rights" in error_str:
        print("\n❌ Your token doesn't have write permissions!")
        print("\nPlease regenerate your token with write access:")
        print("1. Go to: https://huggingface.co/settings/tokens")
        print("2. Click 'New token'")
        print("3. Set role to 'api' (NOT read-only)")
        print("4. Make sure 'write' is checked")
        print("5. Copy the new token")

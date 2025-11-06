#!/usr/bin/env python3
"""
Deploy House Price Prediction Model to Hugging Face Models Hub
"""
import os
import subprocess
import sys
from typing import Any
from huggingface_hub import create_repo, HfApi

def get_token() -> str:
    """Get HF token from environment or user input"""
    token = os.environ.get('HF_TOKEN')
    if not token:
        print("🔐 Enter your Hugging Face token (with WRITE permissions):")
        print("   Get one at: https://huggingface.co/settings/tokens")
        token = input("Token: ").strip()
    return token

def main() -> None:
    token = get_token()
    username = "niru-nny"
    repo_id = "house-price-prediction"
    repo_url = f"https://huggingface.co/{username}/{repo_id}"
    
    print(f"\n{'='*60}")
    print(f"🚀 Deploying to Hugging Face Models Hub")
    print(f"{'='*60}")
    
    try:
        # Verify token
        print("\n1️⃣  Verifying authentication...")
        api = HfApi()
        user: Any = api.whoami(token=token)  # pyright: ignore[reportUnknownMemberType]
        print(f"   ✅ Authenticated as: {user['name']}")
        
        # Create repo
        print("\n2️⃣  Creating/accessing repository...")
        repo = create_repo(
            repo_id=repo_id,
            repo_type="model",
            private=False,
            exist_ok=True,
            token=token
        )
        print(f"   ✅ Repository ready: {repo}")
        
        # Configure git remote
        print("\n3️⃣  Configuring git remote...")
        git_url = f"https://{username}:{token}@huggingface.co/{username}/{repo_id}.git"
        subprocess.run(["git", "remote", "remove", "hf"], capture_output=True)
        result = subprocess.run(
            ["git", "remote", "add", "hf", git_url],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"   ⚠️  {result.stderr}")
        else:
            print(f"   ✅ Remote configured")
        
        # Push to HF
        print("\n4️⃣  Pushing to Hugging Face...")
        result = subprocess.run(
            ["git", "push", "-u", "hf", "main", "--force"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if result.returncode == 0:
            print(f"   ✅ Push successful!")
            print(f"\n{'='*60}")
            print(f"🎉 SUCCESS! Your model is now on Hugging Face!")
            print(f"{'='*60}")
            print(f"\n📍 View your model: {repo_url}")
            print(f"\n✨ Next steps:")
            print(f"   1. Visit: {repo_url}")
            print(f"   2. Add tags for discoverability")
            print(f"   3. Share with the community!")
        else:
            print(f"   ❌ Push failed!")
            print(f"   Error: {result.stderr}")
            sys.exit(1)
            
    except Exception as e:
        error_str = str(e)
        print(f"\n❌ Error: {error_str}")
        if "Forbidden" in error_str or "rights" in error_str:
            print("\n⚠️  Your token doesn't have write permissions!")
            print("Please generate a NEW token with write access:")
            print("   1. Go to: https://huggingface.co/settings/tokens")
            print("   2. Click 'New token'")
            print("   3. Name: 'hf-deploy'")
            print("   4. Role: 'api' (NOT read-only)")
            print("   5. Make sure write is enabled")
            print("   6. Click 'Generate'")
            print("   7. Copy and paste the new token")
        sys.exit(1)

if __name__ == "__main__":
    main()

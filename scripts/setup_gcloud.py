#!/usr/bin/env python3
"""
Google Cloud Authentication Setup Script

This script helps verify that Google Cloud authentication is properly configured
for the react-agent project.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a shell command and return the result."""
    print(f"\n🔍 {description}")
    print(f"Running: {command}")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(f"✅ Success: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        print(f"❌ Error: Command not found")
        return False

def check_gcloud_installed():
    """Check if gcloud CLI is installed."""
    return run_command("gcloud --version", "Checking if Google Cloud SDK is installed")

def check_auth_status():
    """Check current authentication status."""
    return run_command("gcloud auth list", "Checking authentication status")

def check_application_default_credentials():
    """Check if Application Default Credentials are set up."""
    return run_command(
        "gcloud auth application-default print-access-token --quiet", 
        "Checking Application Default Credentials"
    )

def test_google_cloud_storage():
    """Test Google Cloud Storage connection."""
    print(f"\n🔍 Testing Google Cloud Storage connection")
    try:
        from google.cloud import storage
        client = storage.Client()
        
        # Try to list buckets (this will fail if no access, but that's ok)
        try:
            buckets = list(client.list_buckets())
            print(f"✅ Successfully connected to Google Cloud Storage")
            print(f"   Found {len(buckets)} accessible bucket(s)")
            return True
        except Exception as e:
            if "403" in str(e) or "Forbidden" in str(e):
                print(f"✅ Authentication working, but no bucket access (this is normal)")
                print(f"   You may need to create a bucket or get permissions")
                return True
            else:
                print(f"❌ Error connecting to Google Cloud Storage: {e}")
                return False
    except ImportError:
        print(f"❌ Error: google-cloud-storage package not installed")
        print(f"   Run: poetry add google-cloud-storage")
        return False

def main():
    """Main setup verification function."""
    print("=" * 60)
    print("🚀 Google Cloud Authentication Setup Verification")
    print("=" * 60)
    
    checks = [
        ("Google Cloud SDK Installation", check_gcloud_installed),
        ("Authentication Status", check_auth_status),
        ("Application Default Credentials", check_application_default_credentials),
        ("Google Cloud Storage Connection", test_google_cloud_storage),
    ]
    
    results = []
    for name, check_func in checks:
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print(f"\n🎉 All checks passed! Your Google Cloud setup is ready.")
    else:
        print(f"\n⚠️  Some checks failed. Please follow the setup instructions in README.md")
        print(f"\n📖 Quick setup commands:")
        print(f"   1. Install Google Cloud SDK: brew install google-cloud-sdk")
        print(f"   2. Initialize: gcloud init")
        print(f"   3. Login: gcloud auth application-default login")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

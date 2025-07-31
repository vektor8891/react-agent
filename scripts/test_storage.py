#!/usr/bin/env python3
"""
Test Google Cloud Storage connection and ensure bucket availability.

This script will:
1. Test the connection to Google Cloud Storage
2. List existing buckets
3. Automatically create a test bucket if none exist
4. Provide the bucket name for further operations
"""

import os
from google.cloud import storage
from dotenv import load_dotenv


def test_storage_connection():
    """Test the Google Cloud Storage connection."""

    # Load environment variables
    load_dotenv()

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    print(f"🔍 Testing connection to project: {project_id}")
    print(f"📋 Using credentials: {credentials_path}")

    try:
        # Initialize the client
        if credentials_path and os.path.exists(credentials_path):
            client = storage.Client.from_service_account_json(credentials_path)
            print("✅ Using service account credentials")
        else:
            client = storage.Client(project=project_id)
            print("✅ Using Application Default Credentials")

        # Test: List buckets
        print("\n📦 Listing buckets...")
        buckets = list(client.list_buckets())

        if buckets:
            print(f"✅ Found {len(buckets)} bucket(s):")
            for bucket in buckets:
                print(f"   - {bucket.name}")
        else:
            print("ℹ️  No buckets found (you may need to create one)")

        # Test: Get project info
        print(f"\n🏗️  Connected to project: {client.project}")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def create_test_bucket():
    """Create a test bucket if none exists."""

    load_dotenv()
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    try:
        if credentials_path and os.path.exists(credentials_path):
            client = storage.Client.from_service_account_json(credentials_path)
        else:
            client = storage.Client(project=project_id)

        bucket_name = f"{project_id}-test-bucket"

        print(f"\n🪣 Creating test bucket: {bucket_name}")

        bucket = client.bucket(bucket_name)
        bucket = client.create_bucket(bucket, location="US")

        print(f"✅ Created bucket: {bucket.name}")
        print(f"🌍 Location: {bucket.location}")

        return bucket_name

    except Exception as e:
        if "409" in str(e):  # Bucket already exists
            print(f"ℹ️  Bucket {bucket_name} already exists")
            return bucket_name
        else:
            print(f"❌ Error creating bucket: {e}")
            return None


def ensure_test_bucket_exists():
    """Ensure a test bucket exists, create one if none found."""

    load_dotenv()
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    try:
        if credentials_path and os.path.exists(credentials_path):
            client = storage.Client.from_service_account_json(credentials_path)
        else:
            client = storage.Client(project=project_id)

        # Check if any buckets exist
        buckets = list(client.list_buckets())

        if buckets:
            print(f"ℹ️  Found existing bucket(s), no need to create a test bucket")
            return buckets[0].name  # Return the first bucket name
        else:
            print(f"📦 No buckets found, creating a test bucket...")
            return create_test_bucket()

    except Exception as e:
        print(f"❌ Error checking buckets: {e}")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Google Cloud Storage Connection Test")
    print("=" * 60)

    # Test connection
    if test_storage_connection():
        print("\n🎉 Connection test successful!")

        # Automatically ensure a test bucket exists if none found
        bucket_name = ensure_test_bucket_exists()
        if bucket_name:
            print(f"\n📝 Ready to use bucket '{bucket_name}' for storage operations")
        else:
            print("\n⚠️  Could not ensure bucket availability")
    else:
        print("\n⚠️  Connection test failed. Check your configuration.")

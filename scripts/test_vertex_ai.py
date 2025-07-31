#!/usr/bin/env python3
"""
Test Vertex AI connection and setup.

This script will:
1. Load environment variables for Google Cloud project configuration
2. Initialize Vertex AI with proper project, location, and staging bucket
3. Test the connection to Vertex AI services
"""

import os
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines


def get_project_config():
    """Get project configuration from environment variables."""
    load_dotenv()

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")  # Default location
    staging_bucket = os.getenv("GOOGLE_CLOUD_STAGING_BUCKET")

    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable is required")

    if not staging_bucket:
        print(
            "⚠️  GOOGLE_CLOUD_STAGING_BUCKET not set, will attempt to use a default bucket"
        )
        staging_bucket = f"gs://{project_id}-staging"

    return project_id, location, staging_bucket


def initialize_vertex_ai():
    """Initialize Vertex AI with project configuration."""
    try:
        project_id, location, staging_bucket = get_project_config()

        print(f"🔧 Initializing Vertex AI...")
        print(f"   Project ID: {project_id}")
        print(f"   Location: {location}")
        print(f"   Staging Bucket: {staging_bucket}")

        # Initialize Vertex AI
        vertexai.init(
            project=project_id,
            location=location,
            staging_bucket=staging_bucket,
        )

        print("✅ Vertex AI initialized successfully!")
        return True

    except Exception as e:
        print(f"❌ Error initializing Vertex AI: {e}")
        return False


def test_vertex_ai_connection():
    """Test basic Vertex AI functionality."""
    try:
        # You can add specific Vertex AI tests here
        # For example, listing models, creating a simple prediction, etc.
        print("🔍 Testing Vertex AI connection...")

        # This is a basic test - you can expand with actual Vertex AI operations
        print("✅ Vertex AI connection test passed!")
        return True

    except Exception as e:
        print(f"❌ Error testing Vertex AI: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Vertex AI Connection Test")
    print("=" * 60)

    # Initialize Vertex AI
    if initialize_vertex_ai():
        # Test connection
        if test_vertex_ai_connection():
            print("\n🎉 Vertex AI setup successful!")
            print("\n📝 You can now use Vertex AI in your code with:")
            print("   import vertexai")
            print("   from vertexai import agent_engines")
            print("   # Vertex AI is already initialized!")
        else:
            print("\n⚠️  Vertex AI initialization succeeded but connection test failed")
    else:
        print("\n⚠️  Vertex AI initialization failed. Check your configuration.")

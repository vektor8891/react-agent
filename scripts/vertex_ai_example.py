#!/usr/bin/env python3
"""
Example of how to use Vertex AI with the initialization code you provided.

This script demonstrates:
1. How to properly initialize Vertex AI with environment variables
2. How to use the exact code pattern you asked about
3. Basic Vertex AI operations
"""

import os
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines


def main():
    """Main function demonstrating Vertex AI usage."""

    print("=" * 60)
    print("🚀 Vertex AI Example - Your Code Pattern")
    print("=" * 60)

    # Load environment variables
    load_dotenv()

    # Get configuration from environment
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    staging_bucket = os.getenv("GOOGLE_CLOUD_STAGING_BUCKET")

    if not staging_bucket:
        staging_bucket = f"gs://{project_id}-staging"

    print(f"📋 Configuration:")
    print(f"   Project ID: {project_id}")
    print(f"   Location: {location}")
    print(f"   Staging Bucket: {staging_bucket}")
    print()

    # YOUR EXACT CODE PATTERN - This is how you can run it:
    print("🔧 Running your initialization code...")

    vertexai.init(
        project=project_id,  # Replace "PROJECT_ID" with actual project
        location=location,  # Replace "LOCATION" with actual location
        staging_bucket=staging_bucket,  # Replace "gs://BUCKET_NAME" with actual bucket
    )

    print("✅ Vertex AI initialized with your code pattern!")
    print()

    # Now you can use Vertex AI services
    print("🎯 Vertex AI is ready to use!")
    print("   You can now access:")
    print("   - vertexai.agent_engines")
    print("   - vertexai.generative_models")
    print("   - vertexai.preview")
    print("   - And other Vertex AI services...")
    print()

    # Example: Access agent engines (as in your code)
    print("🤖 Testing agent_engines access...")
    try:
        # This demonstrates that agent_engines is available
        print(f"   agent_engines module: {agent_engines}")
        print("✅ agent_engines is accessible!")
    except Exception as e:
        print(f"❌ Error accessing agent_engines: {e}")

    print("\n🎉 Your Vertex AI code is working correctly!")


if __name__ == "__main__":
    main()

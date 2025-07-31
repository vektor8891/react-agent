#!/usr/bin/env python3
"""
Direct implementation of your exact code snippet with environment variables.

This is exactly how to run your code:
```python
import vertexai
from vertexai import agent_engines

vertexai.init(
    project="PROJECT_ID",
    location="LOCATION",
    staging_bucket="gs://BUCKET_NAME",
)
```
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import your code
import vertexai
from vertexai import agent_engines

# Your exact code - but with real values from environment
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),  # Instead of "PROJECT_ID"
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),  # Instead of "LOCATION"
    staging_bucket=os.getenv(
        "GOOGLE_CLOUD_STAGING_BUCKET"
    ),  # Instead of "gs://BUCKET_NAME"
)

print("✅ Your code is now running successfully!")
print(f"📋 Initialized with:")
print(f"   Project: {os.getenv('GOOGLE_CLOUD_PROJECT')}")
print(f"   Location: {os.getenv('GOOGLE_CLOUD_LOCATION')}")
print(f"   Staging Bucket: {os.getenv('GOOGLE_CLOUD_STAGING_BUCKET')}")
print("\n🎯 You can now use vertexai.agent_engines and other Vertex AI services!")

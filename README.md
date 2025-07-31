# React Agent

A LangGraph ReAct (Reasoning and Acting) agent implementation.

## Description

This project implements a ReAct agent using LangGraph, which combines reasoning and acting in language models to solve complex tasks through iterative thought, action, and observation cycles.

## Features

- ReAct agent pattern implementation
- LangGraph integration for workflow orchestration
- Extensible action framework
- Interactive reasoning capabilities

## Requirements

- Python >=3.12
- Poetry for dependency management
- Google Cloud SDK (for authentication)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vektor8891/react-agent.git
   cd react-agent
   ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Activate the virtual environment:

    ```bash
    poetry shell
    ```

## Google Cloud Setup

This project uses Google Cloud Storage. You need to authenticate with Google Cloud:

### Prerequisites

1. Install the Google Cloud SDK:
   - **macOS**: `brew install google-cloud-sdk`
   - **Linux/Windows**: Follow the [official installation guide](https://cloud.google.com/sdk/docs/install)

2. Initialize the SDK (if first time):

   ```bash
   gcloud init
   ```

### Authentication

Set up Application Default Credentials (ADC) for local development:

```bash
gcloud auth application-default login
```

This command will:

- Open your browser for Google Cloud authentication
- Store credentials locally for use by the Google Cloud client libraries
- Allow your application to access Google Cloud services on your behalf

### Verify Authentication

You can verify your authentication status:

```bash
gcloud auth application-default print-access-token
```

Or use the provided setup script to check everything:

```bash
python scripts/setup_gcloud.py
```

This script will verify:

- Google Cloud SDK installation
- Authentication status  
- Application Default Credentials
- Google Cloud Storage connection

You can also test your storage connection specifically:

```bash
python scripts/test_storage.py
```

### Production & Cloud Deployment

#### Option 1: Service Account Key (General Production)

For production environments and cloud deployments, use a service account key file:

1. Create a service account in the Google Cloud Console
2. Grant necessary permissions (e.g., Storage Admin)
3. Download the JSON key file
4. **Securely store it** in the `credentials/` directory (never commit to git!)
5. Set the environment variable:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/project/credentials/service-account-key.json"
   ```

   **Note:** The `credentials/` directory is gitignored for security.

#### Option 2: Workload Identity (Google Cloud Services)

If deploying to Google Cloud services (Cloud Run, GKE, Compute Engine):

1. Enable Workload Identity on your cluster/service
2. Bind your Kubernetes service account to a Google service account
3. No explicit authentication needed in code:

   ```python
   from google.cloud import storage
   # Automatically uses the service's identity
   client = storage.Client()
   ```

#### ❌ Don't Use for Cloud Deployment

**Google Colab authentication** (only for Colab notebooks):

```python
# DON'T use this for cloud deployment
from google.colab import auth
auth.authenticate_user(project_id="PROJECT_ID")
```

### Environment Configuration

1. Copy the environment template:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set your Google Cloud project ID:

   ```bash
   GOOGLE_CLOUD_PROJECT=your-actual-project-id
   ```

## Usage

### Local Development (with ADC)

```python
from google.cloud import storage

# Uses Application Default Credentials (from gcloud auth application-default login)
client = storage.Client()

# Example: List buckets
buckets = client.list_buckets()
for bucket in buckets:
    print(f"Bucket: {bucket.name}")
```

### Production with Service Account

```python
from google.cloud import storage
import os

# Method 1: Using environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/service-account-key.json'
client = storage.Client()

# Method 2: Direct file path
client = storage.Client.from_service_account_json('/path/to/service-account-key.json')

# Method 3: Using project ID explicitly
client = storage.Client(project='your-project-id')
```

### Common Operations

```python
# Upload a file
bucket = client.bucket('your-bucket-name')
blob = bucket.blob('your-file-name')
blob.upload_from_filename('local-file-path')

# Download a file
blob.download_to_filename('downloaded-file.txt')

# List objects in bucket
blobs = bucket.list_blobs()
for blob in blobs:
    print(f"File: {blob.name}")
```

**Note**: Make sure you have completed the appropriate authentication setup before running the code.

## Development

To contribute to this project:

1. Install development dependencies:

    ```bash
    poetry install --with dev
    ```

2. Run tests:

    ```bash
    poetry run pytest
    ```

## License

This project is licensed under the terms specified in the project configuration.

## Author

Viktor Szabo (<vszabo@protonmail.com>)

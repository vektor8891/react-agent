# Scripts Directory

This directory contains utility scripts for project setup, testing, and Vertex AI integration.

## Available Scripts

### Running Google Cloud Storage Scripts

### `setup_gcloud.py`

**Purpose**: Comprehensive Google Cloud authentication verification  
**Usage**: `python scripts/setup_gcloud.py`

**What it checks:**

- Google Cloud SDK installation
- Authentication status (gcloud auth list)
- Application Default Credentials
- Google Cloud Storage connection
- Overall setup health

**When to use:**

- First time setup
- Troubleshooting authentication issues
- Onboarding new team members
- CI/CD health checks

### `test_storage.py`

**Purpose**: Test Google Cloud Storage connection and ensure bucket availability  
**Usage**: `python scripts/test_storage.py`

**What it does:**

- Tests service account or ADC authentication
- Lists available storage buckets
- Automatically creates a test bucket if none exist
- Verifies storage permissions
- Provides bucket name for development use

**Intelligent behavior:**

- ✅ If buckets exist: Reports availability, no user interaction needed
- 🪣 If no buckets exist: Automatically creates a test bucket
- 🚫 No unnecessary prompts or manual intervention

**When to use:**

- After setting up credentials
- Before deploying storage-dependent features
- Testing storage permissions
- Debugging storage connectivity

### Vertex AI Example Scripts

### `test_vertex_ai.py`

**Purpose**: Basic Vertex AI connection and initialization test  
**Usage**: `python scripts/test_vertex_ai.py`

**What it does:**

- Loads configuration from environment variables
- Tests Vertex AI initialization with proper parameters
- Verifies access to Vertex AI services
- Validates project, location, and staging bucket setup

**When to use:**

- After setting up Vertex AI credentials
- Before using Vertex AI in your application
- Debugging Vertex AI connectivity issues
- Verifying environment configuration

### `your_code.py`

**Purpose**: Direct implementation of your exact Vertex AI initialization pattern  
**Usage**: `python scripts/your_code.py`

**What it demonstrates:**

- How to replace hardcoded values with environment variables
- Your exact `vertexai.init()` code pattern in action
- Real-world usage of the initialization code you provided

**Code pattern:**

```python
vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket=os.getenv("GOOGLE_CLOUD_STAGING_BUCKET"),
)
```

**When to use:**

- Learning how to adapt your code to use environment variables
- Testing your specific initialization pattern
- Quick verification that your exact code works

### `vertex_ai_example.py`

**Purpose**: Comprehensive Vertex AI setup example with detailed explanations  
**Usage**: `python scripts/vertex_ai_example.py`

**What it demonstrates:**

- Complete Vertex AI initialization workflow
- Environment variable configuration
- Access to `agent_engines` and other Vertex AI modules
- Error handling and troubleshooting
- Best practices for Vertex AI setup

**Features:**

- Detailed console output with emojis for clarity
- Configuration validation
- Service availability testing
- Educational comments and explanations

**When to use:**

- Learning Vertex AI integration
- Understanding the complete setup process
- Educational purposes and onboarding
- Comprehensive testing of Vertex AI functionality

## Prerequisites

All scripts require:

- Poetry environment: `poetry install --no-root`
- Google Cloud authentication (ADC or service account)
- Environment variables set (see `.env.example`)

**For Vertex AI scripts, additionally:**

- Vertex AI API enabled: `gcloud services enable aiplatform.googleapis.com`
- Proper environment variables for Vertex AI (project, location, staging bucket)

## Running Scripts

From the project root directory:

### Google Cloud Storage Scripts

```bash
# Setup verification
poetry run python scripts/setup_gcloud.py

# Storage testing
poetry run python scripts/test_storage.py
```

### Vertex AI Scripts

```bash
# Basic Vertex AI test
poetry run python scripts/test_vertex_ai.py

# Your exact code pattern
poetry run python scripts/your_code.py

# Comprehensive Vertex AI example
poetry run python scripts/vertex_ai_example.py
```

## Environment Setup

Make sure your environment is configured:

### Basic Setup

```bash
# Copy and edit environment file
cp .env.example .env

# Set up authentication (choose one)
gcloud auth application-default login  # For local development
# OR set GOOGLE_APPLICATION_CREDENTIALS in .env  # For service account
```

### Vertex AI Configuration

Ensure your `.env` file includes:

```bash
# Required for all scripts
GOOGLE_CLOUD_PROJECT=your-project-id

# Required for Vertex AI scripts
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_CLOUD_STAGING_BUCKET=gs://your-staging-bucket

# Optional: Service account path
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
```

### Enable Required APIs

```bash
# Enable Vertex AI API (required for Vertex AI scripts)
gcloud services enable aiplatform.googleapis.com

# Enable Cloud Storage API (usually enabled by default)
gcloud services enable storage.googleapis.com
```

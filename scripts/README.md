# Scripts Directory

This directory contains utility scripts for project setup and testing.

## Available Scripts

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

## Prerequisites

Both scripts require:

- Poetry environment: `poetry install`
- Google Cloud authentication (ADC or service account)
- Environment variables set (see `.env.example`)

## Running Scripts

From the project root directory:

```bash
# Setup verification
poetry run python scripts/setup_gcloud.py

# Storage testing
poetry run python scripts/test_storage.py
```

## Environment Setup

Make sure your environment is configured:

```bash
# Copy and edit environment file
cp .env.example .env

# Set up authentication (choose one)
gcloud auth application-default login  # For local development
# OR set GOOGLE_APPLICATION_CREDENTIALS in .env  # For service account
```

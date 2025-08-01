# React Agent

A LangGraph ReAct (Reasoning and Acting) agent implementation with Google Vertex AI integration.

## Description

This project implements a ReAct agent using LangGraph, which combines reasoning and acting in language models to solve complex tasks through iterative thought, action, and observation cycles. The agent leverages Google Vertex AI's Gemini models for advanced AI capabilities and includes custom tools for real-world interactions.

## Features

- **ReAct Agent Pattern**: Iterative reasoning and acting cycles for complex problem solving
- **LangGraph Integration**: Advanced workflow orchestration with `vertexai.agent_engines.LanggraphAgent`
- **Google Vertex AI**: Gemini 2.0-flash model integration with safety controls
- **Custom Tools**: Exchange rate API integration and extensible tool framework
- **Service Account Authentication**: Production-ready authentication setup
- **Interactive Jupyter Notebook**: Complete testing and development environment
- **Safety Controls**: Configurable harm categories and thresholds

## Requirements

- Python >=3.12
- Poetry for dependency management
- Google Cloud SDK (for authentication)
- Google Cloud Project with Vertex AI API enabled
- Service account with appropriate IAM roles

## Key Dependencies

- `langgraph` - Agent workflow orchestration
- `langchain-google-vertexai` - Vertex AI integration
- `vertexai` - Google AI platform SDK
- `python-dotenv` - Environment variable management
- `requests` - HTTP client for external APIs

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vektor8891/react-agent.git
   cd react-agent
   ```

2. Install dependencies using Poetry:

    ```bash
    poetry install --no-root
    ```

3. Activate the virtual environment:

    ```bash
    poetry shell
    ```

## Google Cloud Setup

This project uses Google Vertex AI for the LangGraph agent. Authentication is configured using service accounts for production-ready deployment.

### Prerequisites

1. Install the Google Cloud SDK:
   - **macOS**: `brew install google-cloud-sdk`
   - **Linux/Windows**: Follow the [official installation guide](https://cloud.google.com/sdk/docs/install)

2. Initialize the SDK (if first time):

   ```bash
   gcloud init
   ```

3. Enable required APIs:

   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```

### Service Account Authentication (Recommended)

For production environments and consistent authentication:

1. Create a service account in [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).

2. Download the service account key to `credentials/service-account-key.json`

3. **Activate the service account**:

   ```bash
   gcloud auth activate-service-account \
     --key-file=credentials/service-account-key.json
   ```

4. **Set environment variable**:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials/service-account-key.json"
   ```

### Alternative: Application Default Credentials (Development)

For local development only, you can use ADC:

```bash
gcloud auth application-default login
```

### Environment Configuration

1. Copy the environment template (if it exists) or create a new `.env` file:

   ```bash
   touch .env
   ```

2. Edit `.env` and set your configuration:

   ```bash
   # Required for Vertex AI
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   
   # Service account authentication (recommended)
   GOOGLE_APPLICATION_CREDENTIALS=./credentials/service-account-key.json
   ```

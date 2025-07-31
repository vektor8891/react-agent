# Credentials Setup

This directory should contain your Google Cloud service account key files.

## For Development Team Members

1. **Get the service account key file** from your team lead or Google Cloud Console
2. **Place it in this directory**: `credentials/service-account-key.json`
3. **Update your .env file** to point to the correct path:

   ```text
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/project/credentials/service-account-key.json
   ```

## Security Notes

⚠️ **NEVER commit credential files to version control**

- The `.gitignore` file is configured to exclude all files in this directory
- Use environment variables to reference credential file paths
- For production, use Workload Identity or other secure methods

## Alternative Setup (Recommended for Production)

Instead of using JSON key files, consider:

1. **Application Default Credentials** (for local development):

   ```bash
   gcloud auth application-default login
   ```

2. **Workload Identity** (for Google Cloud services):
   - No credential files needed
   - Uses the service's built-in identity

3. **Secret Manager** (for other cloud platforms):
   - Store credentials securely in cloud secret management services

## File Structure

```text
credentials/
├── README.md                 # This file
├── service-account-key.json  # Service account key (you need to add this)
└── .gitkeep                  # Ensures directory is tracked in git
```


import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Now you can use the credentials to access the API
from googleapiclient.discovery import build

# Path to your OAuth 2.0 credentials file
CREDENTIALS_FILE = "path_to_your_oauth2_credentials.json"

# Define the required scopes
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/admin.reports.audit.readonly"]

# Try to load saved credentials
creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

# If no valid credentials are available, let the user log in
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build("calendar", "v3", credentials=creds)

# Get the list of events for the user
events_result = service.events().list(calendarId="primary", maxResults=10).execute()
events = events_result.get("items", [])

# Save events to a JSON file
with open("events.json", "w") as f:
    json.dump(events, f, indent=2)

# Print event summaries
for event in events:
    print(event["summary"])

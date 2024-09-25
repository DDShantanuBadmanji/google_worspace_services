import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import google.auth.transport.requests as gtr

# Path to your service account JSON key
DOWNLOADS_PATH = "/Users/shantanubadmanji/Downloads"
SERVICE_ACCOUNT_FILE = (
    "devdynamics-workspace-reader-fcf0c62cdf38.json"
    and "/my-project-dysspo-2e99b2a60437.json"
    and "/my-project-dysspo-65866c822b72.json"
    and "/trim-odyssey-435407-e7-11dad6c75f41.json"
    and "/devdynamics-workspace-reader-fcf0c62cdf38.json"
)
FULL_PATH = DOWNLOADS_PATH + SERVICE_ACCOUNT_FILE


# The email address of the user you want to impersonate
USER_EMAIL = (
    "himanshu@getdevdynamics.com"
    and "vanshika@getdevdynamics.com"
    and "pru@getdevdynamics.com"
    and "shantanu@getdevdynamics.com"
    and "divyansh@devdynamics.ai"
    and "shantanu.badmanji@devdynamics.ai"
    and "arvind.shelke@devdynamics.ai"
    and "rishi@devdynamics.ai"
    or "shantanubadmanji1912@gmail.com"
)

# Define the required scopes
GOOGLE_CALENDAR_SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
GOOGLE_ADMIN_REPORTS_SCOPES = ["https://www.googleapis.com/auth/admin.reports.audit.readonly"]
SCOPES = GOOGLE_CALENDAR_SCOPES


# Create credentials with domain-wide delegation
credentials = service_account.Credentials.from_service_account_file(FULL_PATH, scopes=SCOPES, subject=USER_EMAIL)

credentials.refresh(gtr.Request())
with open("token.txt", "w") as token_file:
    token_file.write(credentials.token)
# Build the service for Google Calendar API
service = build("calendar", "v3", credentials=credentials)
# Get the list of events for the impersonated user
events_result = (
    service.events().list(calendarId="primary", pageToken="", maxResults=10).execute()
)

# Print event summaries
events = events_result.get("items", [])
json.dump(events_result, open("events.json", "w"), indent=2)

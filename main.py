from google.oauth2 import service_account
from googleapiclient.discovery import build

# Authenticate the program using the service account
credentials = service_account.Credentials.from_service_account_file(
    'path/to/service/account/credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar.readonly'])

meet_service = build('calendar', 'v3', credentials=credentials)

# Retrieve the list of attendees for a given meeting
attendees = meet_service.events().get(
    calendarId='primary',
    eventId='[MEETING ID]').execute()['attendees']
#12312312321312123123123123123213122131

# Store the attendance information in a file or database
# ...

import json

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

scopes = ["https://www.googleapis.com/auth/calendar.events"]

flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=scopes)

# credentials = flow.run_local_server(port=0)
#
# with open('token.pkl', 'wb') as token:
#     pickle.dump(credentials, token)

with open('token.pkl', 'rb') as token:
    credentials = pickle.load(token)
service = build('calendar', 'v3', credentials=credentials)
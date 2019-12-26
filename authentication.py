import pickle

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Auth:
    def __init__(self, scopes):
        self.scopes = [scopes]

    def get_auth(self):
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=self.scopes)

        # credentials = flow.run_local_server(port=0)
        #
        # with open('token.pkl', 'wb') as token:
        #     pickle.dump(credentials, token)

        with open('token.pkl', 'rb') as token:
            credentials = pickle.load(token)
        service = build('calendar', 'v3', credentials=credentials)
        return service

import json
from copy import deepcopy

import requests


class GoogleCalendar:
    url = "https://www.googleapis.com/calendar/v3/calendars"

    headers = {
        'authorization':
            'Bearer ya29.Il-1B2yNZ6qR88fvlHVbxG4evpL63rzwDKsRLho0BHic8vO6IV7lHLz4y2UWAZyXdg0Y_qmV37UTJckdGUrV832Z8nvfSs7Bu-bPFYfcCnT7azShCLr3Ll_CbQ25NcJH_w',

        'content-type': 'application/json'
    }

    payload = {
        'end': {
            'date': '2019-12-12'
        },
        'start': {
            'date': '2019-12-12'
        },
        'description': 'AUTOMATION',
        'summary': 'AUTOMATION TEST',
        'location': 'tel-aviv'
    }

    def get_event(self):
        r = requests.get(f"{self.url}/markovich.org@gmail.com/events/2qd50sie64hn0d4el4gsm1r80m", headers=self.headers)
        return r

    def create_event(self, launch_data, i):
        launch_payload = deepcopy(self.payload)
        launch_payload['description'] = launch_data[i][2]
        launch_payload['summary'] = launch_data[i][0]
        launch_payload['location'] = launch_data[i][2][1]
        # month = ''
        # if launch_data[i][1][0] == 'Dec':
        #     month = '12'
        # day = launch_data[i][1][1]
        parsed_date = f'2019-12-14'
        launch_payload['end']['date'] = parsed_date
        launch_payload['start']['date'] = parsed_date
        json_payload = json.dumps(launch_payload)
        r = requests.post(f"{self.url}/markovich.org@gmail.com/events", headers=self.headers, data=json_payload)
        return r
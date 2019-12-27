from copy import deepcopy

from authentication.authentication import Auth
import json


class GoogleCalendar:
    def __init__(self):
        self.service = Auth(scopes="https://www.googleapis.com/auth/calendar.events").get_auth()
        self.payload = self.payload_init()

    @staticmethod
    def payload_init():
        with open('../payload/payload.json') as payload:
            content = json.loads(payload.read())
            return content

    def get_event(self):
        event = self.service.events().get(calendarId='markovich.org@gmail.com',
                                          eventId='0o9llkg08rg9f5bpvf548bljhf').execute()
        return event

    def create_event(self, launch_data, i):
        launch_payload = deepcopy(self.payload)
        launch_payload['description'] = launch_data[i][2]
        launch_payload['summary'] = launch_data[i][1]
        launch_payload['location'] = launch_data[i][2][1]
        month = ''
        if launch_data[i][0][0] == 'dec':
            month = '12'
        elif launch_data[i][0][0] == 'jan':
            month = '01'
        day = launch_data[i][0][1].split('/')
        parsed_date = f'2019-{month}-{day[0]}'
        launch_payload['end']['date'] = parsed_date
        launch_payload['start']['date'] = parsed_date
        event = self.service.events().insert(calendarId='markovich.org@gmail.com', body=launch_payload).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        return event

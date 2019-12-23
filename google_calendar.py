from copy import deepcopy

from authentication import Auth


class GoogleCalendar:
    def __init__(self):
        self.service = Auth().get_auth()

        self.payload = {
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
        event = self.service.events().get(calendarId='markovich.org@gmail.com',
                                          eventId='2qd50sie64hn0d4el4gsm1r80m').execute()
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

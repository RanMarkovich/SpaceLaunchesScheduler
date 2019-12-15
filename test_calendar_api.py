from pytest import fixture
from google_calendar import *
from pytest import fixture

from google_calendar import GoogleCalendar


@fixture()
def google_calendar():
    return GoogleCalendar


def test_get_event_from_calendar(google_calendar):
    event = GoogleCalendar().get_event()
    assert event['summary'] == 'Test Event'


def test_post_event_to_calendar(google_calendar, payload):
    event = GoogleCalendar().create_event(payload, 0)
    event_link = event.get('htmlLink')
    assert event_link is not None

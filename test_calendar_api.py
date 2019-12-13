from pytest import fixture
from google_calendar import *
from pytest import fixture

from google_calendar import GoogleCalendar


@fixture()
def google_calendar():
    return GoogleCalendar


def test_get_event_from_calendar(google_calendar):
    r = GoogleCalendar().get_event()
    assert r.status_code == 200, f"failed to get event, got: {r.text}"


def test_post_event_to_calendar(google_calendar, payload):
    r = GoogleCalendar().create_event(payload)
    assert r.status_code == 200, f"failed to create event, got: {r.text}"

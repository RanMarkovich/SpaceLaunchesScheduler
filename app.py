from driver import Driver
from google_calendar import GoogleCalendar

launch_data = Driver().get_launch_data()

i = 0
for _ in range(4):
    r = GoogleCalendar().create_event(launch_data, i)
    assert r.status_code == 200, f"failed to create event, got: {r.text}"
    i += 1

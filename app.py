from site_scraper import SiteScraper
from google_calendar import GoogleCalendar

launch_data = SiteScraper().get_launch_data()

i = 0
for _ in range(4):
    GoogleCalendar().create_event(launch_data, i)
    i += 1

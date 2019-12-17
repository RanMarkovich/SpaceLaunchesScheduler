#!/usr/bin/env python3

from google_calendar import GoogleCalendar
from site_scraper import SiteScraper


def app_exe():
    launch_data = SiteScraper().get_launch_data()

    i = 0
    for _ in range(4):
        GoogleCalendar().create_event(launch_data, i)
        i += 1


if __name__ == '__main__':
    app_exe()

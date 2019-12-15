import requests
from bs4 import BeautifulSoup


class SiteScraper:
    def __init__(self):
        url = requests.get("https://spaceflightnow.com/launch-schedule/")
        soup = BeautifulSoup(url.content, 'html.parser')
        self.soup = soup

    def get_launch_data(self):
        dates = self.soup.find_all('span', class_='launchdate')
        missions_name = self.soup.find_all('span', class_='mission')
        missions_data = self.soup.find_all('div', class_='missiondata')

        dates_list = []
        names_list = []
        data_list = []

        for i, date in zip(range(4), dates):
            dates_list.append(date.text.lower())
        for i, name in zip(range(4), missions_name):
            names_list.append(name.text.lower())
        for i, data in zip(range(4), missions_data):
            data_list.append(data.text.lower().split('\n'))

        launch_data = list(zip(dates_list, names_list, data_list))
        return launch_data

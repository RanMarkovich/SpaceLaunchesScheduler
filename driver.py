from copy import deepcopy

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Driver:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = Chrome(executable_path='/Users/ranmarkovich/Desktop/Selenium/chromedriver', chrome_options=chrome_options)
    url = 'https://spaceflightnow.com/launch-schedule/'

    launch_payload = {
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

    def get_launch_data(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        launch_date = self.driver.find_elements_by_class_name('launchdate')
        mission_name = self.driver.find_elements_by_class_name('mission')
        mission_data = self.driver.find_elements_by_class_name('missiondata')
        names = []
        dates = []
        data = []
        for _, name in zip(range(4), mission_name):
            names.append(name.text)
        for _, date in zip(range(4), launch_date):
            dates.append(date.text)
        for _, d in zip(range(4), mission_data):
            data.append(str(d.text).split('\n'))
        launch_data = list(zip(names, dates, data))
        self.driver.delete_all_cookies()
        self.driver.close()
        return launch_data

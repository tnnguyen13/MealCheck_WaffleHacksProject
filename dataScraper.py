# DataScraper via Google Maps
# Author: rebeccachen8788

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

s = Service("C:\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service=s, options=options)


class ScrapMapFood:
    def __init__(self, food, zipcode):
        self._food = food
        self._zipcode = zipcode
        self._everything = ""

    def get_food(self):
        return self._food

    def get_zipcode(self):
        return self._zipcode

    def get_restaurant(self):
        search = self.get_food() + "restaurant" + str(self.get_zipcode())
        url_rest = f"https://www.google.com/maps/search/{search}"
        browser.get(url_rest)
        title = browser.find_element(by=By.CLASS_NAME, value="NrDZNb")
        rest_title_string = title.text
        return rest_title_string

    def get_ratings(self):
        # Ratings, reviews, dollars, categories
        restaurant_title = self.get_restaurant()
        url_rest = f"https://www.google.com/maps/search/{restaurant_title}"
        browser.get(url_rest)
        stars = browser.find_element(by=By.CLASS_NAME, value="tAiQdd")
        stars_string = stars.text
        return stars_string

    def get_everything(self):
        restaurant_title = self.get_restaurant()
        search = f"{restaurant_title}{self.get_zipcode()}"
        url_rest = f"https://www.google.com/maps/search/{search}"
        browser.get(url_rest)
        address = browser.find_element(by=By.CLASS_NAME, value="m6QErb")
        self._everything = address.text

    def get_get_everything(self):
        return self._everything

Korean = ScrapMapFood("Korean", 98031)
print(Korean.get_restaurant())
#print(Korean.get_ratings())
Korean.get_everything()
print(Korean.get_get_everything())

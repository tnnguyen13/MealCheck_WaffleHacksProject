# DataScraper via Google Maps
# Author: rebeccachen8788

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe", options=options)


class ScrapMapFood:
    def __init__(self, food, zipcode):
        self._food = food
        self._zipcode = zipcode

    def get_food(self):
        return self._food

    def get_zipcode(self):
        return self._zipcode

    def get_restaurant(self):
        search = self.get_food() + "restaurant" + str(self.get_zipcode())
        url_rest = f"https://www.google.com/maps/search/{search}"
        browser.get(url_rest)
        title = browser.find_element_by_class_name("NrDZNb")
        rest_title_string = title.text
        return rest_title_string

    def get_ratings(self):
        # Ratings, reviews, dollars, categories
        restaurant_title = self.get_restaurant()
        url_rest = f"https://www.google.com/maps/search/{restaurant_title}"
        browser.get(url_rest)
        stars = browser.find_element_by_class_name("tAiQdd")  # "skqShb"
        stars_string = stars.text
        return stars_string

    def get_everything(self):
        # Gives you everything, address, location, phone, reviews, etc...
        restaurant_title = self.get_restaurant()
        url_rest = f"https://www.google.com/maps/search/{restaurant_title}"
        browser.get(url_rest)
        address = browser.find_element_by_class_name("m6QErb")
        address_string = address.text
        return address_string

# DataScraper
# Author: rebeccachen8788
# Date: 06/19/2022

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

s = Service("C:\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service=s, options=options)


class FoodScraper:
    """
    A class used to scrap data from data submission on food category and zipcode user entered.
    Will pull a restaurant name and scrap information on the overall ratings, number of reviews,
    and the amount of dollar signs associated with that restaurant.
    """
    def __init__(self, food, zipcode):
        self._food = food
        self._zipcode = zipcode
        self._restaurant_name = ""
        self._everything = ""
        self._ratings = ""
        self._reviews = ""
        self._price = ""

    def get_food(self):
        """Returns the name of the food category the user inputted."""
        return self._food

    def get_zipcode(self):
        """Returns the zipcode the user inputted."""
        return self._zipcode

    def obtain_restaurant(self):
        """
        Will obtain the first restaurant name that shows up in Google Maps using the
        data the user provided for zipcode and food category.
        """
        search = self.get_food() + "restaurant" + str(self.get_zipcode())
        url_rest = f"https://www.google.com/maps/search/{search}"
        browser.get(url_rest)
        title = browser.find_element(by=By.CLASS_NAME, value="NrDZNb")
        self._restaurant_name = title.text

    def obtain_restaurant_data(self):
        """
        Will obtain restaurant data from Google Maps from the first restaurant
        name received in the initial Google Maps search from the food category and zipcode
        the user entered.
        """
        search = f"{self._restaurant_name} {self.get_zipcode()}"
        url_rest = f"https://www.google.com/maps/search/{search}"
        browser.get(url_rest)
        address = browser.find_element(by=By.CLASS_NAME, value="m6QErb")
        self._everything = address.text
        if self._everything == "":
            self.obtain_restaurant_data()

    def adjust_string(self):
        """
        Will specifically parse out the ratings, reviews, and number
        of dollar signs associated with the 1st restaurant that matches
        the food and zipcode category the user wanted.
        """
        temp_string = self._everything
        counter = 0
        while counter <= 2:
            for line in temp_string.splitlines():
                if counter == 1:
                    self._ratings = line
                elif counter == 2:
                    i = 0
                    for char in line:
                        i += 1
                        if char == 's':
                            self._reviews = line[0:i]
                            self._price = line[i+1:]
                counter += 1

    def get_get_everything(self):
        """ for testing """
        return self._everything

    # getters for foodMain class
    def get_restaurant_name(self):
        """Will return the restaurant name."""
        return self._restaurant_name

    def get_ratings(self):
        """Will return the ratings."""
        return self._ratings

    def get_reviews(self):
        """Will return the reviews."""
        return self._reviews

    def get_price(self):
        """Will return the price."""
        return self._price


def main():
    Korean = FoodScraper("vietnamese", 98031)
    Korean.obtain_restaurant()
    Korean.obtain_restaurant_data()
    Korean.adjust_string()
    print(Korean.get_reviews())


if __name__ == '__main__':
    main()

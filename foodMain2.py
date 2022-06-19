# Authors: rebeccachen8788, scottirons, tnnguyen13
# Date: 06/19/2022
# Description: Create a backend of the Meal program

from dataScraper import FoodScraper
from userName import UserName
import re
import gui
import sys


class MealCheck:
    """ A class that utilizes both the UserName and FoodScraper classes to create a central repository for the
    back end of the MealCheck app. This class includes the ability for users to enter their username, get it
    verified, then find a restaurant based off of their location and search entries. """
    def __init__(self):
        self._user_database = {}     # maintaining a user database for users
        self._current_name = None    # temporary class variable used to store current name of user
        self._current_location = ""  # temporary class variable for location of user
        self._current_search = ""    # temporary class variable for 'type' of food user desires
        self._pattern = '^[0-9]{5}(-[0-9]{4})?$'  # for zip code verification
        self._current = None         # houses object from FoodScraper class
        self.gui = gui.MainWindow()

    def create_user(self):
        """ Create a user, and obtain information required to run parsing procedure. """
        name_checker = False
        while not name_checker:  # infinite loop used to ensure that username is valid.

            name = self.gui.get_name()
            self._current_name = name
            # Auth0 verification via API to be added at a later time
            name_checker = self.verify_user()

        # get food type (I removed the loop so the gui didn't muck up)
        search = self.gui.get_food()
        self._current_search = search

        location_checker = False
        while not location_checker:  # infinite loop used to ensure that zip code is valid
            location = str(self.gui.get_zip())
            location_checker = self.verify_valid_location(location)
        # search = search + " food"
        self._user_database[name] = UserName(name, search, location)  # adding user object to user_database

    def find_restaurant(self):
        """ Uses the FoodScraper class to find a restaurant in the user's locale. """
        self._current = FoodScraper(self._current_search, self._current_location)  # FoodScraper object
        self._current.obtain_restaurant()
        self._current.obtain_restaurant_data()
        self._current.adjust_string()
        self._current_name = ""
        self._current_location = ""
        self._current_search = ""

    def output(self):
        """ Console output - pending GUI addition """
        name = self._current.get_restaurant_name()
        ratings = self._current.get_ratings()
        reviews = self._current.get_reviews()
        price = self._current.get_price()
        self.gui.update_data(self.gui.restaurant, name)
        self.gui.update_data(self.gui.rating, ratings)
        self.gui.update_data(self.gui.reviews, reviews)
        self.gui.update_data(self.gui.price, price)

    def verify_user(self) -> bool:
        """ Temporary user verification until Auth0 verification is added """
        if self._current_name is not None:
            for s in self._current_name:
                if not s.isalpha():
                    return False
            print(f'Verified!')
            return True
        return False

    def verify_valid_location(self, zip_code) -> bool:
        """ Verifies zip code using Regex comparison """
        result = re.match(self._pattern, zip_code)
        if result:
            return True
        return False




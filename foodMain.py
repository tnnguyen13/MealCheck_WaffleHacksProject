# Authors: Rebecca Chen, Scott Irons, Tee Nguyen
# Create a backend of the Meal program

from userName import UserName
import re


class MealCheck:
    def __init__(self):
        self._user_database = {}
        self._current_session = True
        self._current_name = ""
        self._current_location = ""
        self._current_search = ""
        self._zip_list = ['32344-4444', '32344', '323445-44', '323445']
        self._pattern = '^[0-9]{5}(-[0-9]{4})?$'

    def create_user(self):
        name_checker = False
        while not name_checker:
            name = input(str("What is your name? "))
            # verify name
            name_checker = self.verify_user(name)
        search = ""
        while search == "":
            search = input(str("What kind of food do you want? "))
        location_checker = False
        while not location_checker:
            location = input("What is your current zip code? ")
            location_checker = self.verify_valid_location(location)
        search = search + " food"
        self._user_database[name] = UserName(name, search, location)

    def verify_user(self, name) -> bool:
        if name == 'tee':
            print(f'verified!')
            return True
        return False

    def verify_valid_location(self, zip_code) -> bool:
        for each_number in self._zip_list:
            result = re.match(self._pattern, each_number)
            if result:
                return True
        return False


def main():
    test = MealCheck()
    test.create_user()
    print('hello')


if __name__ == '__main__':
    main()

# Authors: Rebecca Chen, Scott Irons, Tee Nguyen
# Create a backend of the Meal program

import userName
import json


class MealCheck:
    def __init__(self):
        self._readFileName = "valUser.json"
        self._writeFileName = ""

    def read_from_json(self):
        """ reads validated user information from json file """
        opening = open(self._readFileName)
        in_object = json.load(opening)
        temp_list = []
        for user_key in in_object['user']:
            temp_list.append(user_key)

        # run parse

        # adding values to history
        temp_list[3].append(temp_list[2])  # appends the current search to the top of the search stack
        temp_list[4].append(temp_list[1])  # appends the current location to the top of the location stack

    def write_to_json(self):
        """ writes all class information to a json file """
        with open(self._writeFileName) as json_file:
            data = json.write(json_file)
            print(data)


def main():
    test = MealCheck()
    test.read_from_json()


if __name__ == '__main__':
    main()

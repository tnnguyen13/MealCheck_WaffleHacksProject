# Authors: rebeccachen8788, scottirons, tnnguyen13
# Date: 06/19/2022
# Description: UserName class to manage the users of the program.

class UserName:
    """ contains user class information; includes username, user's current location, user's current search,
    their search history, and their location history """
    def __init__(self, user, search, location):
        self._user = user
        self._location = location
        self._search = search
        self._searchHistory = []
        self._locationHistory = []

    def get_user(self):
        """ returns user name """
        return self._user

    def get_location(self):
        """ returns user's current location """
        return self._location

    def set_location(self, location: int):
        """ sets the users current location """
        self._location = location
        self._locationHistory.append(location)

    def set_search(self, s: str):
        """ adds user entries to a history """
        self._search = s
        self._searchHistory.append(s)
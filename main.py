# Authors: rebeccachen8788, scottirons, tnnguyen13
# Date: 06/19/2022
# Description: Main run of MealCheck Class - will include future GUI.

from foodMain import MealCheck

def main():
    test = MealCheck()  # creating MealCheck object
    test.create_user()  # creating and verifying a valid user
    test.find_restaurant()  # finding a restaurant per requested parameters
    test.output()   # printing output to console or GUI


if __name__ == '__main__':
    main()

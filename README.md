# MealCheck_WaffleHacksProject
an interactive program that determines local restaurants within the user's radius and returns its location

The primary files in this project are foodMain.py, foodMain2.py, dataScraper.py, gui.py, and userName.py.

foodMain.py and foodMain2.py are the same file except that foodMain2.py includes integration with the PyQt5 GUI in gui.py. 

Both of these files allow users to enter their name, search keywords, and zipcode to find food in their area. 
In addition, it contains methods to pass to dataScraper.py and search for food with the keywords and zipcode from the user input. 
Afterwards, it updates the visible information on the gui to display a result to the user.

userName.py contains information about an individual user and was created with the goal to add authentication and database support in the future.

dataScraper.py is the biggest player in the game, and parses data from Google Maps searches of food and zipcodes. 

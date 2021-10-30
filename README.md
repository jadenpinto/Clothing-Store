# Synopsis

The project is a menu driven program of an online clothing company. The menu guides the user i.e. the customer to different cloth companies and to the checkout. When the user selects a clothing company, they can choose the items they wish to purchase. This item along with its price will get added to a dictionary. At the checkout, the dictionary is converted to a CSV file which is then displayed as the bill, and the values of the dictionary are added up to get the final cost of clothes purchased by the user. After checkout, the user can give feedback of the company and rate its service which will be saved in a CSV file. Since Cyber Security is of great importance especially for online shopping, the user must first confirm that he/she is not a robot by typing in a copy of a random generated number which will be displayed to the user. Only if the numbers match, the user is given access to browse through the shop and if not, user must try again.

# Objectives

The system is built with the following objectives: -
- Adding new items to the shopping cart is easy.
- Security system ensures robots are barred from shopping
- Finding the final price of bill is easy.
- Feedback systems supports development and improvement of store

# Modules used
- csv module
- random module

# Files used
- billing.csv
- FEEDBACK.csv

# Variables used
- shopping_cart- Shopping cart of customer where items are strored
- a – Random generated number for security system
- n – User input of confirmation number which should be same as the random generated number
- l – Keys/Serial number of items in each of the stores
- n – Serial number of the item the user wishes to purchase from store
- total- total price of all items the user has purchased in the bill
- price – price of each item in the shopping cart
- payment_method – means by which the user wishes to pay the bill either by card or by cash
- condition1 – User input of whether they wish to provide feedback
- Name – Name of customer
- Rating – Customer rating for the shops service
- Suggestions – Suggestions of customer to improve the shop(if any)

# Functions used

User defined functions:
- robot() – Used to verify that user is a not robot by providing a verification code which must be typed in properly by the user.
- Nike() – 1st store
- Adidas() – 2nd store
- Puma() – 3rd store
- Levi() – 4th store
- Checkout() – Takes the user to the checkout where the final bill is displayed along with the final price to be paid by the user
- Feedback() – Feed back system for the user to provide feedback on how the shop can improve its services
 Built in functions:
- keys() – Returns the keys of a dictionary in the form of a list
- values()- Returns the values of a dictionary in the form of a list
- int(<data>): this function is used to convert datatype to integer.
- list(<data>): this function is used to convert datatype to list.
- str(<data>): this function is used to convert datatype to string.
- input(<display>): this function allows user to input data when given string parameter is displayed
- print(<items>): this function displays all the given items in parameter.
- open(<filename>): this function opens a file given as parameter.  Randint(a,b): The randint() method returns an integer number selected element from the specified range.
- reader(<file>): this function, imported from csv module, is used to return reader object of the file given as parameter.
- writer(<file>): this function, imported from csv module, is used to return writer object of the file given as parameter.
- close(<file>): this function, imported from csv module, is used to close a file after the operations are completed.
- flush(): this function, imported from csv module, is used to flush the buffer, the data will be immediately written to the file in the buffer, clear the buffer at the same time.
- write(): writes data into the file
- lower(): returns the string after converting all characters to lower case
- upper(): returns the string after converting all characters to upper case  writerow(): The writerow() method writes a row of data into the specified file

 # Conclusion

From this project it is quite evident that online cloth shopping is much more efficient than shopping in stores and malls due to several reasons. The major inspiration behind this project is its practicality. During long periods of lockdown, when malls and stores around the world are all shut down consumers often turn towards online shopping to satisfy their needs. Online shopping stores are open round the clock of 24/7, 7 days a week and 365 days. It is very rare to find any conventional retail stores that are open 24/7. The availability of online stores gives you the freedom to shop at your own pace and convenience. Another major advantage of online shopping is that it is constantly evolving and turning into a seamless experience, thanks to the advancement of technology. 5G will make mobile shopping easier than ever, and hardware such as AR and VR offer a novel way to see and try out a product before clicking on the ‘checkout’ button. Finally, Buying online means that you can read millions of reviews to ensure the quality of the product before purchasing it.

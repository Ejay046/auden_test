# Overview
I have created a small interactive application in python to calculate the price of a basket of items which factors in quantity discounts. (I have tried my best to follow the 1hr max recommendation so it is a bit rough. I ran out of time a bit at the end)

For the interactive application, i have only choosen to implement any functionalities that are related to checking-out the basket due to the time restraints.

The interactive program currently has some dummy data set up. The data can be changed, added to or removed in main.py

to run this application, all you need to do is run the main.py in your terminal
```
python3 main.py
```

for testing, install pytest by running 
```
pip3 install pytest
```

then run
```
pytest
```
or 
```
python3 -m pytest
```
tests have been written for each class, but i have pulled out tests for "checkout" to test_checkout.py for the ease of viewing since that is the goal for the challenge.

# Would Likes
- would've liked to extract promotions out into its own class (for the ease of adding new functionalities in the future) 
- I've started an Inventory class this class would be for a list of items available to add to the basket (this i didn't finish because of the time restrains and it also seemed a bit out of scope.)
- would've added more to the interactive part of the app
- would've liked to pull out a few things in the tests to set as fixtures
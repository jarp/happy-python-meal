import os
from happymeal.models.fries import Fries
from happymeal.models.condiment import Condiment
from happymeal.models.drinks import *
from happymeal.models.hamburger import Hamburger
from happymeal.models.toy import Toy
from happymeal.models.happy_meal import HappyMeal
from happymeal.models.cockroach import Cockroach

os.system("clear")
print("testing out the happy meal models using inheritance and composition\n\n")

# #create the drink and side
sprite = Sprite()
fries = Fries()

# create an array of all the toppings for the hamburher
condiments = []
condiments.append(Condiment("tomato", 10))
condiments.append(Condiment("Lettuce", 10))
condiments.append(Condiment("Mayo", 50))
condiments.append(Cockroach())

hamburger = Hamburger(condiments=condiments)

# add the toy
toy = Toy("car")

# compose the happy meal of all four objects
meal = HappyMeal(drink=sprite, main=hamburger, side=fries, toy=toy)

# output some info to the console:

print("i have just created a happy meal!")
print("this happy meal has {} calories".format(meal.calories()) )


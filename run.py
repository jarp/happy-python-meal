import os
from happymeal.models.fries import Fries
from happymeal.models.condiment import Condiment
from happymeal.models.drinks import *
from happymeal.models.hamburger import Hamburger
from happymeal.models.nuggets import Nuggets
from happymeal.models.toy import Toy
from happymeal.models.happy_meal import HappyMeal

os.system("clear")
print("testing out the happy meal models using inheritance and composition\n\n")

# #create the drink and side
sprite = Sprite()
diet_coke = DietCoke()
fries = Fries()

# create an array of all the toppings for the hamburher
condiments = []
condiments.append(Condiment("tomato", 10))
condiments.append(Condiment("Lettuce", 10))
condiments.append(Condiment("Mayo", 50))

hamburger = Hamburger(condiments=condiments)

nuggets = Nuggets()
# add the toy
toy = Toy("car")

# compose the happy meal of all four objects
meal = HappyMeal(drink=sprite, main=hamburger, side=fries, toy=toy)
meal2 = HappyMeal(drink=diet_coke, main=nuggets, side=fries, toy=toy)

# output some info to the console:

print("i have just created a happy meal!")
print(meal)
print("this happy meal has {} calories".format(meal.calories()) )

print("\n\n****************************\n\n")

print("i have just created a happy meal!")
print(meal2)
print("this happy meal has {} calories".format(meal2.calories()) )


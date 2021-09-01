import os
from happymeal.models.fries import Fries
from happymeal.models.condiment import Condiment
from happymeal.models.drinks import *
from happymeal.models.hamburger import Hamburger
from happymeal.models.toy import Toy
from happymeal.models.happy_meal import HappyMeal


f = Fries()
c = Condiment()
os.system("clear")

print(f.calories)
print(c.calories)


print("testing out the happy meal models using inheritance and composition\n\n")

# #create the drink and side
sprite = Sprite()
fries = Fries()

#create an array of all the toppings for the hamburher
condiments = []
condiments.append(Condiment("tomato", 10))
condiments.append(Condiment("Lettuce", 10))
condiments.append(Condiment("Mayo", 50))

h = Hamburger(condiments=condiments)
print(h.calories())

# # condiments << Cockroach.new
# # condiments << Cockroach.new
# # condiments << Pebble.new

# #create hamburge as the main dish and compose it with the array of toppings
hamburger = Hamburger(condiments)

# #add the toy
toy = Toy("car")

# #compose the happy meal of all four objects
meal = HappyMeal(sprite, hamburger, fries, toy)

# #output some info to the console:

print("i have just created a happy meal!")
print("this happy meal has {} calories".format(meal.calories()) )


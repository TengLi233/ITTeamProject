import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITTeamProject.settings')

import django
django.setup()
from HotPotWebsite.models import MenuCategory, Dish

def populate():

    potbottom_dishes = [
        {"title": "Spicy Bottom",
         "price": 20},
        {"title": "Unspicy Bottom",
         "price": 20},
        {"title": "Mixed Bottom",
         "price": 40}]

    vegetable_dishes = [
        {"title": "Tomato",
         "price": 20},
        {"title": "Tofu",
         "price": 20},
        {"title": "rice flour",
         "price": 40}]

    meat_dishes = [
        {"title": "beef",
         "price": 20},
        {"title": "pig",
         "price": 20},
        {"title": "lamb",
         "price": 40}]

    drinks_dishes = [
        {"title": "coke",
         "price": 20},
        {"title": "7 up",
         "price": 20},
        {"title": "wine",
         "price": 40}]

    cats = {"Pot Bottom": {"dishes": potbottom_dishes},
            "Vegetable": {"dishes": vegetable_dishes},
            "Meat": {"dishes": meat_dishes},
            "Drinks": {"dishes": drinks_dishes}}

    # add them to the dictionary above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # https://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["dishes"]:
            add_dish(c, p["title"], p["price"])

    # Print out the categories we have added.
    for c in MenuCategory.objects.all():
        for p in Dish.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_dish(cat, title, price):
    p = Dish.objects.get_or_create(category=cat, title=title)[0]
    p.price = price
    p.save()
    return p

def add_cat(name):
    c = MenuCategory.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
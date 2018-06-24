"""Data Abstractions"""

from utils import mean


#############################
# Phase 1: Data Abstraction #
#############################


# Reviews

def make_review(restaurant_name, rating):
    """Return a review data abstraction."""
    return [restaurant_name, rating]


def review_restaurant_name(review):
    """Return the restaurant name of the review, which is a string."""
    return review[0]


def review_rating(review):
    """Return the number of stars given by the review, which is a
    floating point number between 1 and 5."""
    return review[1]


# Users

def make_user(name, reviews):
    """Return a user data abstraction."""
    return [name, {review_restaurant_name(r): r for r in reviews}]


def user_name(user):
    """Return the name of the user, which is a string."""
    return user[0]


def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the user."""
    return user[1]


### === +++ USER ABSTRACTION BARRIER +++ === ###

def user_reviewed_restaurants(user, restaurants):
    """Return the subset of restaurants reviewed by user.

    Arguments:
    user -- a user
    restaurants -- a list of restaurant data abstractions
    """
    names = list(user_reviews(user))
    return [r for r in restaurants if restaurant_name(r) in names]


def user_rating(user, restaurant_name):
    """Return the rating given for restaurant_name by user."""
    reviewed_by_user = user_reviews(user)
    user_review = reviewed_by_user[restaurant_name]
    return review_rating(user_review)


# Restaurants

def make_restaurant(name, location, categories, price, reviews):
    """Return a restaurant data abstraction containing the name, location,
    categories, price, and reviews for that restaurant."""
    # BEGIN Question 2
    "*** YOUR CODE HERE ***"
    return [name, location, categories, price, reviews]
    # END Question 2


def restaurant_name(restaurant):
    """Return the name of the restaurant, which is a string."""
    # BEGIN Question 2
    "*** YOUR CODE HERE ***"
    return restaurant[0]
    # END Question 2


def restaurant_location(restaurant):
    """Return the location of the restaurant, which is a list containing
    latitude and longitude."""
    # BEGIN Question 2
    "*** YOUR CODE HERE ***"
    return restaurant[1]
    # END Question 2


def restaurant_categories(restaurant):
    """Return the categories of the restaurant, which is a list of strings."""
    # BEGIN Question 2
    "*** YOUR CODE HERE ***"
    return restaurant[2]
    # END Question 2


def restaurant_price(restaurant):
    """Return the price of the restaurant, which is a number."""
    # BEGIN Question 2
    "*** YOUR CODE HERE ***"
    return restaurant[3]
    # END Question 2


def restaurant_ratings(restaurant):
    """Return a list of ratings, which are numbers from 1 to 5, of the
    restaurant based on the reviews of the restaurant."""
    # BEGIN Question 2
    """>>> restaurant_price(soda)
1
>>> restaurant_ratings(soda)
Traceback (most recent call last):
  File "/Users/screwman/Docker/SICP_python/practice/maps/abstractions.py", line 116, in restaurant_ratings
    return [a[1] for a in list(restaurant[4])]
  File "/Users/screwman/Docker/SICP_python/practice/maps/abstractions.py", line 116, in <listcomp>
    return [a[1] for a in list(restaurant[4])]
  File "/Users/screwman/Docker/SICP_python/practice/maps/tests/test_functions.py", line 31, in __getitem__
    raise AbstractionViolation("Can't use [] notation on {} object".format(datatype(self)))
tests.test_functions.AbstractionViolation: Can't use [] notation on Review object

# Error: expected
#     [4.5, 4]
# but got
#     Traceback (most recent call last):
#       ...
#     AbstractionViolation: Can't use [] notation on Review object
>>> test.restore_implementations(abstractions)

Run only this test case with "python3 ok -q 02 --suite 2 --case 1"
"""
    "*** YOUR CODE HERE ***"
    # print([a[1] for a in list(restaurant[4])])
    return [a[1] for a in list(restaurant[4])]
    # return [restaurant[4][0][1], restaurant[4][1][1]]
    # END Question 2


# if __name__ == '__main__':
#     soda_reviews = [make_review('Soda', 4.5),
#                     make_review('Soda', 4)]
#     print(soda_reviews)

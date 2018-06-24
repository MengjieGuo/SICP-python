"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################
from practice.maps.abstractions import make_restaurant, make_review, restaurant_location, restaurant_name, user_rating, \
    restaurant_categories


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    # BEGIN Question 3
    "*** YOUR CODE HERE ***"
    """distance返回欧几里得距离， min 还是 sorted ， 使用 min 并指定 key 为新数据结构的 distance"""
    distance_data = [[a, distance(location, a)] for a in centroids]
    return min(distance_data, key=lambda x: x[1])[0]  # 这里按照从小到大排序
    # 看到网友有更简短的代码     return min(centroids, key=lambda x: distance(x, location))
    # END Question 3


# if __name__ == '__main__':
#     min_distance = find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
#     print(min_distance)


def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs
    将 pairs 中 key 相同的 value 组成一个list，最终是 list of list。
    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    # BEGIN Question 4
    "*** YOUR CODE HERE ***"
    # python风格的代码
    """对 group_by_first 来说这里的 key 就是距离最近的 centroids， value 是 restaurants
     所以需要先构造    group_by_first 的参数
     最后求得的就是 以 某 centroids 最近的 所有 restaurants 的 list
     餐厅集群
    """
    return group_by_first(
        [[find_closest(restaurant_location(restaurant), centroids), restaurant] for restaurant in restaurants])
    # 下面是拆分后的
    # pairs_collector = []
    # for r in restaurants:
    #     location = restaurant_location(r)
    #     pair = [find_closest(location, centroids), r]
    #     pairs_collector.append(pair)
    # print(pairs_collector)
    # return group_by_first(pairs_collector)
    # END Question 4


#
# if __name__ == '__main__':
#     r1 = make_restaurant('A', [-10, 2], [], 2, [
#         make_review('A', 4), ])
#     r2 = make_restaurant('B', [-9, 1], [], 3, [
#         make_review('B', 5),
#         make_review('B', 3.5), ])
#     c1 = [0, 0]
#     groups = group_by_centroid([r1, r2], [c1])
#     print(groups)


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # BEGIN Question 5
    # 返回集群中餐厅位置的质心。对餐厅集群来说，质心是：[所有餐厅横坐标的平均值，所有餐厅纵坐标的平均值]
    # [mean(), mean()]
    # 然后所有餐厅的横坐标 [restaurant_location(restaurant)[0] for restaurant in cluster]
    # 同理，所有餐厅的纵坐标 [restaurant_location(restaurant)[1] for restaurant in cluster]

    "*** YOUR CODE HERE ***"
    return [mean([restaurant_location(restaurant)[0] for restaurant in cluster]),
            mean([restaurant_location(restaurant)[1] for restaurant in cluster])]
    # END Question 5


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        # BEGIN Question 6
        "*** YOUR CODE HERE ***"
        grouped = group_by_centroid(restaurants, old_centroids)
        centroids = [find_centroid(c) for c in grouped]
        # END Question 6
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}

    xs = [feature_fn(r) for r in restaurants]
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants]
    # 1) the extracted feature value for each restaurant in restaurants
    # Q: What does the list ys represent? 0) user's ratings for the restaurants in restaurants

    # BEGIN Question 7
    """这里主要还是根据提示进行
        需要求 Sxx Syy Sxy 
        然后求 b a R^2
    """
    b, a, r_squared = 0, 0, 0  # REPLACE THIS LINE WITH2 YOUR SOLUTION
    zipped_xy = zip(xs, ys)
    Sxx = sum([pow(x - mean(xs), 2) for x in xs])
    Syy = sum([pow(y - mean(ys), 2) for y in ys])
    Sxy = sum([(x - mean(xs)) * (y - mean(ys)) for x, y in zipped_xy])
    b = Sxy / Sxx
    a = mean(ys) - b * mean(xs)
    r_squared = pow(Sxy, 2) / (Sxx * Syy)

    # END Question 7

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 8
    "*** YOUR CODE HERE ***"
    return max([find_predictor(user, reviewed, f) for f in feature_fns], key=lambda x: x[1])[0]
    # END Question 8


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)
    # BEGIN Question 9
    "*** YOUR CODE HERE ***"
    return {restaurant_name(r): user_rating(user, restaurant_name(r))
            if r in reviewed else predictor(r) for r in restaurants}
    # END Question 9


def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    # BEGIN Question 10
    "*** YOUR CODE HERE ***"
    return [r for r in restaurants if query in restaurant_categories(r)]

    # END Question 10


def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)

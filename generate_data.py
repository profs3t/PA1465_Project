""" Theodor Maran, Abbe Möllerström, Emil Liehl, DVAMI21, BTH """

import pickle
import sys
import math

def recursive_list():
    """ Create a recursive list """
    lst = []
    lst.append(lst)
    return lst

test_recursive_list = recursive_list()

# Random class
# class RandomClass:
#     """ Random number generator class """
#     def __init__(self, seed):
#         self.seed = seed

#     def random(self):
#         """ Generate a random number """
#         self.seed = (self.seed * 1103515245 + 12345) % 2**32

# randomClass = RandomClass(198)

test_dict = {
    "name": "Luna",
    "age": 27,
    "occupation": "Engineer",
    "hobbies": ["painting", "cycling", test_recursive_list],
    "is_student": False,
    "height_cm": math.inf * math.pi,
    "languages": {
        "native": "English",
        "secondary": "Spanish",
        "learning": "Japanese"
    },
    "favorite_foods": ["sushi", "pasta", "ice cream"],
    "lucky_numbers": [7, math.pi, math.inf],
    "pet": {
        "type": "dog",
        "name": "Buddy",
        "age": math.inf
    }
}

def save_pickle(data):
    """ Save data to a pickle file """
    python_version = sys.argv[1]
    operating_system = sys.argv[2]

    filename = f"generated-data-{operating_system}-{python_version}.pkl"

    with open(filename, "wb") as file:
        pickle.dump(data, file)

if __name__ == "__main__":
    save_pickle(test_dict)

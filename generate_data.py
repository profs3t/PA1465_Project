import pickle
import sys
import math

def recursiveList():
    lst = []
    lst.append(lst)
    return lst

test_recursive_list = recursiveList()

# Random class
class Random:
    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (self.seed * 1103515245 + 12345) % 2**32
        return

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
        "type": Random(198),
        "name": "Buddy",
        "age": math.inf
    }
}

def save_pickle(data):
    python_version = sys.argv[1]
    operating_system = sys.argv[2]

    filename = f"generated-data-{operating_system}-{python_version}.pkl"  # Adjust extension as needed

    with open(filename, "wb") as f:
        pickle.dump(data, f)

save_pickle(test_dict)

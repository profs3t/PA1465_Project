import pickle
import sys
from pathlib import Path

test_float = 1.253647850236475839

def recursiveList():
    lst = []
    lst.append(lst)
    return lst

test_recursive_list = recursiveList()

test_dict = {
    "name": "Luna",
    "age": 27,
    "occupation": "Engineer",
    "hobbies": ["painting", "cycling", "gaming"],
    "is_student": False,
    "height_cm": 170.5,
    "languages": {
        "native": "English",
        "secondary": "Spanish",
        "learning": "Japanese"
    },
    "favorite_foods": ["sushi", "pasta", "ice cream"],
    "lucky_numbers": [7, 13, 42],
    "pet": {
        "type": "dog",
        "name": "Buddy",
        "age": 4
    }
}

def save_pickle(data):
    python_version = sys.argv[1]
    operating_system = sys.argv[2]

    filename = f"{operating_system}_{python_version}.pkl"  # Adjust extension as needed

    with open(Path("pkl_files") / filename, "wb") as f:
        pickle.dump(data, f)

save_pickle(test_dict)

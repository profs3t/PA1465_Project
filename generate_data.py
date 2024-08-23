import pickle
import sys
import math

# Test data
test_dict = {
    "name": "Luna",
    "age": 27,
    "occupation": "Engineer",
    "hobbies": ["painting", "cycling", "reading"],
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

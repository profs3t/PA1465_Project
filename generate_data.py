import pickle
import sys
from pathlib import Path

test_float = 1.253647850236475839

def recursiveList():
    lst = []
    lst.append(lst)
    return lst

test_recursive_list = recursiveList()

def save_pickle(data):
    python_version = sys.argv[1]
    operating_system = sys.argv[2]

    folder_name = "pkl_files"
    folder_path = Path(folder_name)
    filename = f"{operating_system}_{python_version}.pkl"  # Adjust extension as needed
    file_path = folder_path / filename  # Use pathlib to construct the full file path

    with file_path.open('wb') as f:
        pickle.dump(data, f)

save_pickle(test_float)

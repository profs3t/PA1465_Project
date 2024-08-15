import pickle
import hashlib

# Mac, Win, Linux
# 3.9, 3.10, 3.11

test_float = 1.253647850236475839678956576587685657456476

def recursiveList():
    lst = []
    lst.append(lst)
    return lst

test_recursive_list = recursiveList()

def save_pickle(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def get_hash(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def compareHashes(filename1, filename2):
    hash1 = get_hash(filename1)
    hash2 = get_hash(filename2)
    return hash1 == hash2

def getPickles(operating_system, python_version):
    save_pickle(test_float, f'float_{operating_system}_{python_version}.pkl')
    save_pickle(test_recursive_list, f'list_{operating_system}_{python_version}.pkl')


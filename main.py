import pickle
import hashlib

test_data = [1,2,3]

# Use sha256 to hash the data
hash1 = hashlib.sha256()
hash1.update(pickle.dumps(test_data))


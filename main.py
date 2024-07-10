import pickle
import hashlib

test_data = 1

def hashData(data, python_version):
    hashPickle = hashlib.sha256()
    hashPickle.update(pickle.dumps(data))
    # Write the hash to a file named 'python_version'.hash
    with open(f"python_{python_version}.hash", "wb") as f:
        f.write(hashPickle.digest())

def compareHashes(filename1, filename2):
    with open(filename1, "rb") as f:
        hash1 = f.read()
    with open(filename2, "rb") as f:
        hash2 = f.read()
    return hash1 == hash2

print(compareHashes('python_3_12_2.hash', 'python_3_9_18.hash'))


def test_correct(input):
    serialized = pickle.dumps(input)
    deserialized = pickle.loads(serialized)

    hash_deserialized = hashlib.sha256(pickle.dumps(deserialized)).hexdigest()

    hash_input = hashlib.sha256(pickle.dumps(input)).hexdigest()

    return hash_input == hash_deserialized

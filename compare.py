import hashlib
import os
from pathlib import Path

def get_hash(filename):
    filepath = filename
    with open(filepath, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def compareHashes(filename1, filename2):
    hash1 = get_hash(filename1)
    hash2 = get_hash(filename2)
    return hash1 == hash2

def read_filenames():
    #create filenames dict
    os_dict = {"windows-latest": [], "macOS-latest": [], "ubuntu-latest": []}
    version_dict = {"3.9": [], "3.11": [], "3.12": []} 

    for filename in os.listdir("."):
        if filename.startswith("windows"):
            os_dict["windows-latest"].append(filename)
        elif filename.startswith("mac"):
            os_dict["mac-latest"].append(filename)
        elif filename.startswith("ubuntu"):
            os_dict["linux-latest"].append(filename)

        if filename.endswith("3.9.pkl"):
            version_dict["3.9"].append(filename)
        elif filename.endswith("3.11.pkl"):
            version_dict["3.11"].append(filename)
        elif filename.endswith("3.12.pkl"):
            version_dict["3.12"].append(filename)
    return os_dict, version_dict

def compare_files(filenames):
    for criteria in filenames:
        for i in range(len(filenames[criteria])):
            for j in range(i+1, len(filenames[criteria])):
                if not compareHashes(filenames[criteria][i], filenames[criteria][j]):
                    # Write to a file
                    print(f"Files {filenames[criteria][i]} and {filenames[criteria][j]} are different")

def main():
    os_dict, version_dict = read_filenames()
    compare_files(os_dict)
    compare_files(version_dict)
    print("Comparison done")

if __name__ == "__main__":
    main()

import hashlib
import os
from pathlib import Path

def get_hash(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def compareHashes(filename1, filename2):
    hash1 = get_hash(filename1)
    hash2 = get_hash(filename2)
    return hash1 == hash2



def read_filenames():
    #create filenames dict
    os_dict = {"windows-latest": [], "mac-latest": [], "linux-latest": []}
    version_dict = {"3.6": [], "3.7": [], "3.8": [], "3.9": [], "3.10": [], "3.11": []} 

    for filename in os.listdir("pkl_files"):
        if filename.startswith("windows"):
            os_dict["windows-latest"].append(filename)
        elif filename.startswith("mac"):
            os_dict["mac-latest"].append(filename)
        elif filename.startswith("linux"):
            os_dict["linux-latest"].append(filename)
        
        if filename.endswith("3.6.pkl"):
            version_dict["3.6"].append(filename)
        elif filename.endswith("3.7.pkl"):
            version_dict["3.7"].append(filename)
        elif filename.endswith("3.8.pkl"):
            version_dict["3.8"].append(filename)
        elif filename.endswith("3.9.pkl"):
            version_dict["3.9"].append(filename)
        elif filename.endswith("3.10.pkl"):
            version_dict["3.10"].append(filename)
        elif filename.endswith("3.11.pkl"):
            version_dict["3.11"].append(filename)
    return os_dict, version_dict

def compare_files(filenames):
    for criteria in filenames:
        for i in range(len(filenames[criteria])):
            for j in range(i+1, len(filenames[criteria])):
                if not compareHashes(filenames[criteria][i], filenames[criteria][j]):
                    #Save the filenames that are different
                    folder_name = "results"
                    Path(folder_name).mkdir(parents=True, exist_ok=True)
                    with open(f"{folder_name}/{criteria}.txt", "a") as f:
                        f.write(f"{filenames[criteria][i]} and {filenames[criteria][j]} are different\n")

def main():
    os_dict, version_dict = read_filenames()
    compare_files(os_dict)
    compare_files(version_dict)


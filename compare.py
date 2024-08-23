""" Theodor Maran, Abbe Möllerström, Emil Liehl, DVAMI21, BTH """

import hashlib
from pathlib import Path
import pickle
from generate_data import test_dict

WRITE_FILE = open('example.txt', 'a+', encoding='utf-8')

def get_hash(filename):
    """ Get the hash of a file """
    filepath = Path(filename) / (filename + ".pkl")
    with open(filepath, "rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()

def get_object(filename):
    """ Get the object from a file """
    filepath = Path(filename) / (filename + ".pkl")
    with open(filepath, "rb") as file:
        data = file.read()
    return pickle.loads(data)

def compare_hashes(filename1, filename2):
    """ Compare the hashes of two files """
    hash1 = get_hash(filename1)
    hash2 = get_hash(filename2)
    if hash1 != hash2:
        WRITE_FILE.write(f"Files {filename1} and {filename2} are different\n")
    return hash1 == hash2

def generate_filenames():
    """ Generate filenames for the different operating systems and python versions """
    os_list = ["windows-latest", "macOS-latest", "ubuntu-latest"]
    version_list = ["3.9", "3.11", "3.12"]
    filenames = [[], [], []]
    for index, operating_system in enumerate(os_list):
        for version in version_list:
            filenames[index].append(f"generated-data-{operating_system}-{version}")
    return filenames

def compare_files(filenames):
    """ Compare the files """
    success_count = 0
    fail_count = 0
    # Compare files within the same operating system
    for os_files in filenames:
        for i in range(len(os_files)):
            for j in range(i + 1, len(os_files)):
                result = compare_hashes(os_files[i], os_files[j])
                if result:
                    success_count+=1
                else:
                    fail_count+=1

    # Compare files across different operating systems for the same python version
    for version_index in range(len(filenames[0])):
        for i in range(len(filenames)):
            for j in range(i + 1, len(filenames)):
                resualt = compare_hashes(filenames[i][version_index], filenames[j][version_index])
                if resualt:
                    success_count+=1
                else:
                    fail_count+=1

    print("Success:", success_count)
    print("Fail:", fail_count)

def compare_deserialized_data(filenames):
    """ Compare the files """
    # Compare each file with the original object
    success_count = 0
    fail_count = 0
    
    for operating_system in filenames:
        for version in operating_system:
            data = get_object(version)
            if data != test_dict:
                fail_count+=1
                WRITE_FILE.write(f"Data in file {version} is different from the original data\n")
            else:
                success_count+=1

    print("Success:", success_count)
    print("Fail:", fail_count)

def main():
    """ Main function """
    filenames = generate_filenames()
    print("Starting hash comparison")
    compare_files(filenames)
    print("Hash comparison done\nStarting object comparison")
    compare_deserialized_data(filenames)
    print("Object comparison done")
    print(WRITE_FILE.read())
    WRITE_FILE.close()

if __name__ == "__main__":
    main()

import hashlib
from pathlib import Path

WRITE_FILE = open('example.txt', 'a')

def get_hash(filename):
    filepath = Path(filename) / (filename + ".pkl")
    with open(filepath, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def compareHashes(filename1, filename2):
    hash1 = get_hash(filename1)
    hash2 = get_hash(filename2)
    if hash1 != hash2:
        WRITE_FILE.write(f"Files {filename1} and {filename2} are different\n")
        return False
    else:
        print(f"Files {filename1} and {filename2} are the same")
        return True

def generate_filenames():
    os_list = ["windows-latest", "macOS-latest", "ubuntu-latest"]
    version_list = ["3.9", "3.11", "3.12"]
    filenames = [[], [], []]
    for index, operating_system in enumerate(os_list):
        for version in version_list:
            filenames[index].append(f"generated-data-{operating_system}-{version}")
    return filenames

def compare_files(filenames):
    #compare files in the same operating system
    success_count = 0
    fail_count = 0
        # Compare files within the same operating system
    for os_files in filenames:
        for i in range(len(os_files)):
            for j in range(i + 1, len(os_files)):
                result = compareHashes(os_files[i], os_files[j])
                if result:
                    success_count+=1
                else:
                    fail_count+=1

    # Compare files across different operating systems for the same version
    for version_index in range(len(filenames[0])):
        for i in range(len(filenames)):
            for j in range(i + 1, len(filenames)):
                resualt = compareHashes(filenames[i][version_index], filenames[j][version_index])
                if resualt:
                    success_count+=1
                else:
                    fail_count+=1

    print(success_count)
    print(fail_count)

    # compareHashes(filenames[0][0], filenames[0][1])
    # compareHashes(filenames[0][0], filenames[0][2])
    # compareHashes(filenames[0][1], filenames[0][2])

    # #macOS
    # compareHashes(filenames[1][0], filenames[1][1])
    # compareHashes(filenames[1][0], filenames[1][2])
    # compareHashes(filenames[1][1], filenames[1][2])

    # #ubuntu
    # compareHashes(filenames[2][0], filenames[2][1])
    # compareHashes(filenames[2][0], filenames[2][2])
    # compareHashes(filenames[2][1], filenames[2][2])

    # #Compare files in different operating system, same version
    # #3.9
    # compareHashes(filenames[0][0], filenames[1][0])
    # compareHashes(filenames[0][0], filenames[2][0])
    # compareHashes(filenames[1][0], filenames[2][0])
    # #3.11
    # compareHashes(filenames[0][1], filenames[1][1])
    # compareHashes(filenames[0][1], filenames[2][1])
    # compareHashes(filenames[1][1], filenames[2][1])
    # #3.12
    # compareHashes(filenames[0][2], filenames[1][2])
    # compareHashes(filenames[0][2], filenames[2][2])
    # compareHashes(filenames[1][2], filenames[2][2])

    """
    for i in range(3):
        for j in range(3):
            compareHashes(filenames[i][j], filenames[i][j])
    """

def main():
    filenames = generate_filenames()
    compare_files(filenames)
    print("Comparison done")

    #print all rows from WRITE_FILE
    print(WRITE_FILE.read())
    WRITE_FILE.close()

if __name__ == "__main__":
    main()

'''
This module contains all file related functions
'''

import binascii
import os

# Default path of the "SAVED.GAM" file to be edited
GameFilePath = "SAVED.GAM" # File in program folder, change to actual "SAVED.GAM" filepath
Content = []


# A function that checks if a given path is a file that exists
def check_file_exists():
    try:
        if not os.path.isfile(GameFilePath): raise IOError
    except IOError:
        path = GameFilePath.split("\\", 2)
        print("{2} file does exist at {0}\\{1}".format(path[0], path[1], path[2]))
        return False
    else: return True


# A function that changes the path for the "SAVED.GAM" file
def change_file_path():
    global GameFilePath
    while not os.path.isfile(GameFilePath):
        GameFilePath = input("Enter correct SAVED.GAM file path: ")


# A function that reads the "SAVED.GAM" file
def read_file():
    global Content
    if not check_file_exists(): change_file_path()
    with open(GameFilePath, 'rb') as f:
        content = f.read()
    content = binascii.hexlify(content)
    content = [(content[i:i + 2]) for i in range(0, len(content), 2)]
    Content = content
    f.close()
    return content


# A function that writes to the "SAVED.GAM" file
def write_file():
    global Content
    content = b''.join(Content)
    content = binascii.unhexlify(content)
    with open(GameFilePath, 'rb+') as f:
        f.write(content)
    f.close()


# A function that changes a value in the "SAVED.GAM" file, given its offset
def change_value(value, rng, value_flag=-1):
    if type(rng) is list:
        Content[rng[0]:rng[1]+1] = value[::value_flag]
    else: Content[rng] = value

import os
from app.utils.globals import globals_instance

def create_folder_path(path, name):
    parent_directory = path + '/'
    full_path = os.path.join(parent_directory, name)

    try:
        os.mkdir(full_path)
    except Exception as e:
        print(f'A aparut eroarea in create_folder: {e} !')

def create_file_path(path, name, mode):
    parent_directory = path + '/'
    name = name + '.txt'
    full_path = os.path.join(parent_directory, name)

    try:
        file = open(full_path, mode)
    except Exception as e:
        print(f'A aparut eroarea in create_file: {e} !')





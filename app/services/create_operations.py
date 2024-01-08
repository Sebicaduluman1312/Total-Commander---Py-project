import os
from app.utils.globals import globals_instance

def create_folder_path(path, name):
    """
    Creates a folder at the specified path with the given name.

    :param path: The path to the parent directory.
    :param name: The name of the folder to be created.
    """
    parent_directory = path + '/'
    full_path = os.path.join(parent_directory, name)

    try:
        os.mkdir(full_path)
    except Exception as e:
        print(f'A aparut eroarea in create_folder: {e} !')

def create_file_path(path, name, mode):
    """
    Creates a file at the specified path with the given name and mode.

    :param path: The path to the parent directory.
    :param name: The name of the file to be created.
    :param mode: The mode in which the file should be opened.
    """
    parent_directory = path + '/'
    name = name + '.txt'
    full_path = os.path.join(parent_directory, name)

    try:
        file = open(full_path, mode)
    except Exception as e:
        print(f'A aparut eroarea in create_file: {e} !')





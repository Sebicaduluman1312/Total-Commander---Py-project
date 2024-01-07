import os

class GlobalVariables:
    home_path = os.path.expanduser("~")
    current_path_left = home_path
    current_path_right = home_path
    return_right = 0
    return_left = 0

globals_instance = GlobalVariables()

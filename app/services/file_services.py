import datetime
import os
from ..utils.formatings import is_directory, is_file, sort_key_folder, format_datetime, icon_dictionary
from ..utils.globals import globals_instance


def get_folder_content(path):
    try:
        content = os.listdir(path)

        all_path = [os.path.join(path, element) for element in content]
        sorted_elements = sorted(all_path, key=sort_key_folder)
        sorted_elements_name = [element.split("/")[-1] for element in sorted_elements]
        sorted_elements.reverse()
        sorted_elements_name.reverse()
        elements_information = [get_element_information(el) for el in sorted_elements]

        return sorted_elements_name, path, elements_information

    except Exception as e:
        print(f"A aparut o eroare {e}!!!!!!!")

def get_only_folders_from_home():
    try:
        content = os.listdir(globals_instance.home_path)
        paths_of_elements = [os.path.join(globals_instance.home_path, element) for element in content]
        only_folder_paths = [path for path in paths_of_elements if is_directory(path)]
        only_folder_names = [name.split("/")[-1] for name in only_folder_paths]

        return only_folder_names

    except FileNotFoundError:
        print("Directorul home nu a fost gasit!")


def get_type_of_file(path):
    img_extension = ['.jpg', '.png', '.jpeg', 'gif']
    exe_extension = ['.exe', '.bat', '.sh']
    archive_extension = ['.zip', '.tar', '.rar']
    sound_video_extension = ['.mp3', '.wav', '.ogg', '.mp4', '.mkv', '.avi']
    source_code_extension = ['.js', '.java', '.py', '.html', '.css', '.c']
    pdf_extension = ['.pdf']

    extension = os.path.splitext(path)[1]
    if extension in img_extension:
        return 'IMG'
    elif extension in exe_extension:
        return 'EXE'
    elif extension in archive_extension:
        return 'ARCHIVE'
    elif extension in source_code_extension:
        return 'CODE'
    elif extension in sound_video_extension:
        return 'SOUND/VIDEO'
    elif extension in pdf_extension:
        return 'PDF'
    elif is_file(path):
        return 'FILE'
    elif is_directory(path):
        return 'DIR'

    return 'UNKNOWN'

def get_icon_of_file(type_of_file):
    type_of = str(type_of_file)

    return icon_dictionary[type_of]


def get_element_information(path):
    try:
        data = {}  # tip element, size, data crearii

        information = os.stat(path)
        dimension = os.path.getsize(path)
        dimension_mb = round(dimension / (1024.0 * 1024.0), 6)

        #Windows
        # c_time = os.path.getctime(path)
        # date_time = datetime.datetime.fromtimestamp(c_time)

        #Mac OS
        c_time = information.st_birthtime
        date_time = datetime.datetime.fromtimestamp(c_time)
        date_time = format_datetime(date_time)

        data['MB'] = str(dimension_mb) + ' MB'
        data['date_time'] = date_time
        data['tip'] = get_type_of_file(path)
        data['icon'] = get_icon_of_file(get_type_of_file(path))

        return data

    except Exception as ex:
        print(f"A aparut o problema: {ex}")

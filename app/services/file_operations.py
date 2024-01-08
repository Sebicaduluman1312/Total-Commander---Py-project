import os
from app.utils.globals import globals_instance

def delete_panel_elements(left_panel, right_panel, left_path, right_path):
    """
    Delete service, it deletes recursevly items from a directory, after that the funtion remove the directory per se.
    It goes from every checked element from every panel

    :param left_panel: - is a vector of checked elements from left panel
    :param right_panel: - is a vector of checked elements from right panel
    :param left_path: - the current path of the left panel
    :param right_path: - the current path of the right panel
    :return: nothing

    """
    for elem in left_panel:
        create_path = left_path + '/'
        full_path = os.path.join(create_path, elem)
        try:
            if os.path.isdir(full_path):
                elements = os.listdir(full_path)
                new_left_path = full_path
                delete_panel_elements(elements, right_panel, new_left_path, right_path)
                if os.path.exists(full_path):
                    os.rmdir(full_path)
            else:
                if os.path.exists(full_path):
                    print(full_path)
                    os.remove(full_path)
        except Exception as e:
            print("Eroare la functia de stergere a elementelor!")

    for elem in right_panel:
        create_path = right_path + '/'
        full_path = os.path.join(create_path, elem)
        try:
            if os.path.isdir(full_path):
                elements = os.listdir(full_path)
                new_right_path = full_path
                delete_panel_elements(left_panel, elements, left_path, new_right_path)
                if os.path.exists(full_path):
                    os.rmdir(full_path)
            else:
                if os.path.exists(full_path):
                    print(full_path)
                    os.remove(full_path)
        except Exception as e:
            print("Eroare la functia de stergere a elementelor!")


def rename_element_path(old_name, new_name):
    """
    Is a function that rename an element from a path. It recieves two names, it makes full path

    :param old_name: - represents the name of selected element
    :param new_name: - represents the new name of element

    """
    current_path_choice1 = globals_instance.current_path_left + '/' + old_name
    current_path_choice2 = globals_instance.current_path_right + '/' + old_name

    print(current_path_choice1, current_path_choice2)
    try:
        if os.path.exists(current_path_choice1):
            new_path = globals_instance.current_path_left + '/' + new_name
            os.rename(current_path_choice1, new_path)
        else:
            new_path = globals_instance.current_path_right + '/' + new_name
            os.rename(current_path_choice2, new_path)
    except Exception as e:
        print("Eroare la functia de rename a elementului!")


def recursive_copy(start, end):
    """
    Recursively copies files and directories from the 'start' path to the 'end' path.

    :param start: The source path (file or directory) to be copied.
    :param end: The destination path where the content from 'start' will be copied.
    :return: None
    """
    for route in start:
        try:
            if os.path.isdir(route):

                name_of_folder = os.path.basename(route)
                path_to_create_dir = os.path.join(end, name_of_folder)
                os.makedirs(path_to_create_dir, exist_ok=True)

                list_of_content = os.listdir(route)
                list_of_paths = [os.path.join(route, name) for name in list_of_content]

                recursive_copy(list_of_paths, path_to_create_dir)

            elif os.path.isfile(route):
                with open(route, 'rb') as original_file_desc:
                    content = original_file_desc.read()

                nume_fisier, _ = os.path.splitext(os.path.basename(route))
                write_route = os.path.join(end, nume_fisier)

                i = 1
                while os.path.exists(write_route):
                    write_route = os.path.join(end, f"{nume_fisier}_{i}")
                    i += 1

                write_route += os.path.splitext(route)[1]

                with open(write_route, 'wb') as destination_file_desc:
                    destination_file_desc.write(content)

        except Exception as e:
            print(f"A aparut o eroare la copiere: {e} pentru sursa: {route}")


def get_file_content(path):
    """
    Reads the content of a file specified by the provided path.

    :param path: The path to the file.
    :return: The content of the file as a string if successful, None otherwise.
    """
    try:
        with open(path, 'r') as file_desc:
            content = file_desc.read()
        return content
    except FileNotFoundError:
        print(f"Fisierul {path} nu a fost gasit")
        return None
    except Exception as e:
        print(f"Eroare la obtine content file: {e}!")
        return None
def write_file_content(path, content):
    """
    Writes the provided content to a file specified by the provided path.

    :param path: The path to the file.
    :param content: The content to be written to the file.
    :return: None if successful, or an error message if an exception occurs.
    """
    try:
        with open(path, 'w') as file_desc:
            file_desc.write(content)
    except FileNotFoundError:
        print(f"Fisierul {path} nu a fost gasit")
        return None
    except Exception as e:
        print(f"Eroare la obtine content file: {e}!")
        return None


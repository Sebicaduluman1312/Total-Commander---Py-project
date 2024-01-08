import os
from app.utils.globals import globals_instance
def delete_panel_elements(left_panel, right_panel, left_path, right_path):
    for elem in left_panel:
        create_path = left_path + '/'
        full_path = os.path.join(create_path, elem)
        try:
            if os.path.isdir(full_path):
                elements = os.listdir(full_path)
                new_left_path = full_path
                delete_panel_elements(elements, right_panel, new_left_path, right_path)
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
                os.rmdir(full_path)
            else:
                if os.path.exists(full_path):
                    print(full_path)
                    os.remove(full_path)
        except Exception as e:
            print("Eroare la functia de stergere a elementelor!")


def rename_element_path(old_name, new_name):
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
    for route in start:
        if os.path.isdir(route):
            try:
                name_of_folder = os.path.basename(route)
                path_to_create_dir = end + '/' + name_of_folder
                os.mkdir(path_to_create_dir)

                # cream lista start recursiv in care sa punem si path urile ca noi o sa avem doar numele
                list_of_content = os.listdir(route)
                list_of_paths = [os.path.join(path_to_create_dir, name) for name in list_of_content]

                recursive_copy(list_of_paths, path_to_create_dir)
            except Exception as e:
                print(f"A aparut o eroare la copierea serviciului, in copierea directorului: {e}!!!")

        elif os.path.isfile(route):
            try:
                with open(route, 'rb') as original_file_desc:
                    content = original_file_desc.read()

                with open(end, 'wb') as destination_file_desc:
                    destination_file_desc.write(content)
            except FileNotFoundError:
                print("Fisierul original nu exista")
            except Exception as e:
                print(f"Eroarea la copierea fisierului: {e}")


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


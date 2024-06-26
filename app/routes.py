import copy
import os.path
from app import app
from flask import render_template, request, jsonify
from app.services.file_services import get_folder_content
from app.services.create_operations import create_folder_path, create_file_path
from app.services.file_operations import delete_panel_elements, rename_element_path, recursive_copy, get_file_content, write_file_content
from app.utils.globals import globals_instance

@app.route("/", methods=['GET', 'POST'])
def render_main_page():
    '''
        The specific function for the '/' route in which the move from one folder to another
        is practically made, we take the parameters from the url, so we keep track of the current
        path that we store in it global variable.
        When we are not on the home path on both panels, we will render to a different
        template in which we get the elements from the left and right panels, after which we
        process them with Jinja on the html

        :return: render_template


    '''
    try:
        left_path = request.args.get('leftPath', default=globals_instance.home_path)
        right_path = request.args.get('rightPath', default=globals_instance.home_path)
        home_path = globals_instance.home_path

        if left_path == home_path and right_path == home_path:

            home_items, path, info = get_folder_content(globals_instance.home_path)

            globals_instance.return_left = 0
            globals_instance.return_right = 0
            globals_instance.current_path_left = globals_instance.home_path
            globals_instance.current_path_right = globals_instance.home_path
            return render_template('index.html', return_to_previous_left=0, return_to_previous_right=0,
                                   items_left=home_items, path_left=path, info_left=info, items_right=home_items,
                                   path_right=path, info_right=info)
        else:
            deep_copy_left = copy.deepcopy(globals_instance.current_path_left)
            deep_copy_right = copy.deepcopy(globals_instance.current_path_right)
            deep_ok_left = copy.deepcopy(globals_instance.return_left)
            deep_ok_right = copy.deepcopy(globals_instance.return_right)

            if globals_instance.current_path_left.strip() != left_path.strip():
                globals_instance.current_path_left = left_path
                globals_instance.return_left = 1

            elif globals_instance.current_path_right.strip() != right_path.strip():
                globals_instance.current_path_right = right_path
                globals_instance.return_right = 1

            if globals_instance.current_path_left == home_path:
                globals_instance.return_left = 0
            if globals_instance.current_path_right == home_path:
                globals_instance.return_right = 0

            left_items, left_path, left_info = get_folder_content(globals_instance.current_path_left)
            right_items, right_path, right_info = get_folder_content(globals_instance.current_path_right)
            return render_template('index.html', return_to_previous_left=globals_instance.return_left,
                                   return_to_previous_right=globals_instance.return_right, items_left=left_items,
                                   path_left=left_path, info_left=left_info, items_right=right_items,
                                   path_right=right_path, info_right=right_info)
    except Exception as e:
        left_items, left_path, left_info = get_folder_content(deep_copy_left)
        right_items, right_path, right_info = get_folder_content(deep_copy_right)
        globals_instance.current_path_left = deep_copy_left
        globals_instance.current_path_right = deep_copy_right
        globals_instance.return_left = deep_ok_left
        globals_instance.return_right = deep_ok_right
        return render_template('index.html', return_to_previous_left=deep_ok_left,
                               return_to_previous_right=deep_ok_right, items_left=left_items,
                               path_left=left_path, info_left=left_info, items_right=right_items,
                               path_right=right_path, info_right=right_info)


@app.route("/create_folder", methods=["GET", "POST"])
def create_folder():
    '''
        The specific function of the /create_folder route in which you receive from the front
        the name of the folder that will be created and the panel in which we want to perform
        the operation

        :return: return json to front
    '''
    data = request.get_json()
    print('Date primite de pe front la create folder: ', data)
    if data['current_panel'] == '1':
        path_to_send = globals_instance.current_path_left
        create_folder_path(path_to_send, data['folder_name'])
    elif data['current_panel'] == '2':
        path_to_send = globals_instance.current_path_right
        create_folder_path(path_to_send, data['folder_name'])

    return jsonify({"status" : "succes", "message" : "The folder was succesfully created"})

@app.route("/create_file", methods=["GET", "POST"])
def create_file():
    """
    Creates a new file.

    :return: JSON response indicating the success or failure of the operation.
    """
    data = request.get_json()
    if data['current_panel'] == '1':
        path_to_send = globals_instance.current_path_left
        create_file_path(path_to_send, data['file_name'], 'wb')
    elif data['current_panel'] == '2':
        path_to_send = globals_instance.current_path_right
        create_file_path(path_to_send, data['file_name'], 'wb')

    return jsonify({"status" : "succes", "message" : "The file was succesfully created"})

@app.route("/delete_elements", methods=["GET", "POST"])
def delete_elements():
    """
    Deletes the selected elements from the specified panels.

    :return: JSON response with success message or an error message.
    """
    data = request.get_json()
    delete_panel_elements(data['left_panel'],data['right_panel'], globals_instance.current_path_left, globals_instance.current_path_right)
    return jsonify({"status" : "succes", "message" : "The files was succesfully deleted"})

@app.route("/rename", methods=["GET","POST"])
def rename_element():
    """
    Renames an element.

    :return: JSON response indicating the success or failure of the operation.
    """
    data = request.get_json()

    rename_element_path(data['old_value'], data['rename_value'], data['c_panel'])

    return jsonify({"status" : "succes", "message" : "The element was succesfully renamed"})

@app.route("/copy", methods=["GET","POST"])
def copy_content():
    """
   Copies the content from one location to another.

   :return: JSON response with success message or an error message.
   """
    data = request.get_json()

    recursive_copy(data["start_path"], data["end_path"])

    return jsonify({"status" : "succes", "message" : "The element was copied"})

@app.route("/move", methods=["GET","POST"])
def move_content():
    """
    Moves the content from one location to another.

    :return: JSON response with success message or an error message.
    """
    data = request.get_json()

    recursive_copy(data["start_path"], data["end_path"])
    delete_panel_elements(data['left_panel'],data['right_panel'], globals_instance.current_path_left, globals_instance.current_path_right)

    return jsonify({"status" : "succes", "message" : "The element was moved"})

@app.route("/get_content", methods=["GET","POST"])
def get_content():
    """
    Gets the content of a file.

    :return: JSON response with the content of the file or an error message.
    """
    data = request.get_json()

    path = data['path']
    content_of_file = get_file_content(path)
    print(content_of_file)

    if content_of_file is None:
        return jsonify({"status" : "error", "message" : "Eroare la citirea fisierului"})
    else:
        return jsonify({"status" : "succes", "content" : content_of_file})


@app.route("/edit_file", methods=["GET","POST"])
def edit_file():
    """
    Edits the content of a file.

    :return: JSON response indicating the success or failure of the operation.
    """
    data = request.get_json()

    print(data)
    path = data['path']
    info = data['content_to']
    write_file_content(path, info)

    return jsonify({"status" : "succes", "message" : "The file was succesfuly edited"})

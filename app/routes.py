import os.path
from app import app
from flask import render_template
from app.services.file_services import get_folder_content
from app.utils.globals import globals_instance
from flask import request


@app.route("/", methods=['GET', 'POST'])
def render_main_page():
    left_path = request.args.get('leftPath', default=globals_instance.home_path)
    right_path = request.args.get('rightPath', default=globals_instance.home_path)
    home_path = globals_instance.home_path

    if left_path == home_path and right_path == home_path:
        home_items, path, info = get_folder_content(globals_instance.home_path)
        globals_instance.return_left = 0
        globals_instance.return_right = 0
        globals_instance.current_path_left = globals_instance.home_path
        globals_instance.current_path_right = globals_instance.home_path
        return render_template('index.html', return_to_previous_left=0, return_to_previous_right=0, items_left=home_items, path_left=path, info_left=info, items_right=home_items, path_right=path, info_right=info)
    else:
        print(globals_instance.current_path_left, left_path)
        print(globals_instance.current_path_right, right_path)
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
        return render_template('index.html', return_to_previous_left=globals_instance.return_left, return_to_previous_right=globals_instance.return_right, items_left=left_items, path_left=left_path, info_left=left_info, items_right=right_items, path_right=right_path, info_right=right_info)


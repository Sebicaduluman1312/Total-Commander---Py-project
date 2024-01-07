import os
import datetime

icon_dictionary = {
    'FILE' : '../static/images/file_img.png',
    'DIR' : '../static/images/folder_img.png',
    'IMG' : '../static/images/img.png',
    'PDF' : '../static/images/pdf_img.png',
    'CODE' : '../static/images/code.png',
    'SOUND/VIDEO' : '../static/images/sound.png',
    'ARCHIVE' : '../static/images/archive.png',
    'EXE' : '../static/images/exec.png',
    'UNKNOWN': '../static/images/unknown.png'
}

def is_directory(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

def sort_key_folder(resource):
    return (os.path.isdir(resource), resource)

def format_datetime(date_time):
    format_data = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return format_data

import os
import shutil


def delete_contents_of_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def force_copy_folder(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def dump_html_to_file(html, path):
    with open(path, 'w') as html_file:
        html_file.write(html)

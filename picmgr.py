import os
import string

global DEFAULT_PIC_DIR
DEFAULT_PIC_DIR = 'pics'

global tags
global tag_table

tags = tuple()
tag_table = {}

def _add_tag(tag, f_name):
    global tags
    global tag_table
    if tag not in tags:
        tags += (tag,)
        tag_table[tag] = [f_name]
    else:
        tag_table[tag].append(f_name)

def _tags_from_filepath(file_path):
    basename = os.path.basename(file_path)
    f_tags = basename.split('-')
    if '.' in basename:
        f_tags = basename[:basename.find('.')].split('-')
    #[1: to drop pics/ folder, :-1] to drop the filename itself
    dir_implied_tags = file_path.split(os.sep)[1:-1]
    f_tags += dir_implied_tags

    for t in f_tags:
        if t.strip()[0].isdigit():
            break
        else:
            _add_tag(t, file_path)

def init(pic_dir=DEFAULT_PIC_DIR):
    for directory_and_files in os.walk('pics'):
        directory = directory_and_files[0]
        for f in directory_and_files[2]:
            if f.startswith('.') or os.path.isdir(f):
                continue
            f_tags = _tags_from_filepath(os.path.join(directory, f))

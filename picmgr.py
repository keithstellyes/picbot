import os

file_paths = os.listdir('pics')
global tags
global tag_table

tags = tuple()
tag_table = {}

def _add_tag(tag, f_name):
    global tags
    global tag_table
    if tag not in tags:
        tags += (tag,)
        tag_table[tag] = [f]
    else:
        tag_table[tag].append(f)

for f in file_paths:
    f_tags = f[:f.index('.')].split('-')
    for t in f_tags:
        try:
            int(t)
            break
        except ValueError:
            pass
        _add_tag(t, f)


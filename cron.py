import os

types = ['docx', 'zip', 'pdf', 'deb', 'mp3', 'csv', 'tar', 'gz', 'txt']

base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'Downloads')
pwd = os.chdir(path)


full_list = os.listdir(pwd)
for type_ in types:
    if type_ not in os.listdir():
        os.mkdir(type_)

for file in full_list:
    for type_ in types:
        if '.' + type_ in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type_, file)
            os.replace(old_path, new_path)
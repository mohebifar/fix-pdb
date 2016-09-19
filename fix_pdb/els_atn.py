import os
from shutil import copyfile


def fix_els_atn(file_path):
    extension = os.path.splitext(file_path)[1]

    if extension == '.pdb':
        with open(file_path, 'r+') as file:

            copyfile(file_path, file_path + '.bak')

            output = []

            lines = file.readlines()

            for record in lines:
                if record[0:4] == 'ATOM':
                    element = record[13:16].strip().rjust(2)
                    record = record[0:76] + element + record[78:]

                output.append(record)

            file.seek(0)
            data = ''.join(output)
            file.write(data)
            file.truncate()

            return '"%s" successfully fixed.' % file_path

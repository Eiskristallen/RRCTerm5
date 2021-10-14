
def read_file(file_name):
    new_data = []
    with open(file_name, 'r') as myfile:
        lines = myfile.readlines()
    for line in lines:
        if line == "Aqua #00ffff\n":
            line = 'Azure #007fff\n'
        new_data.append(line)
        print(line)
    return new_data


def overwrite_file(file_name):
    new_data = read_file(file_name)
    with open(file_name, 'w') as myfile:
        myfile.writelines(new_data)


overwrite_file("test.txt")

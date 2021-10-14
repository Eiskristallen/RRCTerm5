
def read_file(file_name):
    with open(file_name, 'r') as myfile:
        lines = myfile.readlines()
        myfile.close()
    for line in lines:
        if line == "Aqua #00ffff\n":
            line = 'Azure #007fff\n'
        print(line)


read_file("test.txt")


def overwrite_file(file_name):
    new_data = []
    with open(file_name, 'r') as myfile:
        lines = myfile.readlines()
        myfile.close()
    for line in lines:
        if line == "Aqua #00ffff\n":
            line = 'Azure #007fff\n'
        new_data.append(line)
    print(new_data)
    with open(file_name, 'w') as myfile:
        myfile.writelines(new_data)
        myfile.close()


# overwrite_file("test.txt")

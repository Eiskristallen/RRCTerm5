import csv
# 1. Using your favourite text editor, create a CSV file with these lines:
# Temp,Press,Humidity
# 1.1,55.5,22.2
# 3.3,4.4,6.6
# 8.8,99.9,7.7


# 2. Write a function (csv_reader) that reads each line of the csv file into a dictionary using csv.DictReader, and multiplies each number by 2. It should store each modified dictionary in a list, and return a list of dictionaries. Each item in the list is one row of the CSV file, in dictionary format.


def double(filename):
    with open(filename, 'r') as myfile:
        new_list = []
        reader = csv.DictReader(myfile)
        for x in reader:
            new_list.append({
                "Temp": float(x['“Temp”'])*2,
                "Press": float(x[' “Press”'])*2,
                "Humidity": float(x[' “Humidity”'])*2
            })
        return new_list


# print(double('test.csv'))

# 3. Write another function (csv_writer) that takes
# the list of dictionaries as an argument, and writes
# the modified numbers out to a new CSV file, using csv.DictWriter.


def write_csv(list_dict, filename):
    with open(filename, 'w') as csvfile:
        csv_column = list_dict[0].keys()
        csv_column = list(csv_column)
        writer = csv.DictWriter(csvfile, fieldnames=csv_column)
        writer.writeheader()
        for num, val in enumerate(list_dict):
            writer.writerow({csv_column[0]: list_dict[num]['Temp'],
                             csv_column[1]: list_dict[num]['Press'],
                             csv_column[2]: list_dict[num]['Humidity']})


write_csv(double('test.csv'), 'new.csv')

# 4. Here is an example of DictWriter:
# import csv
# with open('names.csv', 'w', newline='') as csvfile:
# fieldnames = ['first_name', 'last_name']
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# writer.writeheader()
# writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
# writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

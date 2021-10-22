# Instructions
# Use the example database code from the class presentation as a base to write a class called DBOperations.

# Create one function/method to initialize the database and create the table.

# Create one function/method to receive a dictionary of dictionaries (sample data below) and correctly insert the data into the DB. Use "Winnipeg, MB" as the location. Don’t hard code your values, use the ? parameter functionality.

# Create one function to print out the data currently in the database.

# Sample Data:

import sqlite3
from sqlite3.dbapi2 import Date
weather = {"2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 7.1},
           "2018-06-02": {"Max": 22.2, "Min": 11.1, "Mean": 15.5},
           "2018-06-03": {"Max": 31.3, "Min": 29.9, "Mean": 30.0}}


class DBOperations:
    def __init__(self):
        try:
            conn = sqlite3.connect("weather.sqlite")
            print("Opened database successfully.")
            self.conn = conn
        except Exception as e:
            print("Error opening DB:", e)
        try:
            cursor = conn.cursor()
            self.cursor = cursor
            self.cursor.execute("""create table samples
                    (id integer primary key autoincrement not null,
                    date text not null,
                    location text not null,
                    min_temp real not null,
                    max_temp real not null,
                     avg_temp real not null);""")
            self.conn.commit()
            print("Table created successfully.")
        except Exception as e:
            print("Error creating table:", e)

    def insert_data(self, dicts):
        try:
            for key, val in dicts.items():
                sql = """insert into samples (date,location,min_temp,max_temp,avg_temp)
                values (?,?,?,?,?)"""
                data = (key, 'Winnipeg,MB', val["Max"],
                        val["Min"], val["Mean"])
                self.cursor.execute(sql, data)
                self.conn.commit()
                print("Added sample successfully.")
        except Exception as e:
            print("Error inserting sample.", e)

    def print_data(self):
        try:
            for row in self.cursor.execute("select * from samples"):
                print(row)
            self.conn.close()
        except Exception as e:
            print("Error fetching samples.", e)


test1 = DBOperations()
test1.insert_data(weather)
test1.print_data()

# keys = list(weather.keys())
# # print(keys)
# # print(type(weather))
# for key, val in weather.items():
#     print(key, val)

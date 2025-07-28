import csv
import os
import custom_module
from datetime import datetime

# task 2
def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for i,row in enumerate(reader):
                if i == 0:
                 data['fields'] = row
                else:
                    rows.append(row)
        data['rows'] = rows
        return data
    except Exception as e:
        print('An exception occurred:', e)

employees = read_employees()
print(employees)

# task 3
def column_index(last_name):
    return employees['fields'].index(last_name)

employee_id_column =column_index('employee_id')
print(employee_id_column)

# task 4

def first_name(row_number):
    index = column_index('first_name')
    return employees['rows'][row_number][index]

# task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches

# task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    return matches

# task 7

def sort_by_last_name():
    employees['rows'].sort(key=lambda row: row[column_index('last_name')])
    return employees['rows']

# task 8
# def employee_dict(row):
#     result = {}
#     for i, field in enumerate(employees['fields']):
#         if field != 'employee_id':
#             result[field] = row[i]
#     return result

def employee_dict(row):
    pairs = zip(employees['fields'], row)

    result = {field: value for field, value in pairs if field != 'employee_id'}
    return result

# task 9

def all_employees_dict():
    result ={}
    employee_id_index = column_index('employee_id')

    for row in employees['rows']:
        employee_id = row[employee_id_index]
        result[employee_id] = employee_dict(row)

    return result

# task 10

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())


# task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret('rainy day!')


#  task 12

def read_minutes():
    minute1 = {}
    minute2 = {}

    try:
        with open('../csv/minutes1.csv', 'r', newline='') as file1:
            reader1 = list(csv.reader(file1))
            minute1['fields'] = reader1[0]
            minute1['rows'] = [tuple(row) for row in reader1[1:]]
    except Exception as e:
        print('minutes1 file not found ', e)
    try:
        with open('../csv/minutes2.csv', 'r', newline='') as file2:
            reader2 = list(csv.reader(file2))
            minute2['fields'] = reader2[0]
            minute2['rows'] = [tuple(row) for row in reader2[1:]]
    except Exception as e:
        print('minutes2 file not found ', e)
    return minute1, minute2

minutes1, minutes2 = read_minutes()

# task 13

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    joint_set =  set1.union(set2)
    return joint_set

minutes_set = create_minutes_set()


# task 14

minutes_list = None
def create_minutes_list():

    global minutes_list
    minutes_list = list(minutes_set)
    # print(f'answer is: {minutes_list}')
    minutes_list = list(map(lambda row: (row[0], datetime.strptime(row[1], "%B %d, %Y")), minutes_list))
    return minutes_list   

create_minutes_list()


# task 15

def write_sorted_list():
    print(minutes_list)
    minutes_list.sort(key=lambda x: x[1])
    # print(f'sorted list: {minutes_list}')
    converted_date_minutes_list = list(map(lambda row: (row[0], datetime.strftime(row[1], "%B %d, %Y")), minutes_list))
    print(f'DATE CONVERTED BACK TO STRING: {converted_date_minutes_list}')   

    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerow(converted_date_minutes_list)
    return converted_date_minutes_list

write_sorted_list()
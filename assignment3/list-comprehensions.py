import csv

file_path = "../csv/employees.csv"
try:
    with open(file_path, 'r', newline='') as file:
        reader = list(csv.reader(file))
        employee_list = [row[0]+" "+row[1] for row in reader[1:]]
        print(employee_list)
        filtered_list = [name for name in employee_list if 'e' in name.lower()]
        print(filtered_list)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found")
except Exception as e:
    print(f"An error accurred {e}")

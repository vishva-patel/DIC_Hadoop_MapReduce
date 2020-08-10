#!/usr/bin/python3
import sys

# Iterate for each record for all files in the given directory
for input_data in sys.stdin:
    input_data = input_data.strip()
    input_values = input_data.split(",")

    # Default values for each file
    employee_id = '0'
    name = '0'
    salary = '0'
    pass_code = '0'
    country = '0'

    # Case 1 - input from join1
    if len(input_values) == 2:
        employee_id = input_values[0]
        name = input_values[1]
        print ('%s\t%s\t%s\t%s\t%s' %
               (employee_id, name, salary, country, pass_code))
    # Case 2 - input from join2 - without comma in country name
    elif len(input_values) == 5:
        employee_id = input_values[0]
        salary = input_values[1]+","+input_values[2]
        country = input_values[3]
        pass_code = input_values[4]
        print ('%s\t%s\t%s\t%s\t%s' %
               (employee_id, name, salary, country, pass_code))
    # Case 3 - input from join2 - with comma in country name
    elif len(input_values) == 6:
        employee_id = input_values[0]
        salary = input_values[1]+","+input_values[2]
        country = input_values[3]+","+input_values[4]
        pass_code = input_values[5]
        print ('%s\t%s\t%s\t%s\t%s' %
               (employee_id, name, salary, country, pass_code))

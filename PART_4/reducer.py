#!/usr/bin/python3
import sys
output_data_1 = {}
output_data_2 = {}

# Print headers
print ('%s\t%s\t%s\t%s\t%s' %
               ('Employee_ID', 'Name', 'Salary',  'Country', 'Passcode'))

# Iterate the output produced from mapper.py
for line in sys.stdin:
    line = line.strip()
    employee_id, name, salary, country, pass_code = line.split('\t')
    # Case 1 - input from join1
    if salary == '0':
        output_data_1[employee_id] = name
    # Case 2 - input from join2
    else:
        output_data_2[employee_id] = [salary, country, pass_code]

# Produce reducer output
for employee_id in output_data_2.keys():
    name = output_data_1[employee_id]
    salary = output_data_2[employee_id][0]
    country = output_data_2[employee_id][1]
    pass_code = output_data_2[employee_id][2]
    print ('%s\t%s\t%s\t%s\t%s'% (employee_id, name, salary, country, pass_code))

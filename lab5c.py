#!/usr/bin/env python3
# Author ID: Michael Carlos

def add(number1, number2):
    try:
        # Try converting inputs to integers if they are strings
        number1 = int(number1) if isinstance(number1, str) else number1
        number2 = int(number2) if isinstance(number2, str) else number2
        
        result = number1 + number2
    except (TypeError, ValueError):
        return 'error: could not add numbers'
    return result

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return 'error: could not read file'
    return lines

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works, string '10' gets converted to integer
    print(add('abc', 5))                     # exception: could not add numbers
    print(read_file('seneca2.txt'))         # works if the file exists
    print(read_file('file10000.txt'))       # exception: could not read file


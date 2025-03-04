#!/usr/bin/env python3
# Author ID: Michael Carlos

def read_file_string(file_name):
    """Reads the entire contents of the file as a string."""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Reads the file and returns its contents as a list of lines."""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

# Function to append a string of lines to a file
def append_file_string(file_name, string_of_lines):
    # Appends the string to the file
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

# Function to write a list of lines to a file
def write_file_list(file_name, list_of_lines):
    # Writes each list item to a new line in the file
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

# Function to copy data from one file and add line numbers
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads data from one file and writes it with line numbers
    with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
        lines = f_read.readlines()
        for i, line in enumerate(lines, start=1):
            f_write.write(f"{i}:{line}")

# Function to read the content of a file and return it as a string
def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# Main block to execute the functions
if __name__ == '__main__':
    # Define file names
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    # Define data to append/write
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string to file1 and display its contents
    append_file_string(file1, string1)
    print(f"Contents of {file1}:\n{read_file_string(file1)}")

    # Write list to file2 and display its contents
    write_file_list(file2, list1)
    print(f"Contents of {file2}:\n{read_file_string(file2)}")

    # Copy contents from file2 to file3 with line numbers and display its contents
    copy_file_add_line_numbers(file2, file3)
    print(f"Contents of {file3}:\n{read_file_string(file3)}")

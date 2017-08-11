# We can open files in different modes:
# 'r' read mode (default)
# 'w' write mode
# 'x' open a file for exclusive creation, if the file already exists the operation fails
# 'a' appending content at the end of the file
# 't' text mode (default)
# 'b' binary mode
# '+' open a file for updating (reading and writing)

# The encoding is platform dependent, so it's highly recommended to specify the encoding type ('cp1252' or 'utf-8')

file = open('test.txt', 'w')
try:
    pass
    # perform some operations
finally:
    file.close()

# a better way to do this is using a manager
with open('test.txt') as x:
    pass
# ---------------------------------------------------------------------------------------------------------------


# Writing to a file
with open('test.txt', 'w') as file:
    file.write('This file\nContains\nThree lines')

# Writing to a file
with open('test.txt', 'r') as file:
    print(file.read())
    print(file.tell())   # get the current file position
    print(file.seek(0))  # bring file cursor to initial position

    for line in file:
        print(line, end='')

# readline() method also reads one line at time
# readlines() method returns a list with every line as an element

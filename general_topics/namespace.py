# We can get the address (in RAM) of an object through the id() method

a = 2
print('id a => {}'.format(id(a)))
print('id 2 => {}'.format(id(2)))
print(a is 2)


def printer():
    print('Hello')

a = printer
a()
# ---------------------------------------------------------------------------------------------------------

# Namespace is a collection of names

# In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects

# A namespace containing all the built-in names is created when we start the Python interpreter and exists as
# long we don't exit

# Each module creates its own global namespace
# This technique by which some data ("Hello world") gets attached to the code is called closure in Python.

# This value in the enclosing scope is remembered even when the variable goes out of scope or the function
# itself is removed from the current namespace.

# Closures can avoid the use of global values and provides some form of data hiding. It can also provide
# an object oriented solution to the problem.

# Decorators in Python make an extensive use of closures as well.


def print_message(message):
    def printer():
        print(message)

    return printer


another = print_message('Hello world')
another()
# ----------------------------------------------------------------------------------------------------------


def make_multiplier_of(n):
    def multiplier(x):
        return n * x

    return multiplier


times_2 = make_multiplier_of(2)
print(times_2(2))
print(times_2(3))

times_5 = make_multiplier_of(5)
print(times_5(5))

# We can find the enclosed value in a closure through the __closure__ attribute
print(times_2.__closure__[0])
print(times_2.__closure__[0].cell_contents)

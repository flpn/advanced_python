# A decorator is a callable that returns a callable
# Basically, a decorator takes a function, add some functionality and returns it


# def make_pretty(func):
#     def inner():
#         print('I got decorated!')
#         func()
#
#     return inner
#
#
# def ordinary():
#     print('I am ordinary!')
#
#
# ordinary = make_pretty(ordinary)
# ordinary()
# ------------------------------------------------------------------------------------------------------

# We can simplify this using the @ symbol

def make_pretty(func):
    def inner():
        print('I got decorated!')
        func()

    return inner


@make_pretty
def ordinary():
    print('I am ordinary')


ordinary()
# ------------------------------------------------------------------------------------------------------

# Decorator with parameters


def smart_divide(func):
    def inner(a, b):
        print('I am going to divide {} by {}'.format(a, b))

        if b <= 0:
            print('Cannot divide by 0')
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(5, 0))
# ------------------------------------------------------------------------------------------------------

# Chaining decorators for any function without a return value (generic decorator)


def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('%' * 30)
        func(*args, *kwargs)
        print('%' * 30)

    return inner


@star
@percent
def printer(message):
    print(message)


printer('Function with chaining decorators.')

# dynamic number of arguments
def args_example(*args):
    return sum(args)

print(args_example(1, 2, 3, 4, 5))


# dynamic number of keyworded arguments
def kwargs_example(**kwargs):
    for key in kwargs:
        print('Key:{} Value: {}'.format(key, kwargs[key]))

kwargs_example(a=1, b=2, c=3)


# unpacking arguments
def unpacking_example(x, y, z):
    return sum((x, y, z))

l = [1, 2, 3]
print(unpacking_example(*l))

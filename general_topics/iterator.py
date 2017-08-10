# An iterator is an object that can be iterated upon.
# An iterator must implement two special methods: __iter__() and __next__() (called iterator protocol).
# An iterable is an object that we can get an iterator from it.

my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))  # 4
print(next(my_iter))  # 7

print(my_iter.__next__())  # 0
print(my_iter.__next__())  # 3
# next(my_iter)  results in an error because there is no more items
# -------------------------------------------------------------------------------------------------------------

# A for loop creates automatically an iterator from the iterable
for _ in my_list:
    print(_)

# How for loop actually works?
iter_obj = iter(my_list)

while True:
    try:
        element = next(iter_obj)
        # do something with the element
    except StopIteration:
        break
# -------------------------------------------------------------------------------------------------------------


# Creating an iterable/iterator from scratch
class PowTwo:
    def __init__(self, max=10):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1

            return result
        else:
            raise StopIteration


x = PowTwo()

for i in x:
    print(i)
# -------------------------------------------------------------------------------------------------------------


# Creating an infinite iterable/iterator
class InfiniteIter:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 2

        return self.x

for i in InfiniteIter():
    print(i)

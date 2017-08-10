# LEFT-SHIFT == (a * 2**b)
a = 10      # 001010
b = 2
c = a << b  # 101000
print(c)


# RIGHT-SHIFT == (a // 2**b)
a = 10      # 001010
b = 2
c = a >> b  # 0010
print(c)


# AND
a = 50     # 110010
b = 25     # 011001
c = a & b  # 010000
print(c)


# OR
a = 50     # 110010
b = 25     # 011001
c = a | b  # 111011
print(c)


# COMPLEMENT == (-a - 1)
a = 50  # 110010
a = ~a  # 001101
print(a)


# EXCLUSIVE OR
a = 50     # 110010
b = 25     # 011001
c = a ^ b  # 101011
print(c)

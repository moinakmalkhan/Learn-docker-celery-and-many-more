# from functools import reduce

# reduce_list = [1, 2, 3, 4, 5]
# reduce_func = lambda x, y: x + y
# print(reduce(reduce_func, reduce_list))


# from functools import total_ordering
# @total_ordering
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def __repr__(self):
#         return "Complex({}, {})".format(self.real, self.imag)
#     def __add__(self, other):
#         self.real += other.real
#         self.imag += other.imag
#         return self
#     def __mul__(self, other):
#         self.real *= other.real
#         self.imag *= other.imag
#         return self
#     def __sub__(self, other):
#         self.real -= other.real
#         self.imag -= other.imag
#         return self
#     def __eq__(self, other):
#         return self.real == other.real and self.imag == other.imag
#     def __lt__(self, other):
#         return self.real < other.real and self.imag < other.imag
# c1 = Complex(1, 2)
# c2 = Complex(2, 3)
# print(c1 - c2)
# print(c1 + c2)
# print(c1 * c2)
# print(c1 == c2)
# print(c1 < c2)
# print(c1 > c2)
# print(c1 <= c2)
# print(c1 >= c2)
# print(c1 != c2)
# print(c1)
# print(c2)


# from functools import cached_property
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @cached_property
#     def name_age(self):
#         print("Calculating name_age")
#         return self.name + " " + str(self.age)
#     def __repr__(self):
#         return "Person({}, {})".format(self.name, self.age)
# p = Person("John", 30)
# print(p.name_age)
# print(p.name_age)
# print(p.name_age)

# from functools import lru_cache
# @lru_cache(maxsize=128)
# def fib(n):
#     print("Calculating fib({})".format(n))
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print([fib(i) for i in range(10)])
# print(fib.cache_info())


# from functools import partial

# add = lambda a, b: a+b

# # add_one = partial(add,1)
# # print(add_one(4))

# add_one = partial(add,a=1)
# print(add_one(b=4))

# from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Running {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
# @my_decorator
# def add(x,y):
#     """This function will add two numbers"""
#     return x+y
# print(add.__name__)
# print(add.__doc__)
# print(add(2,4))


# from functools import singledispatch

# @singledispatch
# def append_one_at_the_last(obj):
#     print("Unsupport type")
#     return obj

# @append_one_at_the_last.register(list)
# def _(obj):
#     return obj+[1]

# @append_one_at_the_last.register(str)
# def _(obj):
#     return obj+str(1)

# print(append_one_at_the_last([2,34,5,3]))

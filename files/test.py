from functools import wraps


# from django.utils.decorators import method_decorator
def int_param_without_wraps(func):
    def wrapper(param):
        if type(param) != int:
            raise ValueError("parameter should be integer")
        return func(param)

    return wrapper


def int_param_with_wraps(func):
    @wraps(func)
    def wrapper(*args):
        param = args[0]
        if type(param) == object:
            param = args[1]
        print(type(args[0]))
        if type(param) != int:
            raise ValueError("parameter should be integer")
        return func(*args)

    return wrapper


# @int_param_without_wraps
# # @int_param_with_wraps
# def squre(num):
#     """This function will return the squre of given number"""
#     return num/0

# # print(squre("sad"))
# print(squre.__name__)
# print(squre.__doc__)
# print(squre(4))


class Squre:
    """Doc string of squre"""

    def __init__(self, num):
        self.result = num ** 2

    @int_param_with_wraps
    def setValue(self, val):
        self.result = val ** 2


s = Squre(5)
s.setValue(4)
print(s.result)
print(s.__doc__)

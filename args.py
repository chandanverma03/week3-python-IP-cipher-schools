# make flexible funcions
# *operator
# *args (by using this funcion we can take n numbers of input inside def funcion)

# def all_total(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(all_total(1,2,3,4))

# def to_power(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "You didn't pass any args"
# nums = [1,2,3]
# print(to_power(2,*nums))
# def to_power(num, *args):
#     l = []
#     for i in args:
#         if args:
#             # i = i**num
#             l.append(i**num)
#         else:
#             print("You didn't pass any args")
#     return l
# nums = [1,2,3,4]
# print(to_power(2,*nums))

# <---------------------------------------------------------------->

# kwargs (keyword arguments)               give output as a dictionary
# **kwargs (double star operator)          kwargs: key word arguments
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}: {v}")
#     print(kwargs)
#     print(type(kwargs))
# func(first_name = 'chandan', last_name = 'verma')

# functions with all parameters
# 1. parameters
# 2. *args
# 3. defaul parameters
# 4. **kwargs

# order of writing all the parameters:=>
# def func(name, *args, last_name = 'unknown', **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
# func('chandan', 1,9,2, a = 1,b = 1)

# def capitial(l,**kwargs):
#     if kwargs.get('reverse.str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]

# names = ['chandan', 'verma']
# print(capitial(names))

# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# l = [1,2,3,4]
# print(sum(*l))














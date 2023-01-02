# lambda expression also knwon as anonymous functions
# def add(a,b):
#     return a+b

# add = lambda a,b: a+b
# print(add(8,9))

# iseven = lambda a: a%2 ==0
# print(iseven(8))
# s = input()
# a = lambda s: s[-1]
# print(a(s))

# lambda with if else 
# word_count = lambda s: True if len(s)>5 else False
# print(word_count('chandan'))

# <---------------------------------------------------------------------------------->
#ENUMERATE FUNCTIONS
# we use enumerate functions with for loop to track position of our items in iterable

# a = ['abc','defg','hijk']
# for b,c in enumerate(a):
#     print(f"{b} <----------> {c}")

# names = ['chandan','asdfgf','verma']
# def common(name,target):
#     for l,m in enumerate(name):
#         if m == target:
#             return l
#     return -1
# print(common(names,'verma'))

# <--------------------------------------------------------------------------------->
#map functions
# numbers = [1,2,3,4,5]
# squares = list(map(lambda a:a**2,numbers))
# print(squares)

# l = ['abc','hd','lmnop']
# length = list(map(len, l))
# print(length)

# <----------------------------------------------------------------------------------->
# filter functions
# l = [1,2,4,7,8,5,4,2,4,5,6,7,8]
# def function(num):
#     return num%2==0
# print(tuple(filter(function,l)))

# <------------------------------------------------------------------------------------>
# zip function
# user_id = ['user1','user2','user3']
# names = ['chandan','verma','asdfgf']
# last_names = ['verma','sharma','kaushal']
# print(list(zip(user_id,names,last_names)))

# example = [('a',1),('b',2)]
# print(dict(example))

# l1 = [1,3,5,7,9]
# l2 = [2,4,6,8,10]

# # l = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# # l1,l2 = zip(*l)
# # print(list(zip(l1,l2)))

# # a,b = list(zip(*l))
# # print(list(a))
# # print(list(b))
# lists = []
# for higher in zip(l1,l2):
#     lists.append(max(higher))
# print(lists)

# def average_finder(*args):
#     average = []
#     for i in zip(*args):
#         average.append(sum(i)/len(i))
#     return average
# print(average_finder([1,2,3],[3,6,4]))

# average = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
# print(average([1,2,3],[1,4,5],[3,5,7]))

#any, all functions
# num = [1,3,5,7,8]
# num1 = [2,4,6,8,10]

# print(all([ i%2==0 for i in num1]))
# num2 = []
# for i in num1:
#     num2.append(i%2==0)
# print(num2)

# print(any([i%2==0 for i in num]))

# def my_sum(*args):
#     if all([(type(i) == int or type(i) == float) for i in args]):
#         total = 0
#         for num in args:
#             total += num
#         return total 
#     else:
#         return "Wrong output Please check your output"

# print(my_sum(1,2,3,3,5))    
#         
#advance max and min functions
# names = ['chandan','verma','asdfgf']
# print("maximum length of name is",max(names, key = lambda items: len(items)))
# print("minimum length of name is",min(names, key = lambda items: len(items)))

# student = {
#     'chandan': {'score': 90, 'age':23},
#     'verma': {'score': 83, 'age':20},
#     'asdfgf': {'score': 73, 'age':25}
# }
# print(max(student, key = lambda items:student[items]['score']))















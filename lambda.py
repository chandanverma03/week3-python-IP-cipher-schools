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
names = ['chandan','kritika','verma']
def common(name,target):
    for l,m in enumerate(name):
        if m == target:
            return l
    return -1
print(common(names,'kritika'))
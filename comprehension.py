#list comprehension
# with the help of list comprehension we can create a list in one line 

# create a list of squares from 1 to 10

# a = []
# for i in range(1,11):
#     i = i**2
#     a.append(i)
# print(a)
# a = [i**2 for i in range(1,11)]  #code in one line
# print(a)

# print([-i for i in range(1,11)])
# l = ['abc','cdg','fsf']
# list1 = [l[::-1] for i in l]
# print(list1)

# def reverse_list(l):
#     return [name[::-1] for name in l]
# print(reverse_list(['abc','hgf','ckv']))

# def reverse_str(l):
#     l1 = []
#     for i in l:
#         l1.append(i[::-1])
#     return l1
# print(reverse_str(['abc','hgf','ckv']))

# list comprehension with if and else statement
# numbers = list(range(1,11))
# nums = []
# for i in numbers:
#     if i%2 == 0:
#         nums.append(i)
# print(nums)

# even_nums = [i for i in numbers if i%2 == 0]
# print(even_nums)

# def num_to_str(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]
# print(num_to_str([True,False, 1.0,3,4,[1,3,4],2.4]))

# l = [1,2,3,4,5,6,7,8,9,9,10]
# l1 = []
# for i in l:
#     if i%2 == 0:
#         l1.append(i*2)
#     else:
#         l1.append(-i)
# print(l1)

# print([i*2 if i%2==0 else -i for i in l])     #list conprehension

# nested : list inside list
# l = [[1,2,3],[1,2,3],[1,2,3]]
# list1 = [[i for i in range(1,4)] for j in range(3)]
# print(list1)

# dictionary comprehension
# example
# di = {i: i**2 for i in range(1,11)}
# print(di)
# dic = {f"square of {i}": i**2 for i in range(1,11)}
# # for k,v in dic.items():
# #     print(f"{k}:{v}")
# print(dic)

# dictionary = {i:('even' if i%2==0 else 'odd') for i in range(1,12)}
# print(dictionary)

# set comprehension rarely used**
# sets = {nums**2 for nums in range(1,11)}
# print(sets)
# names = {'new','hello'}
# var = {name[0] for name in names}
# print(var)


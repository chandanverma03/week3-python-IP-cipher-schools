#cube finder
# def cube_finder(n):
#     a = {}
#     for i in range(1,n+1):
#         a[i] = i**3
#     return a
# print(cube_finder(10))

#word counter
# def word_count(a):
#     count = {}
#     for char in a:
#         count[char] = a.count(char)
#     return count
# print(word_count('chandan'))
# user = {}
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# fav_movies = input("Your favourite movies : ").split(",")
# fav_songs = input("Your favourite songs : ").split(",")
# user['name'] = name
# user['age'] = age
# user['fav_movies'] = fav_movies
# user['fav_songs'] = fav_songs
# # print(user)
# for key , value in user.items():
    # print(f"{key} : {value}")

#sets data type
# it is unordered collection of unique items
# x = {}  
#indexing is not allowed in sets 

# l = [1,2,3,4,5,3,2,5,7,87,75,3,1,3,5,7,]
# s2 = set(l)
# print(s2)

# s2 = list(set(l))
# print(s2)
# all methods are same like add, remove,discare(only put that items which we want to remove)
# clear(it clear all the set), copy
# we can't store list , tuple and dictionary in sets
# list, float, string these will store in sets
# it can print in any order

# s = {'a', 'b', 'c'}
# if 'a' in s:
#     print('present')
# else:
#     print('not present')
# for items in s:
#     print(items) 

# if we want remove duplicate items from any list then we can first convert them into set and 
# then print that set
# 
# union(all element contains in two sets)   | (pipe : symbol of union)
# interesction (common items)    & (for printing common items from the  two sets)
# s = {1,2,3,4,2}
# s1 = {1,3,4,6,6}
# print(s|s1)
# print(s & s1)


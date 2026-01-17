# def func(lis):
#     s = 0
#     for i in lis:
#         if i%2==0:
#             s+=i
#     return s
# lis =  [1, 2, 3, 4, 6]
# print(func(lis))




# def func(lis):
#     s = []
#     for i in lis:
#         if i>0:
#             s.append(i)
#     return s
# lis = [-2, 3, 0, 5, -7]
# print(func(lis))


# def func(lis):
#     maxx=max(lis)
#     minn=min(lis)
#     return (minn,maxx)
# lis = [5, 1, 9, 3]
# print(func(lis))



# def func(lis):
#     return sum(lis)/len(lis)
# lis = [2, 4, 6, 8]
# print(func(lis))



# def func(lis):
#     s = 0
#     for i in lis:
#         if i%2!=0:
#             s+=1
#     return s
# lis =  [1, 2, 3, 4, 5]
# print(func(lis))



# def func(lis):
#     s = []
#     for i in lis:
#         s.append(i**2)
#     return s
# lis = [1,2,3,4]
# print(func(lis))



# def func(dic):
#     s = 0
#     for i in dic.values():
#         s+=i
#     return s
# dic = {"a": 3, "b": 5, "c": 2}
# print(func(dic))




# def func(lis,x):
#     if x in lis:
#         return True
#     else:
#         return False
# print(func([1, 2, 3], 2))




# def func(lis):
#     return sorted(lis,reverse=True)
# lis = [1, 2, 3, 4]
# print(func(lis))



# def func(dic):
#     return max(dic,key=dic.get)
# dic = {"a": 5, "b": 12, "c": 3}
# print(func(dic))



# def func(lis,x):
#     s = []
#     for i in lis:
#         if i>x:
#             s.append(i)
#     return s
# print(func([1, 5, 8, 3], 4))



# def func(lis):
#     dic = {}
#     for i in lis:
#         dic.update({i:len(i)})
#     return dic
# lis = ["apple", "hi"]
# print(func(lis))




# from random import randrange
# def func(x):
#     s = []
#     for i in range(10):
#         q = randrange(2,100,2)
#         s.append(q)
#     return s
# print(func(10))



# def func(x):
#     s = 0
#     for i in range(1,x+1):
#         if x%i==0:
#             s+=1
#     if s==2:
#         return True
#     else:
#         return False
# print(func(13))



# def func(dic):
#     s={}
#     for i,j in dic.items():
#         if j%2==0:
#             s.update({i:j})
#     return s
# dic = {"a": 2, "b": 5, "c": 8}
# print(func(dic))



# def func(lis):
#     dic = {}
#     for i in lis:
#         s = 0
#         x=lis.count(i)
#         s=s+x
#         dic.update({i:s})
#     return dic
# lis = [1, 2, 2, 3, 3, 3]
# print(func(lis))




# def func(lis):
#     return max(lis,key=lis.count)
# lis = [1, 2, 2, 3, 3, 3]
# print(func(lis))



# def func(dic):
#     s = []
#     for i in dic.values():
#         s.append(i)
#     return max(s)-min(s)
# dic = {"a": 10, "b": 3, "c": 7}
# print(func(dic))




# def func(lis):
#     s = []
#     while 

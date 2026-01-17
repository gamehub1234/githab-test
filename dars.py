# a = list(range(350,401))
# arr = []
# for i in a:
#     s=0
#     x=i
#     while i !=0:
#         s+=i%10
#         i=i//10
#     for j in range(2,s):
#         if s%j==0:
#             break
#     else:
#         arr.append(x)
# print(arr)




# data = [1, (-2, 3), [4, -5, (6, -7)], -8]
# for i in data:
#     if isinstance(i,int) or isinstance(i,float):
#         if i>0:


# data = [[1, 2, 3], [4, 5, 6]]
# data2 = []
# x =0
# s= 0
# for i in data:
#     for j in i:
#         s+=j
#         x+=1
# for i in data:
#     for j in i:
#         if s/x<j:
#             data2.append(j)
# print(data2)



# data = ([3, 5, 1], [8, 2, 6])
# for i in data:
#     minn=min(i)
#     i.append(minn)
# print(data)




# data = [1, [2, 3],"hi", [4, 5, 6], (7, 8)]
# s=0
# for i in data:
#     if isinstance(i,list):
#         for j in i:
#             if isinstance(j,int):
#                 s+=j
# print(s)




# data = [(3, 100), (10, 5), (7, 20)]
# for i in data:
#     if i[0]>i[1]:
#         print(i)


#??????????????
# data = [[1, 3, 5], [2, 4, 7], [10, 8, 6]]
# data2 = []
# for i in data:
#     for j in i:
#         x = i[1]-i[0]
#         if x==i[2]-i[1]:
#             data2.append(i)
# print(data2)





# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dic = {}
# for i in range(len(keys)):
#     dic.update({keys[i]:values[i]})
# print(dic)



# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)



# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# x = sampleDict.get("class").get("student").get("marks").get("history")
# print(x)



# a = {
#     "x":[1,1,2,2,3,5,7],
#     "y":[2,2,4,6,9],
#     "z":[3,7,4,4,12]
# }
# for key,vol in a.items():
#     print(f"{key} : {sum(set(vol))}")




# kutubxona = {
#     "badiy":{
#         "Shum bola":25000,
#         "Hurkitilgan Tush":18000,
#         "Kichkina shahzoda":55000
#         },
#     "Ilmiy kitoblar":{
#         "algebra":15000,
#         "fizika": 18000,
#         "biologiya":22000
#     },
#     "ertaklar":{
#         "susambil":8000,
#         'bogrsok':5000,
#         'tuki va bori': 9000
#     }
# }

# savat = {}

# while True:
#     print('Bizda shunday kitobar mavjud')
#     for i in kutubxona:
#         print(i, end=" | ")
#     user_t = input("\nKitoblar bo'limidan birini tanlang: ")
#     if user_t in kutubxona:
#         while True:
#             for i, j in kutubxona.get(user_t).items():
#                 print(i, j, "so'm")
#             user_k = input("kitob nomi: ")
#             if user_k in kutubxona.get(user_t):
#                 savat.update({user_k:kutubxona.get(user_t).get(user_k)})
#             elif user_k == "yoq":
#                 print("\nboshqa bo'limda sizni kutamiz")
#                 break
#             else:
#                 print("\nmavjud bo'lmagan kitob tanladiz")
#     elif user_t == "yoq":
#         a = 0
#         print("Kitoblar     | summasi so'm")
#         for i, j in savat.items():
#             a += j
#             print(f"{i.upper()}     |   {j}  so'm")
#         print("sizdan ", a, 'sum')
#         print("\nxayr rahmat kelib turing")
#         break
#     else:
#         print("\nsiz mavjud bo'lmagan bo'lim tanladiz")






# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# new_dic = {}
# for i in range(len(keys)):
#     new_dic.update({keys[i]:values[i]})
# print(new_dic)




# sample_dict = {'name': 'Ali', 'age': 20, 'city': 'Tashkent'}
# s = 0
# for i in sample_dict.keys():
#     s+=1
# print(s)



# sample_dict = {'math': 80, 'english': 90, 'history': 75}
# s = 0
# for i in sample_dict.values():
#     if isinstance(i,int):
#         s+=i
# print(s)





# sample_dict = {'a': 10, 'b': 20, 'c': 30}
# for i in 






# restoran_menyu = {
#     "Gazaklar": {
#         "Bahorcha Roll": {
#             "narx": 5000,
#             "ingredientlar": ["karam", "sabzi", "shisha vermishel", "qo'ziqorinlar"],
#             "vegetarian": True,
#             "achchiqlik_darajasi": 1
#         },
#         "Qo'ziqorin To'ldirmasi": {
#             "narx": 7500,
#             "ingredientlar": ["qo'ziqorin", "krem pishloq", "ziravorlar", "non uvoqlari"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#     },
#     "Asosiy Taomlar": {
#         "Gril Salmon": {
#             "narx": 18000,
#             "ingredientlar": ["salmon baliq", "limon", "ukrop", "yog'"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#         "Achchiq Tailand Karri": {
#             "narx": 15500,
#             "ingredientlar": ["kokos sut", "tofu", "reyhan", "chili", "guruch"],
#             "vegetarian": True,
#             "achchiqlik_darajasi": 3,
#             "mavjud_hajmlar": ["kichik", "o'rtacha", "katta"]
#         },
#         "Pasta Carbonara": {
#             "narx": 14500,
#             "ingredientlar": ["spagetti", "tuxum", "parmezan", "pancetta"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#     },
#     "Shirinliklar": {
#         "Shokolad Lava Keki": {
#             "narx": 6500,
#             "ingredientlar": ["shokolad", "un", "tuxum", "yog'"],
#             "vegetarian": False,
#             "kaloriya": 450
#         },
#         "Mevali Salat": {
#             "narx": 5000,
#             "ingredientlar": ["qulupnay", "ko'k rezavor", "kivi", "apelsin", "yalpiz"],
#             "vegetarian": True,
#             "kaloriya": 120
#         },
#     },
#     "Ichimliklar": {
#         "Yangi Siqilgan Apelsin Sharbati": {
#             "narx": 3500,
#             "ingredientlar": ["apelsin"],
#             "vegetarian": True
#         },
#         "Ko'k Choy": {
#             "narx": 2000,
#             "ingredientlar": ["ko'k choy barglari"],
#             "vegetarian": True
#         },
#     }
# }

# savat = {}

# while True:
#     print("Bizda shunday turdagi menyular mavjud ")
#     for menyu_tur in restoran_menyu:
#         print(menyu_tur,end=" | ")
#     user_tur = input("\nQaysi turdagi menyuni tanlaysiz  ").title()
#     # user_vek = bool(input("\nSiz vegetarianmisiz (ha/enter)  "))
#     # print(user_vek)
#     if user_tur in restoran_menyu: 
#         while True:
#             for i,j in restoran_menyu.get(user_tur).items():
#                 # if j.get("vegetarian")==user_vek==True:
#                 #     print(i,"  narxi =>",j.get("narx"))
#                 # if j.get("vegetarian")==user_vek==False:
#                 print('\n',i,"  narxi =>",j.get("narx"),)
#                 print("ingredientlari")
#                 for x in j.get("ingredientlar"):
#                     print(x,end=", ")
#             tan_user = input("\nNimani tanlaysiz ").title()
#             if tan_user in restoran_menyu.get(user_tur):
#                 savat.update({tan_user:restoran_menyu.get(user_tur).get(tan_user)})
#                 print("\nYana qanday taom? ")
#             elif tan_user=="Yoq":
#                 print("\nBoshqa turdaki menyularni ham koring! ")
#                 break
#             else:
#                 print("\nBizda bunday narsa mavjut emas ")
#     elif user_tur=="Yoq":
#         summ = 0
#         print("Taomlar         |         summasi somda")
#         for i,j in savat.items():
#             summ+=j["narx"]
#             print(f"{i}       |        {j['narx']}")
#         print("sizdan ", summ, 'sum')
#         print("\nxayr rahmat kelib turing")
#         break
#     else:
#         print("\nSiz mavjut bolmagan turdaki menyunu tanladingiz ")







# def Salom_ber():
#     print("Salom, dunyo!")
# Salom_ber()



# def Salom_ber(a):
#     print(f"Salom {a}")
# Salom_ber("Jamshid")


# def Son_yigindi(x:int,y:int)->int:
#     s=x+y
#     return s

# print(Son_yigindi(29,30))


# def Son_kv(x:int)->int:
#     return x**2

# print(Son_kv(25))




# def Orta_Son(x,y,z):
#     s=(x+y+z)/3
#     return s

# print(Orta_Son(12,34,56))




# def Son_j_t(x:int)->int:
#     if x%2==0:
#         print("juft")
#     else:
#         print("toq")

# Son_j_t(1234)



# def Katta_son(x,y,z):
#     maxx = max(x,y,z)
#     return maxx

# print(Katta_son(12,34,56))


# def palid_soz(str:str)->str:
#     s=""
#     for i in str:
#         s=i+s
#     if s==str:
#         print("Palindrom")
#     else:
#         print("Palindrom emas")

# palid_soz("aziza")







# def Son_manfiy_musbat(x):
#     if x>0:
#         print("musbat")
#     else:
#         print("manfiy")

# Son_manfiy_musbat(23)





# def Kabisa(x):
#     if  x % 4 == 0 and x % 100 != 0 or x % 400 == 0 :
#         print("Kabisa yili")
#     else:
#         print("Kabisa yili emas")

# Kabisa(1832)




# def unli_son(str):
#     unni = ['a','e','i','o','u']
#     s=0
#     for i in str:
#         if i in unni:
#             s+=1
#     return s

# print(unli_son("iawesruvo"))





# def list_uzun(list:list)->list:
#     return len(list)

# a = [1,2,3,4,56,6]
# print(list_uzun(a))




# def katta_kichik(list:list)->int:
#     minn = min(list)
#     maxx = max(list)
#     return minn,maxx

# a = [1,2,3,4,56,6]
# print(katta_kichik(a))




# def teskari(str:str)->str:
#     s = ""
#     for i in str:
#         s=i+s
#     return s

# print(teskari("qwertyuiop"))





# def sozlar_soni(str:str)->str:
#     s=0
#     for i in str.split():
#         s+=1
#     return s

# print(sozlar_soni("Matndagi so‘zlar sonini hisoblaydigan funksiya"))


# def Kv_son(list:list)->list:
#     x = []
#     for i in list:
#         x.append(i**2)
#     return x

# list = [1,2,3,4,5,6]
# print(Kv_son(list))



# def harf(str:str):
#     h=0
#     r=0
#     for i in str:
#         if i.isdigit():
#             r+=1
#         elif i.isalpha():
#             h+=1
#     return r ,h


# print(harf("Berilgan ro‘yxatning 1234545 uzunligini qaytaradigan funksiya"))




# def mukammal_son(x):
#     s=0
#     # for i in range(len(x)):
#     while 
#         if x%i==0:
#             s+=i
#     if x==s:
#         print("Mukammal son")
#     else:
#         print("Mukammal son emas")

# mukammal_son(28)





# def natija(lis):
#     def wrapper(x):
#         l = lis(x)
#         return [i+100 for i in l]
#     return wrapper

# @natija
# def sonlar(l:list) -> list:
#     return l

# lis = [-5, 9, 12, 1, -6, -17, 8, 12, 16]
# print(sonlar(lis))


# def natija(lis):
#     def wrapper(x):
#         l = lis(x)
#         return [i*5 for i in l]
#     return wrapper

# @natija
# def sonlar(l:list) -> list:
#     return l

# lis = [-5, 9, 12, 1, -6, -17, 8, 12, 16]
# print(sonlar(lis))


# def natija(lis):
#     def wrapper(x):
#         l = lis(x)
#         return [i**2 for i in l]
#     return wrapper

# @natija
# def sonlar(l:list) -> list:
#     return l

# lis = [-5, 9, 12, 1, -6, -17, 8, 12, 16]
# print(sonlar(lis))


# def natija(lis):
#     def wrapper(x):
#         l = lis(x)
#         return [i/10 for i in l]
#     return wrapper

# @natija
# def sonlar(l:list) -> list:
#     return l

# lis = [-5, 9, 12, 1, -6, -17, 8, 12, 16]
# print(sonlar(lis))




# def natija(z):
#     def wrapper(x):
#         l = z(x)
#         son = l
#         summ = 0
#         while l!=0:
#             summ+=l%10
#             l = l//10
#         return summ+son
#     return wrapper

# @natija
# def sonlar(l):
#     return l

# print(sonlar(23))




# def natija(son):
#     def wrapper(x):
#         l = son(x)
#         s = 0
#         for i in range(1,l+1):
#             if l%i==0:
#                 s+=1
#         if s==2:
#             return l*2
#         else:
#             return l
#     return wrapper

# @natija
# def sonlar(l):
#     return l

# print(sonlar(7))




# def natija(son):
#     def wrapper(x):
#         l = son(x)
#         if l%3==0:
#             return l
#         else:
#             return 0
#     return wrapper

# @natija
# def sonlar(l):
#     return l

# print(sonlar(9))




# def yaxlitlash(son):
#     def wrapper(x):
#         y = son(x)
#         z = y%10
#         s = y//10
#         if z>=5:
#             return (s+1)*10
#         else:
#             return s*10
#     return wrapper

# @yaxlitlash
# def func(son):
#     return son

# print(func(36))



# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         s=""
#         for i in str(y):
#             s = i+s
#         return int(s)
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(123))




# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         if y<0:
#             return -(y)
#         else:
#             return y
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(15))




# def son_teskari(son):
#     def wrapper(x):
#         l = son(x)
#         lis = []
#         son1 = l
#         while l!=0:
#             z=l%10
#             lis.append(z)
#             l = l//10

#         return son1+max(lis)
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(482))




# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         z = str(y)
#         if z==z[::-1]:
#             return y+1
#         else:
#             return y
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(123))



# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         z = str(y)
#         return y//len(z)
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(200))



# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         if y%2==0:
#             return y
#         else:
#             return y*3
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(6))



# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         lis = []
#         for i in range(1,y+1):
#             if i%3==0:
#                 lis.append(i)
#         return lis
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(15))




# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         lis = []
#         for i in range(1,y+1):
#             if i%2==0:
#                 lis.append(i)
#         return lis
#     return wrapper

# @son_teskari
# def func(son):
#     return son

# print(func(20))





# def son_teskari(son):
#     def wrapper(x):
#         y = son(x)
#         lis = []
#         for i in range(y,1,-1):
#             s=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     s+=1
#             if s==2:
#                 lis.append(i)
#         return lis
#     return wrapper

# @son_teskari
# def func(son):
#     return son
# print(func(10))


 

# def uzun_guruhla(lis):
#     x = {len(i) for i in lis}
#     s = {}
#     for i in x:
#         z = []
#         for j in lis:
#             if i == len(j):
#                 z.append(j)
#         s.update({i:z})
#     return s     

# lis =  ["car","dog","tree"]
# print(uzun_guruhla(lis))



# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n - 1)
# print(fac(5))



# Fibonacci
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1) 
# num = int(input())
# print(f'Fibonaci({num}) => {fib(num)}')




# class Telefon:
#     def __init__(self, abanet_ismi, rakami, manzil,turi):
#         self.abanet= abanet_ismi
#         self.rakami = rakami
#         self.manzil = manzil
#         self.turi = turi
        
        
#     def Info(self):
#         data = f"Assalomu aleykum {self.abanet}\nSiz bizdan {self.turi} rusimdaki Telfon sotip oldingiz\n\n"
#         return data
    
#     def Manzil(self):
#         return f"Bizning manzil {self.manzil}\n\n"
    
#     def Nome(self):
#         return f"Bizning Telfon nomer {self.rakami}"
    
# haridor = Telefon("Jamshid",91865766,"Xiva","Apple")
# print(haridor.Info())
# print(haridor.Manzil())
# print(haridor.Nome())





class Dick:
    def __init__(self, nom, xajim,narxi,mamlakat):
        self.nom= nom
        self.xajim = xajim
        self.narx = narxi
        self.mamlakat = mamlakat
        
        
    def Info(self):
        data = f"Assalomu aleykum \nBizda {self.nom} rusumdaki xotira dicki bor "
        return data
    
    def Manzil(self):
        return f"{self.mamlakat} da ishlab chikilgan"
    
    def Xajmi(self):
        return f"Xajmi {self.xajim} terabayt"
    
    def Narx(self):
        return f"Narxi {self.narx}$"
    
haridor = Dick("Samsung",1,200,"Janubiy Kareya")
print(haridor.Info())
print(haridor.Manzil())
print(haridor.Xajmi())
print(haridor.Narx()) 
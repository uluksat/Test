# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def info(self):
#         return f"Dog{self.name},age{self.age}"


#     def make_sound(self):
#         return f"Gaww"


# class Cat:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def info(self):
#         return f"Cat{self.name},age{self.age}"


#     def make_sound(self):
#         return f"Meouu" 



# class Caw:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def info(self):
#         return f"Caw{self.name},age{self.age}"


#     def make_sound(self):
#         return f"Muuu" 

# dog=Dog("Alabai",12)
# cat=Cat("Alisa",10)
# caw=Caw("Korova",8)



# class Student:
#     def __init__(self, name="Ivan", age=18, Groupnumber="10a"):
#         self.name=name
#         self.age=age
#         self.Groupnumber=Groupnumber


#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

#     def getGroupnumber(self):
#         return self.Groupnumber

#     def setNameAge(self, name, age):
#         self.name = name
#         self.age = age



#     def setGroupnumber(self, grnumber):
#         self.Groupnumber = grnumber

# st = Student()
# print(st.getAge())
# print(st.getName())
# st.setGroupnumber("10B")
# st.setNameAge("Uluksat", 19)

# print(st.name, st.age, st.Groupnumber)

# import string
# from string import ascii_uppercase


# class Alphabet():
#     def __init__(self, lang, letters = string.ascii_uppercase):
#         self.lang = lang
#         self.letters  = letters 
#     def print(self):
#         print(self.letters)
#     def letters_num(self):
#         abc = len(self.letters)
#         print (abc)
# class EngAlphabet(Alphabet):
#     def __init__(self, lang = "EN", letters=string.ascii_uppercase):
#         self.lang = lang
#         self.letters = letters
#     def __letters_num(self):
#         abc = len(self.letters)
#         print (abc)
#     def is_en_letter(self, letter):
#         if letter in self.letters:
#             print(True)
#         else:
#             print(False)
# alfa = Alphabet("EN")
# alfa.print()
# alfa.letters_num()
# engAlphabet = EngAlphabet()
# engAlphabet.is_en_letter("F")
# engAlphabet.is_en_letter("Щ")



# num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# chet=[]
# nechet=[]
# for i in num:
#     if i%2==0:
#         chet.append(i)
#     else:
#         nechet.append(i)
#         print(chet)
#         print(nechet)

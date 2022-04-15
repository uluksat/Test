# class Math(ABC):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b 

#     @abstractmethod
#     def add(self):
#         pass

#     @abstractmethod
#     def sub(self):
#         pass

    
#     def div(self):
#         pass
    
    
#     def mult(self):
#         pass

# class AbcMath(Math):
#     def __init__(self,a,b):
#         super().__init__(a,b)
        
#     def add(self):
#         print(self.a+self.b)

    
#     def sub(self):
#         print(self.-self.b)

#     def div(self):
#         print(self.a/self.b)

#     def mult(self):
#         print(self.a*self.b)


# import random
# random_num=random.randint(1,10)
# n=0
# while True:
#     find_num=int(input("Угадайте цифру: "))
#     if find_num>=1 and find_num <=10:
#         n+=1
#         if n==5:
#             print("У вас законнчилась попытки")
#             break
#         elif find_num == random_num:
#             print("Вы выиграли")
#             break
#         else:
#             print(f"Неверно {5-n} попыток")
#     else:
#         print("Введите числло от 1-10")



# class SlotMachine: 
#     def __init__(self, name, __user_balance, __game_balance): 
#         self.name = name 
#         self.__user_balance = 100 
#         self.__game_balance = 0 
 
#     def info(self): 
#         return self.name, self.__game_balance, self.__user_balance   

#     def top_up_balance():
#         return 

# print("Hello world")
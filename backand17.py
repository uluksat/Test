# import random

# class SlotMachine:
#     def __init__(self, name):
#         self.name = name 
#         self.__user_balance = 100
#         self.__game_balance = 0 

#     def info(self):
#         print(f"Name: {self.name}, user balance: {self.__user_balance}$, game balance: {self.__game_balance}$ ")

#     def top_up_balance(self):
#         how_many = int(input("How many money: "))
#         if how_many <= 100:
#             self.__balance_up(how_many)
#         else:
#             print("Ошибка")

#     def __balance_up(self, how_many):
#         self.__user_balance -= how_many
#         self.__game_balance += how_many

#     def game(self):
#         random_num = random.randint(1, 10)
#         n = 0
#         while True:
#             find_num = int(input("Find num: "))
#             if find_num >= 1 and find_num <= 10:
#                 n += 1
#                 if n == 5:
#                     print("У вас закончись попытки")
#                     self.__game_balance -= 10
#                     self.main() 
#                 elif find_num == random_num:
#                     print("Вы выиграли")
#                     self.__game_balance += 10
#                 else:
#                     print(f"Неверно {5 - n} попыток")
#             else:
#                 print("Введите число от 1 до 10")

#     def conslusion_money(self):
#         conslusion = int(input("How many conslusion: "))
#         if conslusion >= 50:
#             self.__game_balance -= conslusion
#             self.__user_balance += conslusion
#             print(f"You conslusion {conslusion}$ on user balance")
#         else:
#             print("From 50$")

#     def main(self):
#         while True: 
#             command = input("Command: ")
#             if command == "1":
#                 self.info()
#             elif command == "2":
#                 self.top_up_balance()
#             elif command == "3":
#                 self.game()
#             elif command == "4":
#                 self.conslusion_money()
#             else:
#                 print("Error command")

# gamer = SlotMachine("Faha")
# gamer.main()




# class Subscriber:
#     def __init__(self, firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname

#     def __str__(self):
#         return f"{self.firstname}, {self.lastname}"

# sub=Subscriber("Uluksat","Murat")
# print(sub.__str__())

# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.odometr=0
#         self.fuel=70

#     def __add_distance(self,km):
#         self.odometr+=km

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel

#     def drive(self,km):
#         fuel=km/10
#         if self.fuel >= fuel:
#             self.__add_distance(km)
#             self.__subtract_fuel(fuel)
#             print("let's go")
#         else:
#             print("Need more fuel, please, fill more!")

# car=Car("BMW", "X5", 2020)
# car.drive(50)


# class Bank:
#     def __init__(self, money ):
#         self.money = money
    
#     def add(self):
#         n = 10
#         num = int(input("How much: "))
#         num -= n
#         self.money += num
#         print(f"{self.money}")

#     def sub(self):
#         m = 10
#         num = int(input("How much: "))
#         num -= m 
#         self.money -= num
#         print(f"{self.money}")





#     def main(self):
#         while True:
#             a = input("Укажите команду: ")
#             if a == "1":
#                 self.add()
#             elif a == "2":
#                 self.sub()
#             else:
#                 print("Error")

# mun = Bank(100)
# mun.main()


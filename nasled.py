# class Hello:
#     def hello(self):
#         return "Hello"

# class Nasled(Hello):
#     pass

# new=Nasled
# print (new.hello())



# class OldCar:
#     def engine(self):
#         return "Мотор"

#     def door(self):
#         return "Двери"

#     def reels(self):
#         return "Колеса"

# old=OldCar
# print(old.engine())
# print(old.door())
# print(old.reels())

# class NewCar(OldCar):
#     def airbag(self):
#         return "Подушка безопасности"

# new=NewCar
# print(new.engine())
# print(new.door())
# print(new.reels())
# print(new.airbag())



# class Human:
#     def walk(self):
#         return "Я могу ходить"

#     def breath(self):
#         return "Я могу дышать"

#     def talk(self):
#         return "Я могу говорить"

# class Doctor(Human):
#     def cure(self):
#         return "Я могу лечить"

# class Programmer(Doctor):
#     def programming(self):
#         return "Я могу программировать"

# programmist=Programmer
# print(programmist.walk())
# print(programmist.breath())
# print(programmist.talk())
# print(programmist.cure())
# print(programmist.programming())

# doctor=Doctor
# print(doctor.walk())
# print(doctor.breath())
# print(doctor.talk())
# print(doctor.cure())
# print(doctor.programming())



# class Father:
#     def build(self):
#         return "Я могу строить"

#     def cure(self):
#         return "Я могу лечить"

# class Mother:
#     def cook(self):
#         return "Я могу готовить"

# class Son(Mother, Father):
#     def programming(self):
#         return "Я могу программировать"

# son=Son
# print(son.build())
# print(son.cure())
# print(son.cook())
# print(son.programming())



# class A:
#     def hello(self):
#         return "Hello from class A"

# class B:
#     def hello(self):
#         return "Hello frome class B"

# class C:
#     def hello(self):
#         return "Hello from class C"

# class D(C,A,B):
#     def hello1(self):
#         return "Hello from class D"

# d=D()
# print(d.hello())



# class Car:
#     def __init__(self, model, brand, year, color, price):
#         self.model=model
#         self.brand=brand
#         self.year=year
#         self.color=color
#         self.price=price


#     def info(self):
#         return f"{self.model},{self.brand},{self.year},{self.color},{self.price}"

# car=Car("BMW","X5",2020,"Black",10000)
# print(car.info())


# class FutureCar(Car):
#     def __init__(self,model,brand,year,color,price,is_flying):
#         super().__init__(model,brand,year,color,price)
#         self.model=model
#         self.brand=brand
#         self.year=year
#         self.color=color
#         self.price=price
#         self.is_flying=is_flying

#     def info(self):
#         return super().info()+str(self.is_flying)

# future=FutureCar("Tesla","Model X",2021,"White",100000,True)
# print(future.info())

    







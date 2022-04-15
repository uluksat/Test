# class HelloWorld:
#     pass

# print(type(HelloWorld()))


# class Dog:
#     name="Alabai"
#     age=10
#     color="white"

#     def gaw():
#         print("Gaww")

# dog=Dog()
# print(dog.name)
# dog.gaw()
# dog








# class Dog:
#     def __init__(self,name,age,color):
#         self.name=name
#         self.age=age
#         self.color=color

#     def gaw(self):
#         print("Gaww")

#     def fas(self):
#         print("Собака атакует")

#     def info(self):
#         print(f"Name: {self.name}, age: {self.age}, color: {self.color}")

# dog1=Dog("Alabai", 10,"Black")
# dog1.gaw()
# dog1.fas()

# dog2=Dog("Barsik",20,"White")
# dog2.gaw()
# dog2.info()


# class Car:
#     def __init__(self, brand,model, type_kuzov,year,volume,color):
#         self.brand=brand
#         self.model=model
#         self.type_kuzov=type_kuzov
#         self.year=year
#         self.volume=volume
#         self.color=color
#         self.odometer=0
#         self.is_going=False

#     def info_car(self):
#         return f"{self.brand},{self.model},{self.year},{self.odometer} km, status {self.is_going}"

#     def car_is_going(self,km):
#         self.odometer+=km
#         self.is_going=True


#     def stop_car(self):
#         self.is_going=False


# bmw=Car("BMW","18","Kupe",2018,"3.5","White")
# print(bmw.info_car())
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.stop_car()
# bmw.car_is_going(100)
# print(bmw.info_car())

# print("===================")

# audi=Car("Audi","A8","Sedan",2021,"3.5","Black")
# print(audi.info_car())
# audi.car_is_going(500)
# print(audi.info_car())
# audi.stop_car()
# print(audi.info_car())


# class Caw:
#     def make_sound(self):
#         print("Муу!")

# cow = Caw()
# cow.make_sound()



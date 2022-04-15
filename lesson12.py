# def wrapper(func):
#     def hello():
#         print("До вызова декоратора")
#         func()
#         print("После вызова декоратора")

#     return hello 

# @wrapper
# def bye():
#     print("Другая функция")

# bye()




# def time_request(func):
#     import time 

#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Время выполнения {end - start}")

#     return wrapper

# @time_request
# def url_time():
#     import requests
#     webpage = requests.get('https://google.com')

# @time_request
# def url_time_notion():
#     import requests
#     webpage = requests.get('https://backenditrun6.notion.site/759942306b0a4d24a36f1e0abf44d44d')

# url_time()
# url_time_notion()


def wrapper(func):
    def hello():
        print("Я декоратор")
        func()
        print("Я все сделал")

    return hello 

@wrapper
def bye():
    print("Другая функция")

bye()




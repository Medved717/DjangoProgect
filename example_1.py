# class First:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
# class Second(First):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name)
#         self.last_name = last_name
#
# second_class_obj = Second('Иван', 'Иванов')
# first_class_obj = First('Иван')
#
# class Animal:
#     species = "животное"
#
# class Cat(Animal):
#     sound = "мяу"
#
#     def __init__(self, quantity_paw):
#         self.quantity = quantity_paw
#
# c = Cat(4)
#
# # print(c.__dict__)              # {}  — пусто, у объекта ничего нет
# # print(Cat.__dict__)            # есть 'sound' и методы
# # print(Animal.__dict__)         # есть 'species'
# #
# # print(c.sound)                 # мяу  ← нашёл в Cat.__dict__
# # print(c.species)               # животное ← нашёл в Animal.__dict__
#
#
# import sys
# mod = sys.modules[__name__]     # текущий модуль
# # print(mod.__dict__)
# print(mod.__dir__())


class Institute:
    def __init__(self, institute_name):
        self.institute_name = institute_name

class Student:
    def __init__(self, student_name):
        self.student_name = student_name


institut = Institute('МГУ')
institut.student = Student('Леха')
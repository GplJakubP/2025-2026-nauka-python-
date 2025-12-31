# int używamy jak chcemy podać liczby w inpucie które są deafultowo stringiem 
# a = input("podaj a: ")
# b = input("podaj b: ")
#   print (int(a)+int(b))
# float wartości zmienno przecinkowe
# print (float(a) + float (b) )


# Operatory porównania 

#== czyli czy się równa
# print (7 == 5) False
# print (7 == 7) True
# != czy jest różna od 
# print (7 != 6) True
# print (7 != 7) False
# >  wiekszość
# < mniejszość 
# >= większe lub równe
# <+ mniejsze lub równe 


# Instrukcja warunkowa if  else elif

#x = input ("podaj x: ")
#if 5 == (float(x)):
#    print ("prawda")
#elif (float(x)) < 5:
#   print("mniejsze niż 5")
#else:
#    print ("większe niż 5")


# pętla  while
# number = 1
# while number % 2 != 0:
#     number = int(input("podaj liczbę: "))
# print ("hura udało liczba podzielna przez 2 i nie równa 0 to ", number)

# pętla for 
# sporty = ["bieganie", "pływanie", "jazda konno", "tenis"]
# for sport in sporty:
#     print(sport)


# enumerate liczy który to element w indeksie
# sporty = ["bieganie", "pływanie", "jazda konno", "tenis"]
# for index, sport in enumerate(sporty):
#     print(index , sport)

# for number in range(67):
#     print(number)

# poszukiwanie elementu w zbiorze 
# wydatki = [67,69,420,2137,911,789]
# for wydatki in wydatki:
#     print(wydatki)
#     if wydatki > 1000:
#         print("drogi wydatek został znależiony")
#         break
    
# wypisywanie co 2 elementu w zbiorze 
# wydatki = ["67","69","420","2137","911","789"]
# for index, wartości in enumerate(wydatki):
#     if index % 2 != 0:
#         continue
#     print(wartości)
       
       

# def najlepsze_oceny(oceny_z_przedmiotów):
#     najlepsza_ocean = 0
#     for przedmiot, ocena in oceny_z_przedmiotów.items():
#         super_ocena = max(ocena)
#         if super_ocena > najlepsza_ocean:
#             najlepsza_ocean = super_ocena
#         return najlepsza_ocean

# ocenki = {
#     "Matematyka":[4,3,6,1],
#     "Informatyka":[6,3,1,2],
#     "Polski":[1,3,2,4],
# }
# najnaj = najlepsze_oceny(ocenki)
# print (f"najlepsza ocena to {najnaj}")


# importowanie modółów zewnętrznych 
# moduł math import math


# klasy , obiekty własnych typów 

# class Student:
#     pass 
# class Grade:
#     pass
# class School:
#     pass 

# if __name__ == '__main__':
#     student_mikołaj = Student() 
#     grade_a =Grade()
#     grade_b =Grade()  
#     my_School = School()
    
    # print(student_mikołaj)
    # print(grade_a,grade_b)
    # print(my_School)
    
    # print("type(student_mikołaj):",type(student_mikołaj))
    # print("type(grade_a):", type(grade_a))
    
    # all_stydents = [Student(),Student(),Student()]
    # print(all_stydents)
    # print(all_stydents[0])
    # grades = {
    #     1: Grade(),
    #     2: Grade(),
    #     3: Grade(),
    # }
    # print(grades)
    
    
# class Product:
#     pass
# class Apple:
#     pass
# class Potato:
#     pass
# class Order:
#     pass
# if __name__ == "__main__":
#     Red_apple = Apple()
#     Green_apple = Apple()
#     potato = Potato()
#     sweet_potato = Potato()
# print(f"red_apple is type: {type(Red_apple)}")
# print(f"green_apple is type: {type(Green_apple)}")
# print(f"potato is type: {type(potato)}")
# print(f"sweet_potato is type: {type(sweet_potato)}")
# order = [Order(),Order(),Order(),Order(),Order()]

# #  Dictionary  Dictionaries are used to store data values in key:value pairs.

# dict_product = {
#   "Apple":Product(),
#   "Potato":Product(),
#   "Pasta":Product(),
#   "Tomato":Product(),
# }
# print(dict)



# 31.12.2025

# konstruktor i pola obiektu 

# class Student:
#     def __init__(self):
# #         print("Powstaje nowy obiekt ")
# # if __name__ == '__main__':
# #     student = Student()
#         self.first_name = "Jakbu"
#         self.last_name = "Piejko"
#         self.age = 23
# def run_example():
#     student = Student()
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
# if __name__ == '__main__':
#     run_example()
    
#  możemy modyfikować zmiennie za pomocą odwołania się do nich 
# student.first_name = ""



# Zadanie 1-3 

# import random

# class Product:
#     def __init__(self, name, category_name, unit_price):
#         self.name = name
#         self.category_name = category_name
#         self.unit_price = unit_price

# class Order:
#     def __init__(self, first_name, last_name, products_list=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         if products_list is None:
#             products_list = []
#         self.products_list = products_list
#         self.summary_price = calculate_order(products_list)
# class Apple:
#     def __init__(self, species_name, size, price_per_kg):
#         self.species_name = species_name
#         self.size = size
#         self.price_per_kg = price_per_kg

# class Potato:
#     def __init__(self, species_name, size, price_per_kg):
#         self.species_name = species_name
#         self.size = size
#         self.price_per_kg = price_per_kg

# def calculate_order(products_list):
#     total_price = 0
#     for product in products_list:
#         total_price += product.unit_price
#     return total_price  # return poza pętlą!

# def generate_random_products():
#     number_of_products = random.randint(1, 15)
#     products = []
#     for product_number in range(number_of_products):
#         name = f"Produkt-{product_number + 1}"
#         category = f"Kategoria-{product_number + 1}"
#         unit_price = random.randint(1, 8)
#         products.append(Product(name, category, unit_price))
#     return products  # return poza pętlą!

# def print_list_of_products(products):
#     for product in products:
#         print(f"Produkt: {product.name}, Kategoria: {product.category_name}, Cena jednostkowa: {product.unit_price} zł")

# def print_order_summary(order):
#     print("Zamówienie dla:", order.first_name, order.last_name)
#     print("Lista produktów:")
#     print_list_of_products(order.products_list)  # wykorzystujemy funkcję wypisującą produkty
#     print("Cena całkowita:", order.summary_price, "zł")
#     print("-" * 40)

# def run_example():
#     # Ręczne zamówienie
#     apple = Product("Jabłko", "Owoce", 2)
#     potato = Product("Ziemniak", "Warzywa", 3)
#     order1 = Order("Jakub", "P", [apple, potato])
#     print_order_summary(order1)

#     # Losowe zamówienie
#     random_products = generate_random_products()
#     order2 = Order("Jakub", "Piejko", random_products)
#     print_order_summary(order2)

# if __name__ == '__main__':
#     run_example()


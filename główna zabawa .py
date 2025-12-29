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
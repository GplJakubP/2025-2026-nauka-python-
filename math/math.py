import math
def przeciwprostokątna(a,b):
    return math.sqrt(math.pow(a,2)+math.pow(b,2))
ab=float(input("podaj 1 bok "))
ba=float(input("podaj 2 bok "))
c = przeciwprostokątna(ab,ba)


print (f"długośc przeciwprostokątenj to {c:.2f}")
    

# print (f"długośc przeciwprostokątenj to {c:.2f}") f wypisuje ilośc miejsc obliczeń po przecinku 


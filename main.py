def countNumbers(v):
 summa = 0 
 for simbols in v:
    summa = summa + int(simbols)
 return summa
v = input("Ievadit skaitli: ")
rez = countNumbers(v)
print(rez)
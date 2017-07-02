
import math
 
def polyEval(polynom, x):
 
    hodnota = 0 # startovni koeficient polynomu
    hindex = 0  # index na ktery se bude umocnovat
 
    for i in polynom:
 
        hodnota = hodnota + i * (x**hindex)
        hindex = hindex + 1
 
    return hodnota
 
def polySum(poly1, poly2):
    for i in range(len(poly1)):
        if (len(poly1)) > (len(poly2)):
            poly2.append(0)
        elif(len(poly1)) < (len(poly2)):
            poly1.append(0)
 
    vysledek = [poly1[i] + poly2[i] for i in range(len(poly1))]
 
    v = len(vysledek) - 1
    while(v != 0):
        if (vysledek[v] == 0):
            vysledek.pop(v)
        elif vysledek[v] != 0:
            break
        v = v - 1
 
    return vysledek
 
 
 
 
def polyMultiply(poly1, poly2):
 
    vysledek = [0]
    vysledek = vysledek * (len(poly2) + len(poly1) - 1)
 
    for x,k1 in enumerate(poly1):
        for y, k2 in enumerate(poly2):
            vysledek[x + y] = vysledek[x + y] + k1
            vysledek[x + y] *= k2
 
    return vysledek
 
 
 
print(polyMultiply([0,2,4],[2,3.2,0,2]))
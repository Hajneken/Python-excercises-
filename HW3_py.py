def leibnizPi(x):
 
    c = 0 # c jako citatel ve zlomku, pocatecni funkce pi
    p = 1 # p jako jmenovatel ve zlomku, pocatecni hodnota zlomku
    for i in range(x):
        c = float(c + 4/(i*2+1)* p) # i je clen posloupnosti
        p = p * (-1)         #jmenovatel -1 znamenĂˇ zlomek
    return c
 
def nilakanthaPi(x):
 
    p = 3      # prvni hodnota
    j = 2      # hodnota jmenovatele
 
    if x == 1:
        p = float(p)
    elif x <= 0:
        raise ValueError("Unsupported Value")
    else:
        for i in range(1, x):
            if i % 2 == 0:
                p = float(p - 4 / (j * (j + 1) * (j + 2)))
            else:
                p = float(p + 4 / (j * (j + 1) * (j + 2)))
            j = j + 2       # tady byl onen nedostatek ktery si budu pamatovat az na dosmrti :D
    return float(p)
 
import math
 
def newtonPi(x):
    x_0 = float(x)
    calculation = math.sin(x_0)/math.cos(x_0)
    x = x_0 - calculation
    while x != x_0:
        x_0 = x
        x = x_0 - math.sin(x_0)/math.cos(x_0) #vzorec rada
    return x
 
print(newtonPi(3))
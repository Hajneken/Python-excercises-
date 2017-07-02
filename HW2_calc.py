
def addition(x, y):
    "Funkce provede soucet"
    return float(x + y)
 
def subtraction (x, y):
    "Funkce provede rozdil"
    return float(x - y)
 
def multiplication (x, y):
    "Funkce provede nasobeni"
    return float(x * y)
 
def division (x, y):
    "Funkce provede deleni"
    if y == 0:
       raise ValueError('This operation is not supported for given input parameters')
    return float(x / y)
 
def modulo (x, y):
    if x < y or y <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return float(x % y)
 
def secondPower (x):
    "Funkce provede druhou mocninu cisla"
    return float(x ** 2)
 
def power (x, y):
    "Funkce provede xtou mocninu cisla"
    if y<0:
        raise ValueError('This operation is not supported for given input parameters')
    return float(x ** y)
 
def secondRadix  (x):
    if x<=0:
        raise ValueError('This operation is not supported for given input parameters')
    return float((x)**(1/2))
 
def magic(x,y,z,k):
    l = x + k
    m = y + z
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    else:
        z = ((l/m) + 1)
    return float(z)
 
def control(a, x, y, z, k):
    if a == "ADDITION":
        return addition(x, y)
    elif a == "SUBTRACTION":
        return subtraction(x, y)
    elif a == "MULTIPLICATION":
        return multiplication(x, y)
    elif a == "DIVISION":
        return division(x, y)
    elif a == "MOD":
        return modulo(x, y)
    elif a == "SECONDPOWER":
        return secondPower(x)
    elif a == "POWER":
        return power(x, y)
    elif a == "SECONDRADIX":
        return secondRadix(x)
    elif a == "MAGIC":
        return magic(x,y,z,k)
    else:
        raise ValueError('This operation is not supported for given input parameters')
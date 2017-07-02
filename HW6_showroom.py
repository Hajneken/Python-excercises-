
class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None # na zacatku proto none
        self.prevNode = None # na konci proto none
        self.data = data # tam budou data vzdycky zmrde, objekt Car
 
 
class LinkedList:
    def __init__(self):
        self.head= None #protoze na zacatku je prazdnej
        self.end = None # to samy
        self.count = 0 # zatim tam neni nic
 
 
class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
 
# cars = [ Car(1,"Rychlik", "Audi", 9000, True), Car(2,"Pomalik", "Lada", 90, True), Car(3,"Oukej", "Skoda", 90000, False), Car(4,"Tojerychly", "BMW", 7000, True)]
 
db = LinkedList()
 
 
def init(cars): # prijmam cars, pro test mam uz vytvoreno vyse
    cars = sorted(cars, key=lambda car: car.price)
 
    for car in cars:
        uzel = Node(None, None, cars[db.count])  # vytvoril jsem uzel,
        if db.head == None:
            db.head = db.end = uzel
        else:
            uzel.prevNode = db.end
            db.end.nextNode = uzel # nastavuji konec, na novy uzel
            db.end = uzel
        db.count += 1
 
#init(cars)
 
# current = db.end
# for i in range(0, db.count):
#     print(current.data.price)
#     current = current.prevNode
#
# print("-----------")
 
def add(car):
    uzel = Node(None, None, car)
    if not db.head:
        db.head = db.end = uzel
    else:
        if car.price < db.head.data.price: # tyhle dve veci jsou uplne stejny, jenom napsany jinak
        # umistit na zacatek
            uzel.nextNode = db.head
            db.head.prevNode = uzel
            db.head = uzel #zacatek
 
        elif car.price > db.end.data.price:
        # umistit na konec
            db.end.nextNode = uzel
            uzel.prevNode = db.end
            db.end = uzel
 
        else:
            posuvnik = db.end
            nalezeno = False
            while posuvnik != None and not nalezeno:
                if posuvnik.data.price < car.price:
                    nalezeno = True
                    posuvnik.nextNode.prevNode = uzel
                    uzel.nextNode = posuvnik.nextNode
                    posuvnik.nextNode = uzel
                    uzel.prevNode = posuvnik
                else:
                    posuvnik = posuvnik.prevNode
    db.count += 1
 
# add(Car(19,"Prdel", "Hovno", 1, True))
#
# current = db.head
# for i in range(0, db.count):
#     print(current.data.price)
#     current = current.nextNode
 
def updateName(identification, name):
    for i in Car:
        if i == identification:
            Car.name = name
 
 
def updateBrand(identification, brand):
    for i in Car:
        if i == identification:
            Car.brand = brand
 
 
def activateCar(identification):
    for i in Car:
        if i == identification:
            Car.active = True
 
 
def deactivateCar(identification):
    for i in Car:
        if i == identification:
            Car.active = False
 
def getDatabaseHead():
    return db.head
 
 
 
def getDatabase():
    return db
 
 
def calculateCarPrice():
    posuvnik = db.head
    celkovaCena = 0
    for i in range(0, db.count):
        if posuvnik.data.active == True:
            celkovaCena += posuvnik.data.price
        posuvnik = posuvnik.nextNode
    return celkovaCena
 
 
def clean():
    db.head = None
    db.end = None
    db.count = 0
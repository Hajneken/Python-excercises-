
class Node: #reprezentuje jeden uzel ve stromu
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
    value = None
    left = None
    right = None
 
class BinarySearchTree:
 
    zacatek = None
     
    """
    prvotni root prvek od ktereho se vsechny ostatni odvijeji 
    """
     
    navstiveno = 0  # zatim se nenavstivil zadny prvek tzn. 0 pruchodu
 
    def __init__(self):
        self.zacatek = None
        self.navstiveno = 0
 
 
 
    def insert(self, value): #vlozi jednotlie nove uzly
 
        if value:      # if value is not none
            uzel = Node(value) # creating object uzel of the class uzel
            if not self.zacatek:
                self.zacatek = uzel #
            else:
                current = self.zacatek  # current = soucasny vybrany prvek
                while True:
                    if uzel.value > current.value:
                        if current.right:
                            current = current.right
                        else:
                            current.right = uzel
                            break
                    else:
                        if current.left:
                            current = current.left
                        else:
                            current.left = uzel
                            break
 
 
 
    def fromArray(self, array): #vlozi nove uzly z pole
        for i in array:
            self.insert(i)
 
 
 
    def search(self, value): # zjistuje jestli je danĂ˝ prvek je ve stromu
        self.navstiveno = 0
        return self.KontrolaUzlu(self.zacatek, value)
 
 
 
    def min(self): # hleda minimum, v pripade prazdneho stromu vraci None
        self.navstiveno = 0
        uzel = self.zacatek
 
        if not uzel:
            return None
 
        while True:
            self.navstiveno += 1
            if not uzel.left:
                return uzel.value
 
            uzel = uzel.left
 
 
 
    def max(self): # hleda maximum, v pripade prazdneho stromu vraci None
 
        self.navstiveno = 0
        uzel = self.zacatek
 
        if not uzel:
            return None
 
        while True:
            self.navstiveno += 1
            if not uzel.right:
                return uzel.value
            uzel = uzel.right
 
 
 
    def KontrolaUzlu(self, uzel, value):
        self.navstiveno += 1
        if uzel is not None:
            if uzel.value == value:
                return True
 
            if value >= uzel.value:
                if uzel.right:
                    return self.KontrolaUzlu(uzel.right, value)
 
            else:
                if uzel.left:
                    return self.KontrolaUzlu(uzel.left, value)
 
        return False
 
 
 
    def visitedNodes(self): # vrĂˇtĂ­ poÄŤet navĹˇtĂ­venĂ˝ch uzlĹŻ pĹ™i poslednĂ­m volĂˇnĂ­ jednĂ© z metod: search, min nebo max
        return self.navstiveno
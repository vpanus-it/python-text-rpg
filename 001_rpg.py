class  Hrac:
    jmeno=""
    health=100 # procentualni hodnota "kondice" (0=smrt)
    # invertar = []  # seznam zbrani (obsah batohu)
    def __init__(self,jmeno):
        self.jmeno = jmeno
        self.invertar = []
    
    def apin(self,item):  # apin - append in inventory
        self.invertar.append(item)
    
    def attack(self,index,cil):  # poradove cislo zbrane v inventari , cil je nejaky hrac
        utocna_zbran = self.invertar[index]
        utocna_zbran.pouzij(cil)
        
    
class Zbran:    
    def __init__(self,nazev,sila):
        self.nazev = nazev
        self.sila = sila

    def pouzij(self,hrac):  # pouzijeme zbran na daneho jedince
        hrac.health = hrac.health - self.sila 
    
    
h1 = Hrac("Alfons")
h2 = Hrac("Pepa")

mec1 = Zbran("Rezavy Meč",5)
mec1.pouzij(h2) # zautocime na hrace cislo 2, h2

h1.apin(mec1)
h1.apin(Zbran("Tupa sekera",6) )

h1.attack(1,h2)  # proste utok

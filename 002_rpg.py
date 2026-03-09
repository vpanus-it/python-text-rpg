import random
class  Hrac:
    jmeno = ""
    health = 100 # procentualni hodnota "kondice" (0=smrt)
    
    # invertar = []  # seznam zbrani (obsah batohu)
    def __init__(self,jmeno):
        self.jmeno = jmeno
        self.invertar = []
    
    def pridej_do_inventare(self,item):  
        self.invertar.append(item)
    
    def attack(self,index,cil):  # poradove cislo zbrane v inventari , cil je nejaky hrac
        utocna_zbran = self.invertar[index]
        utocna_zbran.pouzij(cil)

class Predmet:    
    def __init__(self,sila):
        self.sila =  sila

class Lekarnicka(Predmet):
    def __init__(self, sila):
        self.sila = sila
    def uzdrav(self,hrac):
        hrac.health = hrac.health + self.sila


class Zbran(Predmet):    
    def __init__(self,nazev,sila):
        self.nazev = nazev
        self.sila = sila

    def pouzij(self,hrac):  # pouzijeme zbran na daneho jedince
        hrac.health = hrac.health - self.sila 
    
class Revolver(Zbran): #potomek typu zbran
    def pouzij(self,hrac):
        zraneni = self.sila * random.random()  # nahodne cislo od 0 do 1
        hrac.health = hrac.health - zraneni

class Luk(Zbran):
    
    def __init__(self,nazev,sila,pocet_sipu):
        self.nazev = nazev
        self.sila = sila
        self.pocet_sipu = pocet_sipu
    def pouzij(self,hrac):
        zraneni = self.sila * random.random()  # *****
        hrac.health = hrac.health - zraneni


h1 = Hrac("Alfons")
h2 = Hrac("Mikula")


mec1 = Zbran("Rezavy Meč",5)
mec1.pouzij(h2) # zautocime na hrace cislo 2, h2

h1.pridej_do_inventare(mec1)
h1.pridej_do_inventare(Zbran("Tupa sekera",6) )

h1.attack(1,h2)  # proste utok

############################################


h3 = Hrac("NPC")
revolver1 = Revolver("Revolver",80)
h3.pridej_do_inventare(revolver1)

cil = random.choice([h1,h2,h3])  # vybere random hrace

h3.attack(0,cil)

print(f"Hrac 1: {h1.jmeno} - Zdravi - {h1.health}")
print(f"Hrac 2: {h2.jmeno} - Zdravi - {h2.health}")
print(f"Hrac 3: {h3.jmeno} - Zdravi - {h3.health}")

lek25 = Lekarnicka(25) 

lek25.uzdrav(h1)

print(f"zdravi hrace 1 {h1.health}")

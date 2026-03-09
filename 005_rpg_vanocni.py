import random
class Hrac:
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
class Misto:    
    def __init__(self,nazev,popis):
        self.nazev =  nazev
        self.popis = popis
        self.vychody = {}
        self.predmety = []
        self.postavy = []
    def pridej_vychod(self,smer,kam):
        self.vychody[smer] = kam    
    def pridej_postavu(self,postava):
        self.postavy.append(postava)
    def pridej_predmet(self,predmet):
        self.predmety.append(predmet)
    def vypis_info(self):    
        print(f"\n--- {self.nazev} ---")
        print(self.popis)
        if self.predmety:
            print("Predmety na zemi")
            for p in self.predmety:
                print(p.nazev,", ",end=" ")
            print("")
        if self.postavy:
            seznam=[]
            for p in self.postavy:
                seznam.append(p.jmeno)
            print("Vidis zde postavy:",", ".join(seznam))
        
        print("Mozne vychody:",", ".join(self.vychody.keys()))


# 1 - Vytvoreni hrace (Josef a Marie)
hrac = Hrac("Josef a Marie")
hul = Zbran("Poutnicka hul",15)
hrac.pridej_do_inventare(hul)

# 2 - Popis mist

nazaret   = Misto("Nazaret","Tvuj domov. Je cas vydat se na cestu, Marie uz ceka")
poust     = Misto("Skalnata poust","Fouka studeny vitr, cesta je nebezpecna")
jeruzalem = Misto("Jeruzalem - brana","Velke mesto plne lidi a rimskych vojaku")
betlem    = Misto("Betlem","Male mestecko. Vsude je plno, hostince praskaji ve svech")
staj      = Misto("Stara staj","Teplo, vune sena a jasna hvezda nad strechou. Cil cesty")

# 3 - Propojeni mist

nazaret.pridej_vychod("jih",poust)
poust.pridej_vychod("jih",jeruzalem)
poust.pridej_vychod("sever",nazaret)
jeruzalem.pridej_vychod("vychod",betlem)
jeruzalem.pridej_vychod("sever",poust)
betlem.pridej_vychod("zapad",jeruzalem)
betlem.pridej_vychod("severozapad",staj)
staj.pridej_vychod("jihovychod",betlem)

# 4 - Pridani prekazek a predmetu

loupeznik = Hrac("Loupeznik")
loupeznik.pridej_do_inventare(Zbran("Rezava dyka",10))
poust.pridej_postavu(loupeznik)

zlaty_dar = Zbran("Zlato pro krale",0)   # predmet bez bojove sily
staj.pridej_predmet(zlaty_dar)

# 5 - Hlavni smycka hry (GAME LOOP)

aktualni_misto = nazaret

while True:
    # 1 - kde jsem
    aktualni_misto.vypis_info()
    
    # 2 - co chci udelat
    prikaz = input("\nCo udelas?(jdi[smer]. utok, invertar, konec): ").lower().split()
    if not prikaz:
        continue
        
    # 3 - co se stane
    akce = prikaz[0]
    
    # ukonceni hry
    if akce == "konec":
        break
    
    # posun po hracim poli    
    elif akce == "jdi":
        if len(prikaz)> 1:
            smer = prikaz[1]
            if smer in aktualni_misto.vychody.keys():
                aktualni_misto = aktualni_misto.vychody[smer]
            else:
                print("Tudy cesta nevede")
        else:
            print("Musis zadat smer(např. jdi jih)")   


    
    
    
  
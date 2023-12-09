import random as rd

Bloquer = False
Parer = False
Fuite = False

def Critique(critluck, dmg):
    crit = False
    critdmg = rd.random() + 1
    if rd.random() < critluck:
        crit = True
        DamageDealt = int(dmg * critdmg)
    else:
        DamageDealt = int(dmg)
    return DamageDealt, crit

def PassifBlockATK():
    global Bloquer
    if rd() < 0.25:
        Bloquer = True
    else:
        Bloquer = False

class Personnage:
    def __init__(self, nom, HP, DEF, DMG, critluck, luck, EXP, lvl):
        self.nom = nom
        self.HP = HP
        self.DEF = DEF
        self.DMG = DMG
        self.critluck = critluck
        self.luck = luck
        self.EXP = EXP
        self.lvl = lvl


    def estVivant(self):
        return self.HP > 0


    def AttaqueBasique(self, target):
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        if Bloquer:
            DamageDealt = 0
            target.DégâtsSubis(DamageDealt, crit)

        if crit == True:
            print(f"{self.name} inflige {DamageDealt} dégâts. C'est un coup critique ! ")
        else:
            print(f"{self.name} inflige {DamageDealt} dégâts. ")


    def LancerProjectile(self, target, choixProjectile):
        if choixProjectile == 1: #Tonneau explosif

            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.9)
            target.DégâtsSubis(DamageDealt, crit)
            if crit == True:
                print(f"Vous infligez {DamageDealt} dégâts (coup critique ! ). ")
            else:
                print(f"Vous infligez {DamageDealt} dégâts. ")
        
        if choixProjectile == 2: #Boule de feu

            global FireCondition
            global FireTours
            global FireDOT
            FireCondition = True
            FireTours = 3
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.80)
            target.DégâtsSubis(DamageDealt, crit)
            FireDOT = self.DMG
            FireDOT = int(FireDOT*0.40)

            if crit == True:
                print(f"Vous infligez {DamageDealt} dégâts (coup critique !) et l'ennemi reçoit {FireDOT} dégâts pendant 3 tours. ")
            else:
                print(f"Vous infligez {DamageDealt} dégâts, et l'ennemi reçoit {FireDOT} dégâts pendant 3 tours. ")
            
        if choixProjectile == 3: #Potion jetable d'acide

            global AcidCondition
            global AcidTours
            global AcidDOT
            AcidCondition = True
            AcidTours = 3
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.25)
            target.DégâtsSubis(DamageDealt, crit)
            AcidDOT = self.DMG
            AcidDOT = int(AcidDOT*0.8)
            
            if crit == True:
                print(f"Vous infligez {DamageDealt} dégâts (coup critique !) et l'ennemi reçoit {AcidDOT} dégâts pendant 3 tours. ")
            else:
                print(f"Vous infligez {DamageDealt} dégâts, et l'ennemi reçoit {AcidDOT} dégâts pendant 3 tours. ")
            
        if choixProjectile == 4: #Parfum de poison

            global PoisonCondition
            global PoisonTours
            global PoisonDOT
            PoisonCondition = True
            PoisonTours = 999
            PoisonDOT = self.DMG
            PoisonDOT = int(PoisonDOT*0.20)
            print(f"L'ennemi recevra {PoisonDOT} à chaque tour.")


    def BloquerUneAttaque(): #Magnus Action 2
        global ParerCondition
        global ParerTours
        global Parer
        ParerCondition = True
        ParerTours = 3
        ChanceParer = 0.50
        if rd.random() < ChanceParer:
            Parer = True
        else:
            Parer = False


    def LancerArme(self, target): #Magnus Action 3
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        DamageDealt = int(DamageDealt*2)
        target.DégâtsSubis(DamageDealt, crit)
        self.DMG = self.DMG / 2

        if crit:
            print(f"Vous infligez {DamageDealt} dégâts (coup critique !). ")
        else:
            print(f"Vous infligez {DamageDealt} dégâts.")


    def UtiliserConsommable(choixConsommable, choixPotionDeSoin = 0):
        if choixConsommable == 1:
            
            if choixPotionDeSoin == 1:
                ...
            if choixPotionDeSoin == 2:
                ...
            if choixPotionDeSoin == 3:
                ...
            
        if choixConsommable == 2:
            ...
        
        if choixConsommable == 3:
            ...
        
        if choixConsommable == 4:
            ...
        
        if choixConsommable == 5:
            ...


    def TentativeFuite(self):
        global Fuite
        ChanceFuite = int(self.luck/2)
        if rd.random < ChanceFuite:
            Fuite = True
        else:
            Fuite = False


    def DégâtsSubis(self, DamageDealt, crit, Bloquer = False, Parer = False):
        if Bloquer:
            DamageDealt = 0
        if Parer:
            DamageDealt = 0

        if crit:
            self.HP -= DamageDealt
        if not crit:
            self.HP -= max(0, DamageDealt - self.DEF)
        if self.HP < 0:
            self.HP = 0
        print(f"{self.nom} prend {DamageDealt} dégâts. Sa vie restante : {self.HP}")

zone = 1 #Village

Monstre = Personnage(
    "Monstre",
    rd.randint(40 + (20 * zone-1), 60 + (20 * zone-1)),     #HP
    rd.randint(1 + (zone-1), 3 + (zone-1)),                 #DEF
    rd.randint(10 + (4 * zone-1), 14 + (4 * zone-1)),       #DMG
    0.20 + (0.05 * zone-1), 0.40, 0, 1)                     #critluck, luck, EXP, lvl

print("Quel personnage voulez-vous choisir ? ")
ChoixHéros = int(input("Entrez un nombre : Salie (1) / Magnus (2)"))
while ChoixHéros != 1 or ChoixHéros != 2:
    ChoixHéros = int(input("Entrez un nombre : Salie (1) / Magnus (2)"))

if ChoixHéros == 1:
    Héros = Personnage("Salie", 100, 5, 12, 0.25, 0.75, 0, 1)
elif ChoixHéros == 2:
    Héros = Personnage("Magnus", 150, 10, 10, 0.30, 0.60, 0, 1)
HérosCombat = Héros

def main():
    global HérosCombat
    global Monstre

    while Héros.estVivant() and Monstre.estVivant():
        if ChoixHéros == 1:
            print("Quelle action ? Entrez un nombre : ")
            print("1 : Attaque basique")
            print("2 : Lancer un objet")
            print("3 : Utiliser un consommable")
            print("4 : Tentative de fuite")
        elif ChoixHéros == 2:
            print("Choisissez votre action : ")
            print("1 : Attaque basique")
            print("2 : Chance de parer (3 attaques)")
            print("3 : Lancer votre arme (2x dégâts, mais vous infligez ensuite dégâts / 2)")
            print("4 : Utiliser un consommable")
            print("5 : Tentative de fuite")
        
        choix = int(input("Votre action : "))
        if choix == 1:
            print(HérosCombat.AttaqueBasique(Monstre))
        elif choix == 2 and ChoixHéros == 1:
            choixProjectile = int(input("Choisissez un projectile (1 à 4): "))
            print(HérosCombat.LancerProjectile(choixProjectile))
        elif choix == 2 and ChoixHéros == 2:
            print(HérosCombat.ParerUneAttaque())
        elif choix == 3 and ChoixHéros == 2:
            print(HérosCombat.LancerArme())
        elif (choix == 3 and ChoixHéros == 1) or (choix == 4 and ChoixHéros == 2):
            choixConsommable = int(input("Choisissez un consommable (1 à 5): "))
            if choixConsommable == 1:
                choixPotionDeSoin = int(input("Choisissez une taille de potion de soin (1 à 3): "))
            print(HérosCombat.UtiliserConsommable(choixConsommable, choixPotionDeSoin))
        elif (choix == 4 and ChoixHéros == 1) or (choix == 5 and ChoixHéros == 2):
            print(HérosCombat.TentativeFuite())
            if Fuite == True:
                break

        if not Monstre.estVivant():
            print("Vous avez gagné ! ")
            break

        Monstre.AttaqueBasique(Héros)

        if not Héros.estVivant():
            print("Vous êtes mort ! ")
            break


if __name__ == "__main__":
    main()

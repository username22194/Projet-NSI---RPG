import random as rd

Bloquer = False
Parer = False
Fuite = False
Esquive = False

def Critique(critluck, dmg):
    crit = False
    critdmg = rd.random() + 1
    if rd.random() < critluck:
        crit = True
        DamageDealt = int(dmg * critdmg)
    else:
        DamageDealt = int(dmg)
    return DamageDealt, crit

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


    def PassifBlockATK(self):
        if rd.random() < 0.20:
            self.Bloquer = True
        else:
            self.Bloquer = False



    def AttaqueBasique(self, target): #Action 1
        print("Attaque Basique")
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        target.DégâtsSubis(DamageDealt, crit)

        if crit == True:
            print(f"{self.nom} inflige {DamageDealt} dégâts. C'est un coup critique ! ")
        else:
            print(f"{self.nom} inflige {DamageDealt} dégâts. ")


    def LancerProjectile(self, target, choixProjectile): #Salie Action 2
        if choixProjectile == 1: #Tonneau explosif
            print("Tonneau explosif")
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.9)
            target.DégâtsSubis(DamageDealt, crit)
            if crit == True:
                print(f"Vous infligez {DamageDealt} dégâts (coup critique ! ). ")
            else:
                print(f"Vous infligez {DamageDealt} dégâts. ")
        
        if choixProjectile == 2: #Boule de feu
            print("Boule de feu")
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.80)
            target.DégâtsSubis(DamageDealt, crit)
            if crit == True:
                print(f"Vous infligez {DamageDealt - target.DEF} dégâts (coup critique !). ")
            else:
                print(f"Vous infligez {DamageDealt - target.DEF} dégâts. ")

            def Enflammé(target):
                global FireCondition
                global FireTours
                global FireDOT
                FireCondition = True
                FireTours = 3
                
                FireDOT = self.DMG
                FireDOT = int(FireDOT*0.40)
                target.HP = int(target.HP - FireDOT)
            print(f"L'ennemi prendra {FireDOT} dégâts de feu pendant 3 tours. ")

            
            
        if choixProjectile == 3: #Potion jetable d'acide
            print("Potion jetable d'acide")
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
            target.PoisonCondition = True
            target.PoisonTours = 999
            target.PoisonDOT
            print("Parfum empoisonné")
            global PoisonCondition
            global PoisonTours
            global PoisonDOT
            PoisonCondition = True
            PoisonTours = 999
            PoisonDOT = self.DMG
            PoisonDOT = int(PoisonDOT*0.20)
            print(f"L'ennemi recevra {PoisonDOT} à chaque tour.")

    def ParerUneAttaque(self): #Magnus Action 2
        self.ParerCondition = True
        self.ParerTours = 3
        ChanceParer = 0.40
        if rd.random() < ChanceParer:
            self.Parer = True
        else:
            self.Parer = False


    def LancerArme(self, target): #Magnus Action 3
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        DamageDealt = int(DamageDealt*2)
        target.DégâtsSubis(DamageDealt, crit)
        self.DMG = self.DMG / 2

        if crit:
            print(f"Vous infligez {DamageDealt} dégâts (coup critique !). ")
        else:
            print(f"Vous infligez {DamageDealt} dégâts.")


    def UtiliserPotionDeSoin(self, Héros, choixPotionDeSoin): #Soin
        if choixPotionDeSoin == 1:
            self.HP = int(self.HP + (Héros.HP*0.20))
            print(f"Vous vous soignez de {int(Héros.HP*0.20)}. Votre vie : {self.HP}")

        if choixPotionDeSoin == 2:
            self.HP = int(self.HP + (Héros.HP*0.45))
            print(f"Vous vous soignez de {int(Héros.HP*0.45)}. Votre vie : {self.HP}")

        if choixPotionDeSoin == 3:
            self.HP = int(self.HP + (Héros.HP*0.70))
            print(f"Vous vous soignez de {int(Héros.HP*0.70)}. Votre vie : {self.HP}")


    def UtiliserConsommable(self, Héros, choixConsommable): #Action 3 / 4
        if choixConsommable == 2: #Regen
            self.RegenCondition = True
            self.RegenTours = 5
            def Régénération(self):
                self.HP += int(Héros.HP*0.2)
                if self.HP > Héros.HP:
                    self.HP = Héros.HP
                print(f"Vous vous soignez de {int(Héros.HP*0.2)} points de vie. Votre vie : {self.HP}")
            print(f"Vous vous soignez de {int(Héros.HP*0.2)} pendant 5 tours. Votre vie : {self.HP}.")
        
        if choixConsommable == 3: #DEFUp
            self.DEFCondition = True
            self.DEFTours = 5
            def AugmentationDEF(self):
                self.DEF = int(Héros.DEF*1.35)
            print(f"Vous augmentez votre défense de {self.DEF} pendant 5 tours. Votre défense : {self.DEF}")
        
        if choixConsommable == 4: #DMGUp
            self.RageCondition = True
            self.RageTours = 5  
            def AugmentationDMG(self):
                self.DMG = int(Héros.DMG*1.50)
            print(f"Vos attaques infligeront 50% de dégats supplémentaires pour 5 tours. Vos dégâts : {self.DMG}.")
        
        if choixConsommable == 5: #Esquive
            self.EsquiveCondition = True
            self.EsquiveTours = 5
            def Esquiver(self):
                if rd.random() < self.luck:
                    self.Esquive = True
                else:
                    self.Esquive = False
            print("Vous avez une chance d'esquiver l'attaque ennemie (5 tours). ")


    def TentativeFuite(self):
        ChanceFuite = self.luck/2
        if rd.random() < ChanceFuite:
            self.Fuite = True
            print("Vous avez réussi à vous enfuire ! ")
        else:
            self.Fuite = False
            print("Vous ne parvenez pas à vous enfuire ! ")



    def DégâtsSubis(self, DamageDealt, crit):
        if self.nom != 'Salie' and self.nom != 'Magnus':
            self.PassifBlockATK()
            if self.Bloquer:
                return "Attaque bloquée ! "
            
        if self.nom == 'Magnus':
            if hasattr(self, "ParerCondition") and self.ParerCondition:
                self.ParerUneAttaque()
                self.ParerTours -= 1
                if self.ParerTours == 0:
                    self.ParerCondition = False
                if self.Parer:
                    return "Attaque parée ! "
            
        if hasattr(self, "EsquiveCondition") and self.EsquiveCondition:
            self.Esquiver()
            self.EsquiveTours -= 1
            if self.EsquiveTours == 0:
                self.EsquiveCondition = False
            if self.Esquive:
                return "Attaque esquivée ! "
            
        if crit:
            self.HP -= DamageDealt
            print(f"{self.nom} prend {DamageDealt} dégâts (coup critique ! ). Sa vie restante : {self.HP}")

        else:
            self.HP -= max(0, DamageDealt - self.DEF)
            print(f"{self.nom} prend {DamageDealt - self.DEF} dégâts. Sa vie restante : {self.HP}")

        if self.HP < 0:
            self.HP = 0



zone = 1 #Village
monstres_zone1 = ['Gobelin', 'Loup']
monstres_zone2 = ['Gobelin', 'Loup', 'Zombie', 'Ogre']
monstres_zone3 = ['Loup-garou', 'Zombie', 'Ogre', 'Ours']
monstres_zone4 = ['Loup', 'Ours', 'Orc']
monstres_zone5 = ['Chevalier déchu']
monstre_zone = [monstres_zone1, monstres_zone2, monstres_zone3, monstres_zone4, monstres_zone5]

Monstre = Personnage(
    rd.choice(monstre_zone[zone-1]),                        #nom
    rd.randint(40 + (20 * zone-1), 60 + (20 * zone-1)),     #HP
    rd.randint(1 + (zone-1), 3 + (zone-1)),                 #DEF
    rd.randint(10 + (4 * zone-1), 14 + (4 * zone-1)),       #DMG
    0.20 + (0.05 * zone-1), 0.40, 0, 1)                     #critluck, luck, EXP, lvl

print("Quel personnage voulez-vous choisir ? ")
ChoixHéros = input("Entrez un nombre : Salie (1) / Magnus (2)")
while True:
    try:
        ChoixHéros = int(ChoixHéros)
        break
    except ValueError:
        print("Veuillez entrer un nombre. ")

while ChoixHéros != 1 and ChoixHéros != 2:
    print("Veuillez entrer un nombre valide. ")
    ChoixHéros = int(input("Entrez un nombre : Salie (1) / Magnus (2)"))

if ChoixHéros == 1:
    Héros = Personnage("Salie", 100, 5, 12, 0.25, 0.75, 0, 1)
    print("Vous avez choisi Salie.")
elif ChoixHéros == 2:
    Héros = Personnage("Magnus", 100, 8, 10, 0.30, 0.60, 0, 1)
    print("Vous avez choisi Magnus.")
HérosCombat = Héros


def main():
    global HérosCombat
    global Monstre

    while Héros.estVivant() and Monstre.estVivant():
        if hasattr(HérosCombat, "RegenCondition") and HérosCombat.RegenCondition:
            HérosCombat.Régénération()
            HérosCombat.RegenTours -= 1
            if HérosCombat.RegenTours == 0:
                HérosCombat.RegenCondition = False
        if hasattr(HérosCombat, "DEFCondition") and HérosCombat.DEFCondition:
            HérosCombat.DEFTours -= 1
            if HérosCombat.DEFTours == 0:
                HérosCombat.DEFCondition = False
                HérosCombat.DEF = Héros.DEF
        if hasattr(HérosCombat, "RageCondition") and HérosCombat.RageCondition:
            HérosCombat.RageTours -= 1
            if HérosCombat.RageTours == 0:
                HérosCombat.RageCondition = False
                HérosCombat.DMG = Héros.DMG
        if hasattr(HérosCombat, "EsquiveCondition") and HérosCombat.EsquiveCondition:
            HérosCombat.EsquiveTours -= 1
            if HérosCombat.EsquiveTours == 0:
                HérosCombat.EsquiveCondition = False

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
        
        choix = input("Votre action : ")
        try:
            choix = int(choix)
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        if choix == 1:
            print(HérosCombat.AttaqueBasique(Monstre))
        elif choix == 2 and ChoixHéros == 1:
            choixProjectile = int(input("Choisissez un projectile : "))
            print("1 : Tonneau explosif")
            print("2 : Boule de feu")
            print("3 : Potion jetable d'acide")
            print("4 : Parfum empoisonné")
            print(HérosCombat.LancerProjectile(Monstre, choixProjectile))
        elif choix == 2 and ChoixHéros == 2:
            HérosCombat.ParerUneAttaque()
            print("Vous avez 40% de chance de parer les trois prochaines attaques. ")
        elif choix == 3 and ChoixHéros == 2:
            print(HérosCombat.LancerArme(Monstre))
        elif (choix == 3 and ChoixHéros == 1) or (choix == 4 and ChoixHéros == 2):
            choixConsommable = int(input("Choisissez un consommable (1 : soin, 2 : régénération, 3 : +def, 4 : +atk, 5 : chance d'esquiver): "))
            if choixConsommable == 1:
                choixPotionDeSoin = int(input("Choisissez une taille de potion de soin (1 à 3): "))
                print(HérosCombat.UtiliserPotionDeSoin(Héros, choixPotionDeSoin))
            else:
                print(HérosCombat.UtiliserConsommable(Héros, choixConsommable))
        elif (choix == 4 and ChoixHéros == 1) or (choix == 5 and ChoixHéros == 2):
            print(HérosCombat.TentativeFuite())
            if Héros.Fuite == True:
                break
        else:
            print("Veuillez entrer un nombre valide.")
            continue
        print()

        if hasattr
        if not Monstre.estVivant():
            print("Vous avez gagné ! ")
            break
        
        print("L'ennemi attaque ! ")
        print(Monstre.AttaqueBasique(Héros))
        print()

        if not Héros.estVivant():
            print("Vous êtes mort ! ")
            break


main()

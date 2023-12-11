import random as rd

Bloquer = False
Parer = False
Fuite = False
Esquive = False
ArmeLancée = False
ChanceParer = 0.40

def VerifType(fonction):
    try:
        fonction = int(fonction)
        return True
    except ValueError:
        print("Veuillez entrer un nombre.")
        return False
    
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
    def __init__(self, nom, HP, DEF, DMG, critluck, luck, EXP = 0, lvl = 1):
        self.nom = nom
        self.HP = HP
        self.DEF = DEF
        self.DMG = DMG
        self.critluck = critluck
        self.luck = luck
        self.EXP = EXP
        self.lvl = lvl
        self.FireDOT = int(self.DMG*0.30)
        self.AcidDOT = int(self.DMG*0.70)
        self.PoisonDOT = int(self.DMG*0.2)

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


    def LancerProjectile(self, target, choixProjectile): #Salie Action 2
        if choixProjectile == 1: #Tonneau explosif
            print("Tonneau explosif")
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.9)
            target.DégâtsSubis(DamageDealt, crit)
        
        if choixProjectile == 2: #Boule de feu
            target.FireCondition = True
            target.FireTours = 3
            print("Boule de feu")
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.80)
            target.DégâtsSubis(DamageDealt, crit)

            def Enflammé(target):
                target.HP = int(target.HP - self.FireDOT)
                target.FireTours -= 1
                if target.FireTours == 0:
                    target.FireCondition = False
            print(f"L'ennemi prendra {self.FireDOT} dégâts de feu pendant 3 tours. ")

            
            
        if choixProjectile == 3: #Potion jetable d'acide
            print("Potion jetable d'acide")
            target.AcidCondition = True
            target.AcidTours = 3
            DamageDealt, crit = Critique(self.critluck, self.DMG)
            DamageDealt = int(DamageDealt*0.25)
            target.DégâtsSubis(DamageDealt, crit)
            
            def Acidifié(target):
                target.HP = int(target.HP - self.AcidDOT)
                target.AcidTours -= 1
                if target.AcidTours == 0:
                    target.AcidCondition = False
            print("L'ennemi prendra {self.AcidDOT} dégâts d'acide pendant 3 tours. ")

            
        if choixProjectile == 4: #Parfum de poison
            target.PoisonCondition = True
            target.PoisonTours = 999
            print("Parfum empoisonné")

            def Empoisonné(target):
                target.HP = int(target.HP - self.PoisonDOT)
                target.PoisonTours -= 1
                if target.PoisonTours == 0:
                    target.PoisonCondition = False
            print(f"L'ennemi recevra {self.PoisonDOT} à chaque tour.")

    def ParerUneAttaque(self): #Magnus Action 2
        self.ParerCondition = True
        self.ParerTours = 3
        if rd.random() < ChanceParer:
            self.Parer = True
        else:
            self.Parer = False

        self.ParerTours -= 1
        if self.ParerTours == 0:
            self.ParerCondition = False
            print("Vous ne pouvez plus parer. ")


    def LancerArme(self, target): #Magnus Action 3
        self.ArmeLancée = True
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        DamageDealt = int(DamageDealt*2)
        target.DégâtsSubis(DamageDealt, crit)
        self.DMG = self.DMG / 2


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
                self.RegenTours -= 1
                if self.RegenTours == 0:
                    self.RegenCondition = False
                    print("La régénération prend fin. ")
            print(f"Vous vous soignerez de {int(Héros.HP*0.2)} pendant 5 tours. Votre vie : {self.HP}.")

        if choixConsommable == 3: #DEFUp
            self.DEFCondition = True
            self.DEFTours = 5                
            self.DEF = int(self.DEF*1.35)

            def AugmentationDEF(self):
                self.DEFTours -= 1
                print(f"Il vous reste {self.DEFTours} tours de défense augmentée. ")
                if self.DEFTours == 0:
                    self.DEFCondition = False
                    self.DEF = Héros.DEF
                    print("Votre défense revient à la normale.")
            print(f"Vous augmentez votre défense de {self.DEF} pendant 5 tours. Votre défense : {self.DEF}")
        
        if choixConsommable == 4: #DMGUp
            self.RageCondition = True
            self.RageTours = 5
            self.DMG = int(self.DMG*1.50)

            def AugmentationDMG(self):
                self.RageTours -= 1
                print(f"Il vous reste {self.DEFTours} tours de dégâts augmentés. ")
                if self.RageTours == 0:
                    self.RageCondition = False
                    if self.ArmeLancée:
                        self.DMG = int(Héros.DMG / 2)
                    else:
                        self.DMG = Héros.DMG
                    print("Vous revenez à l'état normal.")
            print(f"Vous êtes enragé(e) ! Vos attaques infligeront 50% de dégats supplémentaires pendant 5 tours. Vos dégâts : {self.DMG}.")
        
        if choixConsommable == 5: #Esquive
            self.EsquiveCondition = True
            self.EsquiveTours = 5

            def Esquiver(self):
                if rd.random() < self.luck:
                    self.Esquive = True
                else:
                    self.Esquive = False
                self.EsquiveTours -= 1
                if self.EsquiveTours == 0:
                    self.EsquiveCondition = False
                    print("Vous ne pouvez plus esquiver. ")
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
monstres_zone1 = ['Gobelin', 'Loup'] #Village
monstres_zone2 = ['Gobelin', 'Loup', 'Ogre'] #Plaine
monstres_zone3 = ['Loup-garou', 'Zombie', 'Ogre', 'Ours'] #Forêt
monstres_zone4 = ['Loup', 'Ours', 'Orc'] #Montagne
monstres_zone5 = ['Chevalier déchu'] #Château
monstre_zone = [monstres_zone1, monstres_zone2, monstres_zone3, monstres_zone4, monstres_zone5]

def SummonMonstre(zone):
    global Monstre
    Monstre = Personnage(
        rd.choice(monstre_zone[zone-1]),                        #nom
        rd.randint(40 + (20 * zone-1), 60 + (20 * zone-1)),     #HP
        rd.randint(1 + (zone-1), 3 + (zone-1)),                 #DEF
        rd.randint(10 + (4 * zone-1), 14 + (4 * zone-1)),       #DMG
        0.20 + (0.05 * zone-1), 0.40)                           #critluck, luck

def mainCombat():
    HérosCombat = Héros

    while Héros.estVivant() and Monstre.estVivant():
        if hasattr(HérosCombat, "RegenCondition") and HérosCombat.RegenCondition:
            print(HérosCombat.Régénération())
        if hasattr(HérosCombat, "DEFCondition") and HérosCombat.DEFCondition:
            print(HérosCombat.AugmentationDEF())
        if hasattr(HérosCombat, "RageCondition") and HérosCombat.RageCondition:
            print(HérosCombat.AugmentationDMG())

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
        while not VerifType(choix):
            choix = input("Votre action : ")

        if choix == 1:
            print(HérosCombat.AttaqueBasique(Monstre))

        elif choix == 2 and ChoixHéros == 1:
            print("Choisissez un projectile : ")
            print("1 : Tonneau explosif")
            print("2 : Boule de feu")
            print("3 : Potion jetable d'acide")
            print("4 : Parfum empoisonné")
            choixProjectile = input("Votre projectile : ")
            while not VerifType(choixProjectile):
                choixProjectile = input("Votre projectile : ")
            print(HérosCombat.LancerProjectile(Monstre, choixProjectile))

        elif choix == 2 and ChoixHéros == 2:
            HérosCombat.ParerUneAttaque()
            print("Vous avez 40% de chance de parer les trois prochaines attaques. ")

        elif choix == 3 and ChoixHéros == 2:
            print("Vous avez lancé(e) votre arme ! ")
            print(HérosCombat.LancerArme(Monstre))

        elif (choix == 3 and ChoixHéros == 1) or (choix == 4 and ChoixHéros == 2):
            print("Choisissez un consommable")
            print("1 : Potion de soin")
            print("2 : Potion de régénération")
            print("3 : Potion de défense")
            print("4 : Potion de rage (dégâts) ")
            print("5 : Piment (possibilité d'esquiver les attaques ennemies) ")
            choixConsommable = int(input("Votre consommable : "))
            while not VerifType(choixConsommable):
                choixConsommable = int(input("Votre consommable : "))
            if choixConsommable == 1:
                print("Choisissez une taille de potion de soin : ")
                print("1 : Petite potion de soin (soigne 25% de vie) ")
                print("2 : Potion de soin moyenne (soigne 40% de vie) ")
                print("3 : Grande potion de soin (soigne 70% de vie)")
                choixPotionDeSoin = int(input("Choisissez une taille de soin : "))
                while not VerifType(choixPotionDeSoin):
                    choixPotionDeSoin = int(input("Choisissez une taille de soin : "))
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
        print("--------------------")

        if hasattr(Monstre, "FireCondition") and Monstre.FireCondition:
            Monstre.Enflammé()
            print(f"L'ennemi prend {HérosCombat.FireDOT} dégâts de feu. ")
        if hasattr(Monstre, "AcidCondition") and Monstre.AcidCondition:
            Monstre.Acidifié()
            print(f"L'ennemi prend {HérosCombat.AcidDOT} dégâts d'acide. ")
        if hasattr(Monstre, "PoisonCondition") and Monstre.PoisonCondition:
            Monstre.Empoisonné()
            print(f"L'ennemi prend {HérosCombat.PoisonDOT} dégâts de poison. ")
        if not Monstre.estVivant():
            print("--------------------")
            print(f"{Monstre.nom} est mort ! Vous avez gagné ! ")
            break
        
        print("L'ennemi attaque ! ")
        print(Monstre.AttaqueBasique(Héros))
        print("--------------------")

        if not Héros.estVivant():
            print("Vous êtes mort ! ")
            break

print("Quel personnage voulez-vous choisir ? ")
print("1 : Salie (PV : 100, DEF : 4, ATK : 10, ChanceCritique : 25, Chance : 75)")
print("2 : Magnus (PV : 120, DEF : 6, ATK : 8, ChanceCritique : 30, Chance : 60)")
ChoixHéros = input("Entrez un nombre : ")
while not VerifType(ChoixHéros) and ChoixHéros in ['1, 2']:
    print("Veuillez entrer un nombre valide. ")
    ChoixHéros = input("Entrez un nombre : ")

if ChoixHéros == 1:
    Héros = Personnage("Salie", 100, 4, 10, 0.25, 0.75) #nom, PV, DEF, ATK, %crit, %luck
    print("Vous avez choisi Salie.")
elif ChoixHéros == 2:
    Héros = Personnage("Magnus", 120, 6, 8, 0.30, 0.60) #nom, PV, DEF, ATK, %crit, %luck
    print("Vous avez choisi Magnus.")

SummonMonstre(1)
print(f"Vous affrontez {Monstre.nom} ! ")
print(f"Ses statistiques : {Monstre.HP, Monstre.DEF, Monstre.DMG, Monstre.critluck, Monstre.luck}")

mainCombat()
if not Héros.estVivant:
    print("Voulez-vous recommencer le combat ? ")
    restart = input("Entrez un nombre (1 : oui, 2 : non)")
    while not VerifType(restart):
        restart = input("Entrez un nombre (1 : oui, 2 : non)")
    if restart == 1:
        mainCombat()
    else:
        print("Le jeu est fini. ")

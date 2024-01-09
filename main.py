import random as rd
import time
#Mimic on death issue
inventaire = {"(1) Potions de soin": 0, "(2) Potion de régénération": 0, "(3) Potion de défense": 0, "(4) Potion de rage": 0, "(5) Piment": 0}
invPotiondeSoin = {"(1) Potion de soin Faible":0, "(2) Potion de soin Moyen":0, "(3) Potion de soin Elevé":0}
Perdu = False

def YesorNo():
    while True:
        x = input("(Y / N) ? ")
        if x == "Y":
            return True
        elif x == "N":
            return False
        else:
            print("Veuillez entrer une réponse valide.")
            continue

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
        self.maxHP = HP
        self.DEF = DEF
        self.maxDEF = DEF
        self.DMG = DMG
        self.maxDMG = DMG
        self.critluck = critluck
        self.luck = luck
        self.EXP = EXP
        self.lvl = lvl
        self.Bloquer = False
        self.Parer = False
        self.Esquive = False
        self.ArmeLancée = False
        # self.Fuite = False Cette possibilité a été retirée
        self.FireDOT = int(self.DMG*0.35)
        self.AcidDOT = int(self.DMG*0.70)
        self.PoisonDOT = int(self.DMG*0.25)
        
    def estVivant(self):
        return self.HP > 0

    def LVLUP(self):
        self.lvl += 1
        print(f"Vous avez augmenté de niveau ! Votre niveau : {self.lvl}.")
        self.EXP -= 100
        self.maxHP += rd.randint(20, 30)
        self.HP = self.maxHP
        self.maxDEF += rd.randint(1, 4)
        self.maxDMG += rd.randint(2, 6)
        print(f"Vos nouvelles statistiques : PV : {self.HP}, DEF : {self.DEF}, ATK : {self.DMG}.")

    def PassifBlockATK(self):
        if rd.random() < 0.20:
            self.Bloquer = True
        else:
            self.Bloquer = False

#-------------------- Actions --------------------

    def AttaqueBasique(self, target): #Action 1
        if self.nom == "Magnus" or self.nom == "Salie":
            print("Attaque Basique")
            time.sleep(0.5)
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        return target.DégâtsSubis(DamageDealt, crit)


    def LancerProjectile(self, target): #Salie Action 2

        while True:
            print("Choisissez un projectile : ")
            print("1 : Tonneau explosif")
            print("2 : Boule de feu")
            print("3 : Potion jetable d'acide")
            print("4 : Parfum empoisonné")
            choixProjectile = input("Votre projectile : ")

            if choixProjectile == "1": #Tonneau explosif
                print("Tonneau explosif")
                time.sleep(0.5)
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.9)
                return target.DégâtsSubis(DamageDealt, crit)


            if choixProjectile == "2": #Boule de feu
                target.FireCondition = True
                target.FireTours = 3
                print("Boule de feu")
                time.sleep(0.5)
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.75)
                print(target.DégâtsSubis(DamageDealt, crit))
                return f"{target.nom} prendra {self.FireDOT} dégâts de feu pendant 3 tours. "

                
            if choixProjectile == "3": #Potion jetable d'acide
                print("Potion jetable d'acide")
                time.sleep(0.5)
                target.AcidCondition = True
                target.AcidTours = 3
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.30)
                print(target.DégâtsSubis(DamageDealt, crit))
                return f"{target.nom} prendra {self.AcidDOT} dégâts d'acide pendant 3 tours. "

                
            if choixProjectile == "4": #Parfum de poison
                target.PoisonCondition = True
                print("Parfum empoisonné")
                time.sleep(0.5)
                return f"{target.nom} prendra {self.PoisonDOT} dégâts de poison à chaque tour."
            
            else:
                print("Veuillez entrer un nombre valide.")
                continue


    def ParerUneAttaque(self): #Magnus Action 2
        self.ParerTours -= 1
        if self.ParerTours == 0:
            self.ParerCondition = False
            print("(Dernière chance de parer)")
        if rd.random() < self.luck: #0.6
            return True
        else:
            return False


    def LancerArme(self, target): #Magnus Action 3
        self.ArmeLancée = True
        print("Vous lancez votre arme. ")
        time.sleep(0.5)
        DamageDealt, crit = Critique(self.critluck, self.DMG)
        DamageDealt = int(DamageDealt*2)
        self.DMG = int(self.DMG/2)
        return target.DégâtsSubis(DamageDealt, crit)


    def UtiliserConsommable(self): #Action 3 / 4
        global inventaire
        global invPotiondeSoin
        while True:
            print("Quel consommable utiliser ? ")
            for key,value in inventaire.items():
                print(f"{key} : {value}")
            choixConsommable = input("Votre choix : ")
            print()

            if choixConsommable == "1": #Soin
                if inventaire["(1) Potions de soin"] == 0: #Soin
                    print("Vous n'avez plus de potion de soin ! ")
                    continue
                while True:
                    print("Quelle taille de potion de soin ? ")
                    for key,value in invPotiondeSoin.items():
                        print(f"{key} : {value}")
                    choixPotionDeSoin = input("Choisissez une taille de potion : ")

                    if choixPotionDeSoin == "1":
                        if invPotiondeSoin["(1) Potion de soin Faible"] != 0:
                            self.HP = int(self.HP + (self.HP*0.20))
                            if self.HP > self.maxHP:
                                self.HP = self.maxHP
                            invPotiondeSoin["(1) Potion de soin Faible"] -= 1
                            inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(self.maxHP*0.20)}PV. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin faible ! ")
                            print()
                            continue

                    if choixPotionDeSoin == "2":
                        if invPotiondeSoin["(2) Potion de soin Moyen"] != 0:
                            self.HP = int(self.HP + (self.maxHP*0.35))
                            if self.HP > self.maxHP:
                                self.HP = self.maxHP
                            invPotiondeSoin["(2) Potion de soin Moyen"] -= 1
                            inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(self.maxHP*0.35)}PV. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin moyen ! ")
                            print()
                            continue

                    if choixPotionDeSoin == "3":
                        if invPotiondeSoin["(3) Potion de soin Elevé"] != 0:
                            self.HP = int(self.HP + (self.maxHP*0.50))
                            if self.HP > self.maxHP:
                                self.HP = self.maxHP
                            invPotiondeSoin["(3) Potion de soin Elevé"] -= 1
                            inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(self.maxHP*0.50)}PV. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin élevé ! ")
                            print()
                            continue

                    else:
                        print("Veuillez entrer un nombre valide.")
                        continue

            elif choixConsommable == "2": #Regen
                if inventaire["(2) Potion de régénération"] != 0:
                    self.RegenCondition = True
                    self.RegenTours = 5
                    inventaire["(2) Potion de régénération"] -= 1
                    return f"Vous vous soignerez de {int(self.maxHP*0.15)} pendant 5 tours. Votre vie : {self.HP}."
                else:
                    print("Vous n'avez plus de potion de régénération ! ")
                    continue

            elif choixConsommable == "3": #DEFUp
                if inventaire["(3) Potion de défense"] != 0:
                    self.DEFCondition = True
                    self.DEFTours = 5                
                    self.DEF = int(self.maxDEF*1.35)
                    inventaire["(3) Potion de défense"] -= 1
                    return f"Vous augmentez votre défense de 35% pendant 5 tours. Votre défense : {self.DEF}"
                else:
                    print("Vous n'avez plus de potion de défense ! ")
                    continue

            elif choixConsommable == "4": #DMGUp
                if inventaire["(4) Potion de rage"] != 0:
                    self.RageCondition = True
                    self.RageTours = 5
                    if self.ArmeLancée == True:
                        self.DMG = int((self.maxDMG/2)*1.35)
                    else:
                        self.DMG = int(self.maxDMG*1.35)
                    inventaire["(4) Potion de rage"] -= 1
                    return f"Vous êtes enragé(e) ! Vos attaques infligeront 35% de dégats supplémentaires pendant 5 tours. Vos dégâts : {self.DMG}."
                else:
                    print("Vous n'avez plus de potion de rage ! ")
                    continue
            
            elif choixConsommable == "5": #Esquive
                if inventaire["(5) Piment"] != 0:
                    self.EsquiveCondition = True
                    self.EsquiveTours = 5
                    inventaire["(5) Piment"] -= 1
                    return f"Vous avez {int(self.luck*100)}% de chance d'esquiver l'attaque ennemie pendant 5 tours. "
                else:
                    print("Vous n'avez plus de piment ! ")
                    continue

            else:
                print("Veuillez entrer un nombre valide.")
                print()
                continue

#Cette action a été retirée.
    # def TentativeFuite(self):
    #     ChanceFuite = self.luck/2
    #     if rd.random() < ChanceFuite: #Salie : 0.75/2, Magnus : 0.6/2
    #         self.Fuite = True
    #         return "Vous avez réussi à vous enfuir ! "
    #     else:
    #         return "Vous ne parvenez pas à vous enfuir. "

#-------------------- Buffs --------------------

    def Régénération(self):
        self.HP += int(self.maxHP*0.15)
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        print(f"Vous vous soignez de {int(self.maxHP*0.15)} points de vie. ")
        self.RegenTours -= 1
        if self.RegenTours != 0:
            return f"Il vous reste {self.RegenTours} tours de régénération. "
        else:
            self.RegenCondition = False
            return "La régénération prend fin. "

    def AugmentationDEF(self):
        self.DEFTours -= 1
        if self.DEFTours != 0:
            return f"Il vous reste {self.DEFTours} tours de défense augmentée. "
        else:
            self.DEFCondition = False
            self.DEF = self.maxDEF
            return "Votre défense revient à la normale. "
    
    def AugmentationDMG(self):
        self.RageTours -= 1
        if self.RageTours != 0:
            return f"Il vous reste {self.RageTours} tours de rage. "
        else:
            self.RageCondition = False
            if self.ArmeLancée:
                self.DMG = int(self.maxDMG / 2)
            else:
                self.DMG = self.maxDMG
            return "Vos dégâts reviennent à la normale. "

    def Esquiver(self):
        self.EsquiveTours -= 1
        if self.EsquiveTours == 0:
            self.EsquiveCondition = False
            print("(Dernière chance d'esquiver)")
        if rd.random() < self.luck: #Salie : 0.75, Magnus : 0.6
            return True
        else:
            return False

#-------------------- Debuffs --------------------

    def Enflammé(target, self):
        target.HP = int(target.HP - self.FireDOT)
        target.FireTours -= 1
        if target.FireTours == 0:
            target.FireCondition = False
        return ""

    def Acidifié(target, self):
        target.HP = int(target.HP - self.AcidDOT)
        target.AcidTours -= 1
        if target.AcidTours == 0:
            target.AcidCondition = False
        return ""
            
    def Empoisonné(target, self):
        target.HP = int(target.HP - self.PoisonDOT)

#-------------------- Prise de Dégâts --------------------
    
    def DégâtsSubis(self, DamageDealt, crit):
        if self.nom != 'Salie' and self.nom != 'Magnus':
            if self.PassifBlockATK():
                return "Attaque bloquée ! "
            
        if hasattr(self, "ParerCondition") and self.ParerCondition:
            if self.ParerUneAttaque():
                return "Attaque parée ! "

        if hasattr(self, "EsquiveCondition") and self.EsquiveCondition:
            if self.Esquiver():
                return "Attaque esquivée ! "

        if crit:
            self.HP -= DamageDealt
            return f"{self.nom} prend {DamageDealt} dégâts (coup critique ! ). Sa vie restante : {self.HP}"
        else:
            self.HP -= max(0, DamageDealt - self.DEF)
            return f"{self.nom} prend {max(0, DamageDealt - self.DEF)} dégâts. Sa vie restante : {self.HP}"
        
#-------------------- Inventaire -> get consommables --------------------

def ObtenirConsommable(amount):
    global inventaire
    global invPotiondeSoin
    for i in range(amount):
        ConsommableObtenu = rd.choices(list(inventaire.keys()), weights = [0.20, 0.15, 0.30, 0.25, 0.10])[0]
        inventaire[ConsommableObtenu] += 1
        if not ConsommableObtenu == "(1) Potions de soin":
            print(f"{ConsommableObtenu[4:]}")
        else:
            SoinObtenu = rd.choices(list(invPotiondeSoin.keys()), weights = [0.60, 0.25, 0.15])[0]
            invPotiondeSoin[SoinObtenu] += 1
            print(f"{SoinObtenu[4:]}")

    print("\nVotre inventaire : \n")
    for key, value in inventaire.items():
        print(f"{key[4:]} : {value}")
    if "(1) Potions de soin" in ConsommableObtenu:
        print("\nVos potions de soin : ")
        for key, value in invPotiondeSoin.items():
            print(f"{key[4:]} : {value}")
    return ""

#-------------------- Invoc de Monstre --------------------

def SummonMonstre(zone, nom):
    HP_range = [40 + 20 * (zone - 1), 60 + 20 * (zone - 1)]
    DEF_range = [1 + zone, 3 + zone]
    DMG_range = [10 + 4 * (zone - 1), 14 + 4 * (zone - 1)]
    if nom == "Mimic":                                          #stats du Mimic (plus de DMG / DEF, moins de HP)
        nom = nom
        HP = rd.randint(40 + 20 * (zone-2), 60 + 20 * (zone-2)) #HP de zone-1
        DEF = rd.randint(zone, zone +2)                         #DEF plus faible
        DMG = rd.randint(10 + 5 * (zone), 14 + 5 * (zone))      #multiplicateur de DMG plus élevé + zone+1
    else: #monstre avec nom donné
        nom = nom
        HP = rd.randint(*HP_range)
        DEF = rd.randint(*DEF_range)
        DMG = rd.randint(*DMG_range)
    critluck = 0.20 + (0.05 * (zone-1))
    global Monstre
    Monstre = Personnage(nom, HP, DEF, DMG, critluck, 0.40, 0, zone)

#-------------------- main --------------------


def isMimic():
    if rd.random() <= 0.25:
        return True
    else:
        return False
    
def Trésor(zone):
    print("Vous obtenez un trésor ! ")
    print("Voulez-vous l'ouvrir ? ")
    if YesorNo():
        if isMimic():
            print("C'était un Mimic, vous vous êtes fait avoir ! \n")
            mainCombat(zone, "Mimic")
        else:
            print("Vous obtenez les consommables suivants : ")
            return ObtenirConsommable(3)
    else:
        return "Vous laissez le coffre. "
    
def ActionJoueur():    
    while True:

        if ChoixHéros == "1":
            print("Quelle action ? Entrez un nombre : ")
            print("(1) Attaque basique")
            print("(2) Lancer un objet")
            print("(3) Utiliser un consommable")
        if ChoixHéros == "2":
            print("Quelle action ? Entrez un nombre : ")
            print("(1) Attaque basique")
            print("(2) Chance de parer (3 fois)")
            print("(3) Lancer votre arme (2x dégâts, mais vous infligerez ensuite ATK/2)")
            print("(4) Utiliser un consommable")
        
        choix = input("Votre action : ")
        print()

        if choix == "1": #Attaque basique
            print(Héros.AttaqueBasique(Monstre))
            break
        
        elif choix == "2" and ChoixHéros == "1": #Lancer un projectile (Salie)
            print(Héros.LancerProjectile(Monstre))
            break
        
        elif choix == "2" and ChoixHéros == "2": #Parer (Magnus)
            Héros.ParerCondition = True
            Héros.ParerTours = 3
            print(f"Vous avez {int(Héros.luck*100)}% de chance de parer les trois prochaines attaques. ")
            break
        
        elif choix == "3" and ChoixHéros == "2": #Lancer l'arme (Magnus)
            if Héros.ArmeLancée:
                print("Vous avez déjà lancé votre arme ! ")
                time.sleep(0.35)
                continue
            else:
                print(Héros.LancerArme(Monstre))
                break
            
        elif (choix == "3" and ChoixHéros == "1") or (choix == "4" and ChoixHéros == "2"): #Utiliser un consommable
            if all(value == 0 for value in inventaire.values()):
                print("Vous n'avez plus de consommable ! ")
                continue
            print(Héros.UtiliserConsommable())
            break
        
    #Cette action a été retirée.
        # elif (choix == "4" and ChoixHéros == "1") or (choix == "5" and ChoixHéros == "2"): #Fuire
        #     print(Héros.TentativeFuite())
        #     break
        
        else:
            print("Veuillez entrer un nombre valide.")
            time.sleep(0.35)
            continue

def mainCombat(zone, Monstre_nom):
    global Perdu
    SummonMonstre(zone, Monstre_nom)
    print(f"Vous affrontez {Monstre.nom} ! ")
    print(f"Ses statistiques : PV : {Monstre.HP}, DEF : {Monstre.DEF}, ATK : {Monstre.DMG}, Chance de coup critique : {Monstre.critluck}, Chance : {Monstre.luck}")
    print()
    Tour = 0

    while True:
        Tour += 1
        time.sleep(1)
        print("--------------------")
        print(f"Tour : {Tour}")
        print("--------------------")

        if hasattr(Héros, "RegenCondition") and Héros.RegenCondition:
            print(Héros.Régénération())
        if hasattr(Héros, "DEFCondition") and Héros.DEFCondition:
            print(Héros.AugmentationDEF())
        if hasattr(Héros, "RageCondition") and Héros.RageCondition:
            print(Héros.AugmentationDMG())

        print(f"\n{Héros.nom} -> PV : {Héros.HP}/{Héros.maxHP}, DEF : {Héros.DEF}, ATK : {Héros.DMG}\n")
        time.sleep(1)

        ActionJoueur()
        # if Héros.Fuite:
        #     break
        print()
        time.sleep(2)

        if not Monstre.estVivant():
            print(f"{Monstre.nom} est mort, Vous avez gagné ! ")
            Héros.EXP += rd.randint(45, 75)
            print(f"Vous obtenez 50 points d'expérience ({Héros.EXP}/100). ")
            if Héros.EXP >= 100:
                print(Héros.LVLUP())
            if Héros.ArmeLancée:
                print("Vous ramassez votre arme. ")
                Héros.ArmeLancée = False
            time.sleep(1)
            print(Trésor(zone))
            return ""

        if hasattr(Monstre, "FireCondition") and Monstre.FireCondition:
            Monstre.Enflammé(Héros)
            print(f"{Monstre.nom} prend {Héros.FireDOT} dégâts de feu. ")
        if hasattr(Monstre, "AcidCondition") and Monstre.AcidCondition:
            Monstre.Acidifié(Héros)
            print(f"{Monstre.nom} prend {Héros.AcidDOT} dégâts d'acide. ")
        if hasattr(Monstre, "PoisonCondition") and Monstre.PoisonCondition:
            Monstre.Empoisonné(Héros)
            print(f"{Monstre.nom} prend {Héros.PoisonDOT} dégâts de poison. ")

        print()
        print(f"{Monstre.nom} -> PV : {Monstre.HP}/{Monstre.maxHP}, DEF : {Monstre.DEF}, ATK : {Monstre.DMG}")
        print()
        time.sleep(1)

        if not Monstre.estVivant():
            print(f"{Monstre.nom} est mort, Vous avez gagné ! ")
            Héros.EXP += rd.randint(45, 75)
            print(f"Vous obtenez 50 points d'expérience ({Héros.EXP}/100). ")
            if Héros.EXP >= 100:
                print(Héros.LVLUP())
            if Héros.ArmeLancée:
                print("*Vous ramassez votre arme. ")
                Héros.ArmeLancée = False
            time.sleep(1)
            print(Trésor(zone))
            return ""
        
        print("L'ennemi attaque ! ")
        time.sleep(0.5)
        print(Monstre.AttaqueBasique(Héros))
        print()

        if not Héros.estVivant():
            print("Vous êtes mort ! ")
            Perdu = True
            return ""

def main(zone, Monstre_nom):
    while True:
        mainCombat(zone, Monstre_nom)
        if Perdu:
            print("Voulez vous recommencer le combat ? ")
            if YesorNo():
                Héros.HP = Héros.maxHP
                Héros.ArmeLancée = False
                continue
            else:
                exit()
        else:
            break

def ChoisirHéros():
    global ChoixHéros
    global Héros
    while True: #Choix du personnage
        print("Quel personnage voulez-vous choisir ? ")
        print("1 : Salie (PV : 100, DEF : 4, ATK : 10, ChanceCritique : 25, Chance : 75)")
        print("2 : Magnus (PV : 120, DEF : 6, ATK : 8, ChanceCritique : 30, Chance : 60)")
        ChoixHéros = input("Entrez un nombre : \n")

        if ChoixHéros == "1":
            Héros = Personnage("Salie", 100, 4, 10, 0.25, 0.75) #nom, PV, DEF, ATK, %crit, %luck
            print("Vous avez choisi Salie. \n")
            break
        elif ChoixHéros == "2":
            Héros = Personnage("Magnus", 120, 6, 8, 0.30, 0.60) #nom, PV, DEF, ATK, %crit, %luck
            print("Vous avez choisi Magnus. \n")
            break
        else:
            print("Veuillez entrer un nombre valide. ")
            print()
            continue

# ChoisirHéros()
# main(5, "un Gobelin")

#-------------------- Fin du code de combat --------------------

def defilement(liste):
    for element in liste:
        for character in element: 
            print(character, end = "", flush=True)
            time.sleep(0.01)
        print()
        time.sleep(0.5)

def trame_introduction():
    Introduction = [
        "L'histoire prend place au 12e siècle après J.C.. ", 
        "Une rumeur court dans le village de Ravensbrook en Norvège : ", 
        "un roi puissant nommé Harald aurait régné sur la contrée il y 200 ans. ", 
        "Un joyau d'une valeur inestimable aurait été découvert dans la montagne du nord : ", 
        "une montagne où résident de nombreuses créatures terrifiantes. ", 
        "Ce roi aurait donc trouvé ce joyau en réalité maudit et l'aurait placé sur sa couronne. ", 
        "Seulement, les monstres de la montagne sont puissants. ", 
        "Son royaume fût assiégé par ces créatures, le poussant à fuire. ", 
        "Le roi serait parti à la hâte, délaissant le joyau dans son château au sommet de la Montagne Enchantée. "
    ]
    defilement(Introduction)

def commencement_histoire():
    répliques_Salie = [
        "Salie : ",
        "part en quête d'ingrédients préparer une potion revitalisante pour un client lorqu'elle tente d'attraper un guérit-tout au pied d'un arbre.",
        "Un rayon de soleil surgit et attire son attention. Elle se retourne et voit devant elle au loin la Montagne Enchantée. ",
        "Elle repense au joyau : ",
        "Ce joyau doit bien exister. Là quelque part la haut. ",
        "Ce ne sont pas quelques grizzlis ou quelques reptiles de 3 mètres de long qui vont me manger...",
        "J'ai déjà combattu pour notre village. Et d'ailleurs j'en suis la meilleure. ",
        "",
        "Je suis décidée, je pars demain. ",
    ]

    répliques_Magnus = [
        "Magnus : "
        "part couper du bois dans la forêt avoisinnante afin de remplir son stock de buches pour sa cheminée. ",
        "Après s'être aventuré au coeur de celle-ci, un rugissement lointaint attire son attention. ",
        "Il lève les yeux et voit devant lui au loin, la Montagne Enchantée. ",
        "Il repense au joyau : ",
        "Ce caillou doit bien exister. Là, quelque part là haut ! ",
        "Je suis certain qu'aucune des bêtes de la montagne ne peuvent pas rivaliser pas contre moi ! ",
        "au loin: ",
        "Rooooaaaaaaarrr !",
        "...",
        "Magnus : ",
        "C'était quoi ça !? ",
        "Ce n'était pas un ours. Mais alors, qu'est ce que ça peut bien être ? ",
        "Si je veux en savoir plus, je sais ce qu'il me reste à faire...",
        "J'ai déjà combattu pour notre village. Mes capacités aux combats m'ont permis de survivre jusqu'ici.",
    ]
    
    Intro_partie1 = [
        f"Ainsi, {'Salie' if ChoixHéros=='1' else 'Magnus'} rassemble ses affaires et son équipement. Le soir même, il se rendit chez Garry, le vieux sage du village. ",
        "Il est l'un des descendants du fondateur du village, du nom de Raymond ERIKSON. ",
        "Un homme fort et intelligent, aux capacités de survie toutes aussi impressionnantes que ses capacités de combat. ",
        "*5 min plus tard*",
        "Garry : ",
        "HORS DE QUESTION ! ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "S'il te plaît, s'il te plaît, s'il te plaît ! ",
        "Garry : ",
        "Tu me rappelles moi dans ma jeunesse...",
        "A me précipiter à l'aventure sans même réfléchir ou penser aux conséquences",
        "Cette cicatrice sur mon visage... elle a été faite par une créature extrêmement dangereuse, ",
        "un monstre...",
        "",
        "Je n'ai pas de descendants. Prend mon héritage, l'épée des Erikson ! ", 
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Je te revaudrai ça grand-père..",
        "Garry : ",
        "Tu crois vraiment que je vais te la confier de cette manière ? ",
        "L'épée choisit son maître et est capable de libérer un pouvoir dévastateur ! ", 
        "Si tu la veux, tu vas devoir la mériter !"
    ]

    print("*Le héros se réveille un matin. ")
    time.sleep(1)
    if ChoixHéros == "1": #Affichage du texte pour Salie
        defilement(répliques_Salie)
    elif ChoixHéros == "2": #Affichage du texte pour Magnus
        defilement(répliques_Magnus)
    print()
    defilement(Intro_partie1)

def transition_1er_combat():
    trame = [
        "*6 mois se sont écoulés. *",
        "Garry : ",
        "Te voilà novice dans le rang des chasseurs. Chaque cible que tu élimineras te fera monter en rang. Ton savoir n'en sera qu'amélioré...",
        "Sache tout de même que ton premier but est de protéger le village.",
        "Comme par ton entraînement tu as su le comprendre, un grand pouvoir implique de grandes responsabilités...",
        "*Soudainement, un rugissement provenant du coeur du village attire votre attention. *",
        "Oh non...",
        "Garry : ", 
        "C'est l'occasion idéale, va sauver notre village et rapporte moi ce joyau!!",
        ""
    ]
    defilement(trame)  

#premier_combat: vs Gobelin

def fin_introduction():
    répliques = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "OUAHH ! Je viens vraiment de tuer ce monstre !!? ",
        "Oh ! Qu'est ce qui scintille juste là ? ", 
        "*Lorsque vous neutralisez une créature, vous pouvez choisir d'ouvrir ou non le coffre qui vous est offert en récompense",
        "Cool, je pourrais en avoir besoin, un de ces quatre. ",
        "Garry : ",
        "",
        "Pas mal pour une première. Mais on dirait qu'on a eu chaud. On est pas en sécurité ici.",
        "L'avenir de notre village est incertain, il repose entre tes mains désormais. Va! Et ne reviens pas sans avoir détruit ce joyau ! ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Et dire que je voulais juste une retraite paisible...",
        "Garry : ",
        "Mais après tout, ce joyau n'apporte rien de bon. Les créatures s'excitent et se rapprochent du village. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "C'est compris Garry ! Dis à tout le monde qu'ils n'ont rien à craidre car je suis là ! "       
        "",
        "*Ainsi le héros commence sa quête. *",
        ""
    ]

    if ChoixHéros == "2": #Affichage du texte pour Magnus
        répliques[1] = "OUAHH OK ! C'est bien plus impressionnant que ce que je pensais...°~°"
        répliques[14] = "J'ai ressentis les fruits de mon entrainement aujoud'hui... Ca va mal finir pour ces fichus monstres ! "
    
    defilement(répliques)
        
def prairie_niveau_1():
 
    trame_prairie_1 = [
        "*PRAIRIE: Niveau 1",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "OK...",
        "Va falloir que je surveille mes arrières. Je me suis jamais autant approchée de la montagne. ",
        "*Poursuit son entrainement. ",
        "*se repose 2h plus tard. ",
        "*Puis part ensuite en quête de nourriture pour les prochains jours. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Je devrais cherher un point d'eau",
        "*Trouve un ruisseau en pénétrant à travers les bois qui succèdent à la prairie. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "*Sors sa gourde",
        "*Une bête surgit de derrière les buissons ! ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "*Se met en garde.",
        "Oh ce n'est qu'une biche... Qu'elle est mignonne. ",
        "SLAAK ! Un monstre vient de surgir des buissons et d'embraucher violemment la biche avec ses griffes aserrées !!",
        "...! *Regarde le spectacle avec émotion",
        "*Cri de la biche*",
        "*Gloussements du monstre qui déchicte sa proie*",
        "Il faut que je m'en aille. Il a l'air d'avoir l'avantage ici...",
        "Tu vas me le payer sale pourriture ! ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Rentre au camp et repense à ce qui s'est passé. ",
        "*Deux jours se sont écoulés. *",
        "Bon, je sais par où je dois passer pour atteindre le coeur de la forêt. ",
        f"*{'Elle' if ChoixHéros=='1' else 'Il'} se munit de ses affaires et se met en route. ", 
        "*Devant au loin, un gros rocher noir. ",
        "Mais... Oh, Le monstre ! Il s'est endormi en plein milieu de la route ! ",
        "*Tentative d'approche furtive. *",
        "Monstre: ROAAAAAAR !!! ",
        "...",
        "*C'est un piège ! ",
        "Il faut que je l'attire vers la plaine! J'aurai l'avantage. ",
        "*Vous arrivez de justesse à la plaine. Mais le monstre ne se laisse pas devancer si facilement. *",
        "",
        "",   
    ]

    if ChoixHéros == "2": #Affichage du texte pour Magnus
        trame_prairie_1[15] = "Oh une biche! Ca pourrait être mon repas de ce soir. "
    
    defilement(trame_prairie_1)

#Combat contre le Stritominus

def prairie_niveau_2():
    
    répliques_prairie_fin_de_zone = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "J'espère seulement qu'il y a pas la maman dans les parages... hihihi ^-^",
        "*La terre se met à trembler*",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "OK BON AUTANT EN FINIR TOUT DE SUITE... ¨_¨ ",
        "*Un Stritominus 2 fois plus rapide arrive à toute vitesse ! ",
        "",
    ]
       
    defilement(répliques_prairie_fin_de_zone)
        
#Combat final prairie 

def foret_partie_1():
    trame_forêt_1 = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Je devrais me trouver un coin sûr, vu sur quoi je viens de tomber. ",
        f"*En s'enfonçant dans la forêt, {'Salie' if ChoixHéros=='1' else 'Magnus'} trouve une grotte au loin, cachée au pied d'un énorme arbre. ",
        "Super ! J'espère seulement qu'il y aura pas de locataire(s)...",
        "*La grotte est étroite, mais aucune trace du passage de qui ou quoi que ce soit. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Je vais me poser un instant, les combats d'hier m'ont fatigué. ",
        "...",
        "...",
        "...",
        "*6h plus tard",
        f"{'Salie' if ChoixHéros=='1' else 'Magnus'} (s'étirant) : ",
        "Huh.. J'ai dormi combien detemps ? ",
        "Mince ! le soleil est presque couché ! ",
        "Je devrais pas m'aventurer dehors, je connais pas assez bien les environs. ",
        "Faut que je barricade l'entrée de la grotte. ",
        "1 heure plus tard, avec quelques branches et de la mousse, vous avez réussi à camoufler l'entrée de la grotte. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Bon, cette barricade n'empêcherait même pas un écureuil d'entrer... Mais l'avantage c'est que je suis fondu dans le décor. ",
        "*Les prédateurs se réveillent, les loups hurlent à la pleine lune. Le vent souffle. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Je vais continuer sur ma lancée et me reposer jusqu'à l'aube. ",
    ]

    print("*ZONE 2: Au coeur de la forêt")
    if ChoixHéros == "2": #Magnus
        trame_forêt_1[6] = "Je vais me poser un instant. Je vais repenser aux K.O auquel ces monstres ont gouté hier (*baille) "
        trame_forêt_1[7] = "Oui bon je suis exténué en réalité..."
    defilement(trame_forêt_1)

def foret_partie_2_combat_fin():
    répliques_foret_p2 = [
        "*2 heures s'écoulent : ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Impossible de fermer l'oeil, il fait pas hyper chaud non plus. ",
        "*bruits de pas ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "C'était quoi ? ",
        "*Les bruits de pas se rapprochent de l'entrée de la grotte",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "°_° ...",
        "(Cette chose doit être massive, on en ressent les secousses lorsqu'elle se déplace)",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "*Une poussière lui tombe sur le nez. ",
        "ATCHOUM ! ",
        "oh, oh..",
        "Créature : Mhmmmm !!? ",
        "*Les bruits de pas proviennent de dessus de la cavité. ",
        "La créature est juste au dessus...",
        "La Lune laisse apparaître l'ombre de la créature, que vous voyez à travers un petit interstice: ",
        "une bête affreusement poilue et difforme.",
        "*Elle s'en va après un cours instant...",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Fiou ! J'ai cru que j'all...",
        "Créature : WWRRAAAAAAAA !! ",
        "La créature passe son bras à travers la terre et vous attrappe par le col !",
        "Vous vous trouvez nez à nez avec un 'Mordeur' et lui assénez un coup pour le repousser.",
    ]
 
    defilement(répliques_foret_p2)

#Combat contre le Mordeur

def réplique_apres_combat_mordeur():
    répliques_apres_combat_foret = [
        "J'ai...",
        "ré..u..ssi...",
        "_",  
    ]
    for element in répliques_apres_combat_foret: 
        for character in element: 
            print(character, end = "", flush = True)
            if element[character + 1] == ".":
                time.sleep(0.25)
            else:
                time.sleep(0.005)
        time.sleep(1)
        print()
    print(f"{'Salie' if ChoixHéros=='1' else 'Magnus'} s'évanouit. ")

def montagne():
    trame_montagne = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "*reprend vaguement ses esprits. ",
        "Mhmmm... où est ce que je suis ? ",
        "*Regarde autour d'elle. ",
        "Euuh ok... La grotte où j'étais jusque là me paraissait un peu plus petite. '=' ",
        "*Regarde vers l'entrée. ",
        "(°O°) OOOH !! ",
        f"COMMENT JE SUIS ARRIVE{'E' if ChoixHéros=='1' else ''} ICI !!? ",
        "*Vous voilà dans l'entre d'une grotte, située dans la Montagne Enchantée. ",
        "*Un bruit étrange provient de l'extérieur. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "On dirait qu'il se passe quelque chose dehors. "
    ]
    if ChoixHéros == "2":
        trame_montagne[3] = "*Regarde autour de lui. "
    defilement(trame_montagne)
    print("Aller voir ? ")
    if YesorNo():
        trame_déplacement = [
        "Vous avez décidé de vous déplacer jusqu'à la sortie. ",
        "",
        "Soudain une créature humanoîde à la gueule énorme portant une massue émerge, chevauchant un loup noir. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Ah ! Vous avez une sale tête monsieur ! ",
        "Orc : MOUAAAAAAA !! ",
        "Repas réveillé !! ",
        "Loup : WWrrraaa ! ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Eh ! gentil toutou...tout doux..tout do..",
        ]

    else:
        trame_déplacement = [
        "Vous restez au sol. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "C'est le moment ou jamais...",
        ]

    defilement(trame_déplacement)

#Combat contre l'Orc

def montagne_fin():

    trame_2_montagne = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "On dirait que cette petite sieste m'a permise de me requinquer ! ",
        "En quittant la zone de combat, vous levez la tête et apercevez des ruines au sommet de la Monstagne. ",
        "Mais c'est le château ! Je suis presque arrivée, encore un petit effort ! ",
        "En parlant d'effort, j'en fait assez pour aujourd'hui..",
        f"*{'Salie : ' if ChoixHéros=='1' else 'Magnus : '} regarde le loup allongé à moitié mort. ",
        "hehehe...",
        "Loup: *panique",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "VIENS LA !",
        "Loup: AAAAAAAAA !",
        f"*Ainsi, {'Salie' if ChoixHéros=='1' else 'Magnus'} chevauche la bête et atteint, après quelques heures seulement, le château."
    ]
    if ChoixHéros=="2":#Affichage du texte pour Magnus
        trame_2_montagne[3] = "Mais c'est le château que je vois là !? J'y suis presque, encore un petit effort !"      #modification texte à la ligne 3
    defilement(trame_2_montagne)

def Château_abandonné():
    trame_château = [
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Eh bas voilà vous pouvez bien servir à quelque chose des fo..",
        "*En voyant le château, le monstre déguerpit à toute vitesse",
        "Ok.. Ca n'annonce rien de bon.",
        "Je sais que je suis intimidante mais à ce point là ?",
        f"*Les poils de {'Salie' if ChoixHéros=='1' else 'Magnus'} se hérissent",
        "*Une pression hors norme provient de l'intérieur du château",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Oh ! '°'",
        "Le château est immensément grand",
        "La poussière omniprésente est la marque du temps passé à l'abandon et à la mercie des créatures prédatrices environnantes",
        f"*{'Salie (craintive) : ' if ChoixHéros=='1' else 'Magnus (craintif) : '}",
        "Ca y est... nous y sommes.",
        " ",
        " ",
    ]
    if ChoixHéros=="2":#Affichage du texte pour Magnus
        trame_château[3] = "Bah.. A bah d'accord. Je suis trop imposant pour toi c'est ça !?"    #modification texte à la ligne 3
        trame_château[4] = "C'est ça, cours flipp.."                                             #modification texte à la ligne 4                                         
    defilement(trame_château)

    chargement = ["Chargement de la zone finale..."]
    defilement(chargement)
    for i in range(3):
        print("...")
        time.sleep(1)

    trame_entrée_château = [
        "*Cinématique", 
        "Le héros se dirige vers l'entrée du château d'un pas craintif. ",
        "En arrivant devant la porte d'entrée : ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Qu'est ce qui pourrait bien se cacher derrière ? ",
        "De toute façon il ne me semble pas qu'une bête se plairait dans ce château. Endroit reculé, spacieux, et inhabité...",
        "Parfait pour y établir son nid...",
        "Une fois dedans, des dizaines d'ossements humains et animaux jonchent le sol. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Oh ! Ca empeste la mort ici. ",
        "Il y a un étage composé de plusieurs salles, ",
        "peut être y trouverons-nous des indices sur la localisation du joyau ? ",
    ]
    defilement(trame_entrée_château)

    trame_fouille = [
        "Vous allez au premier étage. ",
        "En entrant dans une bibliothèque : ",
        "Vous trouvez plusieurs étagères remplies de livres et de parchemins. Au centre de la salle, un pupitre et une lettre : ",
        "lettre : Sur ordre du roi et en tant que son valet, j'ai mis en lieu sûr sa couronne",
        "dans un coffre caché sous le trone même ! Qui aurait pu y penser ? :)",
        "la clé se trouve là où il n'y pas souvent grand monde, la...",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Le texte s'arrête là. Il a dû se passer quelque chose au moment où l'auteur écrivait...",
        "",
        "Vous entrez dans la cuisine. ",
        "Rien de plus déprimant qu'une cuisine sans rien à manger...",
        "Pas d'indices. ",
        "",
        "Vous entrez dans la chambre d'ami. ",
        "En vous allongeant sur le lit poussiéreux, quelque chose vous dérange sous le coussin presque entièrement déplumé de l'intérieur : ",
        "En le soulevant, vous voyez une clé étrange. ",
        "Vous avez obtenu : clé de coffre ! ",
    ]
    defilement(trame_fouille) 
    
    trame_combat_final = [
        "*Soudain vous êtes surpris(e) par un cri effrayant. ",
        "*Le château commence à s'écrouler. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "AAAAH ! Qu'est ce que c'est !? ",
        "*Un corps céleste jaillit du sol, explosant la toiture  du château. ",
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "Ca y est, c'est maintenant ! ",
        "BOSS FINAL : Chevalier fantôme",  
        f"{'Salie : ' if ChoixHéros=='1' else 'Magnus : '}",
        "A nous deux, sale monstre !!! ",
    ]
    defilement(trame_combat_final)

#combat final

def trame_finale_apres_boss():
    trame_apres_boss = [
        "L'épée scintille ! ",
        f"Son pouvoir s'infiltre à travers les muscles de {'Salie' if ChoixHéros=='1' else 'Magnus'}. ",
        f"{'Elle' if ChoixHéros=='1' else 'Il'} court et bondit sur les décombres, brandit son épée et effectue un saut magistral d'une quarantaine de mètres. ",
        f"Derrière {'Salie' if ChoixHéros=='1' else 'Magnus'}, le corps du fantôme, inerte, se désintègre",
        f"{'Salie' if ChoixHéros=='1' else 'Magnus'} ouvre le coffre sous le trône du roi, prend le joyau maudit et le détruit.²", 
        "*Les montres perdent leur pouvoir et deviennent innoffensifs,",
        f"Sauvant ainsi la contrée et ses habitants, {'Salie' if ChoixHéros=='1' else 'Magnus'} devient un héros.",
        "",
        "FIN"
        "",
        "                       Réalisé par : Majid, Enzo, Monis"
    ]
    defilement(trame_apres_boss)

Bienvenue = ["Bienvenue dans : The Lost Crown."]
defilement(Bienvenue)
time.sleep(1)
input("Appuyez sur Entrer")
trame_introduction()
time.sleep(1)
input("Appuyez sur Entrer")

ChoisirHéros()

while True:
    #ZONE 1
    time.sleep(1)
    commencement_histoire()    #ici-->rencontre de Garry (chasseurs de monstres)
    time.sleep(1)
    input("Appuyez sur Entrer")
    transition_1er_combat()    # ici-->entraînement terminé/premier combat
    time.sleep(1)
    input("Appuyez sur Entrer")
    main(1, "le Gobelin") #Combat contre le Gobelin
    time.sleep(1)
    input("Appuyez sur Entrer")
    fin_introduction()         #héros quitte le village.

    #ZONE 2
    prairie_niveau_1()           #--> prairie  niveau 1
    input("Appuyez sur Entrer")
    main(2, "Stritominus") #Combat contre le Stritominus
    time.sleep(1)
    input("Appuyez sur Entrer")
    prairie_niveau_2()               #dernier combat prairie/ LVL 2
    time.sleep(1)
    input("Appuyez sur Entrer")
    main(2, "Stritominus 2.0") #Combat contre le 2e Stritominus
    time.sleep(1)
    input("Appuyez sur Entrer")

    #ZONE 3
    foret_partie_1()            #nouvelle zone => foret / personnage passe une nuit dans la foret
    time.sleep(1)
    input("Appuyez sur Entrer")
    foret_partie_2_combat_fin() #intrigue menant au combat vs mordeur  LVL 3
    time.sleep(1)
    input("Appuyez sur Entrer")
    main(3, "le Mordeur") #Combat contre le Mordeur
    réplique_apres_combat_mordeur()
    time.sleep(1)
    input("Appuyez sur Entrer")

    #ZONE 4
    montagne()
    time.sleep(1)
    input("Appuyez sur Entrer")
    main(4, "l'Orc") #Combat contre l'Orc
    time.sleep(1)
    input("Appuyez sur Entrer")
    montagne_fin()          #héros chevauche le loup de l'Orc jusqu'à la zone suivante
    time.sleep(1)
    input("Appuyez sur Entrer")

    #ZONE 5
    Château_abandonné()                           #héros arrive au château et le fouille pour trouver le joyau. Apparition du Chevalier Fantôme (BOSS FINAL)
    time.sleep(1)
    input("Appuyez sur Entrer")
    main(5, "le Chevalier Fantôme") #Combat contre le Chevalier Fantôme
    time.sleep(1)
    input("Appuyez sur Entrer")
    trame_finale_apres_boss()                     #trame de fin après le combat et fin de l'histoire

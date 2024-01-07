import random as rd

inventaire = {"(1) Potions de soin":3, "(2) Potion de régénération":1, "(3) Potion de défense":2, "(4) Potion de rage":2, "(5) Piment":1}
invPotiondeSoin = {"(1) Potion de soin Faible":2, "(2) Potion de soin Moyen":1, "(3) Potion de soin Elevé":0}

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
        print("Vous avez augmenté de niveau ! ")
        self.lvl += 1
        self.EXP = 0
        self.maxHP = int(self.maxHP * 1.10)
        self.HP = self.maxHP
        self.maxDEF = int(self.maxDEF * 1.20)
        self.maxDMG = int(self.maxDMG * 1.25)

    def PassifBlockATK(self):
        if rd.random() < 0.20:
            self.Bloquer = True
        else:
            self.Bloquer = False

#-------------------- Actions --------------------

    def AttaqueBasique(self, target): #Action 1
        if self.nom == "Magnus" or self.nom == "Salie":
            print("Attaque Basique")
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
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.9)
                return target.DégâtsSubis(DamageDealt, crit)


            if choixProjectile == "2": #Boule de feu
                target.FireCondition = True
                target.FireTours = 3
                print("Boule de feu")
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.75)
                print(target.DégâtsSubis(DamageDealt, crit))
                return f"{target.nom} prendra {self.FireDOT} dégâts de feu pendant 3 tours. "

                
            if choixProjectile == "3": #Potion jetable d'acide
                print("Potion jetable d'acide")
                target.AcidCondition = True
                target.AcidTours = 3
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.30)
                print(target.DégâtsSubis(DamageDealt, crit))
                return f"{target.nom} prendra {self.AcidDOT} dégâts d'acide pendant 3 tours. "

                
            if choixProjectile == "4": #Parfum de poison
                target.PoisonCondition = True
                print("Parfum empoisonné")
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
    print("Vous obtenez les consommables suivants : ")
    for i in range(amount):
        ConsommableObtenu = rd.choices(list(inventaire.keys()), weights = [0.20, 0.15, 0.30, 0.25, 0.10])[0]
        inventaire[ConsommableObtenu] += 1
        if not ConsommableObtenu == "(1) Potions de soin":
            print(f"{ConsommableObtenu[4:]}")
        else:
            SoinObtenu = rd.choices(list(invPotiondeSoin.keys()), weights = [0.60, 0.25, 0.15])[0]
            invPotiondeSoin[SoinObtenu] += 1
            print(f"{SoinObtenu[4:]}")
    print()

    print("Votre inventaire : ")
    print()
    for key, value in inventaire.items():
        print(f"{key[4:]} : {value}")
    print()
    if "(1) Potions de soin" in ConsommableObtenu:
        print("Vos potions de soin : ")
        for key, value in invPotiondeSoin.items():
            print(f"{key[4:]} : {value}")
    return ""

#-------------------- Invoc de Monstre --------------------

monstres_zone1 = ['Gobelin', 'Loup'] #Village
monstres_zone2 = ['Gobelin', 'Loup', 'Ogre'] #Plaine
monstres_zone3 = ['Loup-garou', 'Zombie', 'Ogre', 'Ours'] #Forêt
monstres_zone4 = ['Loup blanc', 'Ours', 'Orc'] #Montagne
monstres_zone5 = ['Chevalier déchu'] #Château
monstre_zone = [monstres_zone1, monstres_zone2, monstres_zone3, monstres_zone4, monstres_zone5]

def SummonMonstre(zone, nom = None):
    HP_range = [40 + 20 * (zone - 1), 60 + 20 * (zone - 1)]
    DEF_range = [1 + zone, 3 + zone]
    DMG_range = [10 + 4 * (zone - 1), 14 + 4 * (zone - 1)]
    if nom is not None:
        if nom == "Mimic": #stats du Mimic (stats zone + 1)
            nom = "Mimic"
            HP = rd.randint(40 + 20 * (zone), 60 + 20 * (zone))
            DEF = rd.randint(1 + zone+1, 3 + zone+1)
            DMG = rd.randint(10 + 4 * (zone), 14 + 4 * (zone))
        else: #monstre avec nom donné
            nom = nom
            HP = rd.randint(*HP_range)
            DEF = rd.randint(*DEF_range)
            DMG = rd.randint(*DMG_range)
    else: #monstre nom aleatoire
        nom = rd.choice(monstre_zone[zone-1])
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
            print("C'était un Mimic, vous vous êtes fait avoir ! ")
            print()
            mainCombat(zone, "Mimic")
        else:
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
                continue
            else:
                print("Vous avez lancé(e) votre arme ! ")
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
            continue

def mainCombat(zone, Monstre_nom = None):
    SummonMonstre(zone, Monstre_nom)
    print(f"Vous affrontez {Monstre.nom} ! ")
    print(f"Ses statistiques : PV : {Monstre.HP}, DEF : {Monstre.DEF}, ATK : {Monstre.DMG}, Chance de coup critique : {Monstre.critluck}, Chance : {Monstre.luck}")
    print()
    global Héros
    Tour = 0

    while Héros.estVivant() and Monstre.estVivant():
        Tour += 1
        print("--------------------")
        print(f"Tour : {Tour}")
        print("--------------------")
        print()

        if hasattr(Héros, "RegenCondition") and Héros.RegenCondition:
            print(Héros.Régénération())
        if hasattr(Héros, "DEFCondition") and Héros.DEFCondition:
            print(Héros.AugmentationDEF())
        if hasattr(Héros, "RageCondition") and Héros.RageCondition:
            print(Héros.AugmentationDMG())

        print()
        print(f"{Héros.nom} -> PV : {Héros.HP}/{Héros.maxHP}, DEF : {Héros.DEF}, ATK : {Héros.DMG}")
        print()

        ActionJoueur()
        if Héros.Fuite:
            break
        print()

        if not Monstre.estVivant():
            print(f"{Monstre.nom} est mort, Vous avez gagné ! ")
            Héros.EXP += 25
            print(f"Vous obtenez 25 points d'expérience ({Héros.EXP}/100). ")
            if Héros.EXP == 100:
                print(Héros.LVLUP())
            if Héros.ArmeLancée:
                print("Vous ramassez votre arme. ")
                Héros.ArmeLancée = False
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

        if not Monstre.estVivant():
            print(f"{Monstre.nom} est mort, Vous avez gagné ! ")
            Héros.EXP += 25
            print(f"Vous obtenez 25 points d'expérience ({Héros.EXP}/100). ")
            if Héros.EXP == 100:
                print(Héros.LVLUP())
            if Héros.ArmeLancée:
                print("*Vous ramassez votre arme. ")
                Héros.ArmeLancée = False
            print(Trésor(zone))
            return ""
        
        print("L'ennemi attaque ! ")
        print(Monstre.AttaqueBasique(Héros))
        print()

        if not Héros.estVivant():
            print("Vous êtes mort ! ")
            return False
        
                

while True: #Choix du personnage
    print("Quel personnage voulez-vous choisir ? ")
    print("1 : Salie (PV : 100, DEF : 4, ATK : 10, ChanceCritique : 25, Chance : 75)")
    print("2 : Magnus (PV : 120, DEF : 6, ATK : 8, ChanceCritique : 30, Chance : 60)")
    ChoixHéros = input("Entrez un nombre : ")
    print()

    if ChoixHéros == "1":
        Héros = Personnage("Salie", 100, 4, 10, 0.25, 0.75) #nom, PV, DEF, ATK, %crit, %luck
        print("Vous avez choisi Salie.")
        break
    elif ChoixHéros == "2":
        Héros = Personnage("Magnus", 120, 6, 8, 0.30, 0.60) #nom, PV, DEF, ATK, %crit, %luck
        print("Vous avez choisi Magnus.")
        break
    else:
        print("Veuillez entrer un nombre valide. ")
        print()
        continue
print()

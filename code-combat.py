import random as rd


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
        self.Bloquer = False
        self.Parer = False
        self.Esquive = False
        self.ArmeLancée = False
        self.ChanceParer = 0.40
        self.Fuite = False
        self.FireDOT = int(self.DMG*0.35)
        self.AcidDOT = int(self.DMG*0.70)
        self.PoisonDOT = int(self.DMG*0.25)
        self.inventaire = {"(1) Potions de soin":3, "(2) Potion de régénération":1, "(3) Potion de défense":2, "(4) Potion de rage":2, "(5) Piment":1}
        self.invPotiondeSoin = {"(1) Soin Faible":2, "(2) Soin Moyen":1, "(3) Soin Elevé":0}

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
                target.DégâtsSubis(DamageDealt, crit)
                return ""


            if choixProjectile == "2": #Boule de feu
                target.FireCondition = True
                target.FireTours = 3
                print("Boule de feu")
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.75)
                target.DégâtsSubis(DamageDealt, crit)
                print(f"{MonstreCombat.nom} prendra {self.FireDOT} dégâts de feu pendant 3 tours. ")
                return ""

                
            if choixProjectile == "3": #Potion jetable d'acide
                print("Potion jetable d'acide")
                target.AcidCondition = True
                target.AcidTours = 3
                DamageDealt, crit = Critique(self.critluck, self.DMG)
                DamageDealt = int(DamageDealt*0.30)
                target.DégâtsSubis(DamageDealt, crit)
                print(f"{MonstreCombat.nom} prendra {self.AcidDOT} dégâts d'acide pendant 3 tours. ")
                return ""

                
            if choixProjectile == "4": #Parfum de poison
                target.PoisonCondition = True
                target.PoisonTours = 999
                print("Parfum empoisonné")
                print(f"{MonstreCombat.nom} recevra {self.PoisonDOT} à chaque tour.")
                return ""
            
            else:
                print("Veuillez entrer un nombre valide.")
                continue


    def ParerUneAttaque(self): #Magnus Action 2
        if rd.random() < self.ChanceParer: #0.4
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


    def UtiliserConsommable(self, Héros): #Action 3 / 4
        while True:
            print("Quel consommable utiliser ? ")
            for key,value in self.inventaire.items():
                print(f"{key} : {value}")
            choixConsommable = input("Votre choix : ")
            print("--------------------")

            if choixConsommable == "1":
                if self.inventaire["(1) Potions de soin"] == 0: #Soin
                    print("Vous n'avez plus de potion de soin ! ")
                    continue
                while True:
                    print("Quelle taille de potion de soin ? ")
                    for key,value in self.invPotiondeSoin.items():
                        print(f"{key} : {value}")
                    choixPotionDeSoin = input("Choisissez une taille de soin : ")
                    print("--------------------")

                    if choixPotionDeSoin == "1":
                        if self.invPotiondeSoin["(1) Soin Faible"] != 0:
                            self.HP = int(self.HP + (Héros.HP*0.20))
                            if self.HP > Héros.HP:
                                self.HP = Héros.HP
                            self.invPotiondeSoin["(1) Soin Faible"] -= 1
                            self.inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(Héros.HP*0.20)}. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin faible ! ")
                            continue

                    if choixPotionDeSoin == "2":
                        if self.invPotiondeSoin["(2) Soin Moyen"] != 0:
                            self.HP = int(self.HP + (Héros.HP*0.45))
                            if self.HP > Héros.HP:
                                self.HP = Héros.HP
                            self.invPotiondeSoin["(2) Soin Moyen"] -= 1
                            self.inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(Héros.HP*0.45)}. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin moyenne ! ")
                            continue

                    if choixPotionDeSoin == "3":
                        if self.invPotiondeSoin["(3) Soin Elevé"] != 0:
                            self.HP = int(self.HP + (Héros.HP*0.60))
                            if self.HP > Héros.HP:
                                self.HP = Héros.HP
                            self.invPotiondeSoin["(3) Soin Elevé"] -= 1
                            self.inventaire["(1) Potions de soin"] -= 1
                            return f"Vous vous soignez de {int(Héros.HP*0.60)}. Votre vie : {self.HP}"
                        else:
                            print("Vous n'avez plus de potion de soin élevée ! ")
                            continue

                    else:
                        print("Veuillez entrer un nombre valide.")
                        continue

            if choixConsommable == "2": #Regen
                if self.inventaire["(2) Potion de régénération"] != 0:
                    self.RegenCondition = True
                    self.RegenTours = 5
                    self.inventaire["(2) Potion de régénération"] -= 1
                    return f"Vous vous soignerez de {int(Héros.HP*0.2)} pendant 5 tours. Votre vie : {self.HP}."
                else:
                    print("Vous n'avez plus de potion de régénération ! ")
                    continue

            if choixConsommable == "3": #DEFUp
                if self.inventaire["(3) Potion de défense"] != 0:
                    self.DEFCondition = True
                    self.DEFTours = 5                
                    self.DEF = int(Héros.DEF*1.35)
                    self.inventaire["(3) Potion de défense"] -= 1
                    return f"Vous augmentez votre défense de 35% pendant 5 tours. Votre défense : {self.DEF}"
                else:
                    print("Vous n'avez plus de potion de défense ! ")
                    continue

            if choixConsommable == "4": #DMGUp
                if self.inventaire["(4) Potion de rage"] != 0:
                    self.RageCondition = True
                    self.RageTours = 5
                    if self.ArmeLancée == True:
                        self.DMG = int((Héros.DMG/2)*1.35)
                    else:
                        self.DMG = int(Héros.DMG*1.35)
                    self.inventaire["(4) Potion de rage"] -= 1
                    return f"Vous êtes enragé(e) ! Vos attaques infligeront 35% de dégats supplémentaires pendant 5 tours. Vos dégâts : {self.DMG}."
                else:
                    print("Vous n'avez plus de potion de rage ! ")
                    continue
            
            if choixConsommable == "5": #Esquive
                if self.inventaire["(5) Piment"] != 0:
                    self.EsquiveCondition = True
                    self.EsquiveTours = 5
                    self.inventaire["(5) Piment"] -= 1
                    return f"Vous avez {int(self.luck*100)}% de chance d'esquiver l'attaque ennemie pendant 5 tours. "
                else:
                    print("Vous n'avez plus de piment ! ")
                    continue
            
            else:
                print("Veuillez entrer un nombre valide.")
                continue


    def TentativeFuite(self):
        ChanceFuite = self.luck/2
        if rd.random() < ChanceFuite: #Salie : 0.75/2, Magnus : 0.6/2
            self.Fuite = True
            return "Vous avez réussi à vous enfuir ! "
        else:
            return "Vous ne parvenez pas à vous enfuir. "


    def Régénération(self, Héros):
        self.HP += int(Héros.HP*0.2)
        if self.HP > Héros.HP:
            self.HP = Héros.HP
        print(f"Vous vous soignez de {int(Héros.HP*0.2)} points de vie. Votre vie : {self.HP}")
        self.RegenTours -= 1
        if self.RegenTours == 0:
            self.RegenCondition = False
            print("La régénération prend fin. ")

    def AugmentationDEF(self, Héros):
        self.DEFTours -= 1
        print(f"Il vous reste {self.DEFTours} tours de défense augmentée. ")
        if self.DEFTours == 0:
            self.DEFCondition = False
            self.DEF = Héros.DEF
            print("Votre défense revient à la normale.")

    def AugmentationDMG(self, Héros):
        self.RageTours -= 1
        print(f"Il vous reste {self.DEFTours} tours de rage. ")
        if self.RageTours == 0:
            self.RageCondition = False
            if self.ArmeLancée:
                self.DMG = int(Héros.DMG / 2)
            else:
                self.DMG = Héros.DMG
            print("Vos dégâts reviennent à la normale. ")

    def Esquiver(self):
        self.EsquiveTours -= 1
        if self.EsquiveTours == 0:
            self.EsquiveCondition = False
            print("Vous ne pouvez plus esquiver. ")
        if rd.random() < self.luck: #Salie : 75%, Magnus : 60%
            return True
        else:
            return False


    def Enflammé(target, self):
        target.HP = int(target.HP - self.FireDOT)
        target.FireTours -= 1
        if target.FireTours == 0:
            target.FireCondition = False

    def Acidifié(target, self):
        target.HP = int(target.HP - self.AcidDOT)
        target.AcidTours -= 1
        if target.AcidTours == 0:
            target.AcidCondition = False
            
    def Empoisonné(target, self):
        target.HP = int(target.HP - self.PoisonDOT)
        target.PoisonTours -= 1
        if target.PoisonTours == 0:
            target.PoisonCondition = False


    def DégâtsSubis(self, DamageDealt, crit):
        if self.nom != 'Salie' and self.nom != 'Magnus':
            self.PassifBlockATK()
            if self.Bloquer:
                return "Attaque bloquée ! "
            
        if self.nom == 'Magnus':
            if hasattr(self, "ParerCondition") and self.ParerCondition:
                self.ParerUneAttaque()
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
    global MonstreCombat
    Monstre = Personnage(
        rd.choice(monstre_zone[zone-1]),                        #nom
        rd.randint(40 + (20 * zone-1), 60 + (20 * zone-1)),     #HP
        rd.randint(1 + (zone-1), 3 + (zone-1)),                 #DEF
        rd.randint(10 + (4 * zone-1), 14 + (4 * zone-1)),       #DMG
        0.20 + (0.05 * (zone-1)),                               #critluck
        0.40, 0, zone)                                          #luck, EXP, lvl
    MonstreCombat = Monstre

    
def mainCombat():
    global HérosCombat
    Tour = 1
    print(f"Tour : {Tour}")
    print("--------------------")

    while HérosCombat.estVivant() and MonstreCombat.estVivant():
        if hasattr(HérosCombat, "RegenCondition") and HérosCombat.RegenCondition:
            print(HérosCombat.Régénération(Héros))
        if hasattr(HérosCombat, "DEFCondition") and HérosCombat.DEFCondition:
            print(HérosCombat.AugmentationDEF(Héros))
        if hasattr(HérosCombat, "RageCondition") and HérosCombat.RageCondition:
            print(HérosCombat.AugmentationDMG(Héros))

        print(f"La vie de {HérosCombat.nom} : {HérosCombat.HP}")
        print("--------------------")

        if ChoixHéros == "1":
            print("Quelle action ? Entrez un nombre : ")
            print("1 : Attaque basique")
            print("2 : Lancer un objet")
            print("3 : Utiliser un consommable")
            print("4 : Tentative de fuite")
        if ChoixHéros == "2":
            print("Choisissez votre action : ")
            print("1 : Attaque basique")
            print("2 : Chance de parer (3 attaques)")
            print("3 : Lancer votre arme (2x dégâts, mais vous infligez ensuite dégâts / 2)")
            print("4 : Utiliser un consommable")
            print("5 : Tentative de fuite")
        
        choix = input("Votre action : ")

        if choix == "1": #Attaque basique
            print(HérosCombat.AttaqueBasique(MonstreCombat))

        elif choix == "2" and ChoixHéros == "1": #Lancer un projectile (Salie)
            print(HérosCombat.LancerProjectile(MonstreCombat))

        elif choix == "2" and ChoixHéros == "2": #Parer (Magnus)
            HérosCombat.ParerCondition = True
            HérosCombat.ParerTours = 3
            print("Vous avez 40% de chance de parer les trois prochaines attaques. ")

        elif choix == "3" and ChoixHéros == "2": #Lancer l'arme (Magnus)
            if HérosCombat.ArmeLancée:
                print("Vous avez déjà lancé votre arme ! ")
                continue
            else:
                print("Vous avez lancé(e) votre arme ! ")
                print(HérosCombat.LancerArme(MonstreCombat))

        elif (choix == "3" and ChoixHéros == "1") or (choix == "4" and ChoixHéros == "2"): #Utiliser un consommable
            print(HérosCombat.UtiliserConsommable(Héros))

        elif (choix == "4" and ChoixHéros == "1") or (choix == "5" and ChoixHéros == "2"): #Fuire
            print(HérosCombat.TentativeFuite())
            if Héros.Fuite:
                return ""
        else:
            print("Veuillez entrer un nombre valide.")
            print("--------------------")
            continue

        print("--------------------")

        if hasattr(MonstreCombat, "FireCondition") and MonstreCombat.FireCondition:
            MonstreCombat.Enflammé(HérosCombat)
            print(f"{MonstreCombat.nom} prend {HérosCombat.FireDOT} dégâts de feu. ")
        if hasattr(MonstreCombat, "AcidCondition") and MonstreCombat.AcidCondition:
            MonstreCombat.Acidifié(HérosCombat)
            print(f"{MonstreCombat.nom} prend {HérosCombat.AcidDOT} dégâts d'acide. ")
        if hasattr(MonstreCombat, "PoisonCondition") and MonstreCombat.PoisonCondition:
            MonstreCombat.Empoisonné(HérosCombat)
            print(f"{MonstreCombat.nom} prend {HérosCombat.PoisonDOT} dégâts de poison. ")

        print(f"La vie de {MonstreCombat.nom} : {MonstreCombat.HP}/{Monstre.HP}")
        print("--------------------")

        if not MonstreCombat.estVivant():
            print(f"{MonstreCombat.nom} est mort ! Vous avez gagné ! ")
            break
        
        print("L'ennemi attaque ! ")
        print(MonstreCombat.AttaqueBasique(Héros))
        print("--------------------")

        if not HérosCombat.estVivant():
            print("Vous êtes mort ! ")
            break
        
        Tour += 1
        print(f"Tour : {Tour}")
        print("--------------------")


while True:
    print("Quel personnage voulez-vous choisir ? ")
    print("1 : Salie (PV : 100, DEF : 4, ATK : 10, ChanceCritique : 25, Chance : 75)")
    print("2 : Magnus (PV : 120, DEF : 6, ATK : 8, ChanceCritique : 30, Chance : 60)")
    ChoixHéros = input("Entrez un nombre : ")

    if ChoixHéros == "1":
        Héros = Personnage("Salie", 100, 4, 10, 0.25, 0.75) #nom, PV, DEF, ATK, %crit, %luck
        print("Vous avez choisi Salie.")
        HérosCombat = Héros
        break
    elif ChoixHéros == "2":
        Héros = Personnage("Magnus", 120, 6, 8, 0.30, 0.60) #nom, PV, DEF, ATK, %crit, %luck
        print("Vous avez choisi Magnus.")
        HérosCombat = Héros
        break
    else:
        print("Veuillez entrer un nombre valide. ")
        print("--------------------")
        continue

print("--------------------")

SummonMonstre(1)
print(f"Vous affrontez {MonstreCombat.nom} ! ")
print(f"Ses statistiques : PV : {MonstreCombat.HP}, DEF : {MonstreCombat.DEF}, ATK : {MonstreCombat.DMG}, Chance de critiques : {MonstreCombat.critluck}, Chance : {MonstreCombat.luck}")
print("--------------------")

mainCombat()

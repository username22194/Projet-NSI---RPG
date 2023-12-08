# Projet-NSI---RPG
Notre jeu :

Deux personnages : 
   Salie  : HP : 100   DEF : 05   DMG : 12   critluck : 0.25   luck : 0.75   EXP : 0   LVL : 1
   Magnus : HP : 150   DEF : 10   DMG : 10   critluck : 0.30   luck : 0.60   EXP : 0   LVL : 1
Une histoire : Personnage venant de Ravensbrook (village), part à l'aventure. Il commence de son village (lvl0), va dans une plaine (lvl1-2), puis s'enfonce dans la forêt (lvl2-3), avant de gravire une montagne(3-4), dans laquelle il trouve un château abandonné(5-6). Dans chaque zone, il combat un monstre, de niveau différent.
Des événements : des combats
  -> Coups critiques
	-> Les attaques :
		- Attaquer
		- Magnus :
  			Parer
     			Jeter son épée (DMGx2) Mais il perd son arme :
			   DMG = DMG/2
      			   La compétence innée n'est plus utilisable pour le combat.
		- Salie :
  			Lancer un objet:
  			   Tonneau Explosif
     			   Boule de Feu (Type : Feu, Debuff : Fire)
	   		   Potion jetable d'acide (Type : Acide, Debuff : Fire)
			   Potion jetable de Poison (Type : Poison, Debuff : Poison)
		- Utiliser un Consommable :
 				- Potions de Soin (Grande, Moyenne, Petite)
	  			- Potions de Régénération
	  			- Antidote d'effets d'altérations
      				- Poudre de Camouflage (invisible, devient visible à la prochaine attaque, avec 100%CRIT)
	  			- Piment (bonus d'agilité = 25%luck esquiver l'attaque, dure 3 tours)
    				- Potion de Téléportation (1 seul dans le jeu, obtenu au début)
		- Fuire : 25% succès (L'EXP n'est pas obtenu, on va directement à la zone suivante).
	Lors d'une victoire d'un combat, un trésor apparaît :
		-> des récompenses (3 possibilités aléatoires):
			- rd.randint stats d'une arme (Élevé / Moyen / Faible)
   			- rd.randint qté de Consommables:
      				- Potions de Soin (Grande, Moyenne, Petite)
	  			- Potions de Régénération
	  			- Antidote d'effets d'altérations
      				- Poudre de Camouflage
	  			- Piment (bonus d'agilité = 25%luck esquiver l'attaque, dure 3 tours)
			- 10%luck = Mimic :
			   Attaque élevée (+50%)
        		   Il attaque en premier
		    Drop un rd.randint Consommable / Arme avec stats élevées
		-> +100EXP/100EXP -> LVLup HP/DEF/DMG +15%
	Lors d'une défaite : Mort / Recommencer le jeu.
Compétences innées :
	LVL 3 - Magnus -> Berserk : les trois prochaines attaques ont 100% de CRIT.
 	LVL 3 - Salie -> Fureur : lance trois projectiles choisis.
  	LVL 2 -> Adrénaline lorsque HP < 20%, le personnage fait + 50% DMG
Monstres :
	lvl 0 : HP : (40-60)     DEF : (1-3)     DMG : (10-14)   critluck : 0.20   luck : 0.40   EXP : 0   LVL : 0
 	lvl 1 : HP : (61-85)     DEF : (2-5)     DMG : (14-18)   critluck : 0.25   luck : 0.40   EXP : 0   LVL : 1
   	lvl 2 : HP : (86-115)    DEF : (4-8)     DMG : (18-22)   critluck : 0.30   luck : 0.40   EXP : 0   LVL : 2
 	lvl 3 : HP : (116-150)   DEF : (7-13)    DMG : (22-26)   critluck : 0.35   luck : 0.40   EXP : 0   LVL : 3
 	lvl 4 : HP : (151-195)   DEF : (12-18)   DMG : (26-30)   critluck : 0.40   luck : 0.40   EXP : 0   LVL : 4
 	lvl 5 : HP : (196-245)   DEF : (17-24)   DMG : (30-34)   critluck : 0.45   luck : 0.40   EXP : 0   LVL : 5
 	lvl 6 : HP : (246-300)   DEF : (23-31)   DMG : (34-38)   critluck : 0.50   luck : 0.40   EXP : 0   LVL : 6
  	25%luck Parer Attaque basique.

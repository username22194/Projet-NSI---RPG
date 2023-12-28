# Projet-NSI_RPG
Notre jeu :

Deux personnages : 
   Salie  : HP : 100   DEF : 05   DMG : 12   critluck : 0.25   luck : 0.75   EXP : 0   LVL : 1
   Magnus : HP : 150   DEF : 10   DMG : 10   critluck : 0.30   luck : 0.60   EXP : 0   LVL : 1

Une histoire : Personnage venant de Ravensbrook (village), part à l'aventure. Il commence de son village, va dans une plaine, puis s'enfonce dans la forêt, avant de gravire une montagne, dans laquelle il trouve un château abandonné. Dans chaque zone trouve des monstres de niveau plus élevés selon la zone.

Des combats
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
	   		   Potion jetable d'acide (Debuff : Acide)
			   Parfum de Poison (Debuff : Poison)
		- Utiliser un Consommable :
 				- Potion de Soin (Grande, Moyenne, Petite)
	  			- Potion de Régénération
	  			- Potion de Défense
				- Potion de Rage
	  			- Piment (bonus d'agilité = 25%luck esquiver l'attaque, dure 3 tours)
		- Fuire : 25% succès (L'EXP n'est pas obtenu, on va directement à la zone suivante).

Lors d'une victoire de combat, un trésor apparaît :
	-> des récompenses:
		- rd.randint(1, 3) qté de Consommables:
			- Potions de Soin (Grande, Moyenne, Petite)
			- Potions de Régénération
			- Antidote d'effets d'altérations
			- Poudre de Camouflage
			- Piment (bonus d'agilité = 25%luck esquiver l'attaque, dure 3 tours)
		- +25EXP/100EXP
		- 25%luck = Mimic :
		   Attaque élevée (+50%)
		   Il attaque en premier
	    	   Drop un rd.randint(4, 6) de Consommables
		   -> +50EXP/100EXP

Lors d'une défaite : Mort / Recommencer le jeu.

Compétences innées :
	LVL 3 - Magnus -> Berserk : les trois prochaines attaques ont 100% de CRIT (1 par combat).
 	LVL 3 - Salie -> Fureur : lance trois projectiles choisis (5 tours).
  	LVL 2 - Adrénaline : lorsque HP < 20%, le personnage fait + 50% DMG (passif).

Monstres :
	lvl 1 : HP : (40-60)     DEF : (1-3)     DMG : (10-14)   critluck : 0.20   luck : 0.40   EXP : 0   LVL : 0
 	lvl 2 : HP : (61-85)     DEF : (2-5)     DMG : (14-18)   critluck : 0.25   luck : 0.40   EXP : 0   LVL : 1
   	lvl 3 : HP : (86-115)    DEF : (4-8)     DMG : (18-22)   critluck : 0.30   luck : 0.40   EXP : 0   LVL : 2
 	lvl 4 : HP : (116-150)   DEF : (7-13)    DMG : (22-26)   critluck : 0.35   luck : 0.40   EXP : 0   LVL : 3
 	lvl 5 : HP : (151-195)   DEF : (12-18)   DMG : (26-30)   critluck : 0.40   luck : 0.40   EXP : 0   LVL : 4
  	25%luck Parer Attaque basique.

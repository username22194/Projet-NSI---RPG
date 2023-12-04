# Projet-NSI---RPG
Notre jeu :

Deux personnages : Salie / Magnus
Une histoire
Des événements : des combats
  -> coups critiques
	-> les attaques :
		- Attaquer
		- Magnus :
  			Parer
     			Jeter son épée (DMGx2) Mais il perd son arme :
			   DMG = DMG/2
      			   La compétence innée n'est plus utilisable pour le combat.
		- Salie :
  			Lancer un objet:
  			   Proj explosif
     			   Proj inflammable (Debuff : Fire)
			   Potion jetable de Poison (Debuff : Poison)
		- Utiliser un Consommable (soin, défense, attaque)
		- Fuire
	Lors d'une victoire d'un combat, un trésor apparaît :
		-> 3 choix de récompenses (on ne les connaît pas à l'avance):
			- rd.randint stats d'une arme
			- rd.randint statsUP
			- 10%luck = Mimic -> combat désavantagé
			   Attaque élevée (+50%)
        		   Il attaque en premier
		    Drop un rd.randint Consommable / Arme avec stats élevées
		-> +100EXP/100EXP -> LVLup HP/DEF/DMG +15%
	Lors d'une défaite : Mort / recommencer au dernier Point de Sauvegarde.
Compétences innées :
	LVL 3 - Magnus -> Berserk : les trois prochaines attaques ont 100% de CRIT.
 	LVL 3 - Salie -> Fureur : lance trois projectiles choisis.

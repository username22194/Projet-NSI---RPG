import random as rd

statsSalie = {'HP':100,'DEF':5,'DMG':12,'critluck':0.25,'luck':0.75,'EXP':0,'LVL':1}
statsMagnus = {'HP':150,'DEF':10,'DMG':10,'critluck':0.30,'luck':0.6,'EXP':0,'LVL':1}

def Critique(critluck, dmg): # L'attaque est-elle un coup critique / les dégâts ?
    critdmg = rd.random() + 1
    if rd.random() < stats[critluck]:
        dmg = int(dmg*critdmg)
        return "Dégâts : " + str(dmg) + " Vous avez fait un coup critique ! " + "Multiplicateur : " + str(critdmg)
    else:
        return "Dégâts : " + str(dmg)
    
ChoixHéros = int(input('Quel personnage (Salie = 1, Marcus = 2) ? '))
print(ChoixHéros)
assert ChoixHéros == 1 or ChoixHéros == 2, "Veuillez entrer 1 ou 2 pour choisir votre personnage."
if ChoixHéros == 1:
    stats = statsSalie
    print("Vous avez choisi Salie.")
if ChoixHéros == 2:
    stats = statsMagnus
    print("Vous avez choisi Marcus")

print(Critique('critluck', stats['DMG']))
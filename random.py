import time

TEXTE = "wefmsferngmerf,sdf"
Texte = "fdsfregrege"
liste1 = [TEXTE, Texte]
for element in liste1: #TEXTE, Texte
    for character in element: #wefmsferngmerf,sdf
        print(character, end = "", flush = True)
        time.sleep(0.01)
    print()
print("fin")

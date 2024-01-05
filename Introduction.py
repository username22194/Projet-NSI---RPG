import time

Introduction = [
    "L'histoire prend place au 9e siècle après J.C.. ", 
    "Une rumeur court dans le village de Ravensbrook en Norvège : ", 
    "un roi puissant aurait régné sur la contrée il y 200 ans. ", 
    "Un joyau d'une valeur inestimable aurait été découvert dans la montagne du nord : ", 
    "une montagne où résident de nombreuses créatures terrifiantes. ", 
    "Ce roi aurait donc trouvé ce joyau et l'aurait mis sur sa couronne. ", 
    "Seulement, les monstres de la montagne sont puissants. ", 
    "Son royaume fût assiégé par ces créatures, le poussant à l'exil. ", 
    "Le roi serait parti à la hâte, faisant tomber son joyau dans la forêt de la Montagne Enchantée. "
    ] #9 objets
for phrase in Introduction:
    print(phrase)
    time.sleep(2) #attente de 2 secondes avant la prochaine ligne

ChoixHéros = input()
def Intro2():
    print("*Le héros se réveille un matin. *")
    print()
    if ChoixHéros==1:
        print("SALIE : part en quête d'ingrédients préparer une potion revitalisante pour un client lorqu'elle tente d'attraper un guérit-tout au pied d'un arbre.")
        print("Un rayon de soleil surgit et attire son attention. Elle se retourne et voit devant elle au loin la Montagne Enchantée. Elle repense au joyau:")
        print("Ce joyau doit bien exister. Là quelque part la haut. ")
        print("Ce ne sont pas quelques grizzlis ou quelques reptiles de 3 mètres de long qui vont me manger...")
        print("J'ai déjà combattu pour notre village. Et d'ailleurs j'en suis la meilleure. ")
        print()
        print("Je suis décidée, je pars demain. ")
        print("Ainsi Salie rassemble ses affaires et son équipement. Le soir même, elle se rendit chez Garry, le vieux sage du village.")
        print("Il est l'un des descendants du fondateur du village nommé Raymond ERIKSON.")
        print("Un homme fort et intelligent, aux capacités de survie toutes aussi impréssionnantes que ses capacités de combat. ")
    elif ChoixHéros==2:
        print("MAGNUS : part couper du bois dans la forêt avoisinnante afin de remplir son stock de buches pour sa cheminée.")
        print("Après s'être aventuré au coeur de celle-ci, un rugissement lointaint attire son attention.") 
        print("Il lève les yeux et voit devant lui au loin, la _montagne enchantée_ ")
        print("Il repense au joyau:") 
        print("Ce caillou doit bien exister. Là! quelque part la haut!")
        print("Je suis certain que la moitié des bêtes de la montagne ne peuvent pas rivaliser pas contre moi !")
        print("au loin: ")
        print("Rooooaaaaaaarrr !...")
        print("Magnus: 'AAH ! C'était quoi ça !? ")
        print("Ce n'était pas un ours. Mais alors, qu'est ce que ça peut bien être ? ")
        print("Si je veux en savoir plus, je sais ce qu'il me reste à faire...")
        print()
        print("J'ai déjà combattu pour notre village. Mes capacités aux combats m'ont sauvés, moi ainsi que ma division. ")

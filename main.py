from Dictionnaire import Dic
import sys

print("=======================Gestion de stock=======================")
while(1):
    print()
    print ("|            Menu             ")
    print ("|   1 ==> Ajouter un article.  ")
    print ("|   2 ==> Retirer un article.  ")
    print ("|   3 ==> Afficher le stock.   ")
    print ("|   4 ==> Quitter le programme.")
    print ("|")
    choix = input("|  Saisir votre choix : ");
    if (choix == "1"):
        name = input("|\n|  Nom d'article : ")
        qunt = input("|\n|  Quantite d'article : ")
        prix = input("|\n|  Prix d'article : ")
        art = Dic(name, qunt, prix)
        Dic.ajouterArticle(art)
        print ("|\n|  Larticle est ajouter!!")
    
    if (choix == "2"):
        name = input("|\n|  Nom d'article : ")
        Dic.supprimerArticle(name)
        print ("|\n|  Larticle est supprimer!!")
    
    if (choix == "3"):
        print()
        Dic.afficherArticles()

    if (choix == "4"):
        print ("\n  ***Mercii Aurevoire!!!***\n\n")
        sys.exit()
    

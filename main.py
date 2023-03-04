from Dictionnaire import Dic

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
        Dic.ajouterArticle(Dic(name, qunt, prix))
        print ("|\n|  Larticle est ajouter!!")
    
    if (choix == "2"):
        name = input("|\n|  Nom d'article : ")
        Dic.supprimerArticle(name)
        print ("|\n|  Larticle est supprimer!!")
    
    if (choix == "3"):
        print()
        Dic.afficherArticles()
    

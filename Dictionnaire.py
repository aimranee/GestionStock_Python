class Dic:
    def __init__(self, nom, quantite, prix_unitaire):
        self.nom = nom
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    list = []

    def ajouterArticle(Dic c):
        list.append(c)

    def supprimerArticle(nom):
        list.remove(nom)

    def afficherArticles():
        for art in list:
            print(f"|   *{art.nom} : Quantite : {art.quantite} Prix : {art.prix_unitaire}\n")
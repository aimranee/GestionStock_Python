list = []
class Dic:

    def __init__(self, nom, quantite, prix_unitaire):
        self.nom = nom
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    
    def ajouterArticle(self):
        list.append(self)

    def supprimerArticle(nom):
        for art in list:
            if art.nom == nom:
                list.remove(art)

    def afficherArticles():
        if len(list) == 0:
            print("   ==> The list is empty.")
        else:
            for art in list:
                print(f"   ==> Nom : {art.nom}; Quantite : {art.quantite}; Prix : {art.prix_unitaire}")
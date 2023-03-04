class Dic:
    def __init__(self, nom, quantite, prix_unitaire):
        self.nom = nom
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
    
    def afficher(self):
        print(f"Produit : {self.nom} {self.quantite} {self.prix_unitaire}")
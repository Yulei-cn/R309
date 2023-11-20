class Article:
    # Constante pour la TVA
    TVA = 0.20  # 20% de TVA (vous pouvez ajuster cette valeur si nécessaire)

    def __init__(self, nom, code_barre, prix_ht):
        if prix_ht <= 0:
            raise ValueError("Le prix hors taxe doit être supérieur à zéro.")
        self.nom = nom
        self.code_barre = code_barre
        self.prix_ht = prix_ht

    def get_nom(self):
        return self.nom

    def get_code_barre(self):
        return self.code_barre

    def get_prix_ht(self):
        return self.prix_ht

    def set_prix_ht(self, nouveau_prix_ht):
        if nouveau_prix_ht <= 0:
            raise ValueError("Le nouveau prix hors taxe doit être supérieur à zéro.")
        self.prix_ht = nouveau_prix_ht

    def prix_ttc(self):
        prix_ttc = self.prix_ht * (1 + self.TVA)
        return prix_ttc

class Stock:
    def __init__(self):
        self.stock = {}

    def taille(self):
        return len(self.stock)

    def ajout(self, article):
        if article.get_code_barre() in self.stock:
            raise ValueError("Un article avec le même code-barre existe déjà dans le stock.")
        self.stock[article.get_code_barre()] = article

    def recherche_par_code_barre(self, code_barre):
        if code_barre not in self.stock:
            raise ValueError("L'article avec le code-barre spécifié n'est pas en stock.")
        return self.stock[code_barre]

    def recherche_par_nom(self, nom):
        for article in self.stock.values():
            if article.get_nom() == nom:
                return article
        raise ValueError("Aucun article avec le nom spécifié n'est en stock.")

    def supprime_par_code_barre(self, code_barre):
        if code_barre not in self.stock:
            raise ValueError("L'article avec le code-barre spécifié n'est pas en stock.")
        del self.stock[code_barre]

    def supprime_par_nom(self, nom):
        article_a_supprimer = None
        for code_barre, article in self.stock.items():
            if article.get_nom() == nom:
                article_a_supprimer = code_barre
                break
        if article_a_supprimer is not None:
            del self.stock[article_a_supprimer]
        else:
            raise ValueError("Aucun article avec le nom spécifié n'est en stock.")

    def lecture_csv(self, fichier_csv):
        try:
            with open(fichier_csv, 'r') as file:
                for line in file:
                    nom, code_barre, prix_ht = line.strip().split(';')
                    prix_ht = float(prix_ht)
                    article = Article(nom, code_barre, prix_ht)
                    self.ajout(article)
        except FileNotFoundError:
            raise ValueError(f"Le fichier '{fichier_csv}' n'a pas été trouvé.")

    def sauvegarde_csv(self, fichier_csv):
        with open(fichier_csv, 'w') as file:
            for article in self.stock.values():
                line = f"{article.get_nom()};{article.get_code_barre()};{article.get_prix_ht()}\n"
                file.write(line)



# Exemple d'utilisation de la classe Article
article1 = Article("Ordinateur", "123456", 800.0)
print(f"Nom de l'article : {article1.get_nom()}")
print(f"Code-barre : {article1.get_code_barre()}")
print(f"Prix hors taxe : {article1.get_prix_ht()} euros")
print(f"Prix TTC : {article1.prix_ttc()} euros")

# Demander à l'utilisateur de modifier un attribut
choix = input("Que voulez-vous modifier (nom, code-barre, prix) ? ")
if choix == "nom":
    nouveau_nom = input("Entrez le nouveau nom : ")
    article1.set_nom(nouveau_nom)
elif choix == "code-barre":
    nouveau_code_barre = input("Entrez le nouveau code-barre : ")
    article1.set_code_barre(nouveau_code_barre)
elif choix == "prix":
    nouveau_prix_ht = float(input("Entrez le nouveau prix hors taxe : "))
    article1.set_prix_ht(nouveau_prix_ht)

# Afficher les nouveaux détails de l'article
print(f"Nouveau nom de l'article : {article1.get_nom()}")
print(f"Nouveau code-barre : {article1.get_code_barre()}")
print(f"Nouveau prix hors taxe : {article1.get_prix_ht()} euros")
print(f"Nouveau prix TTC : {article1.prix_ttc()} euros")


# Exemple d'utilisation
stock = Stock()
article1 = Article("Article 1", "123456", 10.0)
article2 = Article("Article 2", "789012", 20.0)
stock.ajout(article1)
stock.ajout(article2)

print(f"Taille du stock : {stock.taille()}")
print(f"Recherche par code-barre : {stock.recherche_par_code_barre('123456').get_nom()}")
print(f"Recherche par nom : {stock.recherche_par_nom('Article 2').get_code_barre()}")
stock.sauvegarde_csv("stock.csv")

# Pour lire à partir d'un fichier CSV
nouveau_stock = Stock()
nouveau_stock.lecture_csv("stock.csv")
print(f"Taille du nouveau stock : {nouveau_stock.taille()}")
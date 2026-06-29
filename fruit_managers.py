import json


def ouvrir_prix(path="data/prix.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
    return prix


def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ouvrir_tresorerie(path="data/tresorerie.txt"):
    with open(path, "r", encoding="utf-8") as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def affichier_tresorerie(tresorerie):
    print(f"\n Tresorerie actuelle: {tresorerie:.2f} $")


# creer une fonction pour afficher
def affichier_inventaire(inventaire):
    print("inventaire actuel de la plantation :")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()}: {quantite} unites")


# creer une fonction recolter
def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"\n recolte {quantite} {fruit} supplementaires!")


# creer une fonction pour vendre les fruits
def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        # tresorerie += 1 * quantite
        tresorerie += prix.get(fruit, 0) * quantite
        print(f"\n vendu {quantite} {fruit} !")
        return (inventaire, tresorerie)
    else:
        print(f"pas assez de {fruit} pour vendre {quantite} unites")


def ventre_tout(inventaire, tresorerie, prix):
    print("\n vente de tout l'inventaire: ")
    for fruit, quantite in list(inventaire.items()):
        if quantite > 0:
            revenu = fruit.get(fruit, 0) * quantite
            tresorerie += revenu
            print(
                f"-{fruit.capitalize()}: vendu {quantite} unites pour {revenu: .2f} $"
            )
            inventaire[fruit] = 0
    return inventaire, tresorerie


def valeur_stock(inventaire, prix):
    valeur = {}
    for fruit in inventaire:
        quantite = inventaire[fruit]
        prix_unitaire = prix.get(fruit, 0)
        valeur[fruit] = quantite * prix_unitaire
    return valeur


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    affichier_inventaire(inventaire)
    affichier_tresorerie(tresorerie)
    recolter(inventaire, "bananes", 10)
    inventaire, tresorerie = vendre(inventaire, "bananes", 5, tresorerie, prix)

    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)

import json
import os
import datetime


def ouvrir_prix(path="data/prix.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        prix = json.load(fichier)
    return prix


DATA_DIR = "data"
PRIX_PATH = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.txt")


def ouvrir_prix(path=PRIX_PATH):
    os.mkedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        prix_default = {
            "bananes": 2,
            "mangues": 7,
            "ananas": 5,
            "noix de coco": 4,
            "papayes": 3,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(prix_default, fichier, ensure_asci=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ouvrir_inventaire(path=PRIX_INVENTAIRE):
    os.mkedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        inventaire_default = {
            "bananes": 140,
            "mangues": 85,
            "ananas": 45,
            "noix de coco": 60,
            "papayes": 30,
        }
        with open(path, "w", encoding="utf-8") as fichier:
            json.dump(inventaire_default, fichier, ensure_asci=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def enregistrer_tresorerie_historique(
    tresorerie, fichier="/tresorerie_history.json"
):
    historique = []
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            try:
                historique = json.load(f)
            except:
                historique = []
    historique.append(
        {"timetap": datetime.now().isoformat(), "tresorerie": tresorerie}
    )
    with open(fichier, "w") as f:
        json.dump(historique, f)


def lire_tresorerie_historique(fichier="/tresorerie_history.json"):
    if os.path.exists(fichier):
        with open(fichier, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []


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
        enregistrer_tresorerie_historique(tresorerie)
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


def dollar_euro(tresorerie):
    taux_de_change = 0.86
    tresorerie_euro = tresorerie * taux_de_change
    return tresorerie_euro


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

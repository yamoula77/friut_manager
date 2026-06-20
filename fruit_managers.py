inventaires = {
    "bananes": 120,
    "mangues": 85,
    "ananas": 45,
    "noix de coco": 60,
    "papayes": 30,
}


# creer une fonction pour afficher
def affichier_inventaire(inventaires):
    print("inventaire actuel de la plantation :")
    for fruit, quantite in inventaires.items():
        print(f"- {fruit.capitalize()}: {quantite} unites")


# creer une fonction recolter
def recolter(inventaires, fruit, quantite):
    inventaires[fruit] = inventaires.get(fruit, 0) + quantite
    print(f"\n recolte {quantite} {fruit} supplementaires!")


# creer une fonction pour vendre les fruits
def vendre(inventaires, fruit, quantite):
    if inventaires.get(fruit, 0) >= quantite:
        inventaires[fruit] -= quantite
        print(f"\n vendu {quantite} {fruit} !")
    else:
        print(f"pas assez de {fruit} pour vendre {quantite} unites")


if __name__ == "__main__":
    affichier_inventaire(inventaires)
    recolter(inventaires, "bananes", 10)
    vendre(inventaires, "bananes", 5)
    affichier_inventaire(inventaires)

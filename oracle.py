import requetes as req
import networkx as nx
import matplotlib.pyplot as plt

def menu_principale():
    commnde_faite = False
    while not commnde_faite:
        print("╭─────────────────────────╮")
        print("│      Menu principal     │")
        print("│─────────────────────────│")
        print("│ P: Présentation appli   │")
        print("│ D: Débuter              │")
        print("│ W: Qui sommes nous ?    │")
        print("│ Q: Quitter              │")
        print("╰─────────────────────────╯")
        commande_brute = input("")# input("Entrez une commande: ")
        commande = commande_brute.lower()
        if commande == "p":
            # print("\nPrésentation de l'application")
            presentation()
        elif commande == "d":
            # print("\nDébuter")
            debuter()
        elif commande == "w":
            # print("\nQui sommes nous ?")
            qui_sommes_nous()
        elif commande == "q":
            commnde_faite = True
            print("\nAu revoir !")
            # exit()
        else:
            print("Commande", commande_brute, "inconnue")

def presentation():
    ######### A MODIFIER #########
    print("L'application A la conquête de Hollywood est une application qui permet de retrouver les acteurs qui ont collaboré ensemble dans des films. Elle est basée sur un graphe qui représente les collaborations entre acteurs. Vous pouvez rechercher des acteurs et voir avec qui ils ont collaboré.\n")

def qui_sommes_nous():
    ######### A MODIFIER #########
    print("Nous sommes Alexy WICIAK et Niksan NAGARAJAH, étudiant en première années de BUT informatique à l'IUT d'Orléans. Nous avons réalisé cette application dans le cadre d'un projet.\n")

def debuter():
    commnde_faite = False
    base_choisie = False
    G = None
    while not commnde_faite:
        print("╭─────────────────────────╮")
        print("│      Menu principal     │")
        print("│─────────────────────────│")
        if base_choisie:
            print("│ C: Changer de base de...│")
            print("│ V: Voir graph de la base│")
        else:
            print("│ C: Choisir une base d...│")
            print("│ U: Utiliser notre base  │")
        
        print("│ Q: Quitter              │")
        print("╰─────────────────────────╯")
        commande_brute = input("")# input("Entrez une commande: ")
        commande = commande_brute.lower()
        if commande == "c":
            G = choose_file()
            base_choisie = True
        elif commande == "u":
            G = req.json_vers_nx("./data_2.json")
            base_choisie = True
        elif base_choisie is True and commande == "v":
            nx.draw(G, with_labels=True)
            plt.show()
        elif commande == "q":
            commnde_faite = True
            print("\nAu revoir !")
            # exit()
        else:
            print("\nCommande", commande_brute, "inconnue")

def choose_file():
    chemin = input("Entrez le chemin du fichier JSON à utiliser\n")
    return req.json_vers_nx(chemin)

def lancer_application():
    print("Bienvenue dans l'application A la conquête de Hollywood !")
    menu_principale()

lancer_application()
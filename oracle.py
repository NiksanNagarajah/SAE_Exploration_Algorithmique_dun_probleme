import requetes as req
import networkx as nx
import matplotlib.pyplot as plt

def menu_principale():
    commnde_faite = False
    while not commnde_faite:
        print("╭──────────────────────────╮")
        print("│      Menu principal      │")
        print("│──────────────────────────│")
        print("│ P: Présentation appli    │")
        print("│ D: Débuter               │")
        print("│ W: Qui sommes nous ?     │")
        print("│ Q: Quitter               │")
        print("╰──────────────────────────╯")
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
    print("L'application \"A la conquête de Hollywood\" est une application qui permet de retrouver les acteurs qui ont collaboré ensemble dans des films. Elle est basée sur un graphe qui représente les collaborations entre acteurs. Vous pouvez rechercher des acteurs et voir avec qui ils ont collaboré.\n")

def qui_sommes_nous():
    ######### A MODIFIER #########
    print("Nous sommes Alexy WICIAK et Niksan NAGARAJAH, étudiant en première années de BUT informatique à l'IUT d'Orléans. Nous avons réalisé cette application dans le cadre d'un projet.\n")

def debuter():
    commnde_faite = False
    base_choisie = False
    G = None
    while not commnde_faite:
        print("╭──────────────────────────╮")
        print("│      Menu principal      │")
        print("│──────────────────────────│")
        if base_choisie:
            print("│ C: Changer de base de ...│")
            print("│ V: Voir graph de la base │")
            print("│ M: Collaborateurs communs│")
        else:
            print("│ C: Choisir une base de...│")
            print("│ U: Utiliser notre base   │")
        
        print("│ Q: Quitter               │")
        print("╰──────────────────────────╯")
        commande_brute = input("")# input("Entrez une commande: ")
        commande = commande_brute.lower()
        if commande == "c":
            try:
                G = choose_file()
                base_choisie = True
            except FileNotFoundError:
                print("Désolé nous rencontrons une erreur, le fichier n'existe pas ou est ilisible")
        elif commande == "u":
            G = req.json_vers_nx("./data_100.json")
            base_choisie = True
        elif base_choisie is True and commande == "v":
            nx.draw(G, with_labels=True)
            plt.show()
        elif base_choisie is True and commande == "m":
            collab_communs(G)
        elif base_choisie is True and commande == "p":
            collab_proches(G)
        elif commande == "q":
            commnde_faite = True
            print("\nAu revoir !")
            # exit()
        else:
            print("\nCommande", commande_brute, "inconnue")

def choose_file():
    chemin = input("Entrez le chemin du fichier JSON à utiliser\n")
    return req.json_vers_nx(chemin)

def collab_communs(G):
    acteur1 = input("Entrez le nom du premier acteur\n")
    acteur2 = input("Entrez le nom du deuxième acteur\n")
    collaborateurs = req.collaborateurs_communs(G, acteur1, acteur2)
    if collaborateurs == set():
        print("Les acteurs", acteur1, "et", acteur2, "n'ont pas collaboré ensemble")
    elif collaborateurs is not None:
        print("Les acteurs qui ont collaboré avec", acteur1, "et", acteur2, "sont:")
        print(collaborateurs)

def collab_proches(G):
    acteur = input("Entrez le nom de l'acteur\n")
    distance = input("Entrez la distance souhaitée\n")
    collaborateurs = req.collaborateurs_proches(G, acteur, int(distance))
    if collaborateurs == set():
        print("Aucun acteur n'a collaboré avec", acteur, "à une distance de", distance)
    elif collaborateurs is not None:
        print("Les acteurs qui ont collaboré avec", acteur, "à une distance de", distance, "sont:")
        print(collaborateurs)

def lancer_application():
    print("Bienvenue dans l'application \"A la conquête de Hollywood\" !")
    menu_principale()

lancer_application()
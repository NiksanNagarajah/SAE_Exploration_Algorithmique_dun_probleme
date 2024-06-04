import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
import random
from termcolor import colored

def color_special_chars(text):
    special_chars = ['╭', '─', '╮', '╰', '╯', '│']
    new_text = ""
    for char in text:
        if char in special_chars:
            new_text += colored(char, 'red')
        else:
            new_text += colored(char, attrs=['bold'])
    return new_text

def menu_principale():
    commnde_faite = False
    while not commnde_faite:
        print(color_special_chars("╭──────────────────────────╮    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡠⠤⣤"))
        print(color_special_chars("│  🍿  Menu principal  🍿  │   ⡤⢴⡒⠰⣶⣾⡉⣙⡿⠷⠄⠽⠟⠛⠀⠚"))
        print(color_special_chars("│──────────────────────────│   ⣿⣿⠏⠉⣵⣶⠂⢀⣶⣶⠂⢠⣶⡶⠀⢠"))
        print(color_special_chars("│ P: Présentation appli    │   ⢻⣻⣶⣞⣟⣗⣶⣾⣿⣷⣶⣿⣿⣷⣶⣿"))
        print(color_special_chars("│ D: Débuter               │   ⢸⣽⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"))
        print(color_special_chars("│ W: Qui sommes nous ?     │   ⢸⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"))
        print(color_special_chars("│ Q: Quitter               │   ⢸⣭⣟⣿⣿⢻⣽⣿⣿⣽⣽⣿⣽⣿⣽⣿"))
        print(color_special_chars("╰──────────────────────────╯   ⠘⠛⠛⠛⠛⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛"))
        commande_brute = input("Entrez une commande: ")
        commande = commande_brute.lower()
        if commande == "p":
            # print(color_special_chars("\nPrésentation de l'application")
            presentation()
        elif commande == "d":
            # print(color_special_chars("\nDébuter")
            debuter()
        elif commande == "w":
            # print(color_special_chars("\nQui sommes nous ?")
            qui_sommes_nous()
        elif commande == "q":
            commnde_faite = True
            print(color_special_chars("\nAu revoir !"))
            # exit()
        else:
            print("Commande", commande_brute, "inconnue")

def presentation():
    print(color_special_chars("L'application \"A la conquête de Hollywood\" est une application qui permet de retrouver les acteurs qui ont collaboré ensemble dans des films. \nElle est basée sur un graphe qui représente les collaborations entre acteurs. Vous pouvez rechercher des acteurs et voir avec qui ils ont collaboré.\n"))

def qui_sommes_nous():
    print(color_special_chars("Nous sommes Alexy WICIAK et Niksan NAGARAJAH, étudiants en première années de BUT informatique à l'IUT d'Orléans. Nous avons réalisé cette application dans le cadre d'un projet.\n"))

def debuter():
    commnde_faite = False
    base_choisie = False
    G = None
    while not commnde_faite:
        print(color_special_chars("╭──────────────────────────╮"))
        print(color_special_chars("│  🎬  Menu principal  🎬  │"))
        print(color_special_chars("│──────────────────────────│"))
        if base_choisie:
            print(color_special_chars("│ C: Changer de base de ...│          _._"))
            print(color_special_chars("│ V: Voir graph de la base │        .'   `."))
            print(color_special_chars("│ E: Extrait des personnes │        |     |"))
            print(color_special_chars("│ M: Collaborateurs communs│       \"=======\""))
            print(color_special_chars("│ P: Collaborateurs proches│        $ ^ ^ $ "))
            print(color_special_chars("│ S: Sont proches ?        │        `  #  '"))
            print(color_special_chars("│ D: Distance qui sépare...│         `._.'"))
            print(color_special_chars("│ T: Centralité d'un acteur│      _.'< ' >'-._"))
            print(color_special_chars("│ H: Centre d'Hollywood    │    .'    \ /     '"))
            print(color_special_chars("│ L: Eloignement maximal   │   /       v       \\"))
        else:
            print(color_special_chars("│ C: Choisir une base de...│"))
            print(color_special_chars("│ U: Utiliser notre base   │"))
        
        print(color_special_chars("│ Q: Quitter               │"))
        print(color_special_chars("╰──────────────────────────╯"))
        commande_brute = input("Entrez une commande: ")
        commande = commande_brute.lower()
        if commande == "c":
            try:
                G = choose_file()
                base_choisie = True
            except Exception:
                print(color_special_chars("Désolé nous rencontrons une erreur, le fichier n'existe pas ou est ilisible\n"))
        elif commande == "u":
            G = req.json_vers_nx("./donnees/data_100.json")
            base_choisie = True
        elif base_choisie is True and commande == "e":
            extraire_personne(G)
        elif base_choisie is True and commande == "v":
            nx.draw(G, with_labels=True)
            plt.show()
        elif base_choisie is True and commande == "m":
            collab_communs(G)
        elif base_choisie is True and commande == "p":
            collab_proches(G)
        elif base_choisie is True and commande == "s":
            sont_proches(G)
        elif base_choisie is True and commande == "d":
            distance_separe(G)
        elif base_choisie is True and commande == "t":
            centrelite_acteur(G)
        elif base_choisie is True and commande == "h":
            print(color_special_chars("Le centre d'Hollywood est " + req.centre_hollywood(G) + "\n"))
        elif base_choisie is True and commande == "l":
            print(color_special_chars("La distance maximale entre toute paire d'acteurs/actrices dans le graphe est de " + str(req.eloignement_max(G)) + "\n"))
        elif commande == "q":
            commnde_faite = True
            print(color_special_chars("\nAu revoir !"))
            # exit()
        else:
            print("\nCommande", commande_brute, "inconnue")

def choose_file():
    chemin = input("Entrez le chemin du fichier JSON à utiliser\n")
    return req.json_vers_nx(chemin)

def extraire_personne(G):
    liste = list(G.nodes())
    print(color_special_chars("\nVoici 10 acteurs aléatoires:\n"))
    for _ in range(10):
        print(color_special_chars(" • " + random.choice(liste)))
    # print()

def collab_communs(G):
    acteur1 = input("Entrez le nom du premier acteur\n")
    acteur2 = input("Entrez le nom du deuxième acteur\n")
    collaborateurs = req.collaborateurs_communs(G, acteur1, acteur2)
    if collaborateurs == set():
        print(color_special_chars("Les acteurs " + acteur1 + " et " + acteur2 + " n'ont pas collaboré ensemble"))
    elif collaborateurs is not None:
        print(color_special_chars("Les acteurs qui ont collaboré avec " + acteur1 + " et " + acteur2 + " sont:"))
        print(collaborateurs)

def collab_proches(G):
    try:
        acteur = input("Entrez le nom de l'acteur\n")
        distance = input("Entrez la distance souhaitée\n")
        collaborateurs = req.collaborateurs_proches(G, acteur, int(distance))
        if collaborateurs == set():
            print(color_special_chars("Aucun acteur n'a collaboré avec " +  acteur + " à une distance de " + distance))
        elif collaborateurs is not None:
            print(color_special_chars("Les acteurs qui ont collaboré avec " + acteur + " à une distance de " + distance + " sont:"))
            print(collaborateurs)
    except:
        print(color_special_chars("Le nombre choisi n'est pas valide.\n"))

def sont_proches(G):
    acteur1 = input("Entrez le nom du premier acteur\n")
    acteur2 = input("Entrez le nom du deuxième acteur\n")
    if req.est_proche(G, acteur1, acteur2):
        print(color_special_chars("Les acteurs " + acteur1 + " et " + acteur2 +  " sont proches\n"))
    else:
        print(color_special_chars("Les acteurs " + acteur1 + " et " + acteur2 + " ne sont pas proches\n"))

def distance_separe(G):
    acteur1 = input("Entrez le nom du premier acteur\n")
    acteur2 = input("Entrez le nom du deuxième acteur\n")
    distance = req.distance(G, acteur1, acteur2)
    if distance is not None:
        print(color_special_chars("La distance qui sépare " + acteur1 + " et " + acteur2 + " est de " + str(distance) + "\n"))
    else:
        print(color_special_chars("Les acteurs " + acteur1 + " et " + acteur2 + " ne sont pas reliés\n"))

def centrelite_acteur(G):
    acteur = input("Entrez le nom de l'acteur\n")
    centralite = req.centralite(G, acteur)
    if centralite is not None:
        print(color_special_chars("La centralité de " + acteur + " est de " + str(centralite) + "\n"))
    else:
        print(color_special_chars("L'acteur " + acteur + " n'existe pas dans la base\n"))

def lancer_application():
    print(color_special_chars("Bienvenue dans l'application \"A la conquête de Hollywood\" !"))
    menu_principale()

lancer_application()
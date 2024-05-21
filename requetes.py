import json
import networkx as nx
import matplotlib.pyplot as plt

def corrige_nom(nom):
    nom = nom.replace("[[", "")
    nom = nom.replace("]]", "")
    if "(" in nom:
        nom = nom[:nom.index("(") - 1]
    if "|" in nom:
        nom = nom[:nom.index("|")]
    return nom

def txt_to_json(fichier_txt, nouveau_fichier):
    """
    La fonction permet de convertir un fichier texte en un objet JSON.

    Args:
        fichier_txt (str): Le chemin vers le fichier texte à convertir.

    Returns:
        dict: L'objet JSON représentant le contenu du fichier texte.
    """
    try:
        donnees = [] 
        fichier = open(fichier_txt, 'r', encoding="utf8")
        json_file = open(nouveau_fichier, 'w')
        lesLignes = fichier.readlines()
        for ligne in lesLignes: #On parcourt chaque ligne dans le fichier 
            amodif = json.loads(ligne)
            ajout = {}
            for (cle, valeur) in amodif.items(): #On parcourt le dictionnaire
                if type(valeur) == list:
                    liste = []
                    for nom in valeur:
                        nom = corrige_nom(nom)
                        liste.append(nom)
                    valeur = liste
                ajout[cle] = valeur
            donnees.append(ajout)
        json.dump(donnees, json_file, indent=4, ensure_ascii=False)
        fichier.close()
        json_file.close()
    except:
        print("Désolé nous rencontrons une erreur, le fichier n'existe pas ou est ilisible")

# txt_to_json("data.txt", "data.json")
# txt_to_json("data_100.txt", "data_100.json")



def json_vers_nx(chemin):
    """
    La fonction permet de convertir un fichier JSON en un graphe G.

    Args:
        chemin (str): Le chemin vers le fichier JSON à convertir.

    Returns:
        G (Graphe): Le graphe représentant le contenu du fichier JSON.
    """
    G = nx.Graph()
    json_file = json.load(open(chemin, "r"))
    for film in json_file: #On parcourt chaque film du fichier json
        cast = film['cast']
        for acteur1 in cast:
            for acteur2 in cast:
                G.add_edge(acteur1, acteur2)
    # nx.draw(G, with_labels=True)
    # plt.show()
    return G

# json_vers_nx("./data_2.json")

# def graphe_collaborateurs_communs(acteur1, acteur2, collaborateurs):
#     G = nx.Graph()
#     for acteur in collaborateurs:
#         G.add_edge(acteur1, acteur)
#         G.add_edge(acteur2, acteur)
#     nx.draw(G, with_labels=True)
#     plt.show()


def collaborateurs_communs(G, u, v):
    """
    Retourne l'ensemble des acteurs qui ont collaboré avec à la fois acteur1 et acteur2
    dans les films répertoriés dans le fichier JSON G.

    Paramètres :
    - G : (Graph) Graphe considéré.
    - v : (str) Nom de l'acteur 2.

    Returns :
    - (set) Ensemble des acteurs qui ont collaboré avec acteur1 et acteur2.
    """
    try :
        collaborateurs = set()
        colab_acteur1 = set(G[u].keys())
        colab_acteur2 = set(G[v].keys())
        for acteur in colab_acteur1:
            if acteur in colab_acteur2 and acteur != u and acteur != v:
                collaborateurs.add(acteur)
        return collaborateurs
    except:
        print("Un des noms des acteurs spécifié est incorrecte ou n'est pas dans notre base de données\n")
        return None

# print(collaborateurs_communs(json_vers_nx("./data_2.json"), "Robert Downey Jr.", "Tom Holland"))
# print(collaborateurs_communs(json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young"))

#6.3)

# def collaborateurs_proches(G, u, k):
#     ensemble_colab = set()
#     dico_collab = {0 : {u}}
#     for i in range(k):
#         dico_collab[i+1] = set()
#         for acteur in dico_collab[i]:
#             colab = G.edges(acteur)
#             for (comedien1, comedien2) in colab:
#                 if comedien1 != acteur and comedien1 not in ensemble_colab:
#                     ensemble_colab.add(comedien1)
#                     dico_collab[i+1].add(comedien1)
#                 if comedien2 != acteur and comedien2 not in ensemble_colab:
#                     ensemble_colab.add(comedien2)
#                     dico_collab[i+1].add(comedien2)
#     return list(ensemble_colab)

# Code donné 
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    # print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs and voisin != u:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

# print(collaborateurs_proches(json_vers_nx("data_2.json"), "Rutger Hauer", 3))
# print(collaborateurs_proches(json_vers_nx("./data_100.json"), "Ken Baker", 0))

def est_proche(G,u,v,k=1):
    """
    La fonction permet de savoir si le collaborateur 'u' est proche de 'v'.

    Paramètres :

    - G : (Graph) Graphe considéré.
    - u : (str) Nom de l'acteur 1.
    - v : (str) Nom de l'acteur 2.
    - k : (int) distance proche

    Returns:
        (bool): True si la distance entre les 2 acteurs est considéré comme proche.
    """
    lesColaborateurs = collaborateurs_proches(G, u, k)
    if lesColaborateurs != None:
        if v in lesColaborateurs:
            return True
    return False

# print(est_proche(json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young"))
# print(est_proche(json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall"))

def distance_naive(G, u, v):
    if u not in G.nodes() or v not in G.nodes():
        return None
    degre = 1
    while not est_proche(G, u, v, degre): # PAS MéTHODE ADAPTE (privilégié dico)
        degre += 1
    return degre

# print(distance_naive(json_vers_nx("./data_100.json"), "Sam Raimi", "Anne Francis"))
# print(distance_naive(json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall"))



# !!!!! Pas sur !!!!!
def distance(G, u, v):
    """
    La fonction permet trouver la distance entre 2 acteurs.

    Paramètres :

    - G : (Graph) Graphe considéré.
    - u : (str) Nom de l'acteur 1.
    - v : (str) Nom de l'acteur 2.

    Returns:
        (int): La distance entre les 2 acteurs.
    """
    if u == v:
        return 0
    ensemble_colab = set()
    dico_collab = {0 : {u}}
    i = 0
    while dico_collab[i] != set():
        dico_collab[i+1] = set()
        for acteur in dico_collab[i]:
            colab = G.edges(acteur)
            for (comedien1, comedien2) in colab:
                if comedien1 != acteur and comedien1 not in ensemble_colab:
                    ensemble_colab.add(comedien1)
                    dico_collab[i+1].add(comedien1)
                if comedien2 != acteur and comedien2 not in ensemble_colab:
                    ensemble_colab.add(comedien2)
                    dico_collab[i+1].add(comedien2)
            if v in dico_collab[i+1]:
                return i+1
            # print(colab)
        i += 1
    return None

# print(distance(json_vers_nx("./data_100.json"), "Ben McKenzie", "Elizabeth Hubbard"))
# print(distance(json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall"))


# 6.4)

# !!!!! Pas sur !!!!!
def centralite(G, u):
    # return nx.degree_centrality(G)[u]
    # ou 
    return G.degree(u) 

# print(centralite(json_vers_nx("./data_100.json"), "Robert Gerringer"))

def centre_hollywood(G):
    acteur_maxi = None
    maxi = 0
    for acteur in G.nodes():
        if centralite(G, acteur) > maxi:
            acteur_maxi = acteur
            maxi = centralite(G, acteur)
    return acteur_maxi

# print(centre_hollywood(json_vers_nx("./data_2.json")))

def eloignement_max(G:nx.Graph):
    """
    Retourne les paires d'acteurs les plus éloignés dans le graphe G.

    Args:
        G (nx.Graph): Le graphe des acteurs.

    Returns:
        set: Les paires d'acteurs les plus éloignés.
    """
    max_distance = 0
    acteurs_eloigner = set()
    for acteur1 in G.nodes():
        for acteur2 in G.nodes():
            if acteur1 != acteur2:
                distance_acteurs = distance(G, acteur1, acteur2)
                if distance_acteurs != None and distance_acteurs > max_distance:
                    max_distance = distance_acteurs
                    acteurs_eloigner.add((acteur1, acteur2))
    return len(acteurs_eloigner)

# print(eloignement_max(json_vers_nx("./data_100.json")))


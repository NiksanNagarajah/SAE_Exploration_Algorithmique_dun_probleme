import json
import networkx as nx
import matplotlib.pyplot as plt
import time

def corrige_nom(nom):
    #Complexité : O(N)
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
    #Complexité : O(N)³
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

def json_vers_nx(chemin):
    """
    La fonction permet de convertir un fichier JSON en un graphe G.

    Args:
        chemin (str): Le chemin vers le fichier JSON à convertir.

    Returns:
        G (Graphe): Le graphe représentant le contenu du fichier JSON.
    """
    #Complexité : O(N)³
    G = nx.Graph()
    json_file = json.load(open(chemin, "r"))
    for film in json_file: #On parcourt chaque film du fichier json : O(N)
        cast = film['cast']
        for acteur1 in cast: #O(N)
            for acteur2 in cast: #O(N)
                G.add_edge(acteur1, acteur2)
    # nx.draw(G, with_labels=True)
    # plt.show()
    return G

# G = json_vers_nx("./donnees/data.json")

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
    #Complexité : O(N)
    # start = time.time()
    try :
        collaborateurs = set()
        colab_acteur1 = set(G[u].keys())
        colab_acteur2 = set(G[v].keys())
        for acteur in colab_acteur1: #O(N)
            if acteur in colab_acteur2 and acteur != u and acteur != v:
                collaborateurs.add(acteur)
        # print(time.time()-start)
        return collaborateurs
    except:
        print("Un des noms des acteurs spécifié est incorrecte ou n'est pas dans notre base de données\n")
        # print(time.time()-start)
        return None

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
    #Complexité : O(N)³
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    # print(collaborateurs)
    for _ in range(k): # O(N)
        collaborateurs_directs = set()
        for c in collaborateurs: # O(N)
            for voisin in G.adj[c]: # O(N)
                if voisin not in collaborateurs and voisin != u:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

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
    #Complexité : O(N)³
    lesColaborateurs = collaborateurs_proches(G, u, k) #O(N)³ : appel de la fonction précédente
    if lesColaborateurs != None:
        if v in lesColaborateurs:
            return True
    return False

def distance_naive(G, u, v):
    #Complexité : #O(N)⁴
    if u not in G.nodes() or v not in G.nodes():
        return None
    degre = 0
    while not est_proche(G, u, v, degre): #O(N)⁴ # PAS MéTHODE ADAPTE (privilégié dico)
        degre += 1
    return degre

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
    #Complexité : #O(N)³
    print("ICI")
    if u == v:
        return 0
    if u not in G.nodes() or v not in G.nodes():
        return None
    ensemble_colab = set()
    dico_collab = {0 : {u}}
    i = 0
    while dico_collab[i] != set(): #O(N)
        dico_collab[i+1] = set()
        for acteur in dico_collab[i]: #O(N)
            colab = G.edges(acteur)
            for (comedien1, comedien2) in colab: #O(N)
                if comedien1 not in ensemble_colab:
                    ensemble_colab.add(comedien1)
                    dico_collab[i+1].add(comedien1)
                if comedien2 not in ensemble_colab:
                    ensemble_colab.add(comedien2)
                    dico_collab[i+1].add(comedien2)
            if v in dico_collab[i+1]:
                return i+1
        i += 1
    return None

# 6.4)
def centralite(G, u):
    """
    Déterminer la plus grande distance qui le sépare d’un autre acteur dans le graphe.

    Args:
        G (nx.Graph): Le graphe des acteurs.
        u : (str) Nom de l'acteur

    Returns:
        int : Distance maximale qui sépare l'acteur u d'un autre acteur dans le graphe.
    """
    # Complexité : #O(N)²
    if u not in G.nodes():
        return None
    # # return G.degree(u) 
    # # ou
    # lengths = nx.shortest_path_length(G, source=u)
    # return max(lengths.values())
    distances = {u : 0} # Parcours en largeur 
    a_faire = [u]
    while a_faire: #O(N)
        courant = a_faire.pop(0)
        distance_actuel = distances[courant]
        for voisin in G.neighbors(courant): #O(N)
            if voisin not in distances.keys():
                distances[voisin] = distance_actuel + 1
                a_faire.append(voisin)
    return max(distances.values())

def centre_hollywood(G):
    """
    Déterminer l'acteur le plus central du graphe.

    Args:
        G (nx.Graph): Le graphe des acteurs.

    Returns:
        str : Le nom de l'acteur au centre d'Hollywood
    """
    # acteur_maxi = None
    # maxi = 0
    # for acteur in G.nodes():
    #     if centralite(G, acteur) > maxi:
    #         acteur_maxi = acteur
    #         maxi = centralite(G, acteur)
    # return acteur_maxi, maxi
    # ou
    #Complexité : O(N)³
    les_centralites = {}
    for acteur in G.nodes(): #O(N)
        les_centralites[acteur] = centralite(G, acteur) #O(N)²
    acteur_central = None
    mini = None
    for (acteur, centralite_acteur) in les_centralites.items(): #O(N)
        if mini == None or centralite_acteur < mini:
            mini = centralite_acteur
            acteur_central = acteur
    return acteur_central

def eloignement_max(G:nx.Graph):
    """
    Retourne les paires d'acteurs les plus éloignés dans le graphe G.

    Args:
        G (nx.Graph): Le graphe des acteurs.

    Returns:
        set: Les paires d'acteurs les plus éloignés.
    """
    #Complexité : O(N)³
    les_centralites = {}
    for acteur in G.nodes(): #O(N)
        d = time.time()
        les_centralites[acteur] = centralite(G, acteur) #O(N)²
    return max(les_centralites.values())


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
        for ligne in lesLignes:
            amodif = json.loads(ligne)
            ajout = {}
            for (cle, valeur) in amodif.items():
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


def json_vers_nx(chemin):
    G = nx.Graph()
    json_file = json.load(open(chemin, "r"))
    for film in json_file:
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
    - G : (str) Chemin vers le fichier JSON contenant les informations sur les films et leurs acteurs.
    - u : (str) Nom de l'acteur 1.
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
        print("Un des nom des acteurs spécifié est incorrecte ou n'est pas dans notre base de données")
        return None

# print(collaborateurs_communs(json_vers_nx("./data_2.json"), "Robert Downey Jr.", "Tom Holland"))
# print(collaborateurs_communs(json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young"))

#6.3)

def collaborateurs_proches(G, u, k):
    ensemble_colab = set()
    dico_collab = {0 : {u}}
    for i in range(k):
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
            # print(colab)
    return ensemble_colab#list(ensemble_colab)
    # dico_collab = {0 : {u}}
    # json_file = json.load(open(G, "r"))
    # ensemble_collab = set()
    # for i in range(k):
    #     dico_collab[i+1] = set()
    #     for acteur in dico_collab[i]:
    #         for film in json_file:
    #             cast = film['cast']
    #             for comedien in cast:
    #                 if acteur in cast and comedien != acteur and comedien not in ensemble_collab :
    #                     ensemble_collab.add(comedien)
    #                     dico_collab[i+1].add(comedien)
    # return list(ensemble_collab)

# print(collaborateurs_proches(json_vers_nx("data_2.json"), "Rutger Hauer", 3))

# {'Elizabeth Sanders', 'Pat Hingle', 'Isabella Rossellini', "Chris O'Donnell", 'Ted Raimi', 'Michael Gough', 'Sky du Mont', 'Rutger Hauer', 'Paul Reubens', 'Bruce Campbell', 'Nicole Kidman', 'Leon Vitali', 'Patrick Magee', 'Slim Pickens', 'Michael Keaton'}

def est_proche(G,u,v,k=1):
    lesColaborateurs = collaborateurs_proches(G, u, k)
    if v in lesColaborateurs:
        return True
    return False

# print(est_proche(json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young"))
# print(est_proche(json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall"))

def distance_naive(G, u, v):
    degre = 1
    while not est_proche(G, u, v, degre): # PAS MéTHODE ADAPTE (privilégié dico)
        degre += 1
    return degre

def distance(G, u, v):
    degre = 1
    while not est_proche(G, u, v, degre):
        degre += 1
    return degre

# print(distance(json_vers_nx("./data_2.json"), "Rutger Hauer", "Sean Young"))
# print(distance(json_vers_nx("./data_2.json"), "Rutger Hauer", "Jerry Hall"))
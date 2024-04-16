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
        for acteur in cast:
            G.add_edge(film['title'], acteur)
    nx.draw(G, with_labels=True)
    plt.show()

# print(json_vers_nx("data_2.json"))

def graphe_collaborateurs_communs(acteur1, acteur2, collaborateurs):
    G = nx.Graph()
    for acteur in collaborateurs:
        G.add_edge(acteur1, acteur)
        G.add_edge(acteur2, acteur)
    nx.draw(G, with_labels=True)
    plt.show()

def collaborateurs_communs(fichier, u, v):
    """
    Retourne l'ensemble des acteurs qui ont collaboré avec à la fois acteur1 et acteur2
    dans les films répertoriés dans le fichier JSON G.

    Paramètres :
    - G : (str) Chemin vers le fichier JSON contenant les informations sur les films et leurs acteurs.
    - acteur1 : (str) Nom de l'acteur 1.
    - acteur2 : (str) Nom de l'acteur 2.

    Returns :
    - (set) Ensemble des acteurs qui ont collaboré avec acteur1 et acteur2.
    """
    collaborateurs = set()
    colab_acteur1 = set()
    colab_acteur2 = set()
    json_file = json.load(open(fichier, "r"))
    for film in json_file:
        cast = film['cast']
        if u in cast:
            for acteur in cast:
                if acteur != u:
                    colab_acteur1.add(acteur)
        if v in cast:
            for acteur in cast:
                if acteur != v:
                    colab_acteur2.add(acteur)
    collaborateurs = colab_acteur1.intersection(colab_acteur2)
    # graphe_collaborateurs_communs(u, v, collaborateurs)
    return collaborateurs


#print(len(collaborateurs_communs("data.json", "Robert Downey Jr.", "Tom Holland")))

#6.3)

def collaborateurs_proches(G, u, k):
    dico_collab = {0 : {u}}
    json_file = json.load(open(G, "r"))
    ensemble_collab = set()
    for i in range(k):
        dico_collab[i+1] = set()
        for acteur in dico_collab[i]:
            for film in json_file:
                cast = film['cast']
                for comedien in cast:
                    if comedien != u and comedien not in ensemble_collab :
                        ensemble_collab.add(comedien)
                        dico_collab[i+1].add(comedien)
    return list(ensemble_collab)

print(collaborateurs_proches("data_2.json", "Núria Espert", 1))
    

# print(collaborateurs_communs("data.json", "Robert Downey Jr.", "Tom Holland"))



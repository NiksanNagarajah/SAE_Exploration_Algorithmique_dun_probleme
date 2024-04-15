import json

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
                        nom = nom.replace("[[", "")
                        nom = nom.replace("]]", "")
                        if "(" in nom:
                            nom = nom[:nom.index("(") - 1]
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

def collaborateurs_communs(G, u, v):
    collaborateurs = set()
    json_file = json.load(open(G, "r"))
    for film in json_file:
        cast = film['cast']
        if u in cast and v in cast:
            for actor in cast:
                if actor != u and actor != v:
                    collaborateurs.add(actor)
    return list(collaborateurs)

print(collaborateurs_communs("data.json", "Bruce Campbell", "Ian Abercrombie"))

import json

def txt_to_json(fichier_txt):
    """
    La fonction permet de convertir un fichier texte en un objet JSON.

    Args:
        fichier_txt (str): Le chemin vers le fichier texte à convertir.

    Returns:
        dict: L'objet JSON représentant le contenu du fichier texte.
    """
    with open(fichier_txt, 'r') as file:
        content = file.read()
        lines = content.split('\n')
        data = {"lines": lines}
    return data

json_data = txt_to_json("data.txt")


def txt_to_json(fichier_txt, nouveau_fichier):
    """
    La fonction permet de convertir un fichier texte en un objet JSON.

    Args:
        fichier_txt (str): Le chemin vers le fichier texte à convertir.

    Returns:
        dict: L'objet JSON représentant le contenu du fichier texte.
    """
    liste = [] 
    try:
        fichier = open(fichier_txt, 'r', encoding="utf8")
        json_file = open(nouveau_fichier, 'w')
        #fichier.readline()
    except:
        erreur = "Désolé nous rencontrons une erreur, le fichier n'existe pas ou est ilisible"
        return erreur
    try:
        for ligne in fichier:
            # print(ligne)
            # break
            liste.append(ligne)
            json_file.write(ligne)
            l_champs = ligne.split(",")
            #l_champs = dict(l_champs)
            # print(l_champs)
            # der_val = l_champs[len(l_champs) - 1]
            # print(der_val)
            # for i in l_champs.keys():
            #     print(l_champs[i])
            # break
            # if der_val[0] == 'T':
            #     der_val = True
            # else:
            #     der_val = False
            # liste.append((l_champs[0], l_champs[1], l_champs[2], int(l_champs[3]), int(l_champs[4]), l_champs[5], l_champs[6], l_champs[7], der_val))
        #print(liste)
        # json_file.write(str(liste))
        json_file.close()
        fichier.close()
    except:
        erreur = "Désolé, nous rencontrons un problème lors de la lecture du fichier"
        return erreur
    return liste

txt_to_json("data.txt", "data.json")
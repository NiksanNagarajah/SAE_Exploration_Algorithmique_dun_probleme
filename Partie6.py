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
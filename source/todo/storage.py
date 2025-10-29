import os, json 
from typing import List, Dict, Optional, Any
from pathlib import Path

#chemin_fichier = Path.home() / "data" / "todo_data.json"
chemin_fichier = Path(__file__).parent / "data" / "todo_data.json"

def fichier_existe():
    chemin_fichier.parent.mkdir(parents=True, exist_ok=True) # on cree les repertoires parent necessaires s'ils n'existent pas
    if not chemin_fichier.exists():
        # si le fichier n'existe pas, on le cree avec une liste vide
        with open(chemin_fichier, 'w') as f:
            json.dump([], f)

def lire_taches():
    fichier_existe()
    with open(chemin_fichier, 'r') as f:
        return json.load(f)
    
def sauvegarder_taches(taches: list[dict[str, Any]]) -> None:
    fichier_existe()
    with open(chemin_fichier, 'w') as f:
        json.dump(taches, f, indent =4)
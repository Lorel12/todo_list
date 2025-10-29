from typing import *
from source.todo.storage import lire_taches, sauvegarder_taches
from datetime import datetime

rows = lire_taches()

def ajouter_tache(rows, title, tags, due):
    """ Ajoute une nouvelle taches a la liste des taches."""
    nouvelle_tache = {
        "id": len(rows) + 1,
        "title": title,
        "tags": tags,
        "due": due,
        "done": False,
        "created_at": datetime.now().isoformat()  # datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    rows.append(nouvelle_tache)
    sauvegarder_taches(rows)
    return nouvelle_tache

def lister_taches(rows, show_all, tag):
    """ Liste des taches filtrees par due puis created_at.""" 
    taches_filtrees = []
    for tache in rows:
        #if tache['done']:
        #if not show_all and tache['done']:
            #continue # sauter les taches terminees si show_all est False
        if tag and tag not in tache['tags']:
            continue # sauter les taches qui n'ont pas le tag specifie
        taches_filtrees.append(tache) # ajouter la tache a la liste filtree
    # trier les taches par due date puis par created_at
    taches_triees = sorted(

        taches_filtrees, # la liste des taches a trier
        
        key=lambda x: (
            x['due'] if x['due'] is not None else '2025-12-31', # 
            x['created_at'] # trier par created_at en second
        )
    )
    return taches_triees

def marquer_tache_comme_terminee(rows, task_id):
    """ Marque une tache comme terminee."""
    for tache in rows:
        if tache['id'] == task_id:
            tache['done'] = True
            sauvegarder_taches(rows)
            return tache
        #return None

def supprimer_tache(row, task_id):
    """ Supprime une tache de la liste des taches."""
    for i, tache in enumerate(rows):
        if tache['id'] == task_id:
            del rows[i]
            sauvegarder_taches(rows)
            return tache
    return None

def __prochain_id(rows):
    """ Retourn ele prochain id disponible."""
    if not rows:
        return 1 #print("Anonyme0")
    ids = [int(tache['id'].replace("Anonyme", "")) for tache in rows]
    return max(ids) + 1 if ids else 1
    #return f"Anonyme{max(ids) + 1}"

def valider_due_date(due: str):
    """ Valider le format de la date."""
    if due is None: return None
    try:
        return datetime.strptime(due, "%Y-%m-%d")
        # isoparse(due).date().isoformat()
        
    except ValueError:
        raise ValueError("Le format de la date doit etre AAAA-MM-JJ.")
    

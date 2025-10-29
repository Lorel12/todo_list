# To-Do List CLI (json)

Un outil en ligne de commande pour gérer une liste de tâches avec persistance dans un fichier **JSON**.

Fonctions : 

    **ajouter**, 
    
    **lister**, 
    
    **terminer**, 
    
    **supprimer** une tâche, avec tri par date d’échéance puis date de création.

## 🚀 Fonctionnalités (MVP)

- `add` : ajouter une tâche (tags et due optionnels)
- `list` : lister les tâches (filtres : `--due`, `--created_at`)
- `done` : marquer une tâche comme terminée
- `rm` : supprimer une tâche

## 📦 Installation

--- bash
# 1. Cloner le projet

git clone https://github.com/Lorel12/todo_list.git
cd todo

# 2. Environnement virtuel
python -m venv .env
# Windows
.venv\Scripts\activate
# macOS / Linux
source .env/bin/activate

# 3. Installer les dependances
pip install -r requirements.txt

# Utilisation 

## Aide generale
python -m source.todo.app --help

## 1. Ajouter une tâche

python -m source.todo.app add "Acheter du riz" --tag courses --due 2025-11-10

python -m source.todo.app add "Préparer la réunion" --tag travail

## 2. Lister (non terminées par défaut)


python -m source.todo.app list

python -m source.todo.app list --all

python -m source.todo.app list --tag courses


## 3. Marquer comme terminée (ex: id=1)
python -m source.todo.app done 1

## 4. Supprimer (ex: id=2)
python -m source.todo.app rm 2

🗂️ Arborescence
todo/

  README.md
  
  requirements.txt
  
  data/                    # créé automatiquement
  
  src/
  
    __init__.py
    
    todo/
    
      __init__.py
      
      app.py              # interface CLI (Typer + Rich)
      
      storage.py          # lecture/écriture JSON
      
      models.py           # dataclass Task
      
      logic.py            # fonctions métier (add/list done/rm)
      
  test/
  
    test_basic.py

🗃️ Données (format JSON)

[
  {
  
    "id": 1,
    
    "title": "Acheter du riz",
    
    "tags": ["courses"],
    
    "due": "2025-11-10",
    
    "done": false,
    
    "created_at": "2025-10-29T11:15:00"
  }
]

✅ Tests

Exécuter tous les tests :

pytest -q

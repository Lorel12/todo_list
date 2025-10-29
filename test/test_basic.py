import json
from source.todo.logic import ajouter_tache, lister_taches, marquer_tache_comme_terminee, supprimer_tache
from datetime import datetime

def test_add_and_list(tmp_path):
    rows = []
    nouvelle_tache = ajouter_tache(rows, "Test Task", ["test"], "2024-12-31")
    assert  nouvelle_tache["id"] == 1
    assert nouvelle_tache["title"] == "Test Task"
    
    taches = lister_taches(rows, show_all=True, tag=None)
    assert len(taches) == 1 and taches[0]["done"] is False

def test_due_format_validation():
    rows = []
    try:
        ajouter_tache(rows, "Invalid Due Task", ["test"], "31-12-2024")
        assert False, "Expected ValueError for invalid due date format."
    except ValueError as e:
        pass
        #assert str(e) == "Due date must be in YYYY-MM-DD format."
    
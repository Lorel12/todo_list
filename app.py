import typer
from typing import Optional, List
from source.todo.logic import ajouter_tache, lister_taches, marquer_tache_comme_terminee, supprimer_tache
from source.todo.models import Task
from source.todo.storage import lire_taches, fichier_existe, sauvegarder_taches
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Application de gestion de tâches.")


@app.command()
def add(title: str, tag: List[str] = typer.Option([], "--tag"), due: Optional[str] = None):   
    """ Ajouter une nouvelle tâche à la liste des tâches."""
    rows = lire_taches()
    nouvelle_tache = ajouter_tache(rows, title, tag, due)
    sauvegarder_taches(rows)    
    typer.echo(f"Tâche ajoutée : {nouvelle_tache}")
    
    console = Console()
    console.print(f"[green]Tâche ajoutée : {nouvelle_tache}[/green]")

@app.command()
def list(show_all: bool = False, tag: Optional[str] = None):
    """ Lister les tâches."""
    rows = lire_taches()
    taches = lister_taches(rows, show_all, tag)
    table = Table(title="Liste des tâches")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Titre", style="magenta")
    table.add_column("Tags", style="green")
    table.add_column("Due", style="yellow")
    table.add_column("Done", style="red")
    table.add_column("Created At", style="blue")
    for tache in taches:
        table.add_row(
            str(tache["id"]),
            tache["title"],
            ", ".join(tache["tags"]),
            tache["due"] if tache["due"] else "N/A",
            "✔️" if tache["done"] else "❌",
            tache["created_at"]
        )
    console = Console()
    console.print(table)

@app.command()
def done(task_id: int):
    """ Marquer une tâche comme terminée."""
    rows = lire_taches()
    tache = marquer_tache_comme_terminee(rows, task_id)
    if tache:
        typer.echo(f"Tâche marquée comme terminée : {tache}")
    else:
        typer.echo(f"Aucune tâche trouvée avec l'ID : {task_id}")

@app.command()
def rm(task_id: int):
    """ Supprimer une tâche de la liste des tâches."""
    rows = lire_taches()
    tache = supprimer_tache(rows, task_id)
    if tache:
        typer.echo(f"[red]Tâche supprimée : {tache}[/red]")
    else:
        typer.echo(f"Aucune tâche trouvée avec l'ID : {task_id}")

if __name__ == "__main__":
    app()
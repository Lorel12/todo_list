from typing import *
from dataclasses import dataclass, asdict, field


@dataclass
class Task:
    """ Représente une tâche dans la liste des tâches. """
    id: int
    title: str
    tags: List[str]
    due: Optional[str]
    done: bool
    creadted_at: str


    def to_dict(self):
        return asdict(self)
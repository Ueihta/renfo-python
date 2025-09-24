from typing import Optional
from dataclasses import dataclass

@dataclass
class CoursEntite:
    id: int
    nom: str
    professeur_id: int
    description: Optional[str] = None
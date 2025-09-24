from dataclasses import dataclass, field

@dataclass
class EleveEntite:
    id: int
    nom: str
    prenom: str
    email: str
    cours_ids: list[int] = field(default_factory=list)
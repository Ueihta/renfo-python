from ecole.domain.entite.cours_entite import CoursEntite
from typing import Union, Any
from dataclasses import asdict

class BaseAdaptateur:
    def __init__(self):
        pass

    def entite_serialisation(self, entite: Any) -> Union[dict, list[dict]]:
        return asdict(entite)

class CoursAdaptateur(BaseAdaptateur):
    def __init__(self):
        super().__init__()

    def infrastructure_vers_entite(self, cours_infrastructure: Union[dict, list]) -> Union[list[CoursEntite], CoursEntite]:
        if isinstance(cours_infrastructure, list):
            return [self.infrastructure_vers_entite(cours) for cours in cours_infrastructure]
        elif isinstance(cours_infrastructure, dict):
            return CoursEntite(
                id=cours_infrastructure["id"],
                nom=cours_infrastructure["nom"],
                description=cours_infrastructure["description"],
                professeur_id=cours_infrastructure["professeur_id"]
            )

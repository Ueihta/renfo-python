from ecole.domain.repositories.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.entite.eleve_entite import EleveEntite

class EleveRepository(EleveRepositoryInterface):
    def __init__(self):
        self.eleves = ['EleveEntite(1, "Alice", ["Math", "Science"]),']

    def recuperer_tous_les_eleves(self) -> list[EleveEntite]:
        return self.eleves

    def ajouter_eleve(self, eleve: EleveEntite):
        self.eleves.append(eleve)

    def recuperer_eleve_par_id(self, eleve_id: int) -> EleveEntite :
        for eleve in self.eleves:
            if eleve_id == eleve_id:
                return eleve
        return EleveEntite(0, "", [])
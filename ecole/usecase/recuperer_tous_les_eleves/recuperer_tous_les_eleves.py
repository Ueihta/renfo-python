from ecole.domain.repositories.eleve_repository_interface import EleveRepositoryInterface
from ecole.domain.entite.eleve_entite import EleveEntite
from ecole.architecture.repositories.eleve_repository import EleveRepository

class RecupererTousLesEleves:
    def __init__(self):
        self.eleve_repository: EleveRepositoryInterface = EleveRepository()

    def executer(self) -> list[EleveEntite]:
        return self.eleve_repository.recuperer_tous_les_eleves()
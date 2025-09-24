from abc import ABC, abstractmethod
from ecole.domain.entite.eleve_entite import EleveEntite

class EleveRepositoryInterface(ABC):
    @abstractmethod
    def recuperer_tous_les_eleves(self) -> list[EleveEntite]:
        pass

    @abstractmethod
    def recuperer_eleve_par_id(self, eleve_id: int) -> EleveEntite:
        pass
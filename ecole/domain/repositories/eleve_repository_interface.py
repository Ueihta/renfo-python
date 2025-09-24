from abc import ABC, abstractmethod
from ecole.domain.entite.eleve_entite import EleveEntite

class EleveRepositoryInterface(ABC):
    @abstractmethod
    def recuperer_tous_les_eleves(self) -> list[EleveEntite]:
        pass
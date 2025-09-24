from abc import ABC, abstractmethod
from ecole.domain.entite.professeur_entite import ProfesseurEntite

class ProfesseurRepositoryInterface(ABC):
    @abstractmethod
    def recuperer_tous_les_profs(self) -> list[ProfesseurEntite]:
        pass
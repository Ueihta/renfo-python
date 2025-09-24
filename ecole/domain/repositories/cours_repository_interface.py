from abc import ABC, abstractmethod
from ecole.domain.entite.cours_entite import CoursEntite

class CoursRepositoryInterface(ABC):    
    @abstractmethod
    def recuperer_tous_les_cours(self) -> list[CoursEntite]:
        pass

    @abstractmethod
    def recupere_cours_par_professeur_id(self, professeur_id: int) -> list[CoursEntite]:
        pass

    @abstractmethod
    def recuperer_cours_par_id(self, cours_id: int) -> list[CoursEntite] :
        pass
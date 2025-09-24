from ecole.domain.entite.cours_entite import CoursEntite
from ecole.domain.repositories.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.repositories.eleve_repository_interface import EleveRepositoryInterface
from ecole.architecture.repositories.eleve_repository import EleveRepository
from ecole.architecture.repositories.cours_repository import CoursRepository

class AjouterCoursAUnEleve:
    def __init__(self):
        self.eleve_repository = EleveRepository()
        self.cours_repository = CoursRepository()

    def executer(self, eleve_id: int, cours_id: int) -> list[CoursEntite]:
        eleve = self.eleve_repository.recuperer_eleve_par_id(eleve_id)
        cours = self.cours_repository.recuperer_cours_par_id(cours_id)
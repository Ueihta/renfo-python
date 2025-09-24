from ecole.domain.repositories.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.entite.cours_entite import CoursEntite
from ecole.architecture.repositories.cours_repository import CoursRepository


class RecupererCoursProfesseurParId:
    def __init__(self):
        self.cours_repository = CoursRepository()

    def executer(self, professeur_id: int) -> list[CoursEntite]:
        return self.cours_repository.recupere_cours_par_professeur_id(professeur_id)
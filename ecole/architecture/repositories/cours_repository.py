from ecole.domain.repositories.cours_repository_interface import CoursRepositoryInterface
from ecole.domain.entite.cours_entite import CoursEntite
from ecole.architecture.adaptateurs.cours_adaptateur import CoursAdaptateur
from ecole.architecture.db.data import COURS

class CoursRepository(CoursRepositoryInterface):
    def recuperer_tous_les_cours(self) -> list[CoursEntite]:
        cours = COURS
        return CoursAdaptateur().infrastructure_vers_entite(cours)

    def recupere_cours_par_professeur_id(self, professeur_id: int) -> list[CoursEntite]:
        cours = COURS
        cours_professeur_cible = []
        for cour in cours:
            if cour["professeur_id"] == professeur_id:
                cours_professeur_cible.append(cour)
        return CoursAdaptateur().infrastructure_vers_entite(cours_professeur_cible)
    
    def recuperer_cours_par_id(self, cours_id: int) -> list[CoursEntite] :
        cours = COURS
        cours_eleve_cible = []
        for cour in cours:
            if cour["id"] == cours_id:
                cours_eleve_cible.append(cour)
        return CoursAdaptateur().infrastructure_vers_entite(cours_eleve_cible)
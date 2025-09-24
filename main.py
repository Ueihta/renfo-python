from ecole.usecase.recuperer_cours_proffesseur_par_id.recuperer_cours_professeur_par_id import RecupererCoursProfesseurParId
from ecole.usecase.recuperer_tous_les_eleves.recuperer_tous_les_eleves import RecupererTousLesEleves
from ecole.usecase.ajouter_cours_a_un_eleve.ajouter_cours_a_un_eleve import AjouterCoursAUnEleve

if __name__ == "__main__":
    usecase = RecupererCoursProfesseurParId()
    cours = usecase.executer(1)
    print(cours)

    usecase = RecupererTousLesEleves()
    eleves = usecase.executer()
    print(eleves)

    usecase = AjouterCoursAUnEleve()
    usecase.executer(1, 2)
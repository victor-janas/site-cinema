import os,pymysql
from configDB import dbConnect,serveurConnect
from creation_base_cinema import createBaseMySQL
from requetes import Affichage1,Affichage1_,Affichage1__,Affichage1___ ,Affichage2, Affichage3, Affichage4, Affichage5, Affichage6, Affichage7, Affichage8, Affichage9
from requetes import Affichage9_, Affichage9__, Affichage10, Insert1, Insert2, Insert3, Insert4
from requetes import Insert5, Insert6, Delete1, Delete2, Delete3, Delete4, Delete5, Delete6, Update1
from requetes import Update1_, Update2_, Update2, Update3, Update4

def afficheMenu(choixActions : list ) -> None :
    """ Affichage du menu """
    print ("Choix possibles :")
    for ch  in choixActions:
        print (f'{choixActions.index(ch)+1} : {ch[0]}')
    print (f'{len(choixActions)+1} : Quitter')

def PrintFilmTitre():
    print(Affichage1())

def PrintByYear():
    print(Affichage1_())

def PrintByPrix():
    print(Affichage1__())

def PrintRecette():
    print(Affichage1___())

def PrintActeurFilm():
    titre=input("Entrez le nom du film : ")
    print(Affichage2(titre))
    
def PrintRealisateurFilm():
    titre=input("Entrez le nom du film : ")
    print(Affichage3(titre))

def PrintGensNation():
    Nation=input("Entrez la nationalité (Guatemala/Israel/France/USA/Nouvelle-Zelande/Italie/Chili/Angleterre/Japon/Allemagne/Espagne/Belgique): ")
    Nationz=Nation
    print(Affichage4(Nation,Nationz))

def PrintFilmSalle():
    Salle=input("Entrez la salle souhaitée (de 1 à 10) : ")
    print(Affichage5(Salle))

def PrintSalleFilm():
    Salle=input("Entrez le film souhaité : ")
    print(Affichage6(Salle))

def PrintCategorie():
    Categorie=input('Choississez la catégorie parmi (policier,fantastique,aventure,psychologique,documentaire,historique,autre) : ')
    print(Affichage7(Categorie))

def PrintAnnee():
    Annee=int(input("Entrez l'année souhaitée : "))
    print(Affichage8(Annee))

def PrintDuree():
    Duree=input("Entrez 1 pour moins d'1h35, 2 pour entre 1h35 et 2h, 3 pour plus de 2h : ")
    if Duree=='1':
        print(Affichage9())
    elif Duree=="2":
        print(Affichage9_())
    elif Duree=="3":
        print(Affichage9__())
    else:
        print("valeur incorrecte")

def PrintReservations():
    print(Affichage10())

def InsertFilm():
    tit=input("Entrez le nom du film : ")
    dure=int(input("Entrez la durée du film en minutes : "))
    Annee=int(input("Entrez l'annee de tournage du film : "))
    catego=input("Entrez la catégorie du film (choix possibles : policier,fantastique,aventure,psychologique,documentaire,historique,autre) : ")
    desc=input("Insérer une description : ")
    inter=input("Entrez Oui s'il y a une interdiction ou Non sinon : ")
    prix=int(input("Entrez le prix : "))
    if inter=='Oui' or inter=='Non' and catego=='policier' or catego=='fantastique' or catego=='aventure' or catego=='psychologique' or catego=='documentaire' or catego=='historique' or catego=='autre' :
        print(Insert1(tit,dure,Annee,catego,desc,inter,prix))
    else:
        print("la categorie ou l'interdiction est incorrecte")

def InsertParticipant():
    nom=input("Entrez le nom : ")
    Prenom=input("Entrez le prénom : ")
    jour = int(input("Maintenant sa date de Naissance , d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    Date = f"{int(annee):04d}-{int(mois):02d}-{int(jour):02d}"
    nati=input("Entrez le pays de la personne : ")
    print(Insert2(nom,Prenom,Date,nati))
    
def InsertFilmActeur():
    nom=input("Mettre le nom de l'acteur (il doit déjà exister dans la base) : ")
    prenom=input("Mettre le prénom de l'acteur (il doit déjà exister dans la base) : ")
    titre=input("Mettre le titre du film (il doit déjà exister dans la base) : ")
    print(Insert3(nom,prenom,titre))

def InsertFilmRealisateur():
    nom=input("Mettre le nom du réalisateur (il doit déjà exister dans la base) : ")
    prenom=input("Mettre le prénom du réalisateur (il doit déjà exister dans la base) : ")
    titre=input("Mettre le titre du film (il doit déjà exister dans la base) : ")
    print(Insert4(nom,prenom,titre))

def InsertSeance():
    titre=input("Entrez le nom du film (doit être présent dans la base) : ")
    jour = int(input("Pour la date, d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"
    salle=int(input("Mettre la salle (de 1 à 10) :"))
    nbPlace=int(input("Mettre le nombre maximum de places : "))
    print(Insert5(horaire,salle,titre,nbPlace))

def InsertRes():
    nom=input("Entrez le nom de la personne : ")
    prenom=input("Entrez le prénom de la personne : ")
    titre=input("Entrez le nom du film (doit être dans la base): ")
    jour = int(input("Pour la date (doit être dans la base), d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"  
    print(Insert6(nom,prenom,titre,horaire))

def DeleteFilm():
    tit=input("Entrez le nom du film (doit être dans la base) : ")
    Delete1(tit)
    print('\n')

def DeleteParticipant():
    Nom=input("Entrez le nom de la personne (doit être dans la base) : ")
    Prenom=input("Entrez le prénom de la personne (doit être dans la base) : ")
    Delete2(Nom,Prenom)
    print('\n')

def DeleteFilmActeur():
    Nom=input("Entrez le nom de l'acteur (doit être dans la base) : ")
    Prenom=input("Entrez le prénom de l'acteur (doit être dans la base) : ")
    tit=input("Entrez le nom de son film (doit être dans la base) : ")
    Delete3(Nom,Prenom,tit)
    print("\n")

def DeleteFilmRealisateur():
    Nom=input("Entrez le nom du réalisateur (doit être dans la base) : ")
    Prenom=input("Entrez le prénom du réalisateur (doit être dans la base) : ")
    tit=input("Entrez le nom de son film (doit être dans la base) : ")
    Delete4(Nom,Prenom,tit)
    print("\n")

def DeleteSeance():
    titre=input("Entrez le nom du film (doit être présent dans la base) : ")
    jour = int(input("Pour la date, d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"
    salle=int(input("Mettre la salle (de 1 à 10) :"))
    Delete5(horaire,salle,titre)
    print("\n")

def DeleteReservation():
    nom=input("Entrez le nom de la personne : ")
    prenom=input("Entrez le prénom de la personne : ")
    titre=input("Entrez le nom du film (doit être dans la base): ")
    jour = int(input("Pour la date (doit être dans la base), d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"  
    Delete6(nom,prenom,titre,horaire)
    print("\n")

def UpdateFilm():
    titre=input("Mettre le titre actuel du film (doit être dans la base) : ")
    print(Update1_(titre))
    newtitre =input("Entrez le nouveau nom du titre : ")
    duree=int(input("Entrez la nouvelle durée du film : "))
    anneeTournage=int(input("Entrez la nouvelle année de tournage : "))
    catego=input("Entrez la  nouvelle catégorie du film (choix possibles : policier,fantastique,aventure,psychologique,documentaire,historique,autre) : ")
    desc=input("Entrez une nouvelle description : ")
    inter=input("Entrez Oui s'il y a une interdiction ou Non sinon : ")
    prix=int(input("Entrez le prix : "))
    if inter=='Oui' or inter=='Non' and catego=='policier' or catego=='fantastique' or catego=='aventure' or catego=='psychologique' or catego=='documentaire' or catego=='historique' or catego=='autre' :
        print(Update1(titre,newtitre,duree,anneeTournage,catego,desc,inter,prix))
    else:
        print("la categorie ou l'interdiction est incorrecte")

def UpdateParticipant():
    Nom=input("Mettre le nom actuel de la personne (doit être dans la base) : ")
    Prenom=input("Mettre le prénom actuel de la personne (doit être dans la base) : ")
    print(Update2_(Nom,Prenom))
    newnom=input("Etrez le nouveau nom de la personne : ")
    newprenom=input("Entrez le nouveau prénom de la personne : ")
    jour = int(input("Maintenant sa nouvelle date de Naissance , d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    Date = f"{int(annee):04d}-{int(mois):02d}-{int(jour):02d}"
    nati=input("Entrez le nouveau pays de la personne : ")
    print(Update2(Nom,Prenom,newnom,newprenom,Date,nati))

def UpdateSeance():
    titre=input("Entrez le nom du film (doit être présent dans la base) : ")
    jour = int(input("le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"
    salle=int(input("Mettre la nouvelle salle (de 1 à 10) :"))
    newjour = int(input("le jour : "))
    newmois = int(input("le mois : "))
    newannee = int(input("l'année : "))
    newheure=int(input("L'heure (hh) : "))
    newminu=int(input("Les minutes (mm) : "))
    newhoraire = f"{newannee}-{newmois}-{newjour} {newheure}:{newminu}:00"
    newnbPlace= int(input("Entrez le nombre maximum de place : "))
    print(Update3(horaire,salle,titre,newhoraire,newnbPlace))

def UpdateRes():
    nom=input("Entrez le nom de la personne : ")
    prenom=input("Entrez le prénom de la personne : ")
    titre=input("Entrez le nom du film (doit être dans la base): ")
    jour = int(input("Pour la date (doit être dans la base), d'abord le jour : "))
    mois = int(input("le mois : "))
    annee = int(input("l'année : "))
    heure=int(input("L'heure (hh) : "))
    minu=int(input("Les minutes (mm) : "))
    horaire = f"{annee}-{mois}-{jour} {heure}:{minu}:00"
    newnom=input("Entrez le nouveau nom de la personne : ")
    newprenom=input("Entrez le nouveau prénom de la personne : ")
    print(Update4(nom,prenom,titre,horaire,newnom,newprenom))
    
    
if __name__ == '__main__':
    createBaseMySQL()
    print("création de la base")
    print("Insertion des données")
    listeChoix = [
        ("afficer les titres des films",PrintFilmTitre),
        ("afficher les films par année",PrintByYear),
        ("afficher les films par prix",PrintByPrix),
        ("afficher le(s) acteur(s) d'un film",PrintActeurFilm),
        ("afficher le(s) réalisateur(s) d'un film",PrintRealisateurFilm),
        ("afficher un film avec un réalisateur ou acteur d'une certaine nationalité",PrintGensNation),
        ("afficher les films pour une certaine salle",PrintFilmSalle),
        ("afficher les séances pour un certain film",PrintSalleFilm),
        ("afficher les films selon leur catégorie",PrintCategorie),
        ("afficher les films selon leur année de parution",PrintAnnee),
        ("afficher les films selon un type de durée",PrintDuree),
        ("afficher le montant récolté par le cinéma",PrintRecette),
        ("afficher les réservations",PrintReservations),
        ("insérer un film",InsertFilm),
        ("insérer un participant",InsertParticipant),                
        ("insérer un acteur dans un film",InsertFilmActeur),
        ("insérer un réalisateur dans un film",InsertFilmRealisateur),
        ("insérer une séance",InsertSeance),
        ("insérer une réservation",InsertRes),
        ("supprimer un film",DeleteFilm),
        ("supprimer un participant",DeleteParticipant),
        ("supprimer un acteur d'un film",DeleteFilmActeur),
        ("supprimer un réalisateur d'un film",DeleteFilmRealisateur),
        ("supprimer une séance",DeleteSeance),
        ("supprimer une réservation",DeleteReservation),
        ("modifier un film",UpdateFilm),
        ("modifier un participant",UpdateParticipant),
        ("modifier une séance",UpdateSeance),
        ("modifier une réservation",UpdateRes)
        ]
    while True :
        afficheMenu(listeChoix)
        try :
            choix = int(input("Votre Choix ? : "))
            if ( choix == len(listeChoix) + 1 ):
                    break
            elif 1 <= choix and choix <= len(listeChoix):
                label, fct = listeChoix[choix-1] 
                fct()
            else :
                print ("*** Choix non valide, recommencez!")
        except IndexError as e:
            print ('*** Choix non valide, recommencez!')
        except ValueError as e :
            print ('*** Entrez un entier SVP')
        except pymysql.err.ProgrammingError as e:
            print("*** Introuvable dans la base ! \n")
        except pymysql.err.OperationalError as e:
            print("horaire incorrect ! \n")
    print ("BYE!")

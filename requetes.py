import os,pymysql
from configDB import dbConnect,serveurConnect
from creation_base_cinema import createBaseMySQL


_requetes = {
    "titre" : "select titre from film order by titre;",
    "enumtitres" : "select titre,anneeTournage from film order by titre;",
    "enumNation" : "select  distinct nationalite, nationalite from participant;",
    "enumAnnee" : "select distinct anneeTournage,anneeTournage from film order by anneeTournage;",
    "acteur" : "select prenom, nom, titre from participant join jouer using(numParticipant) join film using(numFilm) where titre= '{}';",
    "nation" : "select DISTINCT titre, nationalite from film join realiser USING(numFilm) JOIN participant USING(numParticipant) WHERE nationalite='{}' UNION SELECT DISTINCT titre, nationalite from film join jouer USING(numFilm) JOIN participant USING(numParticipant) WHERE nationalite='{}';",
    "realisateur" : "select prenom, nom, titre FROM participant JOIN realiser USING(numParticipant) JOIN film USING(numFilm) WHERE titre='{}';",
    "salle" : "SELECT titre, horaire, salle FROM film JOIN seance USING(numFilm) WHERE salle={};",
    "film" : "SELECT salle, horaire FROM film JOIN seance USING(numFilm) WHERE titre='{}';",
    "filmannee" : "SELECT titre,duree,anneeTournage,categorie,interdiction,prix from film order by anneeTournage;",
    "filmprix" : "select titre,duree,anneeTournage,categorie,interdiction,prix from film order by prix;",
    "categorie" : "SELECT titre, categorie FROM film WHERE categorie='{}';",
    "annee" : "SELECT titre FROM film WHERE anneeTournage={};",
    "duree" : "SELECT duree ,titre FROM film WHERE duree<=95;",
    "duree_" : "SELECT duree ,titre FROM film WHERE duree<120 and duree>95;",
    "duree__" : "SELECT duree ,titre FROM film WHERE duree>=120;",
    "reservations" : "SELECT titre, NomRes, PrenomRes, horaire FROM reservation JOIN seance USING(numSeance) JOIN film USING(numFilm);",
    "filmrecette" : "select sum(prix) from reservation join seance using(numSeance) join film using(numFilm);", 
    "insertfilm" : "insert into film (titre,duree,anneeTournage,categorie,description,interdiction,prix) values ('{}',{},{},'{}','{}','{}',{});",
    "voirfilm" : "select titre,duree,anneeTournage,categorie,description,interdiction,prix from film where titre='{}';",
    "insertparticipant" : "insert into participant (nom,prenom,dateNaissance,nationalite) values ('{}','{}','{}','{}');",
    "voirparticipant" : "select nom,prenom,dateNaissance,nationalite from participant where nom='{}' and prenom='{}' and nationalite='{}';",
    "trouvenumpartfilm" : "SELECT numFilm FROM film WHERE titre='{}' UNION SELECT numParticipant FROM participant WHERE nom='{}' and prenom='{}';",
    "relieacteurfilm" : "insert into jouer (numFilm,numParticipant) values ({},{});",
    "relierealisateurfilm" : "insert into realiser (numFilm,numParticipant) values ({},{});",
    "relieseancefilm" : "INSERT INTO seance (numFilm,horaire,salle,nbPlace) VALUES ({},'{}','{}',{});",
    "trouvenumfilm" : "select numFilm from film where titre='{}';",
    "trouvenumSeance" : "select numSeance from seance where numFilm={} and horaire='{}';",
    "relieseanceres" : "insert into reservation (numSeance,NomRes,PrenomRes) values ({},'{}','{}');",
    "seanceres" : "select NomRes,PrenomRes,titre,horaire from reservation join seance using(numSeance) join film using(numFilm) where numSeance={} and NomRes='{}' and PrenomRes='{}';",
    "deletefilm" : "delete from film where titre='{}';",
    "deleteparticipant" : "delete from participant where nom='{}' and prenom='{}';",
    "preuve" : "select titre,horaire,salle,nbPlace from seance join film using(numFilm) where titre='{}' and salle='{}';",
    "deleteacteurfilm" : "delete from jouer where numFilm={} and numParticipant={};",
    "deleterealisateurfilm" : "delete from realiser where numFilm={} and numParticipant={};",
    "deleteseancefilm" : "delete from seance where numFilm={} and horaire='{}' and salle='{}';",
    "deletereservation" : "delete from reservation where numSeance={} and NomRes='{}' and PrenomRes='{}';",
    "filmall" : "select titre,duree,anneeTournage,categorie,description,interdiction,prix from film where titre='{}';",
    "updatefilm" : "UPDATE film SET titre='{}',duree={},anneeTournage={},categorie='{}',description='{}',interdiction='{}', prix={} WHERE titre='{}';",
    "participantall" : "select nom,prenom,dateNaissance,nationalite from participant where nom='{}' and prenom='{}';",
    "updateparticipant" : "UPDATE participant SET nom='{}', prenom='{}', dateNaissance='{}', nationalite='{}' where nom='{}' and prenom='{}';",
    "updateseance" : "UPDATE seance SET horaire='{}',salle='{}', nbPlace={} where numFilm={} and horaire='{}';",
    "filmActeur" : "SELECT nom,prenom,titre,description,prix from participant join jouer USING(numParticipant) JOIN film using(numFilm) where nom='{}' and prenom='{}';",
    "filmReal" : "SELECT nom,prenom,titre,description,prix from participant join realiser USING(numParticipant) JOIN film using(numFilm) where nom='{}' and prenom='{}';",
    "filmInterdit" : "SELECT titre,description,prix,anneeTournage,categorie,duree from film where interdiction='oui';",
    "FilmSeance" : "SELECT titre,TIME(horaire),DATE(horaire) FROM seance JOIN film USING(numFilm) WHERE titre='{}';",
    "SalleFilm" : "SELECT titre, TIME(horaire), DATE(horaire) FROM seance JOIN film USING(numFilm) WHERE salle={};",
    "DateSeance" : "SELECT titre,TIME(horaire) FROM seance JOIN film USING(numFilm) WHERE DATE(horaire) = '{}';",
    "FindResDate" : "SELECT PrenomRes, NomRes, titre, DATE(horaire), TIME(horaire) from reservation JOIN seance USING(numSeance) JOIN film USING(numFilm) WHERE DATE(horaire)='{}';",
    "FindResTitre" : "SELECT PrenomRes, NomRes, titre, DATE(horaire), TIME(horaire) from reservation JOIN seance USING(numSeance) JOIN film USING(numFilm) WHERE titre='{}';",
    "FindInformations" : "SELECT prenom,nom from participant JOIN realiser USING(numParticipant) JOIN film USING(numFilm) where titre='{}' UNION SELECT prenom,nom from participant JOIN jouer USING(numParticipant) JOIN film USING(numFilm) WHERE titre='{}';",
    "SeanceNom" : "SELECT PrenomRes, NomRes, titre, DATE(horaire), TIME(horaire) from reservation JOIN seance USING(numSeance) JOIN film USING(numFilm) WHERE PrenomRes='{}' and NomRes='{}';",
    "updatereservation" : "UPDATE reservation set NomRes='{}',PrenomRes='{}' where numSeance={} and NomRes='{}' and PrenomRes='{}';"
    }

def isoDate2String(date : str ) -> str :
    """ fonction de conversion d'une date-chaîne au format ISO (yyyy-mm-jj)
            au format "habituel" (jj/mm/aaaa) 
    """
    d = date.split('-')
    s= d[2]+"/"+ d[1]+"/"+d[0]
    return s

def FindResTitre(titre):
    req=_requetes["FindResTitre"].format(titre)
    return execute(req)

def FindInformations(titre,titres):
    req=_requetes["FindInformations"].format(titre,titres)
    return execute(req) 

def FindResDate(date):
    req=_requetes["FindResDate"].format(date)
    return execute(req)    

def FindResNom(prenom,nom):
    req=_requetes["SeanceNom"].format(prenom,nom)
    return execute(req)

def filmInterdit():
    req=_requetes["filmInterdit"]
    return execute(req)

def FindDate(date):
    req=_requetes["DateSeance"].format(date)
    return execute(req)

def FindFilmDate(titre):
    req=_requetes["FilmSeance"].format(titre)
    return execute(req)

def FindSalleFilmWeb(salle: int):
    req=_requetes["SalleFilm"].format(salle)
    return execute(req)

def filmTitre():
    req=_requetes["titre"]
    return execute((req))

def FilmTitre():
    req=_requetes["enumtitres"]
    return execute(req)

def FilmNation():
    req=_requetes["enumNation"]
    return execute(req)

def FilmAnnee():
    req=_requetes["enumAnnee"]
    return execute(req)


def filmReal(nom,prenom):
    req=_requetes["filmReal"].format(nom,prenom)
    return execute(req)

def filmActeur(nom,prenom):
    req=_requetes["filmActeur"].format(nom,prenom)
    return execute(req)

def filmYear():
    req=_requetes["filmannee"]
    return execute(req)

def filmPrix():
    req=_requetes["filmprix"]
    return execute((req))

def filmRecette():
    req=_requetes["filmrecette"]
    return execute((req))

def FindActeurFilm(mot : str):
    req=_requetes["acteur"].format(mot)
    return(execute(req))

def FindFilm(titre):
    req=_requetes['filmall'].format(titre)
    return(execute(req))

def FindParticipant(nom,prenom):
    req=_requetes['participantall'].format(nom,prenom)
    return(execute(req))

def FindRealisateurFilm(mot:str):
    req=_requetes["realisateur"].format(mot)
    return(execute(req))

def FindFilmSalle(mot:str):
    req=_requetes["salle"].format(mot)
    return(execute(req))

def FindSalleFilm(mot:str):
    req=_requetes['film'].format(mot)
    return(execute(req))

def FindFilmNation(mot :str,motz:str):
    req=_requetes["nation"].format(mot,motz)
    return(execute(req))

def FindCategorie(mot:str):
    req=_requetes['categorie'].format(mot)
    return(execute(req))

def FindAnnee(mot:str):
    req=_requetes['annee'].format(mot)
    return(execute(req))

def FindDuree():
    req=_requetes['duree']
    return(execute(req))

def FindDuree_():
    req=_requetes['duree_']
    return(execute(req))

def FindDuree__():
    req=_requetes['duree__']
    return(execute(req))

def FindReservations():
    req=_requetes['reservations']
    return(execute(req))

def FindAjout(titre:str):
    req=_requetes['voirfilm'].format(titre)
    return(execute(req))

def Findparti(nom,prenom,nati):
    req=_requetes['voirparticipant'].format(nom,prenom,nati)
    return(execute(req))

def FindPreuve(titre,salle):
    req=_requetes['preuve'].format(titre,salle)
    return(execute(req))

def FindSeanceRes(nom,prenom,numSeance):
    req=_requetes['seanceres'].format(numSeance,nom,prenom)
    return(execute(req))

def Insert1Web(titre:str,duree:int,anneeTournage:int,categorie:str,description:str,interdiction:str,prix:int):
    req=_requetes['insertfilm'].format(titre,duree,anneeTournage,categorie,description,interdiction,prix)
    return execute(req)

def Insert1(titre:str,duree:int,anneeTournage:int,categorie:str,description:str,interdiction:str,prix:int):
    req=_requetes['insertfilm'].format(titre,duree,anneeTournage,categorie,description,interdiction,prix)
    execute(req)
    return (Affichage11(titre))

def Insert2(nom,prenom,date,nati):
    req=_requetes['insertparticipant'].format(nom,prenom,date,nati)
    execute(req)
    return(Affichage12(nom,prenom,nati))

def Insert2Web(nom,prenom,date,nati):
    req=_requetes['insertparticipant'].format(nom,prenom,date,nati)
    return execute(req)

def Insert3_(nom:str,prenom:str,titre:str):
    req=_requetes['trouvenumpartfilm'].format(titre,nom,prenom)
    return(execute(req))

def Insert3(nom:str,prenom:str,titre:str):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['relieacteurfilm'].format(numFilm,numParticipant)
    execute(req)
    s=''
    for k in FindActeurFilm(titre):
        s=s+Rend3(k)+"\n"
    return s

def Insert3Web(nom:str,prenom:str,titre:str):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['relieacteurfilm'].format(numFilm,numParticipant)
    execute(req)

def Insert4Web(nom:str,prenom:str,titre:str):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['relierealisateurfilm'].format(numFilm,numParticipant)
    execute(req)

def Insert4(nom:str,prenom:str,titre:str):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['relierealisateurfilm'].format(numFilm,numParticipant)
    execute(req)
    s=''
    for k in FindRealisateurFilm(titre):
        s=s+Rend3(k)+"\n"
    return s

def Insert5_(horaire,salle,titre):
    req=_requetes['trouvenumfilm'].format(titre)
    return(execute(req))

def Insert5(horaire,salle,titre,nbPlace):
    ch=''
    for k in Insert5_(horaire,salle,titre):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numFilm=ju[0]
    req=_requetes['relieseancefilm'].format(numFilm,horaire,salle,nbPlace)
    execute(req)
    s=''
    for k in FindPreuve(titre,salle):
        s=s+Rend4(k)+"\n"
    return s

def Insert5Web(horaire,salle,titre,nbPlace):
    ch=''
    for k in Insert5_(horaire,salle,titre):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numFilm=ju[0]
    req=_requetes['relieseancefilm'].format(numFilm,horaire,salle,nbPlace)
    execute(req)

def Insert6_(nom,prenom,titre,horaire):
    req=_requetes['trouvenumfilm'].format(titre)
    return(execute(req))

def Insert6__(nom,prenom,titre,horaire):
    ch=''
    for k in Insert6_(nom,prenom,titre,horaire):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numFilm=ju[0]
    req=_requetes['trouvenumSeance'].format(numFilm,horaire)
    return(execute(req))

def Insert6Web(nom,prenom,date,hor,titre):
    newhoraire=date+' '+hor
    ch=''
    for k in Insert6__(nom,prenom,titre,newhoraire):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numSeance=ju[0]
    req=_requetes['relieseanceres'].format(numSeance,nom,prenom)
    execute(req)
    s=FindSeanceRes(nom,prenom,numSeance)
    return s
   
def Insert6(nom,prenom,titre,horaire):
    ch=''
    for k in Insert6__(nom,prenom,titre,horaire):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numSeance=ju[0]
    req=_requetes['relieseanceres'].format(numSeance,nom,prenom)
    execute(req)
    s=''
    for k in FindSeanceRes(nom,prenom,numSeance):
        s=s+Rend4(k)+"\n"
    return s

def Delete1(tit):
    req=_requetes['deletefilm'].format(tit)
    execute(req)

def Delete2(nom,prenom):
    req=_requetes['deleteparticipant'].format(nom,prenom)
    execute(req)

def Delete3(nom,prenom,titre):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['deleteacteurfilm'].format(numFilm,numParticipant)
    execute(req)

def Delete4(nom,prenom,titre):
    ch=''
    for k in Insert3_(nom,prenom,titre):
        ch=ch+Rend1(k)+'/'
    numFilm, numParticipant= map(int, ch.split("/")[:-1])
    req=_requetes['deleterealisateurfilm'].format(numFilm,numParticipant)
    execute(req)
    
def Delete5(horaire,salle,titre):
    ch=''
    for k in Insert5_(horaire,salle,titre):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numFilm=ju[0]
    req=_requetes['deleteseancefilm'].format(numFilm,horaire,salle)
    execute(req)

def Delete6(nom,prenom,titre,horaire):
    ch=''
    for k in Insert6__(nom,prenom,titre,horaire):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numSeance=ju[0]
    req=_requetes['deletereservation'].format(numSeance,nom,prenom)
    execute(req)

def Update1_(titre):
    s=''
    for k in FindFilm(titre):
        s=s+Rend7(k)+"\n"
    return s

def Update1(titre,newtitre,duree,annee,catego,desc,inter,prix):
    req=_requetes['updatefilm'].format(newtitre,duree,annee,catego,desc,inter,prix,titre)
    execute(req)
    s=''
    for k in FindFilm(newtitre):
        s=s+Rend7(k)+"\n"
    return s

def Update2_(nom,prenom):
    s=''
    for k in FindParticipant(nom,prenom):
        s=s+Rend4(k)+"\n"
    return s

def Update2(Nom,Prenom,newnom,newprenom,Date,nati):
    req=_requetes['updateparticipant'].format(newnom,newprenom,Date,nati,Nom,Prenom)
    execute(req)
    s=''
    for k in FindParticipant(newnom,newprenom):
        s=s+Rend4(k)+"\n"
    return s

def Update3(horaire,salle,titre,newhoraire,newnbPlace):
    ch=''
    for k in Insert5_(horaire,salle,titre):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numFilm=ju[0]
    req=_requetes['updateseance'].format(newhoraire,salle,newnbPlace,numFilm,horaire)
    execute(req)
    s=''
    for k in FindPreuve(titre,salle):
        s=s+Rend4(k)+"\n"
    return s

def Update4(nom,prenom,titre,horaire,newnom,newprenom):
    ch=''
    for k in Insert6__(nom,prenom,titre,horaire):
        ch=ch+Rend1(k)+'/'
    ju=ch.split("/")
    numSeance=ju[0]
    req=_requetes['updatereservation'].format(newnom,newprenom,numSeance,nom,prenom)
    execute(req)
    s=''
    for k in FindSeanceRes(newnom,newprenom,numSeance):
        s=s+Rend4(k)+"\n"
    return s

def Rend1(mot : tuple):
    return f"{mot[0]}"

def Affichage1():
    s=''
    for k in filmTitre():
        s=s+Rend1(k)+"\n"
    return s

def Affichage1_():
    s=''
    for k in filmYear():
        s=s+Rend6(k)+"\n"
    return s

def Affichage1__():
    s=''
    for k in filmPrix():
        s=s+Rend6(k)+"\n"
    return s

def Affichage1___():
    s=''
    for k in filmRecette():
        s=s+Rend1(k)+"€"+"\n"
    return s

def Affichage2(mot:str):
    s=''
    for k in FindActeurFilm(mot):
        s=s+Rend2(k)+"\n"
    return s

def Affichage3(mot:str):
    s=''
    for k in FindRealisateurFilm(mot):
        s=s+Rend2(k)+"\n"
    return s

def Affichage4(mot:str,motz:str):
    s=''
    for k in FindFilmNation(mot,motz):
        s=s+Rend1(k)+"\n"
    return s

def Affichage5(mot:str):
    s=''
    for k in FindFilmSalle(mot):
        s=s+Rend2(k)+"\n"
    return s

def Affichage6(mot:str):
    s=''
    for k in FindSalleFilm(mot):
        s=s+Rend2(k)+"\n"
    return s

def Affichage7(mot:str):
    s=''
    for k in FindCategorie(mot):
        s=s+Rend1(k)+"\n"
    return s

def Affichage8(mot:str):
    s=''
    for k in FindAnnee(mot):
        s=s+Rend1(k)+"\n"
    return s

def Affichage9():
    s=''
    for k in FindDuree():
        s=s+Rend2(k)+"\n"
    return s

def Affichage9_():
    s=''
    for k in FindDuree_():
        s=s+Rend2(k)+"\n"
    return s

def Affichage9__():
    s=''
    for k in FindDuree__():
        s=s+Rend2(k)+"\n"
    return s

def Affichage10():
    s=''
    for k in FindReservations():
        s=s+Rend4(k)+"\n"
    return s

def Affichage11(titre:str):
    s=''
    for k in FindAjout(titre):
        s=s+Rend7(k)+"\n"
    return s

def Affichage12(nom,prenom,nati):
    s=''
    for k in Findparti(nom,prenom,nati):
        s=s+Rend4(k)+"\n"
    return s

def convertir_minutes_en_heures(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    if minutes_restantes <10:
        minutes_restantes='0'+str(minutes_restantes)
    s=str(heures)+'h'+str(minutes_restantes)
    return s


def Rend1(mot : tuple):
    return f"{mot[0]}"

def Rend2(mot :str):
    return f"{mot[0]} {mot[1]} "

def Rend3(mot :str):
    return f"{mot[0]} {mot[1]} {mot[2]}"

def Rend4(mot :str):
    return f"{mot[0]} {mot[1]} {mot[2]} {mot[3]}"

def Rend6(mot :str):
    return f"{mot[0]} /{mot[1]} /{mot[2]} /{mot[3]} /{mot[4]} /{mot[5]}"

def Rend7(mot :str):
    return f"{mot[0]} /{mot[1]} /{mot[2]} /{mot[3]} /{mot[4]} /{mot[5]} / {mot[6]}"


def AffichageWeb1():
    s=''
    for k in filmTitre():
        s=s+Rend1(k)+"<br>"
    return s


def AffichageWeb1___():
    s=''
    for k in filmRecette():
        s=s+Rend1(k)+"€"+"<br>"
    return s

def AffichageWeb2(mot):
    s=''
    for k in FindAnnee(mot):
        s=s+Rend1(k)+"<br>"
    return s

###################################################################################
def execute(req:str):
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" or "SELECT" in req :
        res = _cursorEtudiant.fetchall()
    #else :
        _dbEtudiant.commit()
    return res

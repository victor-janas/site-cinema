import cherrypy, os, os.path

from mako.template import Template
from mako.lookup import TemplateLookup
from creation_base_cinema import createBaseMySQL
from requetes import filmPrix,AffichageWeb1___, FindFilm, FilmNation, FilmAnnee, FindInformations
from requetes import isoDate2String, filmYear, AffichageWeb1, FindParticipant, filmInterdit, FindDate, FindFilmDate, FindSalleFilmWeb, FindReservations, FindResTitre, FilmTitre
from requetes import filmReal, filmActeur, AffichageWeb2, FindFilmNation, FindCategorie, FindDuree, FindDuree_, FindDuree__, convertir_minutes_en_heures, FindResNom, FindResDate
from requetes import Insert1Web, Insert2Web, Insert3Web, Insert4Web, Insert5Web, Insert6Web, Delete1, Delete2, Delete3, Delete4, Delete5, Delete6, Update1, Update2, Update3, Update4
from configDB import dbConnect

mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8', module_directory='res/tmp/mako_modules')

class InterfaceWebEtudiants(object):    
    ###### Page d'accueil #############
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()


    @cherrypy.expose
    def Recherche(self):
        mytemplate = mylookup.get_template("Recherche.html")
        return mytemplate.render()

    @cherrypy.expose
    def Seances(self):
        mytemplate = mylookup.get_template("Seances.html")
        return mytemplate.render()

    @cherrypy.expose
    def Reservation(self):
        mytemplate = mylookup.get_template("Reservation.html")
        return mytemplate.render()

    @cherrypy.expose
    def Administration(self):
        mytemplate = mylookup.get_template("Administration.html")
        return mytemplate.render()
    ###### Pages d'affichages ###########        
    @cherrypy.expose
    def affParOrdre(self):
        mytemplate = mylookup.get_template("aff_index.html")
        return mytemplate.render(film=AffichageWeb1())

    @cherrypy.expose
    def affParInfo(self):
        mytemplate = mylookup.get_template("aff_info.html")        
        return mytemplate.render(mesEtud=filmYear())

    @cherrypy.expose
    def affParPrix(self):
        mytemplate = mylookup.get_template("aff_prix.html")        
        return mytemplate.render(monEtud=filmPrix())

    @cherrypy.expose
    def affPageFilm(self):
        mytemplate = mylookup.get_template("AfficheChoixFilm.html")        
        return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffFilm(self,titre):
        if titre:
            try:
                FindFilm(titre)
                message = "Requête réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("SearchBytitre.html")
        return mytemplate.render(message=message, type=typ, mesTitres=FindFilm(titre))

    @cherrypy.expose
    def affPageParticipant(self):
        mytemplate = mylookup.get_template("affPageParticipant.html")        
        return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffParticipant(self,nom,prenom):
        if nom and prenom:
            try:
                FindParticipant(nom,prenom)
                message = "Requête réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("SearchByParticipant.html")
        return mytemplate.render(message=message, type=typ, mesTitres=FindParticipant(nom,prenom))

    @cherrypy.expose
    def affPageReal(self):
            mytemplate = mylookup.get_template("affPageReal.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffReal(self,nom,prenom):
            if nom and prenom:
                try:
                    filmReal(nom,prenom)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByReal.html")
            return mytemplate.render(message=message, type=typ, mesTitres=filmReal(nom,prenom))

    @cherrypy.expose
    def affPageActeur(self):
            mytemplate = mylookup.get_template("affPageActeur.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffActeur(self,nom,prenom):
            if nom and prenom:
                try:
                    filmActeur(nom,prenom)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByActeur.html")
            return mytemplate.render(message=message, type=typ, mesTitres=filmActeur(nom,prenom))

    @cherrypy.expose
    def affPageAnnee(self):
            mytemplate = mylookup.get_template("affPageAnnee.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffAnnee(self,annee):
            if annee :
                try:
                    AffichageWeb2(annee)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByAnnee.html")
            return mytemplate.render(message=message, type=typ, mesTitres=AffichageWeb2(annee))

    @cherrypy.expose
    def affPageNation(self):
            mytemplate = mylookup.get_template("affPageNation.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffNation(self,nations):
            if nations :
                try:
                    FindFilmNation(nations,nations)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByNation.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindFilmNation(nations,nations), Nation=nations)

    @cherrypy.expose
    def affPageInformations(self):
            mytemplate = mylookup.get_template("affPageInformations.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffInformations(self,titre):
            if titre :
                try:
                    FindInformations(titre,titre)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByInformations.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindInformations(titre,titre), Titre=titre)        

    @cherrypy.expose
    def affPageCatego(self):
            mytemplate = mylookup.get_template("affPageCatego.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffCatego(self,catego):
            if catego :
                try:
                    FindCategorie(catego)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByCatego.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindCategorie(catego), Catego=catego)

    @cherrypy.expose
    def affPageDuree(self):
            mytemplate = mylookup.get_template("affPageDuree.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffDuree(self,duree):
            if duree :
                try:
                    if duree=='1':
                        FindDuree()
                        message = "Requête réussie !"
                        typ = "success"
                        mesTitres=FindDuree()
                    if duree=='2':
                        FindDuree_()
                        message = "Requête réussie !"
                        typ = "success"
                        mesTitres=FindDuree_()
                    if duree=='3':
                        FindDuree__()
                        message = "Requête réussie !"
                        typ = "success"
                        mesTitres=FindDuree__()
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByDuree.html")
            return mytemplate.render(message=message, type=typ, Duree=mesTitres)

    @cherrypy.expose
    def affPageInterdit(self):
        mytemplate = mylookup.get_template("affPageInterdit.html")
        return mytemplate.render(film=filmInterdit())


    @cherrypy.expose
    def affPageDate(self):
            mytemplate = mylookup.get_template("affPageDate.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffDate(self,date):
            if date :
                try:
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
                date="0000-00-00"
            mytemplate = mylookup.get_template("SearchByDate.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindDate(date), Date=date)

    @cherrypy.expose
    def affPageSeance(self):
            mytemplate = mylookup.get_template("affPageSeance.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffSeance(self,titre):
            if titre :
                try:
                    FindFilmDate(titre)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchBySeance.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindFilmDate(titre), Titre=titre)


    @cherrypy.expose
    def affPageSalle(self):
            mytemplate = mylookup.get_template("affPageSalle.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffSalle(self,salle):
            if salle :
                try:
                    FindSalleFilmWeb(salle)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchBySalle.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindSalleFilmWeb(salle), Salle=salle)


    @cherrypy.expose
    def affPageRes(self):
            mytemplate = mylookup.get_template("affPageRes.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertRes(self,nom,prenom,date,horaire,titre):
        if nom and prenom and date and horaire and titre :
            try:
                Insert6Web(nom,prenom,date,horaire,titre)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertRes.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affRes(self):
        mytemplate = mylookup.get_template("aff_Res.html")
        return mytemplate.render(film=FindReservations())

    @cherrypy.expose
    def affPageResNom(self):
            mytemplate = mylookup.get_template("affPageResNom.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffResNom(self,nom,prenom):
            if nom and prenom:
                try:
                    FindResNom(prenom,nom)
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
            mytemplate = mylookup.get_template("SearchByResNom.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindResNom(prenom,nom))

    @cherrypy.expose
    def affPageResDate(self):
            mytemplate = mylookup.get_template("affPageResDate.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffResDate(self,date):
            if date :
                try:
                    message = "Requête réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"
                date="0000-00-00"
            mytemplate = mylookup.get_template("SearchByResDate.html")
            return mytemplate.render(message=message, type=typ, mesTitres=FindResDate(date), Date=date)

    @cherrypy.expose
    def affPageResTitre(self):
        mytemplate = mylookup.get_template("affPageResTitre.html")        
        return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def AffResTitre(self,titre):
        if titre:
            try:
                FindResTitre(titre)
                message = "requête réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("SearchByResTitre.html")
        return mytemplate.render(message=message, type=typ, mesTitres=FindResTitre(titre))

    @cherrypy.expose
    def affPageInsertFilm(self):
            mytemplate = mylookup.get_template("affPageInsertFilm.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertFilm(self,titre,duree,anneeTournage,categorie,description,interdiction,prix):
        if titre and duree and anneeTournage and categorie and description and interdiction and prix :
            try:
                Insert1Web(titre,duree,anneeTournage,categorie,description,interdiction,prix)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertFilm.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageInsertParticipant(self):
            mytemplate = mylookup.get_template("affPageInsertParticipant.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertParticipant(self,nom,prenom,date,nation):
        if nom and prenom and date and nation : 
            try:
                Insert2Web(nom,prenom,date,nation)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertParticipant.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageInsertRelationActeur(self):
            mytemplate = mylookup.get_template("affPageInsertRelationActeur.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertRelationActeur(self,nom,prenom,titre):
        if nom and prenom and titre : 
            try:
                Insert3Web(nom,prenom,titre)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertRelationActeur.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageInsertRelationReal(self):
            mytemplate = mylookup.get_template("affPageInsertRelationReal.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertRelationReal(self,nom,prenom,titre):
        if nom and prenom and titre : 
            try:
                Insert4Web(nom,prenom,titre)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertRelationReal.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageInsertSeance(self):
            mytemplate = mylookup.get_template("affPageInsertSeance.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def InsertSeance(self,horaire,salle,titre,nbPlace):
        if horaire and salle and titre and nbPlace : 
            try:
                Insert5Web(horaire,salle,titre,nbPlace)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("InsertSeance.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteFilm(self):
            mytemplate = mylookup.get_template("affPageDeleteFilm.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteFilm(self,titre):
        if titre : 
            try:
                Delete1(titre)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteFilm.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteParticipant(self):
            mytemplate = mylookup.get_template("affPageDeleteParticipant.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteParticipant(self,nom,prenom):
        if nom and prenom : 
            try:
                Delete2(nom,prenom)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteParticipant.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteSeance(self):
            mytemplate = mylookup.get_template("affPageDeleteSeance.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteSeance(self,horaire,salle,titre):
        if horaire and salle and titre : 
            try:
                Delete5(horaire,salle,titre)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteSeance.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteRes(self):
            mytemplate = mylookup.get_template("affPageDeleteRes.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteRes(self,nom,prenom,titre,horaire):
        if nom and prenom and titre and horaire : 
            try:
                Delete6(nom,prenom,titre,horaire)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteRes.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteRelationAct(self):
            mytemplate = mylookup.get_template("affPageDeleteRelationAct.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteRelationAct(self,nom,prenom,titre):
        if nom and prenom and titre : 
            try:
                Delete3(nom,prenom,titre)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteRelationAct.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageDeleteRelationReal(self):
            mytemplate = mylookup.get_template("affPageDeleteRelationReal.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def DeleteRelationReal(self,nom,prenom,titre):
        if nom and prenom and titre : 
            try:
                Delete4(nom,prenom,titre)
                message = "Suppression réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("DeleteRelationReal.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageUpdateFilm(self):
            mytemplate = mylookup.get_template("affPageUpdateFilm.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def UpdateFilm(self,titre):
        if titre:
            try:
                FindFilm(titre)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
            else:
                message = "Tous les champs doivent être remplis !!"
                typ = "warning"       
        mytemplate = mylookup.get_template("UpdateFilm.html")
        return mytemplate.render(message=message, type=typ,mesTitres=FindFilm(titre))

    @cherrypy.expose
    def UpdateFilm1(self,titre,newtitre,duree,annee,catego,desc,inter,prix):
        if titre and newtitre and duree and annee and catego and desc and inter and prix : 
            try:
                Update1(titre,newtitre,duree,annee,catego,desc,inter,prix)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("UpdateFilm1.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageUpdateParticipant(self):
            mytemplate = mylookup.get_template("affPageUpdateParticipant.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def UpdateParticipant(self,nom,prenom):
        if nom and prenom:
            try:
                FindParticipant(nom,prenom)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
            nom='aaaaaa'
            prenom='aaaaa'
        mytemplate = mylookup.get_template("UpdateParticipant.html")
        return mytemplate.render(message=message, type=typ, mesTitres=FindParticipant(nom,prenom))

    @cherrypy.expose
    def UpdateParticipant1(self,Nom,Prenom,newnom,newprenom,Date,nati):
        if newnom and newprenom and Date and nati and Nom and Prenom : 
            try:
                Update2(Nom,Prenom,newnom,newprenom,Date,nati)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("UpdateParticipant1.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageUpdateSeance(self):
            mytemplate = mylookup.get_template("affPageUpdateSeance.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def UpdateSeance(self,Horaire,salle,titre,newhoraire,newnbPlace):
        if Horaire and salle and titre and newhoraire and newnbPlace : 
            try:
                Update3(Horaire,salle,titre,newhoraire,newnbPlace)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("UpdateSeance.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def affPageUpdateReservation(self):
            mytemplate = mylookup.get_template("affPageUpdateReservation.html")        
            return mytemplate.render(message="veuillez remplir tous les champs ", type="info")

    @cherrypy.expose
    def UpdateReservation(self,nom,prenom,titre,horaire,newnom,newprenom):
        if nom and prenom and titre and horaire and newnom and newprenom : 
            try:
                Update4(nom,prenom,titre,horaire,newnom,newprenom)
                message = "Modification réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("UpdateReservation.html")
        return mytemplate.render(message=message, type=typ)


if __name__ == '__main__':
    createBaseMySQL()
    cherrypy.quickstart(InterfaceWebEtudiants(), '/', 'config.txt')

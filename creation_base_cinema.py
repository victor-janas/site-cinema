import os,pymysql
from configDB import dbConnect,serveurConnect

def createBaseMySQL() -> None :
     _dbEtudiant, _cursorEtudiant = serveurConnect()
     _cursorEtudiant.execute(_requetes["drop"])
     _cursorEtudiant.execute(_requetes["createBase"])
     _cursorEtudiant.execute(_requetes["use"])
     _cursorEtudiant.execute(_requetes["test1"])
     _cursorEtudiant.execute(_requetes["test2"])
     _cursorEtudiant.execute(_requetes["test3"])
     _cursorEtudiant.execute(_requetes["reqCrea1"])
     _cursorEtudiant.execute(_requetes["reqCrea2"])
     _cursorEtudiant.execute(_requetes["reqCrea3"])
     _cursorEtudiant.execute(_requetes["reqCrea4"])
     _cursorEtudiant.execute(_requetes["reqCrea5"])
     _cursorEtudiant.execute(_requetes["reqCrea6"])
     donneesFilm()
     donneesJouer()
     donneesParticipant()
     donneesRealiser()
     donneesReservation()
     donneesSeance()
     _cursorEtudiant.execute(_requetes["contrainte1"])
     _cursorEtudiant.execute(_requetes["contrainte2"])
     _cursorEtudiant.execute(_requetes["contrainte3"])
     _cursorEtudiant.execute(_requetes["contrainte4"])
     



def donneesFilm() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/film.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 7 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numFilm = champs[0]
            titre = champs[1]
            duree = champs[2]
            anneeTournage = champs[3]	
            categorie = champs[4]
            description	= champs[5]
            interdiction = champs[6]
            prix = champs[7]
            s= _requetes["insert1"].format(numFilm,titre,duree,anneeTournage,categorie,description,interdiction,prix)
            _cursorEtudiant.execute(s)
            _dbEtudiant.commit()

def donneesJouer() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/jouer.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 2 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numFilm = champs[0]
            numParticipant= champs[1] 
            s= _requetes["insert2"].format(numFilm,numParticipant)
            _cursorEtudiant.execute(s)
            _dbEtudiant.commit()

def donneesParticipant() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/participant.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 5 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numParticipant = champs[0]
            nom= champs[1]
            prenom = champs[2]
            date = champs[3]
            d = date.split('/')
            dateNaissance = d[2]+"-"+ d[1]+"-"+d[0]
            nationalite = champs[4]
            s= _requetes["insert3"].format(numParticipant,nom,prenom,dateNaissance,nationalite)
            _cursorEtudiant.execute(s)
            _dbEtudiant.commit()

def donneesRealiser() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/realiser.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 2 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numFilm = champs[0]
            numParticipant= champs[1] 
            s= _requetes["insert4"].format(numFilm,numParticipant)
            _cursorEtudiant.execute(s)
            _dbEtudiant.commit()

def donneesReservation() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/reservation.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 4 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numSeance = champs[0]
            numRes = champs[1]
            NomRes = champs[2]
            PrenomRes = champs[3]	
            s= _requetes["insert5"].format(numSeance,numRes,NomRes,PrenomRes)
            res=_cursorEtudiant.execute(s)
            _dbEtudiant.commit()

def donneesSeance() -> None:
    import csv
    _dbEtudiant, _cursorEtudiant = serveurConnect()
    _cursorEtudiant.execute(_requetes["use"])
    with open('CSV/seance.csv', newline='\n',encoding='utf-8') as csvFile :
        lignesEtud = csv.reader(csvFile,delimiter=';')
        for champs in lignesEtud :
            if len(champs) < 5 :
                print ("ligne incorrecte : <{}>, ignorée".format(champs))
                continue
            numFilm = champs[0]
            numSeance= champs[1]
            date = champs[2]
            d = date.split('/')
            horaire = d[2]+"-"+ d[1]+"-"+d[0]+" "+d[3]
            salle = champs[3]
            nbPlace = champs[4]
            s= _requetes["insert6"].format(numFilm,numSeance,horaire,salle,nbPlace)
            _cursorEtudiant.execute(s)
            _dbEtudiant.commit()

_requetes = {
     "insert1" : "INSERT INTO film (numFilm , titre, duree, anneeTournage, categorie, description, interdiction,prix) VALUES ({},'{}',{},{},'{}','{}','{}',{});",
     "insert2" : "INSERT INTO jouer (numFilm , numParticipant) VALUES ({},{});",
     "insert3" : "INSERT INTO participant (numParticipant,nom,prenom,dateNaissance,nationalite) VALUES ({},'{}','{}','{}','{}');",
     "insert4" : "INSERT INTO realiser (numFilm , numParticipant) VALUES ({},{});",
     "insert5" : "INSERT INTO reservation (numSeance,numRes,NomRes,PrenomRes) VALUES ({},{},'{}','{}');",
     "insert6" : "INSERT INTO seance (numFilm,numSeance,horaire,salle,nbPlace) VALUES ({},{},'{}','{}',{});",
     
    "drop" : "DROP DATABASE IF EXISTS cinema",
    "createBase" : "CREATE DATABASE IF NOT EXISTS cinema DEFAULT CHARACTER SET utf8",
    "use" : "USE cinema",

    "test1":"""SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";""",
    "test2":"""START TRANSACTION;""",
    "test3":"""SET time_zone = "+00:00";""",

   "reqCrea1":"""CREATE TABLE film (numFilm int NOT NULL AUTO_INCREMENT,\
      titre varchar(30) NOT NULL,\
      duree int DEFAULT NULL,\
      anneeTournage year DEFAULT NULL,\
      categorie enum('policier','fantastique','aventure','psychologique','documentaire','historique','autre') NOT NULL,\
      description text NOT NULL,\
      interdiction enum('Oui','Non'),\
      prix int ,\
      PRIMARY KEY (numFilm)
    )ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;""",

    "reqCrea2":"""CREATE TABLE jouer (numFilm int NOT NULL,\
      numParticipant int NOT NULL,\
      PRIMARY KEY (numFilm,numParticipant),
      KEY numFilm (numFilm,numParticipant),
      KEY numParticipant (numParticipant)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT;""",

    "reqCrea3":"""CREATE TABLE participant (numParticipant int NOT NULL AUTO_INCREMENT,\
      nom varchar(30) NOT NULL,\
      prenom varchar(30) NOT NULL,\
      dateNaissance date DEFAULT NULL,\
      nationalite varchar(30) DEFAULT NULL,\
      PRIMARY KEY (numParticipant)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT;""",

    "reqCrea4":"""CREATE TABLE realiser (numFilm int NOT NULL,\
      numParticipant int NOT NULL,\
      PRIMARY KEY (numFilm,numParticipant),
      KEY numFilm (numFilm,numParticipant),
      KEY numParticipant (numParticipant)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT;""",

    "reqCrea5":"""CREATE TABLE reservation (numSeance int NOT NULL,\
      numRes int NOT NULL AUTO_INCREMENT,\
      NomRes text NOT NULL,\
      PrenomRes text NOT NULL,\
      PRIMARY KEY (numRes),
      KEY numFilm (numSeance),
      KEY numParticipant (numSeance),
      KEY numSeance (numSeance),
      KEY numSeance_2 (numSeance)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT;""",

    "reqCrea6":"""CREATE TABLE seance (numFilm int NOT NULL,
      numSeance int NOT NULL AUTO_INCREMENT,\
      horaire datetime NOT NULL,\
      salle int NOT NULL,\
      nbPlace int NOT NULL,\
      PRIMARY KEY (numFilm,numSeance),
      KEY numFilm (numFilm,numSeance),
      KEY numParticipant (numSeance),
      KEY numSeance (numSeance),
      KEY numSeance_2 (numSeance)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=COMPACT;""",

     "contrainte1":"""ALTER TABLE jouer
       ADD CONSTRAINT jouer_ibfk_1 FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE,
       ADD CONSTRAINT jouer_ibfk_2 FOREIGN KEY (numParticipant) REFERENCES participant (numParticipant) ON DELETE CASCADE ON UPDATE CASCADE;""",

    "contrainte2":"""ALTER TABLE realiser
       ADD CONSTRAINT realiser_ibfk_1 FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE,
       ADD CONSTRAINT realiser_ibfk_2 FOREIGN KEY (numParticipant) REFERENCES participant (numParticipant) ON DELETE CASCADE ON UPDATE CASCADE;""",

    "contrainte3":"""ALTER TABLE reservation
       ADD CONSTRAINT reservation_ibfk_1 FOREIGN KEY (numSeance) REFERENCES seance (numSeance) ON DELETE CASCADE ON UPDATE CASCADE;""",

    "contrainte4":"""ALTER TABLE seance
       ADD CONSTRAINT seance_ibfk_1 FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE;
       """}


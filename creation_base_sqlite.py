import sqlite3
import os

CreateTableFilm = """
CREATE TABLE IF NOT EXISTS film (
    numFilm INTEGER PRIMARY KEY AUTOINCREMENT,
    titre VARCHAR(30) NOT NULL,
    duree INTEGER DEFAULT NULL,
    anneeTournage INTEGER DEFAULT NULL,
    categorie TEXT NOT NULL CHECK(categorie IN ('policier','fantastique','aventure','psychologique','documentaire','historique','autre')),
    description TEXT NOT NULL,
    interdiction TEXT NOT NULL CHECK(interdiction IN ('Oui','Non')),
    prix INTEGER
);"""

CreateTableJouer = """
CREATE TABLE jouer (
    numFilm INTEGER NOT NULL,
    numParticipant INTEGER NOT NULL,
    PRIMARY KEY (numFilm, numParticipant),
    FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (numParticipant) REFERENCES participant (numParticipant) ON DELETE CASCADE ON UPDATE CASCADE
);"""

CreateTableParticipant = """
CREATE TABLE participant (
    numParticipant INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(30) NOT NULL,
    prenom VARCHAR(30) NOT NULL,
    dateNaissance DATE DEFAULT NULL,
    nationalite VARCHAR(30) DEFAULT NULL
);"""

CreateTableRealiser = """
CREATE TABLE realiser (
    numFilm INTEGER NOT NULL,
    numParticipant INTEGER NOT NULL,
    PRIMARY KEY (numFilm, numParticipant),
    FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (numParticipant) REFERENCES participant (numParticipant) ON DELETE CASCADE ON UPDATE CASCADE
);"""

CreateTableReservation = """
CREATE TABLE reservation (
    numSeance INTEGER NOT NULL,
    numRes INTEGER NOT NULL PRIMARY KEY,
    NomRes TEXT NOT NULL,
    PrenomRes TEXT NOT NULL,
    FOREIGN KEY (numSeance) REFERENCES seance (numSeance) ON DELETE CASCADE ON UPDATE CASCADE
);"""

CreateTableSeance = """
CREATE TABLE seance (
    numFilm INTEGER NOT NULL,
    numSeance INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    horaire DATETIME NOT NULL,
    salle INTEGER NOT NULL,
    nbPlace INTEGER NOT NULL,
    FOREIGN KEY (numFilm) REFERENCES film (numFilm) ON DELETE CASCADE ON UPDATE CASCADE
);"""

import sqlite3

InsertFilm = """
INSERT INTO film (numFilm, titre, duree, anneeTournage, categorie, description, interdiction, prix) VALUES
     (5, 'Sicko', 110, 2007, 'documentaire', 'Le cineaste Michael Moore jette un regard critique sur le systeme de sante americain
', 'Non',5),
     (6, 'Bowling for Columbine', 100, 2002, 'documentaire', 'Michael Moore enquete sur la violence provoquee par les armes a feu aux Etats-Unis. Son point de depart est la tragedie du lycee Columbine dans le Colorado en 1999. Des dizaines de lyceens avaient alors ete assassines par deux de leurs camarades.
', 'Non',5),
     (7, 'Le Decameron', 107, 1971, 'psychologique', 'Un film compos de huit sketches adaptes des fameux contes paillards de Boccace.
', 'Non',4),
     (8, 'Le Seigneur des Anneaux', 140, 2001, 'fantastique', 'Prenant place dans le monde fictionnel de la Terre du Milieu, il suit la quete du hobbit Frodon Sacquet (Frodo Bessac), qui doit detruire lAnneau unique afin que celui-ci ne tombe pas entre les mains de Sauron, le Seigneur des tenebres, qui a cree.
', 'Non',5),
     (10, 'Le Grand Bleu', 183, 1988, 'aventure', 'Chef doeuvre intergenerationnel signe Luc Besson sur une musique envoutante dEric Serra, Le Grand Bleu raconte lhistoire de deux hommes definitivement lies a la mer, Jacques Mayol et Enzo Molinari, plongeurs en apnee, mais aussi une magnifique histoire damour avec Johana qui represente la terre.
', 'Non',4),
     (11, 'Star Wars I', 135, 1999, 'fantastique', 'Lhistoire de Star Wars, se deroule dans une galaxie qui est le theatre daffrontements entre les Chevaliers Jedi et les Seigneurs Sith, personnes antagonistes sensibles a la Force, un champ energetique mysterieux leur procurant des pouvoirs psychiques.
', 'Non',5),
     (12, 'La vie des autres', 137, 2006, 'psychologique', 'Le film La Vie des autres evoque une page sombre de lhistoire allemande, celle du controle politique et ideologique exerce par les autorites de lancienne RDA sur sa propre population sans aucun respect des droits humains pendant pratiquement toute la duree du regime.
', 'Non',5),
     (13, 'Ran', 155, 1985, 'historique', 'Dans le Japon du XVIe siecle, le seigneur Hidetora Ichimonji decide de se retirer et de partager son domaine entre ses trois fils, Taro, Jiro et Saburo. Mais la repartition de cet heritage va dechirer la famille.
', 'Non',5),
     (14, 'Le sourire de mona lisa', 114, 2004, 'psychologique', 'LE SOURIRE DE MONA LISA evoque non-seulement la liberalisation des moeurs mais egalement celle des femmes et de leur place dans la societe.
', 'Non',4),
     (16, 'Matador', 107, 1988, 'psychologique', 'Diego Montes, un celebre torero, doit prendre une retraite prematuree apres une blessure mal soignee. Maria Cardenal, avocate en criminologie, aime tuer ses amants lors de leurs ebats amoureux. Diego cree une ecole de tauromachie, car pour lui  arreter de tuer, cest arreter de vivre .
', 'Non',5),
     (17, 'Oceans twelve', 125, 2004, 'aventure', 'a sa sortie de prison dans le New Jersey, Daniel  Danny  Ocean sapprete a monter un coup qui semble impossible a realiser  cambrioler la reserve dargent des trois plus gros casinos de Las Vegas le Bellagio, le Mirage et le MGM Grand Las Vegas
', 'Non',5),
     (18, 'Oceans 13', 122, 2002, 'policier', 'Douce vengeance sous le ciel de Las Vegas. Danny Ocean et sa bande ne pouvaient avoir quun seul motif pour tenter leur braquage le plus audiacieux a ce jour sauver un des leurs. Mais la chance ne suffit pas toujours lorsque lon veut faire sauter The Bank.
', 'Non',5),
     (19, 'Good night, good luck', 115, 2005, 'aventure', 'Dans les annees 50, Edward R. Murrow, le presentateur du journal televise americain de CBS de lepoque, et le producteur Fred Friendly ont contribue a la chute du senateur Joseph McCarthy, a lorigine de la chasse aux communistes.
', 'Non',5),
     (20, 'Orgueils et Prejuges', 122, 2005, 'psychologique', 'La campagne anglaise a la fin du XVIIIe siecle. Mrs. Bennet et son mari sont ravis dapprendre quun jeune homme fortune  et celibataire  vient de sinstaller dans le manoir voisin. Desargentes, les Bennet se font fort de marier lune de leurs cinq filles au nouvel arrivant... Ce dernier ne tarde pas a seprendre de la belle Jane, lainee de la famille, lors dun bal de campagne.
', 'Non',5),
     (21, 'Rockn Roll', 123, 2016, 'autre', 'Guillaume Canet, comedien de 43 ans, se remet en question le jour ou, sur un plateau de tournage, sa jeune partenaire a lecran lui dit quil nest plus un objet de desir pour les femmes de la jeune generation.
', 'Non',4),
     (22, 'Deux jours, une nuit', 95, 2013, 'autre', 'Une mere de famille que lon menace de licenciee, doit mener un combat impossible contre lesprit avide dargent de ses collegues, et ainsi, tenter de les convaincre que son avenir de mere vaut plus quune simple prime.', 'Non',4),
     (23, 'Nikita', 117, 1989, 'autre', 'Le film raconte les aventures de Nikita, le surnom dune jeune femme francaise toxicomane qui fait partie dune bande de jeunes voyous sans scrupules. etant en manque, Nikita demande au chef de sa bande, son copain Rico, de lui procurer de la drogue.', 'Non',4),
     (25, 'Scream VI', 122, 2023, 'autre', 'Les survivants des derniers meurtres de Ghostface, les soeurs Samantha et Tara Carpenter et les jumeaux Chad et Mindy Meeks, quittent Woodsboro et entament un nouveau chapitre de leur vie a New York. Ils y sont a nouveau victimes dune serie de meurtres commis par un nouveau tueur Ghostface.', 'Oui', 6);
"""

InsertJouer = """
INSERT INTO jouer (numFilm, numParticipant) VALUES
     (6, 1),
     (7, 2),
     (6, 3),
     (6, 4),
     (6, 5),
     (5, 6),
     (8, 8),
     (8, 9),
     (8, 10),
     (10, 17),
     (23, 17),
     (11, 18),
     (17, 22),
     (18, 22),
     (21, 25),
     (21, 26),
     (22, 26),
     (11, 27),
     (25, 30),
     (20, 31);
"""

InsertParticipant = """
INSERT INTO participant (numParticipant, nom, prenom, dateNaissance, nationalite) VALUES
     (1, 'Moore', 'Mickael', '1954-04-23', 'USA'),
     (2, 'Pasolini', 'Paolo', '1922-03-05', 'Italie'),
     (3, 'Bush', 'Georges', '1924-06-12', 'USA'),
     (4, 'Arbenz', 'Jacobo', '1913-09-14', 'Guatemala'),
     (5, 'Pinochet', 'Augusto', '1915-11-25', 'Chili'),
     (6, 'Clinton', 'Bill', '1946-08-19', 'USA'),
     (7, 'Jackson', 'Peter', '1961-10-31', 'Nouvelle-Zelande'),
     (8, 'Wood', 'Elijah', '1981-01-28', 'USA'),
     (9, 'Astin', 'Sean', '1971-02-25', 'USA'),
     (10, 'Mac Kellen', 'Ian', '1939-05-25', 'Angleterre'),
     (11, 'Ventura', 'Lino', '1919-07-14', 'Italie'),
     (12, 'Kurosawa', 'Akira', '1910-03-23', 'Japon'),
     (13, 'Nakadai', 'Tatsuya', '1932-01-01', 'Japon'),
     (14, 'Roberts', 'Julia', '1967-10-28', 'USA'),
     (15, 'Dunst', 'Kirsten', '1982-04-20', 'USA'),
     (16, 'Besson', 'Luc', '1959-03-18', 'France'),
     (17, 'Reno', 'Jean', '1948-07-30', 'France'),
     (18, 'Portman', 'Natalie', '1981-06-09', 'Israel'),
     (19, 'Knigthley', 'Keira', '1985-03-26', 'Angleterre'),
     (20, 'Lucas', 'Georges', '1944-05-14', 'USA'),
     (21, 'Henckel von Donnersmark', 'Florian', NULL, 'Allemagne'),
     (22, 'Clooney', 'Georges', '1961-05-06', 'USA'),
     (23, 'Soderbergh', 'Steven', '1963-01-14', 'USA'),
     (24, 'Almodovar', 'Pedro', '1949-09-25', 'Espagne'),
     (25, 'Canet', 'Guillaume', '1973-04-10', 'France'),
     (26, 'Cotillard', 'Marion', '1975-09-30', 'France'),
     (27, 'Lloyd', 'Jake', '1989-03-05', 'USA'),
     (28, 'Dardenne', 'Jean-Pierre', '1951-04-21', 'Belge'),
     (29, 'Dardenne', 'Luc', '1954-03-10', 'Belge'),
     (30, 'Ortega', 'Jenna', '2002-09-27', 'USA'),
     (31, 'Knightley', 'Keira', '1985-03-26', 'Angleterre');
"""

InsertRealiser = """
INSERT INTO realiser (numFilm, numParticipant) VALUES
     (5, 1),
     (6, 1),
     (7, 2),
     (8, 7),
     (13, 12),
     (10, 16),
     (23, 16),
     (11, 20),
     (12, 21),
     (19, 22),
     (17, 23),
     (18, 23),
     (16, 24),
     (21, 25),
     (22, 28),
     (22, 29);
"""

InsertReservation = """
INSERT INTO reservation (numSeance, numRes, NomRes, PrenomRes) VALUES
     (1, 1, 'Poutou', 'Philipe'),
     (2, 2, 'Arnault', 'Bernard'),
     (2, 3, 'Arnault', 'Bernardette'),
     (2, 4, 'Arnault', 'Francois'),
     (3, 5, 'Mbappe', 'Killian'),
     (5, 6, 'Sebastien', 'Patrick'),
     (7, 7, 'Ronaldo', 'Christiano'),
     (8, 8, 'Messi', 'Lionel'),
     (6, 9, 'Pitt', 'Brad'),
     (6, 10, 'Jolie', 'Angelina'),
     (10, 11, 'Maradona', 'Diego'),
     (11, 12, 'Griezman', 'Antoine'),
     (12, 13, 'Cruise', 'Tom'),
     (13, 14, 'Johnson', 'Dwayne'),
     (18, 15, 'Arnault', 'Bernard'),
     (39, 16, 'Arnault', 'Bernard');
"""

InsertSeance = """
INSERT INTO seance (numFilm, numSeance, horaire, salle, nbPlace) VALUES
     (5, 1, '2023-05-10 21:00:00', 1, 50),
     (6, 2, '2023-04-19 16:59:43', 2, 50),
     (7, 3, '2023-04-19 16:59:43', 3, 50),
     (8, 4, '2023-04-19 16:59:43', 4, 50),
     (10, 5, '2023-04-19 16:59:43', 5, 50),
     (11, 6, '2023-04-19 16:59:43', 0, 50),
     (12, 7, '2023-04-19 16:59:43', 0, 50),
     (13, 8, '2023-04-19 16:59:43', 0, 50),
     (16, 9, '2023-04-19 16:59:43', 0, 50),
     (17, 10, '2023-04-19 16:59:43', 0, 50),
     (18, 11, '2023-04-19 16:59:43', 0, 50),
     (19, 12, '2023-04-19 16:59:43', 0, 50),
     (21, 13, '2023-04-19 16:59:43', 0, 50),
     (22, 14, '2023-04-19 16:59:43', 0, 50),
     (22, 15, '2023-04-19 16:59:43', 0, 50),
     (23, 16, '2023-04-19 16:59:43', 0, 50),
     (5, 18, '2023-01-06 14:00:00', 1, 50),
    (5, 19, '2023-01-06 16:00:00', 2, 50),
    (5, 20, '2023-01-06 20:00:00', 3, 50),
    (5, 21, '2023-02-06 15:00:00', 1, 50),
    (5, 22, '2023-02-06 17:00:00', 2, 50),
    (5, 23, '2023-02-06 21:00:00', 3, 50),
    (5, 24, '2023-03-06 14:00:00', 1, 50),
    (5, 25, '2023-03-06 16:00:00', 2, 50),
    (5, 26, '2023-03-06 20:00:00', 3, 50),
    (5, 27, '2023-04-06 15:00:00', 1, 50),
    (5, 28, '2023-04-06 17:00:00', 2, 50),
    (5, 29, '2023-04-06 21:00:00', 3, 50),
    (5, 30, '2023-05-06 14:00:00', 1, 50),
    (5, 31, '2023-05-06 16:00:00', 2, 50),
    (5, 32, '2023-05-06 20:00:00', 3, 50),
    (5, 33, '2023-06-06 15:00:00', 1, 50),
    (5, 34, '2023-06-06 17:00:00', 2, 50),
    (5, 35, '2023-06-06 21:00:00', 3, 50),
    (5, 36, '2023-07-06 14:00:00', 1, 50),
    (5, 37, '2023-07-06 16:00:00', 2, 50),
    (5, 38, '2023-07-06 20:00:00', 3, 50),
    (6, 39, '2023-01-06 14:30:00', 4, 50),
    (6, 40, '2023-01-06 16:30:00', 5, 50),
    (6, 41, '2023-01-06 20:30:00', 6, 30),
    (6, 42, '2023-02-06 15:30:00', 4, 50),
    (6, 43, '2023-02-06 17:30:00', 5, 50),
    (6, 44, '2023-02-06 21:30:00', 6, 30),
    (6, 45, '2023-03-06 14:30:00', 4, 50),
    (6, 46, '2023-03-06 16:30:00', 5, 50),
    (6, 47, '2023-03-06 20:30:00', 6, 30),
    (6, 48, '2023-04-06 15:30:00', 4, 50),
    (6, 49, '2023-04-06 17:30:00', 5, 50),
    (6, 50, '2023-04-06 21:30:00', 6, 30),
    (6, 51, '2023-05-06 14:30:00', 4, 50),
    (6, 52, '2023-05-06 16:30:00', 5, 50),
    (6, 53, '2023-05-06 20:30:00', 6, 30),
    (6, 54, '2023-06-06 15:30:00', 4, 50),
    (6, 55, '2023-06-06 17:30:00', 5, 50),
    (6, 56, '2023-06-06 21:30:00', 6, 30),
    (6, 57, '2023-07-06 14:30:00', 4, 50),
    (6, 58, '2023-07-06 16:30:00', 5, 50),
    (6, 59, '2023-07-06 20:30:00', 6, 30),
    (25, 60, '2023-08-06 22:00:00', 10, 30),
    (20, 61, '2023-09-06 21:00:00', 4, 50);
"""




base = "cinema.db"
if os.path.isfile(base):
    os.remove(base)
    print(f"Le fichier {base} existait déjà et a été supprimé.")

db = sqlite3.connect(base)
cursor = db.cursor()
cursor.execute(CreateTableFilm)
cursor.execute(CreateTableJouer)
cursor.execute(CreateTableParticipant)
cursor.execute(CreateTableRealiser)
cursor.execute(CreateTableReservation)
cursor.execute(CreateTableSeance)
cursor.execute(InsertFilm)
cursor.execute(InsertParticipant)
cursor.execute(InsertJouer)
cursor.execute(InsertRealiser)
cursor.execute(InsertSeance)
cursor.execute(InsertReservation)
print("Données insérées.")
db.commit()
db.close()

print("La base a été créée avec succés.")

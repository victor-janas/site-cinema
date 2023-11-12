Pour faire fonctionner le site il suffit d'avoir téléchargés sur sa machine le logiciel mysql

Pour lancer le site, il suffit d'executer le fichier interface.py. Sur la configuration avec identifiant : root et pas de mot de passe. Sinon adapté dans le document configDB.txt, il est conseillé d'être déjà connecté à phpmyadmin/mysql car la toute première connection ne fonctionne pas directement avec le login et mot de passe admin.


Le fichier cinema.SQL est la base exportée si les fichiers pythons venaient à ne pas fonctionner.
Le fichier configDB.py est un fichier python pour se connecter à la base.
Le fichier configDB.txt contient les paramètres de connections à la base (login,mdp).
Le fichier creation_base_cinema.py permet de créer la base vide puis de la remplir à l'aide de CSV.
Le fichier interface.py permet de récupérer toutes lrequêtes en CLI.
Le fichier requetes.py permet de lancer toutes les requêtes sql.
Le fichier creation_base_sqlite.py permet de créer une base en sqlite avec des données se trouvant dans le fichier python.
Le fichier cinema.db pour avoir la base en sqlite.
Le fichier Web.py permet de lancer l'interface Web. Pour s'y connecter il suffit d'aller sur une page internet et d'entrer : http://127.0.0.1:8080
Le dossier CSV contient toutes les données de chaque table sous forme de csv.

Le dossier res contient 5 autres dossiers : 
Le dossier css avec un fichier css pour le site.
Le dossier images avec les images pour le site.
Le dossier js avec les fichiers javascript pour le site.
Le dossier templates avec tous les templates pour le site.
Le dossier tmp avec tous les fichiers mako.

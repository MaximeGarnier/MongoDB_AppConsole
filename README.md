NA17 Groupe 9 Etudoc

Modules requis pour exécuter le projet:

- Mongo (server et BDD)
- Python3
- Pymongo

Pourquoi avoir utilisé Python?

- Python est un langage général qui peut se trouver utile dans diverses situations et sa syntaxe est plutôt simple.
- Un application console est suffisante dans le cadre de notre projet. A ce titre python nous a permis de développer une application 
  simplement et rapidement, et qui répondais à toutes nos attentes.
- Il existe le module Pymongo qui permet de lier notre BDD Mongo à Python avec des commandes similaires au langage de Mongo, 
  ce qui nous a permis d'adapter nos requêtes déjà formulée pour Mongo.

Instructions pour l'utilisation de notre application

- Nous considérons que l’utilisateur de notre application possède le statut d'administrateur. 
  Par conséquent il peut supprimer des documents, des étudiants, et a accès aux documents archivés.

- Nous avons utilisé la version 3.4.10 de Mongo (fonctionne également sur une version 2.6.10), la version 3.5.2 de Python sur Linux et la version 3.6 de pymongo.


1 - Lancer l'application

	Avant de lancer l'application, il faut ouvrir un terminal et saisir la commande "mongod" pour lancer le serveur mongo.
	Puis, dans un deuxième terminal (il ne faut pas fermer le premier), il faut se placer dans le dossier où se situe les scripts 
	et saisir la commande "python insertion.py" afin de remplir la base de donnée avec des valeurs exemple.
	Après ces 2 étapes, l'environnement est prêt pour l'utilisation de notre application.
	Dans le même terminal, il suffit de saisir la commande "python etudoc.py"
 
 2 - Utiliser l'application
 
	a - Fonctions d'affichage
	
		i- Afficher tous les étudiants
			Pour sélectionner cette option, il faut saisir "1" dans le menu.
			La liste de tous les étudiants s'affiche avec pour chaque étudiant :
				-son nom
				-son prénom
				-son login
				-son semestre

		ii- Afficher tous les documents
			Saisir "2" dans le menu.
			Les informations suivantes sont renvoyées pour chaque document : 
				-Titre
				-Date de publication
				-Mots clés
				-Auteurs
				-Etat(archivé ou pas)
				
		iii- Afficher tous les documents archivés 
			Saisir "3" dans le menu.
			Même principe que pour "afficher tous les documents"
			
		iv- Afficher tous les documents non archivés 
			Saisir "4" dans le menu.
			Même principe que pour "afficher tous les documents"
			
	b - Fonctions de recherche
	
		i- Rechercher un document par titre
			Saisir "5" dans le menu.
			Saisir des mots contenus dans le titre. Les résultats seront triés par pertinence (nombre d'occurences des mots saisis). 
		
		ii- Rechercher un document par mot-clé
			Saisir "6" dans le menu
			Saisir des mots-clés (cette fois il faut saisir exactement le mot-clé pour trouver le document).
		
		iii- Rechercher un document par date
			Saisir "7" dans le menu
			Choisir un mode de recherche parmi : 
			Documents publiés avant une date, Documents publiés après une date, Documents publiés entre deux dates, Documents publiés à une date précise
			Saisir la date en suivant les instructions que donne l'application
			L'application retournera alors la liste des documents qui respectent

		iv- Rechercher un document par étudiant
			Saisir "8" dans le menu
			Saisir le numéro correspondant à l'étudiant souhaité dans la liste.

	c- Fonctions d'ajout

		i- Ajouter un étudiant
			Saisir "9" dans le menu
			Remplir les champs nom, prénom, login, semestre au fur et à mesure que l'application les demande.

		ii- Ajouter un document
			Saisir "10" dans le menu
			Suivre les instructions que renvoie l'application

	d- Fonctions de suppression

		i- Supprimer un etudiant
			Saisir "11" dans le menu
			Choisir l'étudiant.
			Le nom cet étudiant sera retiré de la liste d'auteurs pour chacun de ses rapports. 
			Les documents dont il est le seul auteur seront supprimés (en effet, un document ne peut pas exister s'il n'a pas d'auteur). 

		ii- Supprimer un document
			Saisir "12" dans le menu
			Choisir le document parmi la liste.

	e- Fonctions de gestion des archives

		i- Archiver un document
			Saisir "13" dans le menu
			La liste des documents non archivés s'affiche. Choisir celui qu'on veut archiver.

		ii- Restaurer un document
			Saisir "14" dans le menu
			La liste des documents archivés s'affiche. Choisir celui qu'on veut retirer des archives.

	f - Retour au menu
		Pour retourner au menu principal après avoir exécuté une fonction, il suffit de faire "entrée"
	
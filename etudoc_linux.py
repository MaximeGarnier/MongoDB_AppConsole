#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import datetime
import os
os.system('clear')

#####################################################
#            Connexion/paramètres Mongo             #
#####################################################
client = MongoClient()

db = client.na17g9
docs = db.Document
etus = db.Etudiant


#####################################################
#             Définition des fonctions              #
#####################################################

###########################Documents
#get_doc_all()
def get_doc_all():
    return docs.find()

#get_doc_archive(archive)
def get_doc_archive(archive):
    if archive==0 :
        return docs.find({"archive":False})
    else:
        return docs.find({"archive":True})

#print_docs(documents)
def print_docs(documents):
    for doc in documents:
        print(" Titre:",doc.get("titre"))
        print(" Date de publication:",doc.get("datePub").day,"/",doc.get("datePub").month,"/",doc.get("datePub").year)
        print(" Mot-clés:")
        for mot in doc.get("motcles"):
            print(" -",mot.get("mot"))
        print(" Auteurs:")
        for etu in doc.get("etudiant"):
            e=get_etu_id(etu.get("idetu"))
            print(" -",e.get("nom"),e.get("prenom"))
        if doc.get("archive") == False:
            print(" Etat: Non archivé")
        else:
            print(" Etat: Archivé")
        print("\n")


###########################Etudiants
#get_etu_all()
def get_etu_all():
    return etus.find()

#get_etu_id(_id)
def get_etu_id(_id):
    return etus.find_one({"_id":_id})

###########################Interface

#aff_etus()
def aff_etus():
    etudiants = get_etu_all()
    for etu in etudiants:
        print("Nom:",etu.get("nom"))
        print("Prenom:",etu.get("prenom"))
        print("Login:",etu.get("login"))
        print("Semestre:",etu.get("semestre"))
        print("\n")
    
#aff_docs()
def aff_docs(etat):
    if etat == "all":
        documents = get_doc_all()
    elif etat == "arch":
        documents = get_doc_archive(1)
    elif etat == "narch":
        documents = get_doc_archive(0)
    print_docs(documents)

#rech_titre()
def rech_titre():
    db.Document.create_index([('titre','text')])
    recherche=input ("Quel(s) terme(s) souhaitez vous rechercher ? (Vous pouvez entrez plusieurs mots séparés par un espace)\n")
    documents = docs.find({'$text' : {'$search': recherche}},{'score': {'$meta': 'textScore'}}).sort([('score', {'$meta':'textScore'})])
    print_docs(documents)


#rech_mcle()
def rech_mcle():
    mcle = input("Entrez un mot clé?\n")
    print("\n")
    documents = docs.find({"motcles.mot":mcle})
    print_docs(documents)

#rech_etu()
def rech_etu():
    etudiants = get_etu_all()
    k=1
    for etu in etudiants:
        print(k,">",etu.get("nom"),etu.get("prenom"),etu.get("semestre"))
        k += 1
    l = int(input("Quel est le numero de l'étudiant?\n"))
    etudiant = get_etu_all()[l-1].get("_id")
    documents = docs.find({"etudiant":{"idetu":etudiant}})
    print_docs(documents)

#rech_date()
def rech_date():
    tmp = "f"
    while tmp=="f":
        os.system('clear')
        print("Voici les différentes recherches disponibles:\n")
        print("1 > Documents publiés avant une date")
        print("2 > Documents publiés après une date")
        print("3 > Documents publiés entre deux dates")
        print("4 > Documents publiés à une date précise\n")
        choix = input("Quelle recherche voulez-vous effectuer?\n")
        
        if choix == "1":
            y = int(input("\nEntrez l'année: "))
            m = int(input("Entrez le mois: "))
            d = int(input("Entrez le jour: "))
            documents = db.Document.find({"datePub":{'$lte':datetime.datetime(y,m,d)}}).sort([( "datePub", -1 )])
            os.system('clear')
            print_docs(documents)
            tmp="t"
        elif choix == "2":
            y = int(input("\nEntrez l'année: "))
            m = int(input("Entrez le mois: "))
            d = int(input("Entrez le jour: "))
            documents = db.Document.find({"datePub":{'$gte':datetime.datetime(y,m,d)}}).sort([( "datePub", -1 )])
            os.system('clear')
            print_docs(documents)
            tmp="t"
        elif choix == "3":
            print("\nDate de début")
            y1 = int(input("\nEntrez l'année: "))
            m1 = int(input("Entrez le mois: "))
            d1 = int(input("Entrez le jour: "))
            print("\nDate de fin")
            y2 = int(input("\nEntrez l'année: "))
            m2 = int(input("Entrez le mois: "))
            d2 = int(input("Entrez le jour: "))
            documents = db.Document.find({"datePub":{'$gte':datetime.datetime(y1,m1,d1),'$lte':datetime.datetime(y2,m2,d2)}}).sort([( "datePub", -1 )])
            os.system('clear')
            print_docs(documents)
            tmp="t"
        elif choix == "4":
            y = int(input("\nEntrez l'année: "))
            m = int(input("Entrez le mois: "))
            d = int(input("Entrez le jour: "))
            documents = db.Document.find({"datePub":datetime.datetime(y,m,d)})
            os.system('clear')
            print_docs(documents)
            tmp="t"                                                   

#arch_doc()
def arch_doc():
    documents = get_doc_archive(0)
    i=1
    for doc in documents:
        print(i,">",doc.get("titre"))
        i += 1
    choix = int(input("\nQuelle document souhaitez vous archiver?\n"))
    choix -= 1
    documents = get_doc_archive(0)
    docs.update({"_id":ObjectId(documents[choix].get("_id"))}, {'$set' : {"archive": True}})

#rest_doc()
def rest_doc():
    documents = get_doc_archive(1)
    i=1
    for doc in documents:
        print(i,">",doc.get("titre"))
        i += 1
    choix = int(input("\nQuelle document souhaitez vous archiver?\n"))
    choix -= 1
    documents = get_doc_archive(1)
    docs.update({"_id":ObjectId(documents[choix].get("_id"))}, {'$set' : {"archive": False}})
    

#add_doc()
def add_doc():
    titre = input("Entrez le titre du document:\n")
    nb_mcle = int(input("\nCombien de mot-clés pour le document?\n"))
    i = 0
    mots = []
    while i != nb_mcle:
        print("\nEntrez le mot",i+1,":")
        mot = input()
        mots.append(mot)
        i += 1
    encore = 'o'
    etus_add = []
    while encore != 'n':
        os.system('clear')
        print("Voici la base de donnée des étudiants")
        etudiants = get_etu_all()
        k=1
        for etu in etudiants:
            print(k,">",etu.get("nom"),etu.get("prenom"),etu.get("semestre"))
            k += 1
        etu_exist = input("\nL'étudiant existe-t-il dans la base? (o/n)\n")
        if etu_exist == 'o':
            l = int(input("\nQuel est sont numéro?\n"))
            etudiants = get_etu_all()
            etus_add.append(etudiants[l-1].get("_id"))
        elif etu_exist == 'n':
            os.system('clear')
            new = add_etu()
            etus_add.append(new)
        else:
            print("\nErreur, entrée non acceptée\n")
        encore = input("\nVoulez-vous ajouter un nouvel auteur? (o/n)\n")

    id_doc = docs.insert_one(
        {
        "titre": titre,
        "datePub": datetime.datetime.now(),
        "archive": False,
        "motcles":
                [
                ],
        "etudiant":
          [
          ]
        }).inserted_id
    for mot in mots:
        docs.update({ "_id": id_doc},{'$addToSet' : {"motcles":{"mot":mot}}})

    for etu in etus_add:
        docs.update({ "_id": id_doc},{'$addToSet' : {"etudiant":{"idetu":etu}}})

#add_etu()
def add_etu():
    print("Vous allez ajouter un nouvel etudiant:\n\n")
    nom =  input("Entrez son nom:  ")
    prenom = input("Entrez son prenom:  ")
    login = input("Entrez son login UTC:  ")
    semestre = input("Entrez son semestre actuel (fomat GI01) :  ")
    return etus.insert_one(
                {
                "login": login,
                "nom": nom,
                "prenom": prenom,
                "semestre": semestre
                }).inserted_id

#supp_doc()
def supp_doc():
    documents = get_doc_all()
    i=1
    for doc in documents:
        print(i,">",doc.get("titre"))
        i += 1
    choix = int(input("\nQuelle document souhaitez vous supprimer?\n"))
    choix -= 1
    documents = get_doc_all()
    docs.remove({"_id":ObjectId(documents[choix].get("_id"))})

#supp_etu()
def supp_etu():
    etudiants = get_etu_all()
    k=1
    for etu in etudiants:
        print(k,">",etu.get("nom"),etu.get("prenom"),etu.get("semestre"))
        k += 1
    l = int(input("Quel est le numero de l'étudiant a supprimer?\n"))
    etudiant = get_etu_all()[l-1].get("_id")
    docs.update_many({"etudiant.idetu":ObjectId(etudiant)},{'$pull':{"etudiant":{"idetu":ObjectId(etudiant)}}})
    etus.remove({"_id":ObjectId(etudiant)})
    docs.remove({"etudiant":[]})
        

#####################################################
#           Interface de l'application              #
#####################################################

t="a"
while t!="q":
    os.system('clear')
    print("======== Menu BDD EtuDoc ======== \n")

    print("Affichage:")
    print("       1 > Afficher tous les etudiants")
    print("       2 > Afficher tous les documents")
    print("       3 > Afficher tous les documents archives")
    print("       4 > Afficher tous les documents non archives\n")
    print("Recherche:")
    print("       5 > Rechercher un document par titre")
    print("       6 > Rechercher un document par mot-cle")
    print("       7 > Rechercher un document par date")
    print("       8 > Rechercher un document par etudiant\n")
    print("Ajout:")
    print("       9 > Ajouter un etudiant")
    print("      10 > Ajouter un document\n")
    print("Suppression:")
    print("      11 > Supprimer un etudiant")
    print("      12 > Supprimer un document\n")
    print("Gestion des archives:")
    print("      13 > Archiver un document")
    print("      14 > Restaurer un document\n")
    
    print("Pour quitter, tapez 'q'")
    t = input("Entrez votre choix: ")

    if t == '1':
        os.system('clear')
        aff_etus()
        input("\n\nEntrer pour revenir au menu")
    elif t == '2':
        os.system('clear')
        aff_docs("all")
        input("\n\nEntrer pour revenir au menu")
    elif t == '3':
        os.system('clear')
        aff_docs("arch")
        input("\n\nEntrer pour revenir au menu")
    elif t == '4':
        os.system('clear')
        aff_docs("narch")
        input("\n\nEntrer pour revenir au menu")
    elif t == '5':
        os.system('clear')
        rech_titre()
        input("\n\nEntrer pour revenir au menu")
    elif t == '6':
        os.system('clear')
        rech_mcle()
        input("\n\nEntrer pour revenir au menu")
    elif t == '7':
        os.system('clear')
        rech_date()
        input("\n\nLes documents sont triés par ordre décroissant\n\n\n\n\nEntrer pour revenir au menu")
    elif t == '8':
        os.system('clear')
        rech_etu()
        input("\n\nEntrer pour revenir au menu")
    elif t == '9':
        os.system('clear')
        add_etu()
        input("\n\nEntrer pour revenir au menu")
    elif t == '10':
        os.system('clear')
        add_doc()
        input("\n\nEntrer pour revenir au menu")
    elif t == '11':
        os.system('clear')
        supp_etu()
        input("\n\nEntrer pour revenir au menu")
    elif t == '12':
        os.system('clear')
        supp_doc()
        input("\n\nEntrer pour revenir au menu")
    elif t == '13':
        os.system('clear')
        arch_doc()
        input("\n\nEntrer pour revenir au menu")
    elif t == '14':
        os.system('clear')
        rest_doc()
        input("\n\nEntrer pour revenir au menu")
    
print("A bientôt")


#!/usr/bin/python3
#-*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import datetime


#####################################################
#            Connexion/paramètres Mongo             #
#####################################################
client = MongoClient()

db = client.na17g9
docs = db.Document
etus = db.Etudiant
                  
#####################################################
#             Initialisation de la base             #
#####################################################

#Etudiants
etus.drop()

elallema = etus.insert_one(
{
"login": "elallema",
"nom": "Lallemand",
"prenom": "Elise",
"semestre": "HU05"
}).inserted_id

mmargera = etus.insert_one(
{
"login": "mmargera",
"nom": "Margerand",
"prenom": "Marie",
"semestre": "GI01"
}).inserted_id

maxigarn = etus.insert_one(
{
"login": "maxigarn",
"nom": "Garnier",
"prenom": "Maxime",
"semestre": "GI01"
}).inserted_id

wezheng = etus.insert_one(
{
"login": "wezheng",
"nom": "Zheng",
"prenom": "Weiming",
"semestre": "GI04"
}).inserted_id

cgamorai = etus.insert_one(
{
"login": "cgamorai",
"nom": "Gamoraix",
"prenom": "Corentin",
"semestre": "GSU03"
}).inserted_id

lbertran = etus.insert_one(
{
"login": "lbertran",
"nom": "Bertrand",
"prenom": "Lucie",
"semestre": "TC03"
}).inserted_id

paudemar = etus.insert_one(
{
"login": "paudemar",
"nom": "Audemard",
"prenom": "Pauline",
"semestre": "GP05"
}).inserted_id

vhouberd = etus.insert_one(
{
"login": "vhouberd",
"nom": "Houberdon",
"prenom": "Vincent",
"semestre": "GB03"
}).inserted_id


#Documents
docs.drop()

docs.insert(
{
"titre": "Projet GE37 sur la robotique",
"datePub": datetime.datetime(2017, 9, 12),
"archive": False,
"motcles":
	[
  	{"mot": "ouvrier"},
  	{"mot": "robot"}
  ],
"etudiant":
  [
    {"idetu": maxigarn}
  ]
})

docs.insert(
{
"titre": "L'évolution des techniques de tissage et de filage de la laine en France",
"datePub": datetime.datetime(2016,11,1),
"archive": True,
"motcles":
	[
  	{"mot": "ouvrier"},
  	{"mot": "filage"},
        {"mot": "tissage"},
	],
"etudiant":
  [
    {"idetu": elallema},
    {"idetu": mmargera}
  ]
})

docs.insert(
{
"titre": "Rapport stage ouvrier",
"datePub": datetime.datetime(2017,5,30),
"archive": False,
"motcles":
	[
	{"mot": "ouvrier"},
  ],
"etudiant":
  [
    {"idetu": mmargera}
  ]
})

docs.insert(
{
"titre": "Elaboration d’une méthodologie de localisation et de dimensionnement des stations de rechargement des voitures électriques",
"datePub": datetime.datetime(2017,3,11),
"archive": False,
"motcles":
	[
	{"mot": "voiture"},
	{"mot": "électrique"},
	{"mot": "rechargement"},
	{"mot": "localisation"}
  ],
"etudiant":
  [
    {"idetu": cgamorai}
  ]
})

docs.insert(
{
"titre": "Les procédés de fabrication des colles industrielles",
"datePub": datetime.datetime(2004,12,21),
"archive": True,
"motcles":
	[
	{"mot": "colle"},
	{"mot": "industrie"},
	{"mot": "procédés"}
  ],
"etudiant":
  [
    {"idetu": paudemar}
  ]
})

docs.insert(
{
"titre": "Les différences de vocabulaire selon les régions de France",
"datePub": datetime.datetime(2017,11,24),
"archive": False,
"motcles":
	[
	{"mot": "langage"},
	{"mot": "vocabulaire"},
	{"mot": "localisation"},
	{"mot": "région"}
  ],
"etudiant":
  [
    {"idetu": lbertran},
    {"idetu": elallema}
  ]
})

docs.insert(
{
"titre": "Evaluation de la conformité d'un aspirateur",
"datePub": datetime.datetime(2016,10,17),
"archive": False,
"motcles":
	[
	{"mot": "qualité"},
	{"mot": "aspirateur"},
	{"mot": "industrie"},
	{"mot": "conformité"}
  ],
"etudiant":
  [
    {"idetu": vhouberd},
    {"idetu": wezheng},
    {"idetu": cgamorai}
  ]
})


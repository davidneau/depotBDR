from datetime import datetime
from pprint import pprint
from django.db import IntegrityError
from django import db
import sqlite3
from monappli.models import livre_physique,utilisateur,emprunt,commande
import re

pattern = re.compile(r"INSERT.*VALUES.*\('(.*)','(.*?)','(.*?)',(.*),'(.*)',(.*),'(.*)','(.*)','(.*)','(.*)','(.*)','(.*)','(.*)','(.*)',(.*);")
# ~ (`auteur`, `titre`, `collection`, `numcoll`, `editeur`, `date`, `isbn`, `ams`, `cle`, `cote`, `inventaire`, `type`, `lang`, `lango`, `numfiche`)


with open("newcatalogue.py","r",encoding="utf-8") as f:
	for line in f:
		found = pattern.search(line)
		if found:
			# ~ pprint(found.groups())
			auteur=found.group(1)
			titre=found.group(2)
			collection=found.group(3)
			numcoll=found.group(4)
			editeur=found.group(5)
			date=found.group(6)
			# ~ iss=found.group(7)
			# ~ ams=found.group(8)
			# ~ cle=found.group(9)
			co=found.group(10)
			# ~ inventaire=found.group(11)
			# ~ typeo=found.group(12)
			lang=found.group(13)
			lango=found.group(14)
			# ~ numfiche=found.group(15)
			# ~ numfiche=numfiche.replace(')','')
			
			book=livre_physique(cote=date)# ~ auteur=auteur,titre=titre,collection=collection,cote=co,langue=lang,langue_original=lango)
			book.save()

#Création de Toto et Livre.perdu

Toto=utilisateur(identifiant='toto',identité='001')
Toto.save()
Livreperdu=utilisateur(identifiant='Perte',identité='002')
Livreperdu.save()

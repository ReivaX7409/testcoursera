# -*- coding: utf-8 -*-
"""
BONNARD Xavier Gr3

TP1

Exo1

"""

#Les imports 
import csv


#Les fonctions
from operator import itemgetter

def ajouter_pos (exposants, nom, age, email, ventes, jour):
 """
Fonction qui ajoute les
données d’un exposant à la liste des exposants en paramètre. Le nom est stocké majuscule.

    Parameters
    ----------
    exposants list(dict): liste des exposants
    nom str: nom du nouvel exposant      
    age int:  age du nouvel exposant       
    email str:   email du nouvel exposant      
    ventes int: ventes du nouvel exposant     
    jour str: jour des ventes du nouvel exposant
       
    Return: none

 """       
 exposants.append({"nom":nom,"age":age,"email":email,"ventes":ventes,"jour":jour})


def ajouter_opt (exposants, nom, ventes ,age=0, email="", jour=""):
    exposants.append({"nom":nom,"age":age,"email":email,"ventes":ventes,"jour":jour})

def export(exposants,file="exposants.csv"):
    """exps=sorted(exposants, key= itemgetter ("ventes","nom"))
    """
    """
    Attention: tri par 2 clés dans 2 ordres différents
    1. on trie par la 2ème clé en 1er
    2. et ensuite on retrie la structure résultat par la 1ère
    """
    exp1=sorted(exposants,key=lambda exp:exp["nom"])
    exp2=sorted(exp1,key=lambda exp:exp["ventes"],reverse=True)
    
    with open(file,"w", newline='', encoding='utf-8') as fichier:
        fields=list(exp2[0].keys())
        writer= csv.DictWriter(fichier, fieldnames= fields, delimiter=";")
        writer.writeheader()
        writer.writerows(exp2)
        
    print("fichier",file,"créé avec succes")
    

def ajouterExp (exposants, **args):
    exposants.append(args)

#L"appli
les_exp=[]
ajouter_pos(les_exp, "thomas",25,"thomas@gmail.com",180,"lundi")

print(les_exp)

#Q3
liste1=["julie",27,"julie.julie@gmail.com",40, "mardi"]
ajouter_pos(les_exp, *liste1)


print(les_exp[0])
print(("{:<20}"*len(les_exp[0])).format(*(les_exp[0].keys()))) 
[print(("{:<20}"*len(exp)).format(*(exp.values()))) for exp in les_exp]
[print(("{:<20}"*len(les_exp[0])).format(*(les_exp[0].keys()))), (print(("{:<20}"*len(exp)).format(*(exp.values()))) for exp in les_exp)]
    
#Q4
d={"nom" :"Théo","age" :22,"email" :"ttheo@gmail.com","ventes" :80, "jour":"mardi"}
ajouter_pos(les_exp, **d)
[print(("{:<20}"*len(exp)).format(*(exp.values()))) for exp in les_exp]

#Q5
les_vars = ["email" ,"nom", "age", "ventes" ,"jour",]
les_vals = ["alice@gmail.com" ,"alice",30,127,"mardi"]

#methode 1 construire un dictionnaire
d1={les_vars[i]:les_vals[i] for i in range(len(les_vars))}
print("d1=",d1)
d2=dict(zip(les_vars,les_vals))
print("d2=",d2)
ajouter_pos(les_exp, **d1)
[print(("{:<20}"*len(exp)).format(*(exp.values()))) for exp in les_exp]

#Q7
ajouter_opt(les_exp, "Sara", 90,22)
ajouter_opt(les_exp, "Lucas", 15, email="lucas@♠gmail.fr", jour="mercredi")
ajouter_opt(les_exp, "Ines", 250,40, jour="mardi")
ajouter_opt(les_exp, "Alex", 110,30,jour="lundi")
export(les_exp,file="exposants.csv")

#Q10
ajouterExp (les_exp, nom="Fred",age=55, ventes=190, jour="lundi")
ajouterExp (les_exp, nom="Tom", ventes=60, horaires="12h_15h",jour="mercredi")
ajouterExp (les_exp, nom="Clara", ventes=2, jour="mardi", telephone="0610203040")
ajouterExp (les_exp, nom="Alex",ventes=400)
ajouterExp (les_exp, nom="Julie", ventes=8, statut="stagiaire", telephone="0650203648")

[print(exp) for exp in les_exp]



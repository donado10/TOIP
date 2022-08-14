#!/usr/bin/env python3

import re
from Database import Database
import datetime


def GetListe(Terrain:dict,date:str):
    db = Database("GT1_2022")
    Terrain["GT1"] = db.GetTerrain(date)

    db = Database("GT2_2022")
    Terrain["GT2"] = db.GetTerrain(date)

    db = Database("PT_2022")
    Terrain["PT"] = db.GetTerrain(date)

def FormatDate(date):
    match = re.search(r"([0-9]+).([0-9]+).([0-9]+)",date)

    today = datetime.datetime.now().day
    month = datetime.datetime.now().month

    if match:
        date = match.group(3)+ '-' + match.group(2) + '-' + match.group(1)

    if int(match.group(2)) < month:
        return "Desole, cette date est depassee"

    if int(match.group(2)) == month and int(match.group(1)) < today:
        return "Desole, cette date est depassee"
    return date

def ListeFactory(ListeHour:list):
    Liste = list()
    for hour in ListeHour:
        Liste.append(f"{hour[0]}h")
    return Liste

def StringReplace(phrase:str):
    phrase = phrase.replace("'","")
    phrase = phrase.replace('[',"")
    phrase = phrase.replace(']',"")
    return phrase

def CheckDispo(Liste:list):
    if len(Liste) == 0:
        return "Full"
    elif len(Liste) == 10:
        return "Empty"
    else:
        return None

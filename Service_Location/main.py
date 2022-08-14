#!/usr/bin/env python3

from sys import argv
import MyLib

date = argv[1]

date = MyLib.FormatDate(date)

if date == "Desole, cette date est depassee":
    print(date)
else:
    Terrain = dict()
    MyLib.GetListe(Terrain,date)

    HourGT1 = MyLib.ListeFactory(Terrain["GT1"])
    HourGT2 = MyLib.ListeFactory(Terrain["GT2"])
    HourPT = MyLib.ListeFactory(Terrain["PT"])

    if MyLib.CheckDispo(HourGT1) == None:
        phrase = f"Grand terrain 1 : {HourGT1[0:-1]}"
        phrase = MyLib.StringReplace(phrase)
        print(phrase)

    elif MyLib.CheckDispo(HourGT1) == "Full":
        print("Grand terrain 1: Tous les terrains ont ete reserve ")

    elif MyLib.CheckDispo(HourGT1) == "Empty":
        print("Grand terrain 1: Tous les terrains sont disponible ")


    if MyLib.CheckDispo(HourGT2) == None:
        phrase = f"Grand terrain 2 : {HourGT2[0:-1]}"
        phrase = MyLib.StringReplace(phrase)
        print(phrase)
    elif MyLib.CheckDispo(HourGT2) == "Full":
        print("Grand terrain 2: Tous les terrains ont ete reserve ")
    elif MyLib.CheckDispo(HourGT2) == "Empty":
        print("Grand terrain 2: Tous les terrains sont disponible ")

    if MyLib.CheckDispo(HourPT) == None:
        phrase = f"Petit terrain : {HourPT[0:-1]}"
        phrase = MyLib.StringReplace(phrase)
        print(phrase)
    elif MyLib.CheckDispo(HourPT) == "Full":
        print("Petit terrain : Tous les terrains ont ete reserve ")

    elif MyLib.CheckDispo(HourPT) == "Empty":
        print("Petit terrain : Tous les terrains sont disponible ")



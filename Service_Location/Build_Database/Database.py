#!/usr/bin/env python3

import random
from time import sleep
import pandas
import mysql.connector
from mysql.connector import Error



class Database:

    host = 'localhost'
    database = str()
    user = 'root'
    password = 'root'

    connection = None

    def __init__(self,database):
        self.database = database
        self.connection = self.InitConn()

    def InitConn(self):
        try:      
            connection = mysql.connector.connect(host=self.host,
                                                database=self.database,
                                                user=self.user,
                                                password=self.password)
            return connection
        except mysql.connector.Error as e:
            print(e)

    def InputDate(self):
        liste = pandas.date_range('2022-01-01', '2022-12-31').strftime('%m-%d')
        for date in liste:
            date = "2022-" + date
            self.IDatabaseDate(date)

    def InputHour(self):
        liste = [16,17,18,19,20,21,22,23,00,1]
        for hour in liste:
            self.IDatabasehour(hour)

    def InputDateHour(self):
        listeD = pandas.date_range('2022-01-01', '2022-12-31').strftime('%m-%d')
        listeH = [16,17,18,19,20,21,22,23,00,1]
        for date in listeD:
            date = "2022-" + date
            for hour in listeH:
                self.IDatabaseDH(date,hour)
            
    def GetHighest_DateID(self):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_date from Date order by ID_date desc LIMIT 1"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall() 
            if len(records) == 0:           
                ID = 1
                records.append(ID)
            else:
                ID = 1 + records[0][0]

            return ID
        except mysql.connector.Error as e:
            print(e)

    def GetHighest_HourID(self):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_hour from Hour order by ID_hour desc LIMIT 1"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall() 
            if len(records) == 0:           
                ID = 1
                records.append(ID)
            else:
                ID = 1 + records[0][0]

            return ID
        except mysql.connector.Error as e:
            print(e)

    def IDatabaseDate(self,date):
        try:
            ID_Date = self.GetHighest_DateID()
            mySql_insert_query = f"""INSERT INTO Date(ID_date,Period) 
                                VALUES 
                                ({ID_Date},'{date}') """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)

            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            print(error)
    
    def IDatabasehour(self,hour):
        try:
            ID_Hour = self.GetHighest_HourID()
            mySql_insert_query = f"""INSERT INTO Hour(ID_hour,Period) 
                                VALUES 
                                ({ID_Hour},{hour}) """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)

            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            print(error)

    def GetID_Date(self,date):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_date from Date where Period = '{date}'"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall() 
            
            return records[0][0]
        except mysql.connector.Error as e:
            print(e)

    def GetID_Hour(self,hour):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_hour from Hour where Period = {hour}"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            return records[0][0]

        except mysql.connector.Error as e:
            print(e)


    def UpdateDispo(self):
        try:
            listeD = pandas.date_range('2022-07-01', '2022-07-31').strftime('%m-%d')
            listeH = [16,17,18,19,20,21,22,23,00,1]
            cursor = self.connection.cursor()
            for date in listeD:
                date = "2022-" + date
                date = self.GetID_Date(date)

                for hour in listeH:
                    hour = self.GetID_Hour(hour)
                    x = random.randint(0,1)
                    sql_update_Query = f"Update Date_Hour set Disponibilite = {x} where ID_date = {date} And ID_hour = {hour}"
                    cursor.execute(sql_update_Query)

                    self.connection.commit()
            cursor.close()

        except mysql.connector.Error as e:
            print(e)

    def IDatabaseDH(self,date,hour):
        try:
            ID_Date = self.GetID_Date(date)
            ID_Hour = self.GetID_Hour(hour)
            mySql_insert_query = f"""INSERT INTO Date_Hour(ID_date,ID_hour,Disponibilite) 
                                VALUES 
                                ({ID_Date},{ID_Hour},1) """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)

            self.connection.commit()
            cursor.close()

        except mysql.connector.Error as error:
            print(error)
        



'''''
    #Fonction qui retourne True si un artiste est présent dans la base de donnée 
    def VerifierArtiste(self,Artiste:str) :
        try:
            sql_select_Query = f"select * from Artiste where Name = '{Artiste}'"
            cursor = self.connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            return cursor.rowcount == 1

        except mysql.connector.Error as e:
            return False

    def GetHighest_ArtisteID(self):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_Artiste from Artiste order by ID_Artiste desc LIMIT 1"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall() 
            if len(records) == 0:           
                ID = 1
                records.append(ID)
            else:
                ID = 1 + records[0][0]

            return ID
        except mysql.connector.Error as e:
            return False

    def GetHighest_AlbumID(self):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select ID_Album from Album order by ID_Album desc LIMIT 1"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall() 
            if len(records) == 0:           
                ID = 1
                records.append(ID)
            else:
                ID = 1 + records[0][0]

            return ID
        except mysql.connector.Error as e:
            return False

    def InputArtisteAlbum(self,liste:list):
        try:
            ID_Artiste = self.GetHighest_ArtisteID()
            mySql_insert_query = f"""INSERT INTO Artiste(ID_Artiste,NameArtiste) 
                                VALUES 
                                ({ID_Artiste},'{liste[0]}') """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)


            ID_Album =  self.GetHighest_AlbumID()
            mySql_insert_query = f"""INSERT INTO Album(ID_Album,NameAlbum,NameArtiste) 
                                VALUES 
                                ({ID_Album},'{liste[1]}','{liste[0]}') """

            cursor = self.connection.cursor()
            cursor.execute(mySql_insert_query)

            self.connection.commit()
            cursor.close()
            return True

        except mysql.connector.Error as error:
            return False


    def OutputArtisteAlbum(self,Name_Artiste):
            try:
                if self.VerifierArtiste(Name_Artiste) == True:
                    sql_select_Query = f"select NameAlbum,Year from Album where Artiste = '{Name_Artiste}'"
                    cursor = self.connection.cursor()
                    cursor.execute(sql_select_Query)
                    # get all records
                    records = cursor.fetchall()
                    return records
                else:
                    pass
            except mysql.connector.Error as error:
                pass

'''''
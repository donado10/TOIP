#!/usr/bin/env python3

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

    def GetTerrain(self,date):
        try:
            cursor = self.connection.cursor()
            sql_select_Query = f"select Hour.Period from Date_Hour inner join Hour on Hour.ID_hour = Date_Hour.ID_hour inner join Date on Date.ID_date = Date_Hour.ID_date where Date.Period = '{date}'  AND disponibilite = 1"
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()             
            return records
        except mysql.connector.Error as e:
            print(e)

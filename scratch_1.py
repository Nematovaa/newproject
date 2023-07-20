import os

os.system("cls")
import mysql.connector as con


def baza_yaratish(database_name):
    Con = con.connect(user="root", password="root", host="localhost")
    cur = Con.cursor()
    sql = f"Create database if not exists {database_name}"
    cur.execute(sql)


baza_yaratish("vazifalar")

import mariadb
from mariadb import Error

def VerifierMail(liste) -> list:
    try:
        connection = mariadb.connect(host='localhost',
                                            database='projet',
                                            user='',
                                            password='')

        query = f"select * from user where Mail = '{liste[2]}'"
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return cursor.rowcount == 0

    except mariadb.Error as e:
        return False

def Inscription(list) -> list:
    if VerifierMail(list) == False:
        return False

    try:
        connection = mariadb.connect(host='localhost',
                                            database='projet',
                                            user='',
                                            password='')
        query = f"""INSERT INTO user(Nom, Prenom, Mail, Password) 
                            VALUES 
                            ('{list[0]}', '{list[1]}', '{list[2]}', '{list[3]}') """

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except mariadb.Error as error:
        return False

def Connexion(liste)-> list:
    try:
        connection = mariadb.connect(host='localhost',
                                            database='projet',
                                            user='',
                                            password='')

        query = f"select * from user where Mail = '{liste[0]}' AND Password = '{liste[1]}'"
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return cursor.rowcount == 1

    except mariadb.Error as e:
        return False
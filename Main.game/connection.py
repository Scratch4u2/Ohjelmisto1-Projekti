import mysql.connector


def connector():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="root",
        autocommit=True
    )
    return connection

sql_connection = connector()
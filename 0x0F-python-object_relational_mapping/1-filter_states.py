#!/usr/bin/python3
from sys import argv
import MySQLdb
"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
"""


def filter_states():
    """ SQL INFO FROM ARGV """
    sql_usrname, sql_password, sql_database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = 3306

    """ SETTING MySQLdb Connection """
    db_connection = MySQLdb.connect(
        port=port,
        host=host,
        user=sql_usrname,
        password=sql_password,
        database=sql_database)

    cur = db_connection.cursor()

    """ EXECUTING SQL QUERY """
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    """ FETCHING DATA """
    states = cur.fetchall()

    for state in states:
        print(state)

    db_connection.close()


if __name__ == '__main__':
    filter_states()

import random
import string

import psycopg2


# command = """
# INSERT INTO users (phone_number, full_name) values (%s, %s);
# """


def get_connection():
    try:
        connection = psycopg2.connect(database="market", user="marketuser", password="marketpassword")
        return connection
    except Exception as e:
        print(e)


def select_all_data_from_table():
    cursor = get_connection().cursor()
    command = """
        SELECT * FROM users order by id;
    """

    cursor.execute(command)

    return cursor.fetchall()


def add_data_to_table(phone_number, full_name):
    connection = get_connection()
    cursor = connection.cursor()
    command = "INSERT INTO users (phone_number, full_name) values (%s, %s);"

    cursor.execute(command, (phone_number, full_name))
    # row = cursor.fetchone()
    connection.commit()

    # return row[0]
# Сайдамов Садам Сраждинович


def remove_data_from_table():
    connection = get_connection()
    cursor = connection.cursor()

    command = "DELETE from users where id = (SELECT id from users order by id desc limit 1)"

    cursor.execute(command)
    # row = cursor.fetchone()
    connection.commit()

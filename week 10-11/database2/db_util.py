import psycopg2


def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="university",
            user="universityuser",
            password="universitypass"
        )
        return connection
    except Exception as e:
        print(e)


def get_students():
    command = "SELECT * FROM students order by id"

    connection = get_connection()
    curs = connection.cursor()
    curs.execute(command)
    return curs.fetchall()


def add_student_to_db(grade, full_name):
    command = "INSERT INTO STUDENTS(grade, full_name) VALUES (%s, %s)"

    connection = get_connection()
    curs = connection.cursor()

    curs.execute(command, (grade, full_name))
    connection.commit()


def remove_student_from_db():
    command = "DELETE FROM students where id = (SELECT MAX(id) from students)"
    connection = get_connection()
    curs = connection.cursor()

    curs.execute(command)
    connection.commit()


def get_average():
    command = "SELECT AVG(grade) from students"

    connection = get_connection()
    curs = connection.cursor()

    curs.execute(command)
    return curs.fetchall()


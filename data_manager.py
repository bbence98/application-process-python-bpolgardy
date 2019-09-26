import database_common
from psycopg2 import sql


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nicknames(cursor, city):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = %(city)s
                   """,
                   {'city': city})
    nicknames = cursor.fetchall()
    return nicknames


@database_common.connection_handler
def get_applicant_info(cursor, applicant_name):
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE first_name = %(applicant_name)s
                   """,
                   {'applicant_name': applicant_name})
    applicant_info = cursor.fetchall()
    return applicant_info


@database_common.connection_handler
def get_applicant_info_by_email(cursor, email):
    pattern = f'%{email}%'
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE email LIKE %(email)s
                   """,
                   {'email': pattern})
    applicant_info = cursor.fetchall()
    return applicant_info


@database_common.connection_handler
def append_to_database(cursor, table_name, user_input):
    print(type(user_input))
    cursor.execute(
        sql.SQL("""INSERT INTO {table} (first_name, last_name, phone_number, email, application_code)
                   VALUES (%s, %s, %s, %s, %s)
                """)
            .format(table=sql.Identifier(table_name)),
        [user_input.get('first_name'),
         user_input.get('last_name'),
         user_input.get('phone_number'),
         user_input.get('email'),
         user_input.get('application_code')]
    )


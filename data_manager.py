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
                    SELECT first_name, last_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nicknames(cursor, city):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = %(city)s;
                   """,
                   {'city': city})
    nicknames = cursor.fetchall()
    return nicknames


@database_common.connection_handler
def get_applicant_info(cursor, applicant_name):
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE first_name = %(applicant_name)s;
                   """,
                   {'applicant_name': applicant_name})
    applicant_info = cursor.fetchall()
    return applicant_info


@database_common.connection_handler
def get_applicant_info_by_email(cursor, email):
    pattern = f'%{email}%'
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE email LIKE %(email)s;
                   """,
                   {'email': pattern})
    applicant_info = cursor.fetchall()
    return applicant_info\

@database_common.connection_handler
def get_applicant_info_by_id(cursor, applicant_id):
    cursor.execute("""
                    SELECT * FROM applicants
                    WHERE id = %(applicant_id)s;
                   """,
                   {'applicant_id': applicant_id})
    applicant_info = cursor.fetchall()
    return applicant_info

@database_common.connection_handler
def list_applicants(cursor):
    cursor.execute("""
                    SELECT * FROM applicants
                    """)
    applicant_info = cursor.fetchall()
    return applicant_info



@database_common.connection_handler
def append_to_database(cursor, table_name, user_input):
    print(type(user_input))
    cursor.execute(
        sql.SQL("""INSERT INTO {table} (first_name, last_name, phone_number, email, application_code)
                   VALUES (%s, %s, %s, %s, %s);
                """)
            .format(table=sql.Identifier(table_name)),
        [user_input.get('first_name'),
         user_input.get('last_name'),
         user_input.get('phone_number'),
         user_input.get('email'),
         user_input.get('application_code')])

@database_common.connection_handler
def update_applicant(cursor, applicant_id, user_input):
    cursor.execute("""
                    UPDATE applicants SET first_name = %(first_name)s,
                                        last_name = %(last_name)s,
                                        phone_number = %(phone_number)s,
                                        email = %(email)s,
                                        application_code = %(application_code)s
                    WHERE id = %(applicant_id)s
                    """,
                   {'applicant_id' : applicant_id,
                    'first_name' : user_input[0],
                    'last_name' : user_input[1],
                    'phone_number' : user_input[2],
                    'email' : user_input[3],
                    'application_code' : user_input[4]})

@database_common.connection_handler
def schools_with_mentors(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country 
                        FROM mentors
                    INNER JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id
                    """)
    result = cursor.fetchall()
    return result\


@database_common.connection_handler
def schools_even_without_mentors(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country 
                        FROM mentors
                    RIGHT JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id
                    """)
    result = cursor.fetchall()
    return result


@database_common.connection_handler
def mentors_by_country(cursor):
    cursor.execute("""
                    SELECT schools.country, COUNT(*) FROM mentors
                    JOIN schools ON schools.city = mentors.city
                    GROUP BY schools.country
                    ORDER BY    schools.country
                    """)
    result = cursor.fetchall()
    return result


@database_common.connection_handler
def contacts_by_schools(cursor):
    cursor.execute("""
                    SELECT s.name, m.first_name, m.last_name FROM mentors AS m 
                    JOIN schools s on m.id = s.contact_person;                    
                    """)
    result = cursor.fetchall()
    return result


@database_common.connection_handler
def applicants_application(cursor):
    cursor.execute("""
                    SELECT a.first_name, a.application_code, a_m.creation_date
                        FROM applicants AS a 
                    JOIN applicants_mentors a_m ON a.id = a_m.applicant_id
                    WHERE a_m.creation_date >= '2016-01-01'
                    ORDER BY a_m.creation_date DESC;
                    """)
    result = cursor.fetchall()
    return result\


@database_common.connection_handler
def applicants_with_mentors(cursor):
    cursor.execute("""
                    SELECT a.first_name, a.application_code, m.first_name AS mentor_first_name,
                        m.last_name FROM applicants AS a 
                    JOIN applicants_mentors a_m ON a.id = a_m.applicant_id
                    JOIN mentors m on a_m.mentor_id = m.id
                    ORDER BY a_m.applicant_id
                    """)
    result = cursor.fetchall()
    return result
















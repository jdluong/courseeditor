import mysql.connector as mysql


def create_course(name,instr,letter,sign,quarter,year,thoughts):
    """
    course_data: tuple
    """

    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()
    insert_stmt = ("INSERT INTO courses (name, instructor, letter_grade, sign_grade, quarter, year, thoughts) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)")

    cur.execute(insert_stmt,(name,instr,letter,sign,quarter,year,thoughts))
    con.commit()

    cur.close()
    con.close()

def get_courses():
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()
    get_stmt = ("SELECT * FROM courses")
    
    cur.execute(get_stmt)
    courses = cur.fetchall()

    cur.close()
    con.close()
    return courses

def get_single_course(course_id):
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()
    get_stmt = ("SELECT * FROM courses "
                "WHERE course_id=(%s)")
    
    cur.execute(get_stmt,(course_id,))
    course = cur.fetchone()

    cur.close()
    con.close()
    return course
    

def delete_single_course(course_id):
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()

    delete_stmt = ("DELETE FROM courses "
                    "WHERE course_id = (%s)")
    
    cur.execute(delete_stmt,(course_id,))
    con.commit()

    cur.close()
    con.close()

def delete_all_courses():
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()

    all_courses = get_courses()

    delete_stmt = ("DELETE FROM courses "
                    "WHERE name = (%s)")
    for _, course in all_courses:
        cur.execute(delete_stmt,(course,))
        con.commit()

    cur.close()
    con.close()

def update_course():
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()

    all_courses = get_courses()
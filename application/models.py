import mysql.connector as mysql


def create_course(name,prof,grade,quarter,thoughts):
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
    insert_stmt = ("INSERT INTO Courses (Name, Professor, Grade, Quarter, Thoughts) "
                    "VALUES (%s,%s,%s,%s,%s)")

    cur.execute(insert_stmt,(name,prof,grade,quarter,thoughts))
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
    get_stmt = ("SELECT * FROM Courses")
    
    cur.execute(get_stmt)
    courses = cur.fetchall()

    cur.close()
    con.close()
    return courses

def delete_single_course(course_id):
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()

    delete_stmt = ("DELETE FROM Courses "
                    "WHERE ID=(%s)")
    
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
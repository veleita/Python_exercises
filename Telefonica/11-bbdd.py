import sqlite3

def createCourseDatabase():
    connection = sqlite3.connect("CourseDatabase")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Categorías (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE Cursos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL, FOREIGN KEY(categoria_id) REFERENCES categoria(id))")
    return cursor

def addCategory(cursor, category):
    if category not in ("Fácil", "Intermedio", "Avanzado"):
        raise ValueError("Categoría incorrecta")
    else:
        cursor.execute("INSERT INTO Categorías VALUES('" + category + "')")

def addCourse(cursor, category_id, course):
    if category_id not in ("Fácil", "Intermedio", "Avanzado"):
        raise ValueError("Categoría incorrecta")
    else:
        cursor.execute("INSERT INTO Cursos VALUES('" + course + ", " + category_id + "')")

def getCoursesFromCategory(cursor, category_id):
    if category_id not in ("Fácil", "Intermedio", "Avanzado"):
        raise ValueError("Categoría incorrecta")
    else:
        cursor.execute("SELECT * FROM Cursos WHERE categoria_id=" + category_id)


cursor = createCourseDatabase()
addCategory(cursor, "Fácil")
addCategory(cursor, "Intermedio")
addCategory(cursor, "Difícil")
try:
    addCategory(cursor, "Patata")
except:
    print(ValueError)
addCourse(cursor, 2, "Python")
addCourse(cursor, 2, "Behave")
addCourse(cursor, 3, "C")
getCoursesFromCategory(cursor, 2)
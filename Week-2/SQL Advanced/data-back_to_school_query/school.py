def students_from_city(db, city):
    """return a list of students from a specific city"""
    #keyword = "Paris"
    c = [city]
    query = '''SELECT * FROM students
        WHERE birth_city LIKE ?
        '''


    db.execute(query, c)
    rows = db.fetchall()
    return rows

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py

# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))

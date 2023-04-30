# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # return the number of directors contained in the database
    db.execute("""
    SELECT COUNT(*)
    FROM directors
               """)
    row = db.fetchone()
    return row[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("""
    SELECT name
    FROM directors
    ORDER BY name ASC
               """)
    rows = db.fetchall()
    out_list = []
    for name in rows:
        out_list.append(name[0])
    return out_list


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute("""
    SELECT title FROM movies WHERE UPPER(title)
    LIKE '% LOVE %' OR UPPER(title) LIKE 'LOVE %'
    OR UPPER(title) LIKE '% LOVE' OR UPPER(title) LIKE 'LOVE'
    OR UPPER(title) LIKE '% LOVE''%' OR UPPER(title) LIKE '% LOVE.'
    OR UPPER(title) LIKE 'LOVE,%' ORDER BY title ASC
               """)
    rows = db.fetchall()
    out_list = []
    for name in rows:
        out_list.append(name[0])
    return out_list


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    db.execute(query, (f"%{name}%",))
    count = db.fetchone()
    return count[0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = """
        SELECT title
        FROM movies
        WHERE minutes > ?
        ORDER BY title
    """
    db.execute(query, (min_length,))
    movies = db.fetchall()
    return [movie[0] for movie in movies]

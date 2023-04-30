# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    db.execute("""
    SELECT movies.title, movies.genres, directors.name
    FROM movies
    JOIN directors ON directors.id = movies.director_id
    """)
    rows = db.fetchall()
    return rows


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    db.execute("""
    SELECT movies.title,
    movies.start_year
    FROM movies INNER JOIN directors ON directors.id = movies.director_id
    WHERE directors.death_year < movies.start_year
    ORDER BY directors.name ASC
               """)
    rows = db.fetchall()
    out_list = []
    for name in rows:
        out_list.append(name[0])
    return out_list


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query = ("""
    SELECT genres, count(*), ROUND(AVG(minutes), 2)
    FROM movies
    WHERE genres = ?
    """)
    db.execute(query, (genre_name,))
    stat = db.fetchone()
    print(stat)
    return {
        "genre": stat[0],
        "number_of_movies": stat[1],
        "avg_length": stat[2]}


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query = ('''
    SELECT directors.name, COUNT(*) AS number_of_movies
    FROM movies
    JOIN directors ON directors.id = movies.director_id
    WHERE movies.genres = ?
    GROUP BY directors.name
    ORDER BY number_of_movies DESC, directors.name
    LIMIT 5
    ''')
    db.execute(query, (genre_name,))
    rows = db.fetchall()
    return rows


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    query = """
    SELECT (minutes / 30 + 1)*30 time_range, COUNT(*)
    FROM movies
    WHERE minutes IS NOT NULL
    GROUP BY time_range
    """
    return db.execute(query).fetchall()


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    query = """
    SELECT directors.name,
    movies.start_year - directors.birth_year AS age
    FROM directors
    JOIN movies ON directors.id = movies.director_id
    GROUP BY directors.name
    HAVING age IS NOT NULL
    ORDER BY age
    LIMIT 5
    """
    db.execute(query)
    rows = db.fetchall()
    return rows

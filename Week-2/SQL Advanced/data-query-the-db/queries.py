# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    query = '''SELECT * FROM orders
        ORDER BY OrderID ASC
        '''
    db.execute(query)
    rows = db.fetchall()
    return rows

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)

    db.execute("""
               SELECT *
        FROM orders
        WHERE OrderDate > ?
        AND OrderDate <= ?
               """,(date_from, date_to))
    rows = db.fetchall()
    return rows

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = '''
    SELECT * , JULIANDAY(orders.ShippedDate) - JULIANDAY(orders.OrderDate)
    as time_delta
    FROM orders
    ORDER BY time_delta
    '''

    db.execute(query)
    rows = db.fetchall()
    return rows

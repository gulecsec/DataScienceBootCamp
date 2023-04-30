# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    db.execute('''
               SELECT orders.orderid, orders.customerid, orders.orderdate,
RANK() OVER (PARTITION BY orders.customerid ORDER BY orders.orderdate) AS order_rank
FROM orders
JOIN customers ON customers.customerid = orders.customerid
ORDER BY customers.customerid
               ''')
    rows = db.fetchall()
    return rows


def order_cumulative_amount_per_customer(db):
    db.execute('''
    SELECT DISTINCT orders.orderid, orders.customerid, orders.orderdate, SUM(orderdetails.unitprice * orderdetails.quantity)
OVER (PARTITION BY orders.customerid ORDER BY orders.orderdate) AS order_rank
FROM orders
JOIN orderdetails ON orderdetails.orderid =orders.orderid
JOIN customers on customers.customerid = orders.customerid
ORDER by orders.customerid''')
    rows = db.fetchall()
    return rows

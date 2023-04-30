# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    db.execute('''
    SELECT orders.orderid, customers.contactname, employees.firstname
    FROM orders
    JOIN customers ON orders.Customerid = customers.CustomerID
    JOIN employees ON employees.employeeid = orders.employeeid
    ''')
    rows = db.fetchall()
    return rows

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    db.execute('''
    SELECT customers.contactname,
    SUM(orderdetails.unitprice * orderdetails.quantity) as total_spent
    FROM orderdetails
    JOIN orders ON orders.orderid = orderdetails.orderid
    JOIN customers on customers.customerid = orders.customerid
    GROUP BY customers.contactname
    ORDER BY total_spent''')
    rows = db.fetchall()
    return rows

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    db.execute('''
    SELECT Employees.FirstName,Employees.LastName, SUM(OrderDetails.UnitPrice*OrderDetails.Quantity) AS sum_of_purchase
    FROM Employees
    JOIN Orders ON Orders.EmployeeID  = Employees.EmployeeID
    JOIN OrderDetails ON OrderDetails.OrderID  = Orders.OrderID
    GROUP BY Employees.FirstName
    ORDER BY sum_of_purchase DESC
    LIMIT 1
    ''')
    rows = db.fetchall()
    for i in rows:
        result=()
        result += i
    return result

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    pass  # YOUR CODE HERE
    db.execute('''
    Select c2.ContactName, count (OrderID)
            from Customers c2
            LEFT JOIN Orders o  ON c2.CustomerID =o.CustomerID
            Group BY c2.ContactName
            Order BY count(OrderID) ASC
    ''')
    rows = db.fetchall()
    return rows

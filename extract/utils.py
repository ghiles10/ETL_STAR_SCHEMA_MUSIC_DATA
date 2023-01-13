def insert(table, cur, query):
    
    """this function insert data into the table"""
    
    for row in range(table.count()):
        cur.execute(query, tuple(table.collect()[row]) )
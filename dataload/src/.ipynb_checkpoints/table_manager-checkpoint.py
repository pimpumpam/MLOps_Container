def fetch_one(cursor, query):
    
    cursor.execute(query)
    
    return cursor.fetchone()
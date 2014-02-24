class BaseConnection():
    """Serves as a base for database connections
    """
    
    def __init__(self):
        """Initialize a new connection
        """
        self._closed = False
        
    def close(self):
        """Close the connection. The connection will not be usable after closing.
        """
        self._closed = True
        return self._connection.close()   
            
    def commit(self):
        """Commit the transaction to the database.
        """
        return self._connection.commit()
    
    def rollback(self):
        """Rollback the changes made in the transaction.
        """
        return self._connection.rollback()

class BaseCursor():
    """Serves as a base for a database cursor
    """
    
    def __init__(self, connection):
        """Initialize a new cursor, a true DB-API2.0 connection is needed.
        """
        self._connection = connection
        self._cursor = self._connection.cursor()
                      
    def fetchone(self):
        """Fetch one result from the cursor
        """
        return self._cursor.fetchone()
    
    def fetchall(self):
        """Fetch all results from the cursor
        """
        return self._cursor.fetchall()
    
    def _get_row_count(self):
        """Get the actual row count for the last operation executed on the cursor
        """
        return self._cursor.rowcount
    
    rowcount = property(_get_row_count, None, 
    """The actual row count for the last operation executed on the cursor. This is a read-only 
    property
    """)
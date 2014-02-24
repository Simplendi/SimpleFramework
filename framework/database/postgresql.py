import postgresql.driver.dbapi20 as postgresql

from .base import BaseConnection, BaseCursor

"""This offers a connection to PostgreSQL with the py-postgresql package (the module is named
postgresql).
"""

class Connection(BaseConnection):
    
    def __init__(self, **kwargs):
        """Connect to the server with the arguments passed through.
        """
        super(Connection, self).__init__()
        
        self._connection = postgresql.connect(**kwargs)
        
    def cursor(self):
        """Get a cursor.
        """
        return Cursor(self._connection)
        

class Cursor(BaseCursor):
        
    def execute(self, operation, parameters = None):
        """Execute a SQL operation with arguments on the cursor. The parameters should be wrapped in
        a single tuple. Returns the cursor itself.
        """
        if parameters == None:
            self._cursor = self._cursor.execute(operation)
        else:
            self._cursor = self._cursor.execute(operation, parameters)
        return self

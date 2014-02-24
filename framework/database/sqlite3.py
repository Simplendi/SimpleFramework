import sqlite3

from .base import BaseConnection, BaseCursor

"""This module connects to sqlite3 with the build in sqlite3 library of Python 3
"""

class Connection(BaseConnection):
    
    def __init__(self, **kwargs):
        """Connect to the server with the arguments passed through.
        """        
        super(Connection, self).__init__()
        
        self._connection = sqlite3.connect(**kwargs)
        
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
            operation = operation.replace("%s","?")
            self._cursor = self._cursor.execute(operation, parameters)
        return self

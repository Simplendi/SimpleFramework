class Pool():
    """A database connection pool. Follow PEP 249: DB-API2 with positional 
    """    
    def __init__(self, database_type = None, **kwargs):
        self._pool = []
        self._connection_arguments = kwargs
        self._importDatabaseModule(database_type)

    def _importDatabaseModule(self, database_type):
        """Find and import the database module which fits the given database_type. 
        """
        if database_type.upper() == "SQLITE3":
            try:
                import sqlite3
            except ImportError:
                raise ValueError("No library available to support sqlite3 databases.")
            else:
                import framework.database.sqlite3
                self._databasemodule = framework.database.sqlite3
        elif database_type.upper() == "POSTGRESQL":
            try:
                import postgresql
            except ImportError:
                raise ValueError("No library available to support postgresql databases.")
            else:
                import framework.database.postgresql
                self._databasemodule = framework.database.postgresql
        else:
            raise ValueError("Unknown database type.")
    
    def connect(self):
        """Returns a connection from the pool or create one if none exists
        """
        
        # If no connection exists
        if not len(self._pool):
            # Create a connection
            connection = self._databasemodule.Connection(**self._connection_arguments)
            
            # Add it to the pool
            self._pool.append(connection)
        
        return self._pool[0]
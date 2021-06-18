from .httpexception import HttpException

class HttpForbiddenException(HttpException):
    """Exception thrown when a 403 status code has to be returned
    """
       
    def __init__(self, reason = None):
        """Initialize a HttpForbiddenException
        """
        
        # Set status code
        self.statuscode = 403
        
        # Set reason
        if not reason:
            reason = ""
        self.reason = reason
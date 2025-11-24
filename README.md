# SimpleFramework

A lightweight WSGI web framework for Python that provides essential tools for building web applications with minimal complexity.

## Features

- **WSGI-compliant**: Compatible with any WSGI server
- **Flexible routing**: Support for URL patterns with regex, static file serving, and request forwarding
- **Session management**: Built-in session handling with database persistence
- **Cookie handling**: Full cookie support including HttpOnly, Secure, and SameSite attributes
- **Request parsing**: Support for form data, JSON, and multipart/form-data
- **HTTP exceptions**: Clean exception handling for HTTP status codes
- **Email support**: Built-in email sending capabilities
- **Static file serving**: Efficient static file handler with MIME type detection

## Installation

```bash
pip install SimpleFramework
```

## Quick Start

```python
from framework import Application, Router, State

# Create application and router
app = Application()
router = Router()

# Define a route
def hello(state):
    state.response.body = "Hello, World!"
    return state

router.addMapping(r'^/$', hello)

# Set the router as the controller
app.controller = router

# Run the development server
if __name__ == '__main__':
    app.serve(port=8000)
```

## Core Components

### Application
The main application class that handles WSGI requests and manages the request/response lifecycle.

### Router
Handles URL routing with support for:
- Regular expression patterns
- Static file serving
- Request forwarding to sub-applications
- HTTP method filtering

### State
Encapsulates request, response, and session data for each request.

### Request
Provides access to:
- HTTP method, headers, and cookies
- Query parameters and form data
- JSON request bodies
- Accept headers (content negotiation)

### Response
Manage responses with:
- Status codes
- Headers and cookies
- Body content (text, JSON, binary)
- Redirects

### Session
Dictionary-like session storage with:
- Automatic session ID generation (64-byte secure random IDs)
- Expiration management
- Database persistence support

## Configuration

```python
from framework import Config

config = Config()
config["session_cookie"] = "session_id"
config["session_lifetime"] = 1  # hours
config["session_httponly"] = True
config["session_secure"] = True
config["session_samesite"] = "Lax"  # "Strict", "Lax", or "None"
```

## Examples

### Handling JSON Requests

```python
def api_endpoint(state):
    if state.request.content_type.startswith("application/json"):
        data = state.request.body
        state.response.setJsonBody({"status": "success", "data": data})
    return state
```

### Using Sessions

```python
def login(state):
    state.session["user_id"] = 123
    state.session["username"] = "john"
    state.response.body = "Logged in!"
    return state
```

### Static Files

```python
router.addStaticMapping(r'^/static/', '/path/to/static/files')
```

### Setting Cookies

```python
def set_cookie(state):
    state.response.cookies["my_cookie"] = "value"
    state.response.cookies.setHttpOnly("my_cookie", True)
    state.response.cookies.setSecure("my_cookie", True)
    state.response.cookies.setSameSite("my_cookie", "Strict")
    return state
```

## Requirements

- Python 3.7+

## License

MIT License

## Author

Simplendi - info@simplendi.com

## Repository

https://github.com/Simplendi/SimpleFramework

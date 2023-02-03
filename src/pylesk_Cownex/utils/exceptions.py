class PylesException(Exception):
    """Base Exception"""
    pass


class Forbidden(Exception):
    """Raise when 403"""
    pass


class NotFound(Exception):
    """Raise when 404"""
    pass


class BadRequest(Exception):
    """Raise when url/parameter wrong"""
    pass


class APIError(Exception):
    """Raise when api error"""
    pass

class PicardWebsiteError(Exception):
    """ Base class for app exceptions. """
    pass


class BaseError(PicardWebsiteError):
    def __init__(self, code, desc=None, status=400):
        self.code = code
        self.desc = desc
        self.status = status


class LoginError(PicardWebsiteError):
    def __init__(self, code, redirect_uri=None):
        self.code = code
        self.redirect_uri = redirect_uri


class NotFound(PicardWebsiteError):
    def __init__(self, desc=None):
        self.code = 'not_found'
        self.desc = desc
        self.status = 404


class AccessDenied(BaseError):
    def __init__(self):
        super(AccessDenied, self).__init__(
            code='access_denied',
            desc='Access to the requested resource has been denied',
            status=403)


class NotAuthorized(BaseError):
    def __init__(self):
        super(NotAuthorized, self).__init__(
            code='not_authorized',
            desc='You need to be authorized to access the requested resource',
            status=401)


class ServerError(BaseError):
    def __init__(self):
        super(ServerError, self).__init__(
            code='server_error',
            desc='The authorization server encountered an unexpected '
                 'condition that prevented it from fulfilling the request.',
            status=500)


class LimitExceeded(BaseError):
    def __init__(self, desc=''):
        super(LimitExceeded, self).__init__(
            code='limit_exceeded',
            desc=desc,
            status=403)


class InvalidRequest(BaseError):
    def __init__(self, desc=''):
        super(InvalidRequest, self).__init__(
            code='invalid_request',
            desc=desc,
            status=400)


class ParserError(PicardWebsiteError):
    def __init__(self, key, desc):
        self.key = key
        self.desc = desc


class MissingDataError(ParserError):
    def __init__(self, key):
        super(MissingDataError, self).__init__(
            key=key,
            desc='missing')

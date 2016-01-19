"""
Access Token Auth plugin for HTTPie.

"""

from httpie.plugins import AuthPlugin

try:
    import urlparse
except ImportError:
    import urllib.parse

__version__ = '0.1.0'
__author__ = 'Nick Satterly'
__licence__ = 'MIT'


class TokenAuth:
    def __init__(self, token_type, access_token):
        self.token_type = token_type
        self.access_token = access_token.encode('ascii')

    def __call__(self, r):

        r.headers['Authorization'] = '%s %s' % (self.token_type, self.access_token)

        return r


class TokenAuthPlugin(AuthPlugin):

    name = 'Access Token auth'
    auth_type = 'token'
    description = ''

    def get_auth(self, username, password):
        return TokenAuth(token_type=username, access_token=password)

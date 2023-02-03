# Base API

import exceptions


class PleskAPIClient(object):
    """"""

    def __int__(self, api_token=None, username=None, password=None, basic_auth=False):
        """
        Create an API Instance.
        :param api_token: Plesk-API Token
        :param username:Admin Username
        :param password:Admin Password
        :param basic_auth: Use Basic auth with Username and Password.
        """
        self._api_token = api_token
        self._username = username
        self._password = password

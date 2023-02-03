# Base API
import requests

import exceptions


def format_response(response):
    """
    Check and Format header
    :param response:
    :return: response
    """
    return response


class PleskAPIClient(object):
    """"""

    def __int__(self, url, api_token=None):
        """
        Create an API Instance.
        :param api_token: Plesk-API Token
        :param username:Admin Username
        :param password:Admin Password
        :param basic_auth: Use Basic auth with Username and Password.
        """
        if not api_token:
            raise exceptions.PylesException('No API-Token defined.')
        self.url = url
        self._api_token = api_token

    def _api_request(self, endpoint, methode='GET', params=None, data=None, custom_header=None):
        if not endpoint:
            raise exceptions.BadRequest('No Endpoint defined.')
        if not methode:
            raise exceptions.BadRequest('No Methode defined.')
        url = self.url + endpoint
        if custom_header:
            headers = custom_header
        else:
            headers = {
                'Authorization': f'Bearer {self._api_token}',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        if methode == 'GET':
            response = requests.get(url, params=params, data=data, headers=headers)
        elif methode == 'POST':
            response = requests.post(url, params=params, data=data, headers=headers)
        elif methode == 'PUT':
            response = requests.put(url, params=params, data=data, headers=headers)
        elif methode == 'DELETE':
            response = requests.delete(url, params=params, data=data, headers=headers)
        else:
            raise exceptions.PylesException('No valid Methode defined.')
        return format_response(response)

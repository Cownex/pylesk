import array

from ..utils.base_api import PleskAPIClient
from ..utils.exceptions import BadRequest

"""Auth entry points"""
class Authentication(PleskAPIClient):

    def generate_secret_key(self, login: str, description: str, ip: str = None, ips: array =None):
        """
        Generate a secret key
        :param ip: The IP address that will be linked to the key. If this node or 'ips' node is not specified, the IP address of the request sender will be used.
        :param ips: Array of IP addresses that will be linked to the key. If this node or 'ip' node is not specified, the IP address of the request sender will be used.
        :param login: The login name of an existing customer or a reseller that will have this secret key. The customer's or reseller's account should be active. If this node is not specified, the administrator's login will be used.
        :param description: Additional information about the key.
        :return:
        """
        if not login or not description:
            raise BadRequest('Required Parameter not defined.')
        data = {
            'ip': ip,
            'ips': ips,
            'login': login,
            'description': description
        }
        return self._api_request('/auth/keys', methode='POST', data=data)

    def delete_secret_key(self, key_id: str):
        """
        Delete a secret key
        :param key_id: Key ID
        :return:
        """
        if not key_id:
            raise BadRequest('Required Parameter not defined.')
        return self._api_request(f'/auth/keys/{key_id}', methode='DELETE')

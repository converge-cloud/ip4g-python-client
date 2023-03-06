# coding: utf-8

"""
    IBM Power Systems for Google Cloud API

    IBM Power Systems for Google Cloud API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: ip4g@convergetp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.p_cloud_instance_ssh_keys_api import PCloudInstanceSSHKeysApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPCloudInstanceSSHKeysApi(unittest.TestCase):
    """PCloudInstanceSSHKeysApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.p_cloud_instance_ssh_keys_api.PCloudInstanceSSHKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pcloud_cloudinstances_sshkeys_delete(self):
        """Test case for pcloud_cloudinstances_sshkeys_delete

        Delete a CloudInstance's SSH key by name  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_sshkeys_get(self):
        """Test case for pcloud_cloudinstances_sshkeys_get

        Get a CloudInstance's SSH Key by name  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_sshkeys_getall(self):
        """Test case for pcloud_cloudinstances_sshkeys_getall

        List a CloudInstance's SSH Keys  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_sshkeys_post(self):
        """Test case for pcloud_cloudinstances_sshkeys_post

        Add a new SSH key to Cloud Instance  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_sshkeys_put(self):
        """Test case for pcloud_cloudinstances_sshkeys_put

        Update an SSH Key by SSH name  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
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
from swagger_client.api.p_cloud_instances_api import PCloudInstancesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPCloudInstancesApi(unittest.TestCase):
    """PCloudInstancesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.p_cloud_instances_api.PCloudInstancesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pcloud_cloudinstances_delete(self):
        """Test case for pcloud_cloudinstances_delete

        Delete a Power Cloud Instance  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_get(self):
        """Test case for pcloud_cloudinstances_get

        Get a Cloud Instance's current state/information  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_put(self):
        """Test case for pcloud_cloudinstances_put

        Update / Upgrade a Cloud Instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

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

import ip4g
from ip4g.api.p_cloud_snapshots_api import PCloudSnapshotsApi  # noqa: E501
from ip4g.rest import ApiException


class TestPCloudSnapshotsApi(unittest.TestCase):
    """PCloudSnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = ip4g.api.p_cloud_snapshots_api.PCloudSnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pcloud_cloudinstances_snapshots_delete(self):
        """Test case for pcloud_cloudinstances_snapshots_delete

        Delete a PVM instance snapshot of a cloud instance  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_snapshots_get(self):
        """Test case for pcloud_cloudinstances_snapshots_get

        Get the detail of a snapshot  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_snapshots_getall(self):
        """Test case for pcloud_cloudinstances_snapshots_getall

        List all PVM instance snapshots for this cloud instance  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_snapshots_put(self):
        """Test case for pcloud_cloudinstances_snapshots_put

        Update a PVM instance snapshot  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

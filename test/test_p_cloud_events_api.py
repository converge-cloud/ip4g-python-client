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
from ip4g.api.p_cloud_events_api import PCloudEventsApi  # noqa: E501
from ip4g.rest import ApiException


class TestPCloudEventsApi(unittest.TestCase):
    """PCloudEventsApi unit test stubs"""

    def setUp(self):
        self.api = ip4g.api.p_cloud_events_api.PCloudEventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pcloud_events_get(self):
        """Test case for pcloud_events_get

        Get a single event  # noqa: E501
        """
        pass

    def test_pcloud_events_getquery(self):
        """Test case for pcloud_events_getquery

        Get events from this cloud instance since a specific timestamp  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

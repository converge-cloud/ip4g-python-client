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
from swagger_client.api.p_cloud_volumes_api import PCloudVolumesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPCloudVolumesApi(unittest.TestCase):
    """PCloudVolumesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.p_cloud_volumes_api.PCloudVolumesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pcloud_cloudinstances_volumes_action_post(self):
        """Test case for pcloud_cloudinstances_volumes_action_post

        Perform an action on a Volume  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_volumes_delete(self):
        """Test case for pcloud_cloudinstances_volumes_delete

        Delete a cloud instance volume  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_volumes_get(self):
        """Test case for pcloud_cloudinstances_volumes_get

        Detailed info of a volume  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_volumes_getall(self):
        """Test case for pcloud_cloudinstances_volumes_getall

        List all volumes for this cloud instance  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_volumes_post(self):
        """Test case for pcloud_cloudinstances_volumes_post

        Create a new data Volume  # noqa: E501
        """
        pass

    def test_pcloud_cloudinstances_volumes_put(self):
        """Test case for pcloud_cloudinstances_volumes_put

        Update a cloud instance volume  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_delete(self):
        """Test case for pcloud_pvminstances_volumes_delete

        Detach a volume from a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_get(self):
        """Test case for pcloud_pvminstances_volumes_get

        Detailed info of a volume attached to a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_getall(self):
        """Test case for pcloud_pvminstances_volumes_getall

        List all volumes attached to a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_post(self):
        """Test case for pcloud_pvminstances_volumes_post

        Attach a volume to a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_put(self):
        """Test case for pcloud_pvminstances_volumes_put

        Update a volume attached to a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_pvminstances_volumes_setboot_put(self):
        """Test case for pcloud_pvminstances_volumes_setboot_put

        Set the PVMInstance volume as the boot volume  # noqa: E501
        """
        pass

    def test_pcloud_v2_pvminstances_volumes_post(self):
        """Test case for pcloud_v2_pvminstances_volumes_post

        Attach all volumes to a PVMInstance  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumes_clone_post_v2(self):
        """Test case for pcloud_v2_volumes_clone_post_v2

        Create a volume clone for specified volumes  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumes_clonetasks_get(self):
        """Test case for pcloud_v2_volumes_clonetasks_get

        Get the status of a volumes clone request for the specified clone task ID  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumes_post(self):
        """Test case for pcloud_v2_volumes_post

        Create multiple data volumes from a single definition  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_cancel_post(self):
        """Test case for pcloud_v2_volumesclone_cancel_post

        Cancel a volumes-clone request, initiates the Cleanup action Cleanup action performs the cleanup of the preparatory clones and snapshot volumes   # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_delete(self):
        """Test case for pcloud_v2_volumesclone_delete

        Delete a volumes-clone request  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_execute_post(self):
        """Test case for pcloud_v2_volumesclone_execute_post

        Initiate the Execute action for a volumes-clone request Execute action creates the cloned volumes using the volume snapshots   # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_get(self):
        """Test case for pcloud_v2_volumesclone_get

        Get the details for a volumes-clone request  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_getall(self):
        """Test case for pcloud_v2_volumesclone_getall

        Get the list of volumes-clone request for a cloud instance  # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_post(self):
        """Test case for pcloud_v2_volumesclone_post

        Create a new volumes clone request and initiates the Prepare action   Requires a minimum of two volumes   Requires a minimum of one volume to be in the 'in-use' state   Requires a unique volumes clone name   Prepare action does the preparatory work for creating the snapshot volumes   # noqa: E501
        """
        pass

    def test_pcloud_v2_volumesclone_start_post(self):
        """Test case for pcloud_v2_volumesclone_start_post

        Initiate the Start action for a volumes-clone request Start action starts the consistency group to initiate the flash copy   # noqa: E501
        """
        pass

    def test_pcloud_volumes_clone_post(self):
        """Test case for pcloud_volumes_clone_post

        Create a volume clone for specified volumes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

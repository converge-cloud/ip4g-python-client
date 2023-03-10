# coding: utf-8

"""
    IBM Power Systems for Google Cloud API

    IBM Power Systems for Google Cloud API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: ip4g@convergetp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ip4g.api_client import ApiClient


class PCloudPlacementGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pcloud_placementgroups_delete(self, cloud_instance_id, placement_group_id, **kwargs):  # noqa: E501
        """Delete Server Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_delete(cloud_instance_id, placement_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_delete_with_http_info(cloud_instance_id, placement_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_delete_with_http_info(cloud_instance_id, placement_group_id, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_delete_with_http_info(self, cloud_instance_id, placement_group_id, **kwargs):  # noqa: E501
        """Delete Server Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_delete_with_http_info(cloud_instance_id, placement_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'placement_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_delete`")  # noqa: E501
        # verify the required parameter 'placement_group_id' is set
        if self.api_client.client_side_validation and ('placement_group_id' not in params or
                                                       params['placement_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `placement_group_id` when calling `pcloud_placementgroups_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'placement_group_id' in params:
            path_params['placement_group_id'] = params['placement_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_placementgroups_get(self, cloud_instance_id, placement_group_id, **kwargs):  # noqa: E501
        """Get Server Placement Group detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_get(cloud_instance_id, placement_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_get_with_http_info(cloud_instance_id, placement_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_get_with_http_info(cloud_instance_id, placement_group_id, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_get_with_http_info(self, cloud_instance_id, placement_group_id, **kwargs):  # noqa: E501
        """Get Server Placement Group detail  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_get_with_http_info(cloud_instance_id, placement_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'placement_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_get`")  # noqa: E501
        # verify the required parameter 'placement_group_id' is set
        if self.api_client.client_side_validation and ('placement_group_id' not in params or
                                                       params['placement_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `placement_group_id` when calling `pcloud_placementgroups_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'placement_group_id' in params:
            path_params['placement_group_id'] = params['placement_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlacementGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_placementgroups_getall(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Get all Server Placement Groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_getall(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: PlacementGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_getall_with_http_info(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Get all Server Placement Groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_getall_with_http_info(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: PlacementGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_getall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_getall`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlacementGroups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_placementgroups_members_delete(self, cloud_instance_id, placement_group_id, body, **kwargs):  # noqa: E501
        """Remove Server from Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_members_delete(cloud_instance_id, placement_group_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :param PlacementGroupServer body: Parameters for removing a Server in a Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_members_delete_with_http_info(cloud_instance_id, placement_group_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_members_delete_with_http_info(cloud_instance_id, placement_group_id, body, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_members_delete_with_http_info(self, cloud_instance_id, placement_group_id, body, **kwargs):  # noqa: E501
        """Remove Server from Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_members_delete_with_http_info(cloud_instance_id, placement_group_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :param PlacementGroupServer body: Parameters for removing a Server in a Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'placement_group_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_members_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_members_delete`")  # noqa: E501
        # verify the required parameter 'placement_group_id' is set
        if self.api_client.client_side_validation and ('placement_group_id' not in params or
                                                       params['placement_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `placement_group_id` when calling `pcloud_placementgroups_members_delete`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `pcloud_placementgroups_members_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'placement_group_id' in params:
            path_params['placement_group_id'] = params['placement_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}/members', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlacementGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_placementgroups_members_post(self, cloud_instance_id, placement_group_id, body, **kwargs):  # noqa: E501
        """Add Server to Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_members_post(cloud_instance_id, placement_group_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :param PlacementGroupServer body: Parameters for adding a server to a Server Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_members_post_with_http_info(cloud_instance_id, placement_group_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_members_post_with_http_info(cloud_instance_id, placement_group_id, body, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_members_post_with_http_info(self, cloud_instance_id, placement_group_id, body, **kwargs):  # noqa: E501
        """Add Server to Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_members_post_with_http_info(cloud_instance_id, placement_group_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str placement_group_id: Placement Group ID (required)
        :param PlacementGroupServer body: Parameters for adding a server to a Server Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'placement_group_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_members_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_members_post`")  # noqa: E501
        # verify the required parameter 'placement_group_id' is set
        if self.api_client.client_side_validation and ('placement_group_id' not in params or
                                                       params['placement_group_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `placement_group_id` when calling `pcloud_placementgroups_members_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `pcloud_placementgroups_members_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'placement_group_id' in params:
            path_params['placement_group_id'] = params['placement_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlacementGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_placementgroups_post(self, cloud_instance_id, body, **kwargs):  # noqa: E501
        """Create a new Server Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_post(cloud_instance_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param PlacementGroupCreate body: Parameters for the creation of a new Server Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_placementgroups_post_with_http_info(cloud_instance_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_placementgroups_post_with_http_info(cloud_instance_id, body, **kwargs)  # noqa: E501
            return data

    def pcloud_placementgroups_post_with_http_info(self, cloud_instance_id, body, **kwargs):  # noqa: E501
        """Create a new Server Placement Group  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_placementgroups_post_with_http_info(cloud_instance_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param PlacementGroupCreate body: Parameters for the creation of a new Server Placement Group (required)
        :return: PlacementGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_placementgroups_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_placementgroups_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `pcloud_placementgroups_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlacementGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

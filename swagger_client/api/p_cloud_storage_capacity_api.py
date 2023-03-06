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

from swagger_client.api_client import ApiClient


class PCloudStorageCapacityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pcloud_storagecapacity_pools_get(self, cloud_instance_id, storage_pool_name, **kwargs):  # noqa: E501
        """Storage capacity for a storage pool in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_pools_get(cloud_instance_id, storage_pool_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str storage_pool_name: Storage pool name (required)
        :return: StoragePoolCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_storagecapacity_pools_get_with_http_info(cloud_instance_id, storage_pool_name, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_storagecapacity_pools_get_with_http_info(cloud_instance_id, storage_pool_name, **kwargs)  # noqa: E501
            return data

    def pcloud_storagecapacity_pools_get_with_http_info(self, cloud_instance_id, storage_pool_name, **kwargs):  # noqa: E501
        """Storage capacity for a storage pool in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_pools_get_with_http_info(cloud_instance_id, storage_pool_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str storage_pool_name: Storage pool name (required)
        :return: StoragePoolCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'storage_pool_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_storagecapacity_pools_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_storagecapacity_pools_get`")  # noqa: E501
        # verify the required parameter 'storage_pool_name' is set
        if self.api_client.client_side_validation and ('storage_pool_name' not in params or
                                                       params['storage_pool_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_pool_name` when calling `pcloud_storagecapacity_pools_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'storage_pool_name' in params:
            path_params['storage_pool_name'] = params['storage_pool_name']  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-pools/{storage_pool_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoragePoolCapacity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_storagecapacity_pools_getall(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Storage capacity for all available storage pools in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_pools_getall(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: StoragePoolsCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_storagecapacity_pools_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_storagecapacity_pools_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
            return data

    def pcloud_storagecapacity_pools_getall_with_http_info(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Storage capacity for all available storage pools in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_pools_getall_with_http_info(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: StoragePoolsCapacity
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
                    " to method pcloud_storagecapacity_pools_getall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_storagecapacity_pools_getall`")  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-pools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoragePoolsCapacity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_storagecapacity_types_get(self, cloud_instance_id, storage_type_name, **kwargs):  # noqa: E501
        """Storage capacity for a storage type in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_types_get(cloud_instance_id, storage_type_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str storage_type_name: Storage type name (required)
        :return: StorageTypeCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_storagecapacity_types_get_with_http_info(cloud_instance_id, storage_type_name, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_storagecapacity_types_get_with_http_info(cloud_instance_id, storage_type_name, **kwargs)  # noqa: E501
            return data

    def pcloud_storagecapacity_types_get_with_http_info(self, cloud_instance_id, storage_type_name, **kwargs):  # noqa: E501
        """Storage capacity for a storage type in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_types_get_with_http_info(cloud_instance_id, storage_type_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str storage_type_name: Storage type name (required)
        :return: StorageTypeCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'storage_type_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_storagecapacity_types_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_storagecapacity_types_get`")  # noqa: E501
        # verify the required parameter 'storage_type_name' is set
        if self.api_client.client_side_validation and ('storage_type_name' not in params or
                                                       params['storage_type_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `storage_type_name` when calling `pcloud_storagecapacity_types_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'storage_type_name' in params:
            path_params['storage_type_name'] = params['storage_type_name']  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-types/{storage_type_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageTypeCapacity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_storagecapacity_types_getall(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Storage capacity for all available storage types in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_types_getall(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: StorageTypesCapacity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_storagecapacity_types_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_storagecapacity_types_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
            return data

    def pcloud_storagecapacity_types_getall_with_http_info(self, cloud_instance_id, **kwargs):  # noqa: E501
        """Storage capacity for all available storage types in a region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_storagecapacity_types_getall_with_http_info(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :return: StorageTypesCapacity
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
                    " to method pcloud_storagecapacity_types_getall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_storagecapacity_types_getall`")  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageTypesCapacity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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


class PCloudTenantsSSHKeysApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pcloud_tenants_sshkeys_delete(self, tenant_id, sshkey_name, **kwargs):  # noqa: E501
        """Delete a Tenant's SSH key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_delete(tenant_id, sshkey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_tenants_sshkeys_delete_with_http_info(tenant_id, sshkey_name, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_tenants_sshkeys_delete_with_http_info(tenant_id, sshkey_name, **kwargs)  # noqa: E501
            return data

    def pcloud_tenants_sshkeys_delete_with_http_info(self, tenant_id, sshkey_name, **kwargs):  # noqa: E501
        """Delete a Tenant's SSH key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_delete_with_http_info(tenant_id, sshkey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'sshkey_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_tenants_sshkeys_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `pcloud_tenants_sshkeys_delete`")  # noqa: E501
        # verify the required parameter 'sshkey_name' is set
        if self.api_client.client_side_validation and ('sshkey_name' not in params or
                                                       params['sshkey_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sshkey_name` when calling `pcloud_tenants_sshkeys_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501
        if 'sshkey_name' in params:
            path_params['sshkey_name'] = params['sshkey_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name}', 'DELETE',
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

    def pcloud_tenants_sshkeys_get(self, tenant_id, sshkey_name, **kwargs):  # noqa: E501
        """Get a Tenant's SSH Key by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_get(tenant_id, sshkey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_tenants_sshkeys_get_with_http_info(tenant_id, sshkey_name, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_tenants_sshkeys_get_with_http_info(tenant_id, sshkey_name, **kwargs)  # noqa: E501
            return data

    def pcloud_tenants_sshkeys_get_with_http_info(self, tenant_id, sshkey_name, **kwargs):  # noqa: E501
        """Get a Tenant's SSH Key by name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_get_with_http_info(tenant_id, sshkey_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'sshkey_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_tenants_sshkeys_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `pcloud_tenants_sshkeys_get`")  # noqa: E501
        # verify the required parameter 'sshkey_name' is set
        if self.api_client.client_side_validation and ('sshkey_name' not in params or
                                                       params['sshkey_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sshkey_name` when calling `pcloud_tenants_sshkeys_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501
        if 'sshkey_name' in params:
            path_params['sshkey_name'] = params['sshkey_name']  # noqa: E501

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
            '/pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SSHKey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_tenants_sshkeys_getall(self, tenant_id, **kwargs):  # noqa: E501
        """List a Tenant's SSH Keys  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_getall(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :return: SSHKeys
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_tenants_sshkeys_getall_with_http_info(tenant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_tenants_sshkeys_getall_with_http_info(tenant_id, **kwargs)  # noqa: E501
            return data

    def pcloud_tenants_sshkeys_getall_with_http_info(self, tenant_id, **kwargs):  # noqa: E501
        """List a Tenant's SSH Keys  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_getall_with_http_info(tenant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :return: SSHKeys
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_tenants_sshkeys_getall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `pcloud_tenants_sshkeys_getall`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501

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
            '/pcloud/v1/tenants/{tenant_id}/sshkeys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SSHKeys',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_tenants_sshkeys_post(self, tenant_id, body, **kwargs):  # noqa: E501
        """Add a new SSH key to the Tenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_post(tenant_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param SSHKey body: Parameters for the creation of a new SSH key (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_tenants_sshkeys_post_with_http_info(tenant_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_tenants_sshkeys_post_with_http_info(tenant_id, body, **kwargs)  # noqa: E501
            return data

    def pcloud_tenants_sshkeys_post_with_http_info(self, tenant_id, body, **kwargs):  # noqa: E501
        """Add a new SSH key to the Tenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_post_with_http_info(tenant_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param SSHKey body: Parameters for the creation of a new SSH key (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_tenants_sshkeys_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `pcloud_tenants_sshkeys_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `pcloud_tenants_sshkeys_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501

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
            '/pcloud/v1/tenants/{tenant_id}/sshkeys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SSHKey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_tenants_sshkeys_put(self, tenant_id, sshkey_name, body, **kwargs):  # noqa: E501
        """Update an SSH Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_put(tenant_id, sshkey_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :param SSHKey body: Parameters for updating a Tenant's SSH Key (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_tenants_sshkeys_put_with_http_info(tenant_id, sshkey_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_tenants_sshkeys_put_with_http_info(tenant_id, sshkey_name, body, **kwargs)  # noqa: E501
            return data

    def pcloud_tenants_sshkeys_put_with_http_info(self, tenant_id, sshkey_name, body, **kwargs):  # noqa: E501
        """Update an SSH Key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_tenants_sshkeys_put_with_http_info(tenant_id, sshkey_name, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str sshkey_name: SSH key name for a pcloud tenant (required)
        :param SSHKey body: Parameters for updating a Tenant's SSH Key (required)
        :return: SSHKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'sshkey_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_tenants_sshkeys_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `pcloud_tenants_sshkeys_put`")  # noqa: E501
        # verify the required parameter 'sshkey_name' is set
        if self.api_client.client_side_validation and ('sshkey_name' not in params or
                                                       params['sshkey_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sshkey_name` when calling `pcloud_tenants_sshkeys_put`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `pcloud_tenants_sshkeys_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501
        if 'sshkey_name' in params:
            path_params['sshkey_name'] = params['sshkey_name']  # noqa: E501

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
            '/pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SSHKey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_broker_auth_callback(self, **kwargs):  # noqa: E501
        """Returns an accessToken (and set cookie)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_callback(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_callback_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_callback_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_callback_with_http_info(self, **kwargs):  # noqa: E501
        """Returns an accessToken (and set cookie)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_callback_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_callback" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/callback', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_device_code_post(self, **kwargs):  # noqa: E501
        """Request a authorization device code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_device_code_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DeviceCode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_device_code_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_device_code_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_device_code_post_with_http_info(self, **kwargs):  # noqa: E501
        """Request a authorization device code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_device_code_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DeviceCode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_device_code_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/device/code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_device_token_post(self, body, **kwargs):  # noqa: E501
        """Poll for authorization device token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_device_token_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: Parameters for polling authorization device code (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_device_token_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_device_token_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def service_broker_auth_device_token_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Poll for authorization device token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_device_token_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: Parameters for polling authorization device code (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_device_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `service_broker_auth_device_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/auth/v1/device/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_info_token(self, **kwargs):  # noqa: E501
        """Information about current access token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_info_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TokenExtra
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_info_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_info_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_info_token_with_http_info(self, **kwargs):  # noqa: E501
        """Information about current access token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_info_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: TokenExtra
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_info_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/info/token', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenExtra',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_info_user(self, **kwargs):  # noqa: E501
        """Information about current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_info_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_info_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_info_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_info_user_with_http_info(self, **kwargs):  # noqa: E501
        """Information about current user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_info_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_info_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/info/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_login(self, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_login(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user id of the user
        :param str redirect_url: The URL to redirect to after login/registration
        :param str access_type: Determines if a refresh token is returned
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_login_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_login_with_http_info(self, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_login_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: The user id of the user
        :param str redirect_url: The URL to redirect to after login/registration
        :param str access_type: Determines if a refresh token is returned
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'redirect_url', 'access_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_login" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirect_url', params['redirect_url']))  # noqa: E501
        if 'access_type' in params:
            query_params.append(('access_type', params['access_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/login', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_logout(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_logout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_logout_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_logout_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_logout_with_http_info(self, **kwargs):  # noqa: E501
        """Logout  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_logout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_logout" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/logout', 'GET',
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

    def service_broker_auth_registration(self, tenant_id, entitlement_id, plan, icn, regions, **kwargs):  # noqa: E501
        """Registration of a new Tenant and Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_registration(tenant_id, entitlement_id, plan, icn, regions, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str entitlement_id: Entitlement ID of for this tenant (required)
        :param str plan: Plan for this tenant and entitlement (required)
        :param str icn: IBM Customer Number (ICN) for this tenant (required)
        :param list[str] regions: An array of regions matching the number of cloud-instances in the plan (required)
        :param str redirect_url: The URL to redirect to after login/registration
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_registration_with_http_info(tenant_id, entitlement_id, plan, icn, regions, **kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_registration_with_http_info(tenant_id, entitlement_id, plan, icn, regions, **kwargs)  # noqa: E501
            return data

    def service_broker_auth_registration_with_http_info(self, tenant_id, entitlement_id, plan, icn, regions, **kwargs):  # noqa: E501
        """Registration of a new Tenant and Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_registration_with_http_info(tenant_id, entitlement_id, plan, icn, regions, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: Tenant ID of a pcloud tenant (required)
        :param str entitlement_id: Entitlement ID of for this tenant (required)
        :param str plan: Plan for this tenant and entitlement (required)
        :param str icn: IBM Customer Number (ICN) for this tenant (required)
        :param list[str] regions: An array of regions matching the number of cloud-instances in the plan (required)
        :param str redirect_url: The URL to redirect to after login/registration
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'entitlement_id', 'plan', 'icn', 'regions', 'redirect_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and ('tenant_id' not in params or
                                                       params['tenant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `tenant_id` when calling `service_broker_auth_registration`")  # noqa: E501
        # verify the required parameter 'entitlement_id' is set
        if self.api_client.client_side_validation and ('entitlement_id' not in params or
                                                       params['entitlement_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `entitlement_id` when calling `service_broker_auth_registration`")  # noqa: E501
        # verify the required parameter 'plan' is set
        if self.api_client.client_side_validation and ('plan' not in params or
                                                       params['plan'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `plan` when calling `service_broker_auth_registration`")  # noqa: E501
        # verify the required parameter 'icn' is set
        if self.api_client.client_side_validation and ('icn' not in params or
                                                       params['icn'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `icn` when calling `service_broker_auth_registration`")  # noqa: E501
        # verify the required parameter 'regions' is set
        if self.api_client.client_side_validation and ('regions' not in params or
                                                       params['regions'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `regions` when calling `service_broker_auth_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenant_id', params['tenant_id']))  # noqa: E501
        if 'entitlement_id' in params:
            query_params.append(('entitlement_id', params['entitlement_id']))  # noqa: E501
        if 'plan' in params:
            query_params.append(('plan', params['plan']))  # noqa: E501
        if 'icn' in params:
            query_params.append(('icn', params['icn']))  # noqa: E501
        if 'regions' in params:
            query_params.append(('regions', params['regions']))  # noqa: E501
            collection_formats['regions'] = 'csv'  # noqa: E501
        if 'redirect_url' in params:
            query_params.append(('redirect_url', params['redirect_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/registration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_registration_callback(self, **kwargs):  # noqa: E501
        """Associates the user with a tenant and returns an accessToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_registration_callback(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_registration_callback_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_registration_callback_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_broker_auth_registration_callback_with_http_info(self, **kwargs):  # noqa: E501
        """Associates the user with a tenant and returns an accessToken  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_registration_callback_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AccessToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_registration_callback" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/v1/callback-registration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccessToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_broker_auth_token_post(self, body, **kwargs):  # noqa: E501
        """Request a new token from a refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_token_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenRequest body: Parameters for requesting a new Token from a Refresh Token (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_broker_auth_token_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.service_broker_auth_token_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def service_broker_auth_token_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Request a new token from a refresh token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_broker_auth_token_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenRequest body: Parameters for requesting a new Token from a Refresh Token (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_broker_auth_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `service_broker_auth_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/auth/v1/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

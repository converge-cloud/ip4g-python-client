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


class PCloudJobsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pcloud_cloudinstances_jobs_delete(self, cloud_instance_id, job_id, **kwargs):  # noqa: E501
        """Delete a cloud instance job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_delete(cloud_instance_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str job_id: PCloud Job ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_cloudinstances_jobs_delete_with_http_info(cloud_instance_id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_cloudinstances_jobs_delete_with_http_info(cloud_instance_id, job_id, **kwargs)  # noqa: E501
            return data

    def pcloud_cloudinstances_jobs_delete_with_http_info(self, cloud_instance_id, job_id, **kwargs):  # noqa: E501
        """Delete a cloud instance job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_delete_with_http_info(cloud_instance_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str job_id: PCloud Job ID (required)
        :return: Object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_cloudinstances_jobs_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_cloudinstances_jobs_delete`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in params or
                                                       params['job_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `job_id` when calling `pcloud_cloudinstances_jobs_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/jobs/{job_id}', 'DELETE',
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

    def pcloud_cloudinstances_jobs_get(self, cloud_instance_id, job_id, **kwargs):  # noqa: E501
        """List the detail of a job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_get(cloud_instance_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str job_id: PCloud Job ID (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_cloudinstances_jobs_get_with_http_info(cloud_instance_id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_cloudinstances_jobs_get_with_http_info(cloud_instance_id, job_id, **kwargs)  # noqa: E501
            return data

    def pcloud_cloudinstances_jobs_get_with_http_info(self, cloud_instance_id, job_id, **kwargs):  # noqa: E501
        """List the detail of a job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_get_with_http_info(cloud_instance_id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str job_id: PCloud Job ID (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_cloudinstances_jobs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_cloudinstances_jobs_get`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in params or
                                                       params['job_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `job_id` when calling `pcloud_cloudinstances_jobs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/jobs/{job_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pcloud_cloudinstances_jobs_getall(self, cloud_instance_id, **kwargs):  # noqa: E501
        """List up to the last 5 jobs initiated by the cloud instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_getall(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str operation_id: Operation ID to filter jobs (optional)
        :param str operation_target: Operation target to filter jobs (optional)
        :param str operation_action: Operation action to filter jobs (optional) vmCapture - includes operation action value (vmCapture) imageExport - includes operation action value (imageExport) imageImport - includes operation action value (imageImport) storage - includes operation action values (vmCapture,imageExport,imageImport)
        :return: Jobs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pcloud_cloudinstances_jobs_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pcloud_cloudinstances_jobs_getall_with_http_info(cloud_instance_id, **kwargs)  # noqa: E501
            return data

    def pcloud_cloudinstances_jobs_getall_with_http_info(self, cloud_instance_id, **kwargs):  # noqa: E501
        """List up to the last 5 jobs initiated by the cloud instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pcloud_cloudinstances_jobs_getall_with_http_info(cloud_instance_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cloud_instance_id: Cloud Instance ID of a PCloud Instance (required)
        :param str operation_id: Operation ID to filter jobs (optional)
        :param str operation_target: Operation target to filter jobs (optional)
        :param str operation_action: Operation action to filter jobs (optional) vmCapture - includes operation action value (vmCapture) imageExport - includes operation action value (imageExport) imageImport - includes operation action value (imageImport) storage - includes operation action values (vmCapture,imageExport,imageImport)
        :return: Jobs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cloud_instance_id', 'operation_id', 'operation_target', 'operation_action']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pcloud_cloudinstances_jobs_getall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cloud_instance_id' is set
        if self.api_client.client_side_validation and ('cloud_instance_id' not in params or
                                                       params['cloud_instance_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cloud_instance_id` when calling `pcloud_cloudinstances_jobs_getall`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cloud_instance_id' in params:
            path_params['cloud_instance_id'] = params['cloud_instance_id']  # noqa: E501

        query_params = []
        if 'operation_id' in params:
            query_params.append(('operation.id', params['operation_id']))  # noqa: E501
        if 'operation_target' in params:
            query_params.append(('operation.target', params['operation_target']))  # noqa: E501
        if 'operation_action' in params:
            query_params.append(('operation.action', params['operation_action']))  # noqa: E501

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
            '/pcloud/v1/cloud-instances/{cloud_instance_id}/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Jobs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

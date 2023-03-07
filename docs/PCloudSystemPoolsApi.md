# ip4g.PCloudSystemPoolsApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_systempools_get**](PCloudSystemPoolsApi.md#pcloud_systempools_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/system-pools | List of available system pools within a particular DataCenter


# **pcloud_systempools_get**
> SystemPools pcloud_systempools_get(cloud_instance_id)

List of available system pools within a particular DataCenter

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudSystemPoolsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List of available system pools within a particular DataCenter
    api_response = api_instance.pcloud_systempools_get(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudSystemPoolsApi->pcloud_systempools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |

### Return type

[**SystemPools**](SystemPools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

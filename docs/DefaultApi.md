# ip4g.DefaultApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_storagetypes_get**](DefaultApi.md#pcloud_cloudinstances_storagetypes_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-types | Get the list of storage types available for the given cloud instance&#39;s associated plan. 


# **pcloud_cloudinstances_storagetypes_get**
> StorageTypes pcloud_cloudinstances_storagetypes_get(cloud_instance_id)

Get the list of storage types available for the given cloud instance's associated plan. 

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = ip4g.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
configuration = ip4g.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ip4g.DefaultApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Get the list of storage types available for the given cloud instance's associated plan. 
    api_response = api_instance.pcloud_cloudinstances_storagetypes_get(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pcloud_cloudinstances_storagetypes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**StorageTypes**](StorageTypes.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


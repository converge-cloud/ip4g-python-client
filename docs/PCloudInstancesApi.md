# swagger_client.PCloudInstancesApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_delete**](PCloudInstancesApi.md#pcloud_cloudinstances_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id} | Delete a Power Cloud Instance
[**pcloud_cloudinstances_get**](PCloudInstancesApi.md#pcloud_cloudinstances_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id} | Get a Cloud Instance&#39;s current state/information
[**pcloud_cloudinstances_put**](PCloudInstancesApi.md#pcloud_cloudinstances_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id} | Update / Upgrade a Cloud Instance


# **pcloud_cloudinstances_delete**
> Object pcloud_cloudinstances_delete(cloud_instance_id)

Delete a Power Cloud Instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Delete a Power Cloud Instance
    api_response = api_instance.pcloud_cloudinstances_delete(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstancesApi->pcloud_cloudinstances_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_get**
> CloudInstance pcloud_cloudinstances_get(cloud_instance_id)

Get a Cloud Instance's current state/information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Get a Cloud Instance's current state/information
    api_response = api_instance.pcloud_cloudinstances_get(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstancesApi->pcloud_cloudinstances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**CloudInstance**](CloudInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_put**
> CloudInstance pcloud_cloudinstances_put(cloud_instance_id, body)

Update / Upgrade a Cloud Instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.CloudInstanceUpdate() # CloudInstanceUpdate | Parameters for updating a Power Cloud Instance

try:
    # Update / Upgrade a Cloud Instance
    api_response = api_instance.pcloud_cloudinstances_put(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstancesApi->pcloud_cloudinstances_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**CloudInstanceUpdate**](CloudInstanceUpdate.md)| Parameters for updating a Power Cloud Instance | 

### Return type

[**CloudInstance**](CloudInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


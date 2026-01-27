# ip4g.PCloudInstancesApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_delete**](PCloudInstancesApi.md#pcloud_cloudinstances_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id} | Delete a Power Cloud Instance
[**pcloud_cloudinstances_get**](PCloudInstancesApi.md#pcloud_cloudinstances_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id} | Get a Cloud Instance&#39;s current state/information
[**pcloud_cloudinstances_post**](PCloudInstancesApi.md#pcloud_cloudinstances_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id} | Create a Cloud Instance
[**pcloud_cloudinstances_put**](PCloudInstancesApi.md#pcloud_cloudinstances_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id} | Update / Upgrade a Cloud Instance


# **pcloud_cloudinstances_delete**
> Object pcloud_cloudinstances_delete(cloud_instance_id)

Delete a Power Cloud Instance

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
api_instance = ip4g.PCloudInstancesApi(ip4g.ApiClient(configuration))
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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

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
api_instance = ip4g.PCloudInstancesApi(ip4g.ApiClient(configuration))
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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_post**
> CloudInstance pcloud_cloudinstances_post(cloud_instance_id, body)

Create a Cloud Instance

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
api_instance = ip4g.PCloudInstancesApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.CloudInstancePublicCreate() # CloudInstancePublicCreate | Parameters for creating a Power Cloud Instance

try:
    # Create a Cloud Instance
    api_response = api_instance.pcloud_cloudinstances_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstancesApi->pcloud_cloudinstances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**CloudInstancePublicCreate**](CloudInstancePublicCreate.md)| Parameters for creating a Power Cloud Instance | 

### Return type

[**CloudInstance**](CloudInstance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

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
api_instance = ip4g.PCloudInstancesApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.CloudInstanceUpdate() # CloudInstanceUpdate | Parameters for updating a Power Cloud Instance

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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


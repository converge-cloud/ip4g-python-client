# ip4g.PCloudTasksApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_tasks_delete**](PCloudTasksApi.md#pcloud_tasks_delete) | **DELETE** /pcloud/v1/tasks/{task_id} | Delete a Task
[**pcloud_tasks_get**](PCloudTasksApi.md#pcloud_tasks_get) | **GET** /pcloud/v1/tasks/{task_id} | Get a Task


# **pcloud_tasks_delete**
> Object pcloud_tasks_delete(task_id)

Delete a Task

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
api_instance = ip4g.PCloudTasksApi(ip4g.ApiClient(configuration))
task_id = 'task_id_example' # str | PCloud Task ID

try:
    # Delete a Task
    api_response = api_instance.pcloud_tasks_delete(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTasksApi->pcloud_tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| PCloud Task ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_tasks_get**
> Task pcloud_tasks_get(task_id)

Get a Task

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
api_instance = ip4g.PCloudTasksApi(ip4g.ApiClient(configuration))
task_id = 'task_id_example' # str | PCloud Task ID

try:
    # Get a Task
    api_response = api_instance.pcloud_tasks_get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTasksApi->pcloud_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| PCloud Task ID | 

### Return type

[**Task**](Task.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ip4g.PCloudTasksApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

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

# create an instance of the API class
api_instance = ip4g.PCloudTasksApi()
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

No authorization required

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

# create an instance of the API class
api_instance = ip4g.PCloudTasksApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

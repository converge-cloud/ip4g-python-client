# ip4g.PCloudJobsApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_jobs_delete**](PCloudJobsApi.md#pcloud_cloudinstances_jobs_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/jobs/{job_id} | Delete a cloud instance job
[**pcloud_cloudinstances_jobs_get**](PCloudJobsApi.md#pcloud_cloudinstances_jobs_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/jobs/{job_id} | List the detail of a job
[**pcloud_cloudinstances_jobs_getall**](PCloudJobsApi.md#pcloud_cloudinstances_jobs_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/jobs | List up to the last 5 jobs initiated by the cloud instance


# **pcloud_cloudinstances_jobs_delete**
> Object pcloud_cloudinstances_jobs_delete(cloud_instance_id, job_id)

Delete a cloud instance job

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
api_instance = ip4g.PCloudJobsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
job_id = 'job_id_example' # str | PCloud Job ID

try:
    # Delete a cloud instance job
    api_response = api_instance.pcloud_cloudinstances_jobs_delete(cloud_instance_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudJobsApi->pcloud_cloudinstances_jobs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **job_id** | **str**| PCloud Job ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_jobs_get**
> Job pcloud_cloudinstances_jobs_get(cloud_instance_id, job_id)

List the detail of a job

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
api_instance = ip4g.PCloudJobsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
job_id = 'job_id_example' # str | PCloud Job ID

try:
    # List the detail of a job
    api_response = api_instance.pcloud_cloudinstances_jobs_get(cloud_instance_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudJobsApi->pcloud_cloudinstances_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **job_id** | **str**| PCloud Job ID | 

### Return type

[**Job**](Job.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_jobs_getall**
> Jobs pcloud_cloudinstances_jobs_getall(cloud_instance_id, operation_id=operation_id, operation_target=operation_target, operation_action=operation_action)

List up to the last 5 jobs initiated by the cloud instance

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
api_instance = ip4g.PCloudJobsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
operation_id = 'operation_id_example' # str | Operation ID to filter jobs (optional) (optional)
operation_target = 'operation_target_example' # str | Operation target to filter jobs (optional) (optional)
operation_action = 'operation_action_example' # str | Operation action to filter jobs (optional) vmCapture - includes operation action value (vmCapture) imageExport - includes operation action value (imageExport) imageImport - includes operation action value (imageImport) storage - includes operation action values (vmCapture,imageExport,imageImport) (optional)

try:
    # List up to the last 5 jobs initiated by the cloud instance
    api_response = api_instance.pcloud_cloudinstances_jobs_getall(cloud_instance_id, operation_id=operation_id, operation_target=operation_target, operation_action=operation_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudJobsApi->pcloud_cloudinstances_jobs_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **operation_id** | **str**| Operation ID to filter jobs (optional) | [optional] 
 **operation_target** | **str**| Operation target to filter jobs (optional) | [optional] 
 **operation_action** | **str**| Operation action to filter jobs (optional) vmCapture - includes operation action value (vmCapture) imageExport - includes operation action value (imageExport) imageImport - includes operation action value (imageImport) storage - includes operation action values (vmCapture,imageExport,imageImport) | [optional] 

### Return type

[**Jobs**](Jobs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


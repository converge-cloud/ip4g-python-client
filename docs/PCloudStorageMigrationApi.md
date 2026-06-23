# ip4g.PCloudStorageMigrationApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_storagemigration_action_post**](PCloudStorageMigrationApi.md#pcloud_cloudinstances_storagemigration_action_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-migration/{migration_id}/action | Perform an action on a storage migration job.
[**pcloud_cloudinstances_storagemigration_get**](PCloudStorageMigrationApi.md#pcloud_cloudinstances_storagemigration_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-migration/{migration_id} | Gets the status of a storage migration job.
[**pcloud_cloudinstances_storagemigration_getall**](PCloudStorageMigrationApi.md#pcloud_cloudinstances_storagemigration_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-migration | Lists all storage migration jobs for a given cloud instance.
[**pcloud_cloudinstances_storagemigration_post**](PCloudStorageMigrationApi.md#pcloud_cloudinstances_storagemigration_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-migration | Create a new storage migration job.


# **pcloud_cloudinstances_storagemigration_action_post**
> StorageMigrationActionResponse pcloud_cloudinstances_storagemigration_action_post(cloud_instance_id, migration_id, body=body)

Perform an action on a storage migration job.

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
api_instance = ip4g.PCloudStorageMigrationApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
migration_id = 'migration_id_example' # str | 
body = ip4g.StorageMigrationAction() # StorageMigrationAction |  (optional)

try:
    # Perform an action on a storage migration job.
    api_response = api_instance.pcloud_cloudinstances_storagemigration_action_post(cloud_instance_id, migration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageMigrationApi->pcloud_cloudinstances_storagemigration_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **migration_id** | **str**|  | 
 **body** | [**StorageMigrationAction**](StorageMigrationAction.md)|  | [optional] 

### Return type

[**StorageMigrationActionResponse**](StorageMigrationActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_storagemigration_get**
> StorageMigrationJobDetails pcloud_cloudinstances_storagemigration_get(cloud_instance_id, migration_id)

Gets the status of a storage migration job.

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
api_instance = ip4g.PCloudStorageMigrationApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
migration_id = 'migration_id_example' # str | 

try:
    # Gets the status of a storage migration job.
    api_response = api_instance.pcloud_cloudinstances_storagemigration_get(cloud_instance_id, migration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageMigrationApi->pcloud_cloudinstances_storagemigration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **migration_id** | **str**|  | 

### Return type

[**StorageMigrationJobDetails**](StorageMigrationJobDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_storagemigration_getall**
> StorageMigrationJobs pcloud_cloudinstances_storagemigration_getall(cloud_instance_id)

Lists all storage migration jobs for a given cloud instance.

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
api_instance = ip4g.PCloudStorageMigrationApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Lists all storage migration jobs for a given cloud instance.
    api_response = api_instance.pcloud_cloudinstances_storagemigration_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageMigrationApi->pcloud_cloudinstances_storagemigration_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**StorageMigrationJobs**](StorageMigrationJobs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_storagemigration_post**
> StorageMigrationJobDetails pcloud_cloudinstances_storagemigration_post(cloud_instance_id, body=body)

Create a new storage migration job.

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
api_instance = ip4g.PCloudStorageMigrationApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.StorageMigrationCreate() # StorageMigrationCreate |  (optional)

try:
    # Create a new storage migration job.
    api_response = api_instance.pcloud_cloudinstances_storagemigration_post(cloud_instance_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageMigrationApi->pcloud_cloudinstances_storagemigration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**StorageMigrationCreate**](StorageMigrationCreate.md)|  | [optional] 

### Return type

[**StorageMigrationJobDetails**](StorageMigrationJobDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


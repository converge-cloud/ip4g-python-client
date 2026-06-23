# ip4g.PCloudStorageCapacityApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_storagecapacity_pools_get**](PCloudStorageCapacityApi.md#pcloud_storagecapacity_pools_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-pools/{storage_pool_name} | Storage capacity for a storage pool in a region
[**pcloud_storagecapacity_pools_getall**](PCloudStorageCapacityApi.md#pcloud_storagecapacity_pools_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-pools | Storage capacity for all available storage pools in a region
[**pcloud_storagecapacity_types_get**](PCloudStorageCapacityApi.md#pcloud_storagecapacity_types_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-types/{storage_type_name} | Storage capacity for a storage type in a region
[**pcloud_storagecapacity_types_getall**](PCloudStorageCapacityApi.md#pcloud_storagecapacity_types_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/storage-capacity/storage-types | Storage capacity for all available storage types in a region


# **pcloud_storagecapacity_pools_get**
> StoragePoolCapacity pcloud_storagecapacity_pools_get(cloud_instance_id, storage_pool_name)

Storage capacity for a storage pool in a region

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
api_instance = ip4g.PCloudStorageCapacityApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
storage_pool_name = 'storage_pool_name_example' # str | Storage pool name

try:
    # Storage capacity for a storage pool in a region
    api_response = api_instance.pcloud_storagecapacity_pools_get(cloud_instance_id, storage_pool_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageCapacityApi->pcloud_storagecapacity_pools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **storage_pool_name** | **str**| Storage pool name | 

### Return type

[**StoragePoolCapacity**](StoragePoolCapacity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_storagecapacity_pools_getall**
> StoragePoolsCapacity pcloud_storagecapacity_pools_getall(cloud_instance_id)

Storage capacity for all available storage pools in a region

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
api_instance = ip4g.PCloudStorageCapacityApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Storage capacity for all available storage pools in a region
    api_response = api_instance.pcloud_storagecapacity_pools_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageCapacityApi->pcloud_storagecapacity_pools_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**StoragePoolsCapacity**](StoragePoolsCapacity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_storagecapacity_types_get**
> StorageTypeCapacity pcloud_storagecapacity_types_get(cloud_instance_id, storage_type_name)

Storage capacity for a storage type in a region

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
api_instance = ip4g.PCloudStorageCapacityApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
storage_type_name = 'storage_type_name_example' # str | Storage type name

try:
    # Storage capacity for a storage type in a region
    api_response = api_instance.pcloud_storagecapacity_types_get(cloud_instance_id, storage_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageCapacityApi->pcloud_storagecapacity_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **storage_type_name** | **str**| Storage type name | 

### Return type

[**StorageTypeCapacity**](StorageTypeCapacity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_storagecapacity_types_getall**
> StorageTypesCapacity pcloud_storagecapacity_types_getall(cloud_instance_id)

Storage capacity for all available storage types in a region

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
api_instance = ip4g.PCloudStorageCapacityApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Storage capacity for all available storage types in a region
    api_response = api_instance.pcloud_storagecapacity_types_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudStorageCapacityApi->pcloud_storagecapacity_types_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**StorageTypesCapacity**](StorageTypesCapacity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ip4g.PCloudPlacementGroupsApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_placementgroups_delete**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id} | Delete Server Placement Group
[**pcloud_placementgroups_get**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id} | Get Server Placement Group detail
[**pcloud_placementgroups_getall**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups | Get all Server Placement Groups
[**pcloud_placementgroups_members_delete**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_members_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}/members | Remove Server from Placement Group
[**pcloud_placementgroups_members_post**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_members_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups/{placement_group_id}/members | Add Server to Placement Group
[**pcloud_placementgroups_post**](PCloudPlacementGroupsApi.md#pcloud_placementgroups_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/placement-groups | Create a new Server Placement Group


# **pcloud_placementgroups_delete**
> Object pcloud_placementgroups_delete(cloud_instance_id, placement_group_id)

Delete Server Placement Group

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
placement_group_id = 'placement_group_id_example' # str | Placement Group ID

try:
    # Delete Server Placement Group
    api_response = api_instance.pcloud_placementgroups_delete(cloud_instance_id, placement_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **placement_group_id** | **str**| Placement Group ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_placementgroups_get**
> PlacementGroup pcloud_placementgroups_get(cloud_instance_id, placement_group_id)

Get Server Placement Group detail

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
placement_group_id = 'placement_group_id_example' # str | Placement Group ID

try:
    # Get Server Placement Group detail
    api_response = api_instance.pcloud_placementgroups_get(cloud_instance_id, placement_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **placement_group_id** | **str**| Placement Group ID | 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_placementgroups_getall**
> PlacementGroups pcloud_placementgroups_getall(cloud_instance_id)

Get all Server Placement Groups

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Get all Server Placement Groups
    api_response = api_instance.pcloud_placementgroups_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**PlacementGroups**](PlacementGroups.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_placementgroups_members_delete**
> PlacementGroup pcloud_placementgroups_members_delete(cloud_instance_id, placement_group_id, body)

Remove Server from Placement Group

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
placement_group_id = 'placement_group_id_example' # str | Placement Group ID
body = ip4g.PlacementGroupServer() # PlacementGroupServer | Parameters for removing a Server in a Placement Group

try:
    # Remove Server from Placement Group
    api_response = api_instance.pcloud_placementgroups_members_delete(cloud_instance_id, placement_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_members_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **placement_group_id** | **str**| Placement Group ID | 
 **body** | [**PlacementGroupServer**](PlacementGroupServer.md)| Parameters for removing a Server in a Placement Group | 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_placementgroups_members_post**
> PlacementGroup pcloud_placementgroups_members_post(cloud_instance_id, placement_group_id, body)

Add Server to Placement Group

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
placement_group_id = 'placement_group_id_example' # str | Placement Group ID
body = ip4g.PlacementGroupServer() # PlacementGroupServer | Parameters for adding a server to a Server Placement Group

try:
    # Add Server to Placement Group
    api_response = api_instance.pcloud_placementgroups_members_post(cloud_instance_id, placement_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **placement_group_id** | **str**| Placement Group ID | 
 **body** | [**PlacementGroupServer**](PlacementGroupServer.md)| Parameters for adding a server to a Server Placement Group | 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_placementgroups_post**
> PlacementGroup pcloud_placementgroups_post(cloud_instance_id, body)

Create a new Server Placement Group

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
api_instance = ip4g.PCloudPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.PlacementGroupCreate() # PlacementGroupCreate | Parameters for the creation of a new Server Placement Group

try:
    # Create a new Server Placement Group
    api_response = api_instance.pcloud_placementgroups_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPlacementGroupsApi->pcloud_placementgroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**PlacementGroupCreate**](PlacementGroupCreate.md)| Parameters for the creation of a new Server Placement Group | 

### Return type

[**PlacementGroup**](PlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


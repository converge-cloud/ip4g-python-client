# ip4g.SharedProcessorPoolsPlacementGroupsApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_spp_placementgroups_add_member**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_add_member) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups/{spp_pg_name_or_id}/members | Add Shared Processor Pool(s) as a member of a Shared Processor Pool Placement Group 
[**pcloud_spp_placementgroups_create**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_create) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups | Create a new Shared Processor Pool Placement Group. 
[**pcloud_spp_placementgroups_delete**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups/{spp_pg_name_or_id} | Delete a Shared Processor Pool Placement Group from a cloud instance 
[**pcloud_spp_placementgroups_delete_member**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_delete_member) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups/{spp_pg_name_or_id}/members/{spp_name_or_id} | Delete Shared Processor Pool member from a Shared Processor Pool Placement Group 
[**pcloud_spp_placementgroups_get**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups/{spp_pg_name_or_id} | Get the detail of a Shared Processor Pool Placement Group for a cloud instance 
[**pcloud_spp_placementgroups_getall**](SharedProcessorPoolsPlacementGroupsApi.md#pcloud_spp_placementgroups_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/spp-placement-groups | Get the list of Shared Processor Pool Placement Groups for a cloud instance. 


# **pcloud_spp_placementgroups_add_member**
> SppPlacementGroupAddedMembers pcloud_spp_placementgroups_add_member(cloud_instance_id, spp_pg_name_or_id, body)

Add Shared Processor Pool(s) as a member of a Shared Processor Pool Placement Group 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
spp_pg_name_or_id = 'spp_pg_name_or_id_example' # str | Shared Processor Pool Placement Group Name or ID
body = ip4g.SppPlacementGroupAddMembers() # SppPlacementGroupAddMembers | Parameters for adding Shared Processor Pool(s) to a Shared Processor Pool Placement Group in Cloud Instance 

try:
    # Add Shared Processor Pool(s) as a member of a Shared Processor Pool Placement Group 
    api_response = api_instance.pcloud_spp_placementgroups_add_member(cloud_instance_id, spp_pg_name_or_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **spp_pg_name_or_id** | **str**| Shared Processor Pool Placement Group Name or ID | 
 **body** | [**SppPlacementGroupAddMembers**](SppPlacementGroupAddMembers.md)| Parameters for adding Shared Processor Pool(s) to a Shared Processor Pool Placement Group in Cloud Instance  | 

### Return type

[**SppPlacementGroupAddedMembers**](SppPlacementGroupAddedMembers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_spp_placementgroups_create**
> SppPlacementGroup pcloud_spp_placementgroups_create(cloud_instance_id, body)

Create a new Shared Processor Pool Placement Group. 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.SppPlacementGroupCreate() # SppPlacementGroupCreate | Parameters for the creation of a new Shared Processor Pool Placement Group in Cloud Instance 

try:
    # Create a new Shared Processor Pool Placement Group. 
    api_response = api_instance.pcloud_spp_placementgroups_create(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**SppPlacementGroupCreate**](SppPlacementGroupCreate.md)| Parameters for the creation of a new Shared Processor Pool Placement Group in Cloud Instance  | 

### Return type

[**SppPlacementGroup**](SppPlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_spp_placementgroups_delete**
> Object pcloud_spp_placementgroups_delete(cloud_instance_id, spp_pg_name_or_id)

Delete a Shared Processor Pool Placement Group from a cloud instance 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
spp_pg_name_or_id = 'spp_pg_name_or_id_example' # str | Shared Processor Pool Placement Group Name or ID

try:
    # Delete a Shared Processor Pool Placement Group from a cloud instance 
    api_response = api_instance.pcloud_spp_placementgroups_delete(cloud_instance_id, spp_pg_name_or_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **spp_pg_name_or_id** | **str**| Shared Processor Pool Placement Group Name or ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_spp_placementgroups_delete_member**
> SppPlacementGroup pcloud_spp_placementgroups_delete_member(cloud_instance_id, spp_pg_name_or_id, spp_name_or_id)

Delete Shared Processor Pool member from a Shared Processor Pool Placement Group 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
spp_pg_name_or_id = 'spp_pg_name_or_id_example' # str | Shared Processor Pool Placement Group Name or ID
spp_name_or_id = 'spp_name_or_id_example' # str | Shared Processor Pool Name or ID

try:
    # Delete Shared Processor Pool member from a Shared Processor Pool Placement Group 
    api_response = api_instance.pcloud_spp_placementgroups_delete_member(cloud_instance_id, spp_pg_name_or_id, spp_name_or_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_delete_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **spp_pg_name_or_id** | **str**| Shared Processor Pool Placement Group Name or ID | 
 **spp_name_or_id** | **str**| Shared Processor Pool Name or ID | 

### Return type

[**SppPlacementGroup**](SppPlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_spp_placementgroups_get**
> SppPlacementGroup pcloud_spp_placementgroups_get(cloud_instance_id, spp_pg_name_or_id)

Get the detail of a Shared Processor Pool Placement Group for a cloud instance 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
spp_pg_name_or_id = 'spp_pg_name_or_id_example' # str | Shared Processor Pool Placement Group Name or ID

try:
    # Get the detail of a Shared Processor Pool Placement Group for a cloud instance 
    api_response = api_instance.pcloud_spp_placementgroups_get(cloud_instance_id, spp_pg_name_or_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **spp_pg_name_or_id** | **str**| Shared Processor Pool Placement Group Name or ID | 

### Return type

[**SppPlacementGroup**](SppPlacementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_spp_placementgroups_getall**
> SppPlacementGroups pcloud_spp_placementgroups_getall(cloud_instance_id)

Get the list of Shared Processor Pool Placement Groups for a cloud instance. 

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
api_instance = ip4g.SharedProcessorPoolsPlacementGroupsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Get the list of Shared Processor Pool Placement Groups for a cloud instance. 
    api_response = api_instance.pcloud_spp_placementgroups_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedProcessorPoolsPlacementGroupsApi->pcloud_spp_placementgroups_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**SppPlacementGroups**](SppPlacementGroups.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


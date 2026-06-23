# ip4g.PrivateConnectionsApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_private_connections_get**](PrivateConnectionsApi.md#pcloud_private_connections_get) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/private-connections/{private_connection_name_or_id} | Get the details of a Private Connection
[**pcloud_private_connections_list**](PrivateConnectionsApi.md#pcloud_private_connections_list) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/private-connections | List available Private Connections
[**pcloud_private_connections_put**](PrivateConnectionsApi.md#pcloud_private_connections_put) | **PUT** /pcloud/v2/cloud-instances/{cloud_instance_id}/private-connections/{private_connection_name_or_id} | Update a Private Connection


# **pcloud_private_connections_get**
> PrivateConnection pcloud_private_connections_get(cloud_instance_id, private_connection_name_or_id)

Get the details of a Private Connection

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
api_instance = ip4g.PrivateConnectionsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
private_connection_name_or_id = 'private_connection_name_or_id_example' # str | Name or ID of private connection

try:
    # Get the details of a Private Connection
    api_response = api_instance.pcloud_private_connections_get(cloud_instance_id, private_connection_name_or_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateConnectionsApi->pcloud_private_connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **private_connection_name_or_id** | **str**| Name or ID of private connection | 

### Return type

[**PrivateConnection**](PrivateConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_private_connections_list**
> PrivateConnections pcloud_private_connections_list(cloud_instance_id)

List available Private Connections

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
api_instance = ip4g.PrivateConnectionsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List available Private Connections
    api_response = api_instance.pcloud_private_connections_list(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateConnectionsApi->pcloud_private_connections_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**PrivateConnections**](PrivateConnections.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_private_connections_put**
> PrivateConnection pcloud_private_connections_put(cloud_instance_id, private_connection_name_or_id, body)

Update a Private Connection

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
api_instance = ip4g.PrivateConnectionsApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
private_connection_name_or_id = 'private_connection_name_or_id_example' # str | Name or ID of private connection
body = ip4g.PrivateConnectionUpdate() # PrivateConnectionUpdate | Parameters for the update of a private connection

try:
    # Update a Private Connection
    api_response = api_instance.pcloud_private_connections_put(cloud_instance_id, private_connection_name_or_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateConnectionsApi->pcloud_private_connections_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **private_connection_name_or_id** | **str**| Name or ID of private connection | 
 **body** | [**PrivateConnectionUpdate**](PrivateConnectionUpdate.md)| Parameters for the update of a private connection | 

### Return type

[**PrivateConnection**](PrivateConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


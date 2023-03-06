# swagger_client.PCloudNetworksApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_networks_delete**](PCloudNetworksApi.md#pcloud_networks_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id} | Delete a Network
[**pcloud_networks_get**](PCloudNetworksApi.md#pcloud_networks_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id} | Get a network&#39;s current state/information
[**pcloud_networks_getall**](PCloudNetworksApi.md#pcloud_networks_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks | Get all networks in this cloud instance
[**pcloud_networks_ports_delete**](PCloudNetworksApi.md#pcloud_networks_ports_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id}/ports/{port_id} | Delete a Network Port
[**pcloud_networks_ports_get**](PCloudNetworksApi.md#pcloud_networks_ports_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id}/ports/{port_id} | Get a port&#39;s information
[**pcloud_networks_ports_getall**](PCloudNetworksApi.md#pcloud_networks_ports_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id}/ports | Get all ports for this network
[**pcloud_networks_ports_post**](PCloudNetworksApi.md#pcloud_networks_ports_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id}/ports | Perform port addition, deletion, and listing
[**pcloud_networks_ports_put**](PCloudNetworksApi.md#pcloud_networks_ports_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id}/ports/{port_id} | Update a port&#39;s information
[**pcloud_networks_post**](PCloudNetworksApi.md#pcloud_networks_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks | Create a new Network
[**pcloud_networks_put**](PCloudNetworksApi.md#pcloud_networks_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/networks/{network_id} | Update a Network


# **pcloud_networks_delete**
> Object pcloud_networks_delete(cloud_instance_id, network_id)

Delete a Network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID

try:
    # Delete a Network
    api_response = api_instance.pcloud_networks_delete(cloud_instance_id, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_get**
> Network pcloud_networks_get(cloud_instance_id, network_id)

Get a network's current state/information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID

try:
    # Get a network's current state/information
    api_response = api_instance.pcloud_networks_get(cloud_instance_id, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_getall**
> Networks pcloud_networks_getall(cloud_instance_id, filter=filter)

Get all networks in this cloud instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
filter = 'filter_example' # str | A filter expression that filters resources listed in the response (optional)

try:
    # Get all networks in this cloud instance
    api_response = api_instance.pcloud_networks_getall(cloud_instance_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **filter** | **str**| A filter expression that filters resources listed in the response | [optional] 

### Return type

[**Networks**](Networks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_ports_delete**
> Object pcloud_networks_ports_delete(cloud_instance_id, network_id, port_id)

Delete a Network Port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID
port_id = 'port_id_example' # str | Port ID

try:
    # Delete a Network Port
    api_response = api_instance.pcloud_networks_ports_delete(cloud_instance_id, network_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_ports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 
 **port_id** | **str**| Port ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_ports_get**
> NetworkPort pcloud_networks_ports_get(cloud_instance_id, network_id, port_id)

Get a port's information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID
port_id = 'port_id_example' # str | Port ID

try:
    # Get a port's information
    api_response = api_instance.pcloud_networks_ports_get(cloud_instance_id, network_id, port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_ports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 
 **port_id** | **str**| Port ID | 

### Return type

[**NetworkPort**](NetworkPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_ports_getall**
> NetworkPorts pcloud_networks_ports_getall(cloud_instance_id, network_id)

Get all ports for this network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID

try:
    # Get all ports for this network
    api_response = api_instance.pcloud_networks_ports_getall(cloud_instance_id, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_ports_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 

### Return type

[**NetworkPorts**](NetworkPorts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_ports_post**
> NetworkPort pcloud_networks_ports_post(cloud_instance_id, network_id, body=body)

Perform port addition, deletion, and listing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID
body = swagger_client.NetworkPortCreate() # NetworkPortCreate | Create a Network Port (optional)

try:
    # Perform port addition, deletion, and listing
    api_response = api_instance.pcloud_networks_ports_post(cloud_instance_id, network_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_ports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 
 **body** | [**NetworkPortCreate**](NetworkPortCreate.md)| Create a Network Port | [optional] 

### Return type

[**NetworkPort**](NetworkPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_ports_put**
> NetworkPort pcloud_networks_ports_put(cloud_instance_id, network_id, port_id, body)

Update a port's information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID
port_id = 'port_id_example' # str | Port ID
body = swagger_client.NetworkPortUpdate() # NetworkPortUpdate | Parameters for updating a Port

try:
    # Update a port's information
    api_response = api_instance.pcloud_networks_ports_put(cloud_instance_id, network_id, port_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_ports_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 
 **port_id** | **str**| Port ID | 
 **body** | [**NetworkPortUpdate**](NetworkPortUpdate.md)| Parameters for updating a Port | 

### Return type

[**NetworkPort**](NetworkPort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_post**
> Network pcloud_networks_post(cloud_instance_id, body)

Create a new Network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.NetworkCreate() # NetworkCreate | Parameters for the creation of a new network

try:
    # Create a new Network
    api_response = api_instance.pcloud_networks_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**NetworkCreate**](NetworkCreate.md)| Parameters for the creation of a new network | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_networks_put**
> Network pcloud_networks_put(cloud_instance_id, network_id, body)

Update a Network

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudNetworksApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
network_id = 'network_id_example' # str | Network ID
body = swagger_client.NetworkUpdate() # NetworkUpdate | Parameters to update a Network

try:
    # Update a Network
    api_response = api_instance.pcloud_networks_put(cloud_instance_id, network_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudNetworksApi->pcloud_networks_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **network_id** | **str**| Network ID | 
 **body** | [**NetworkUpdate**](NetworkUpdate.md)| Parameters to update a Network | 

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


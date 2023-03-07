# ip4g.PCloudPVMInstancesApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_pvminstances_action_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_action_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/action | Perform an action (start stop reboot immediate-shutdown reset) on a PVMInstance
[**pcloud_pvminstances_capture_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_capture_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/capture | Capture a PVMInstance and create a deployable image
[**pcloud_pvminstances_clone_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_clone_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/clone | Clone a PVMInstance
[**pcloud_pvminstances_console_get**](PCloudPVMInstancesApi.md#pcloud_pvminstances_console_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/console | List all console languages
[**pcloud_pvminstances_console_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_console_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/console | Generate the noVNC Console URL
[**pcloud_pvminstances_console_put**](PCloudPVMInstancesApi.md#pcloud_pvminstances_console_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/console | Update PVMInstance console laguage code
[**pcloud_pvminstances_delete**](PCloudPVMInstancesApi.md#pcloud_pvminstances_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id} | Delete a PCloud PVM Instance
[**pcloud_pvminstances_get**](PCloudPVMInstancesApi.md#pcloud_pvminstances_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id} | Get a PVM Instance&#39;s current state/information
[**pcloud_pvminstances_getall**](PCloudPVMInstancesApi.md#pcloud_pvminstances_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances | Get all the pvm instances for this cloud instance
[**pcloud_pvminstances_networks_delete**](PCloudPVMInstancesApi.md#pcloud_pvminstances_networks_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/networks/{network_id} | Remove all Address of Network from a PVM Instance
[**pcloud_pvminstances_networks_get**](PCloudPVMInstancesApi.md#pcloud_pvminstances_networks_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/networks/{network_id} | Get a PVM Instance&#39;s network information
[**pcloud_pvminstances_networks_getall**](PCloudPVMInstancesApi.md#pcloud_pvminstances_networks_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/networks | Get all networks for this PVM Instance
[**pcloud_pvminstances_networks_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_networks_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/networks | Perform network addition
[**pcloud_pvminstances_operations_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_operations_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/operations | Perform an operation on a PVMInstance
[**pcloud_pvminstances_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances | Create a new Power VM Instance
[**pcloud_pvminstances_put**](PCloudPVMInstancesApi.md#pcloud_pvminstances_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id} | Update a PCloud PVM Instance
[**pcloud_pvminstances_snapshots_getall**](PCloudPVMInstancesApi.md#pcloud_pvminstances_snapshots_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/snapshots | Get all snapshots for this PVM Instance
[**pcloud_pvminstances_snapshots_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_snapshots_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/snapshots | Create a PVM Instance snapshot
[**pcloud_pvminstances_snapshots_restore_post**](PCloudPVMInstancesApi.md#pcloud_pvminstances_snapshots_restore_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/snapshots/{snapshot_id}/restore | Restore a PVM Instance snapshot
[**pcloud_v2_pvminstances_capture_get**](PCloudPVMInstancesApi.md#pcloud_v2_pvminstances_capture_get) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/capture | Get detail of last capture job
[**pcloud_v2_pvminstances_capture_post**](PCloudPVMInstancesApi.md#pcloud_v2_pvminstances_capture_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/capture | Add a capture pvm-instance to the jobs queue


# **pcloud_pvminstances_action_post**
> Object pcloud_pvminstances_action_post(cloud_instance_id, pvm_instance_id, body)

Perform an action (start stop reboot immediate-shutdown reset) on a PVMInstance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceAction() # PVMInstanceAction | Parameters for the desired action

try:
    # Perform an action (start stop reboot immediate-shutdown reset) on a PVMInstance
    api_response = api_instance.pcloud_pvminstances_action_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceAction**](PVMInstanceAction.md)| Parameters for the desired action |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_capture_post**
> Object pcloud_pvminstances_capture_post(cloud_instance_id, pvm_instance_id, body)

Capture a PVMInstance and create a deployable image

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceCapture() # PVMInstanceCapture | Parameters for the capture PVMInstance

try:
    # Capture a PVMInstance and create a deployable image
    api_response = api_instance.pcloud_pvminstances_capture_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_capture_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceCapture**](PVMInstanceCapture.md)| Parameters for the capture PVMInstance |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_clone_post**
> PVMInstance pcloud_pvminstances_clone_post(cloud_instance_id, pvm_instance_id, body)

Clone a PVMInstance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceClone() # PVMInstanceClone | Clone PVM Instance parameters

try:
    # Clone a PVMInstance
    api_response = api_instance.pcloud_pvminstances_clone_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceClone**](PVMInstanceClone.md)| Clone PVM Instance parameters |

### Return type

[**PVMInstance**](PVMInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_console_get**
> ConsoleLanguages pcloud_pvminstances_console_get(cloud_instance_id, pvm_instance_id)

List all console languages

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # List all console languages
    api_response = api_instance.pcloud_pvminstances_console_get(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_console_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**ConsoleLanguages**](ConsoleLanguages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_console_post**
> PVMInstanceConsole pcloud_pvminstances_console_post(cloud_instance_id, pvm_instance_id)

Generate the noVNC Console URL

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # Generate the noVNC Console URL
    api_response = api_instance.pcloud_pvminstances_console_post(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_console_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**PVMInstanceConsole**](PVMInstanceConsole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_console_put**
> ConsoleLanguage pcloud_pvminstances_console_put(cloud_instance_id, pvm_instance_id, body)

Update PVMInstance console laguage code

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.ConsoleLanguage() # ConsoleLanguage | Parameters to update a PVMInstance console required codepage

try:
    # Update PVMInstance console laguage code
    api_response = api_instance.pcloud_pvminstances_console_put(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_console_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**ConsoleLanguage**](ConsoleLanguage.md)| Parameters to update a PVMInstance console required codepage |

### Return type

[**ConsoleLanguage**](ConsoleLanguage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_delete**
> Object pcloud_pvminstances_delete(cloud_instance_id, pvm_instance_id, delete_data_volumes=delete_data_volumes)

Delete a PCloud PVM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
delete_data_volumes = true # bool | Indicates if all data volumes attached to the PVMInstance should be deleted when deleting the PVMInstance. Shared data volumes will be deleted if there are no other PVMInstances attached. (optional)

try:
    # Delete a PCloud PVM Instance
    api_response = api_instance.pcloud_pvminstances_delete(cloud_instance_id, pvm_instance_id, delete_data_volumes=delete_data_volumes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **delete_data_volumes** | **bool**| Indicates if all data volumes attached to the PVMInstance should be deleted when deleting the PVMInstance. Shared data volumes will be deleted if there are no other PVMInstances attached. | [optional]

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_get**
> PVMInstance pcloud_pvminstances_get(cloud_instance_id, pvm_instance_id)

Get a PVM Instance's current state/information

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # Get a PVM Instance's current state/information
    api_response = api_instance.pcloud_pvminstances_get(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**PVMInstance**](PVMInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_getall**
> PVMInstances pcloud_pvminstances_getall(cloud_instance_id)

Get all the pvm instances for this cloud instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Get all the pvm instances for this cloud instance
    api_response = api_instance.pcloud_pvminstances_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |

### Return type

[**PVMInstances**](PVMInstances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_networks_delete**
> Object pcloud_pvminstances_networks_delete(cloud_instance_id, pvm_instance_id, network_id, body=body)

Remove all Address of Network from a PVM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
network_id = 'network_id_example' # str | Network ID
body = ip4g.PVMInstanceRemoveNetwork() # PVMInstanceRemoveNetwork | Remove a network from PVM Instance parameters (optional)

try:
    # Remove all Address of Network from a PVM Instance
    api_response = api_instance.pcloud_pvminstances_networks_delete(cloud_instance_id, pvm_instance_id, network_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_networks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **network_id** | **str**| Network ID |
 **body** | [**PVMInstanceRemoveNetwork**](PVMInstanceRemoveNetwork.md)| Remove a network from PVM Instance parameters | [optional]

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_networks_get**
> PVMInstanceNetworks pcloud_pvminstances_networks_get(cloud_instance_id, pvm_instance_id, network_id)

Get a PVM Instance's network information

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
network_id = 'network_id_example' # str | Network ID

try:
    # Get a PVM Instance's network information
    api_response = api_instance.pcloud_pvminstances_networks_get(cloud_instance_id, pvm_instance_id, network_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **network_id** | **str**| Network ID |

### Return type

[**PVMInstanceNetworks**](PVMInstanceNetworks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_networks_getall**
> PVMInstanceNetworks pcloud_pvminstances_networks_getall(cloud_instance_id, pvm_instance_id)

Get all networks for this PVM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # Get all networks for this PVM Instance
    api_response = api_instance.pcloud_pvminstances_networks_getall(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_networks_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**PVMInstanceNetworks**](PVMInstanceNetworks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_networks_post**
> PVMInstanceNetwork pcloud_pvminstances_networks_post(cloud_instance_id, pvm_instance_id, body)

Perform network addition

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceAddNetwork() # PVMInstanceAddNetwork | Add network to PVM Instance parameters

try:
    # Perform network addition
    api_response = api_instance.pcloud_pvminstances_networks_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_networks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceAddNetwork**](PVMInstanceAddNetwork.md)| Add network to PVM Instance parameters |

### Return type

[**PVMInstanceNetwork**](PVMInstanceNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_operations_post**
> Object pcloud_pvminstances_operations_post(cloud_instance_id, pvm_instance_id, body)

Perform an operation on a PVMInstance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceOperation() # PVMInstanceOperation | Parameters for the desired operations

try:
    # Perform an operation on a PVMInstance
    api_response = api_instance.pcloud_pvminstances_operations_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_operations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceOperation**](PVMInstanceOperation.md)| Parameters for the desired operations |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_post**
> PVMInstanceList pcloud_pvminstances_post(cloud_instance_id, body, skip_host_validation=skip_host_validation)

Create a new Power VM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.PVMInstanceCreate() # PVMInstanceCreate | Parameters for the creation of a new Power VM Instance
skip_host_validation = true # bool | Option to skip host validation on PVMInstance Create API (optional)

try:
    # Create a new Power VM Instance
    api_response = api_instance.pcloud_pvminstances_post(cloud_instance_id, body, skip_host_validation=skip_host_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **body** | [**PVMInstanceCreate**](PVMInstanceCreate.md)| Parameters for the creation of a new Power VM Instance |
 **skip_host_validation** | **bool**| Option to skip host validation on PVMInstance Create API | [optional]

### Return type

[**PVMInstanceList**](PVMInstanceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_put**
> PVMInstanceUpdateResponse pcloud_pvminstances_put(cloud_instance_id, pvm_instance_id, body)

Update a PCloud PVM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceUpdate() # PVMInstanceUpdate | Parameters to update a PCloud PVM Instance

try:
    # Update a PCloud PVM Instance
    api_response = api_instance.pcloud_pvminstances_put(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceUpdate**](PVMInstanceUpdate.md)| Parameters to update a PCloud PVM Instance |

### Return type

[**PVMInstanceUpdateResponse**](PVMInstanceUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_snapshots_getall**
> Snapshots pcloud_pvminstances_snapshots_getall(cloud_instance_id, pvm_instance_id)

Get all snapshots for this PVM Instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # Get all snapshots for this PVM Instance
    api_response = api_instance.pcloud_pvminstances_snapshots_getall(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_snapshots_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_snapshots_post**
> SnapshotCreateResponse pcloud_pvminstances_snapshots_post(cloud_instance_id, pvm_instance_id, body)

Create a PVM Instance snapshot

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.SnapshotCreate() # SnapshotCreate | PVM Instance snapshot create parameters

try:
    # Create a PVM Instance snapshot
    api_response = api_instance.pcloud_pvminstances_snapshots_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**SnapshotCreate**](SnapshotCreate.md)| PVM Instance snapshot create parameters |

### Return type

[**SnapshotCreateResponse**](SnapshotCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_snapshots_restore_post**
> Snapshot pcloud_pvminstances_snapshots_restore_post(cloud_instance_id, pvm_instance_id, snapshot_id, body, restore_fail_action=restore_fail_action)

Restore a PVM Instance snapshot

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
snapshot_id = 'snapshot_id_example' # str | PVM Instance snapshot id
body = ip4g.SnapshotRestore() # SnapshotRestore | PVM Instance snapshot restore parameters
restore_fail_action = 'restore_fail_action_example' # str | Action to take on a failed snapshot restore (optional)

try:
    # Restore a PVM Instance snapshot
    api_response = api_instance.pcloud_pvminstances_snapshots_restore_post(cloud_instance_id, pvm_instance_id, snapshot_id, body, restore_fail_action=restore_fail_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_pvminstances_snapshots_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **snapshot_id** | **str**| PVM Instance snapshot id |
 **body** | [**SnapshotRestore**](SnapshotRestore.md)| PVM Instance snapshot restore parameters |
 **restore_fail_action** | **str**| Action to take on a failed snapshot restore | [optional]

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_pvminstances_capture_get**
> Job pcloud_v2_pvminstances_capture_get(cloud_instance_id, pvm_instance_id)

Get detail of last capture job

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # Get detail of last capture job
    api_response = api_instance.pcloud_v2_pvminstances_capture_get(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_v2_pvminstances_capture_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_pvminstances_capture_post**
> JobReference pcloud_v2_pvminstances_capture_post(cloud_instance_id, pvm_instance_id, body)

Add a capture pvm-instance to the jobs queue

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudPVMInstancesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = ip4g.PVMInstanceCapture() # PVMInstanceCapture | Parameters for the capture

try:
    # Add a capture pvm-instance to the jobs queue
    api_response = api_instance.pcloud_v2_pvminstances_capture_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudPVMInstancesApi->pcloud_v2_pvminstances_capture_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **pvm_instance_id** | **str**| PCloud PVM Instance ID |
 **body** | [**PVMInstanceCapture**](PVMInstanceCapture.md)| Parameters for the capture |

### Return type

[**JobReference**](JobReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# swagger_client.PCloudVolumesApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_volumes_action_post**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_action_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/{volume_id}/action | Perform an action on a Volume
[**pcloud_cloudinstances_volumes_delete**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/{volume_id} | Delete a cloud instance volume
[**pcloud_cloudinstances_volumes_get**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/{volume_id} | Detailed info of a volume
[**pcloud_cloudinstances_volumes_getall**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes | List all volumes for this cloud instance
[**pcloud_cloudinstances_volumes_post**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes | Create a new data Volume
[**pcloud_cloudinstances_volumes_put**](PCloudVolumesApi.md#pcloud_cloudinstances_volumes_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/{volume_id} | Update a cloud instance volume
[**pcloud_pvminstances_volumes_delete**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes/{volume_id} | Detach a volume from a PVMInstance
[**pcloud_pvminstances_volumes_get**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes/{volume_id} | Detailed info of a volume attached to a PVMInstance
[**pcloud_pvminstances_volumes_getall**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes | List all volumes attached to a PVMInstance
[**pcloud_pvminstances_volumes_post**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes/{volume_id} | Attach a volume to a PVMInstance
[**pcloud_pvminstances_volumes_put**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes/{volume_id} | Update a volume attached to a PVMInstance
[**pcloud_pvminstances_volumes_setboot_put**](PCloudVolumesApi.md#pcloud_pvminstances_volumes_setboot_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes/{volume_id}/setboot | Set the PVMInstance volume as the boot volume
[**pcloud_v2_pvminstances_volumes_post**](PCloudVolumesApi.md#pcloud_v2_pvminstances_volumes_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/pvm-instances/{pvm_instance_id}/volumes | Attach all volumes to a PVMInstance
[**pcloud_v2_volumes_clone_post_v2**](PCloudVolumesApi.md#pcloud_v2_volumes_clone_post_v2) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes/clone | Create a volume clone for specified volumes
[**pcloud_v2_volumes_clonetasks_get**](PCloudVolumesApi.md#pcloud_v2_volumes_clonetasks_get) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes/clone-tasks/{clone_task_id} | Get the status of a volumes clone request for the specified clone task ID
[**pcloud_v2_volumes_post**](PCloudVolumesApi.md#pcloud_v2_volumes_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes | Create multiple data volumes from a single definition
[**pcloud_v2_volumesclone_cancel_post**](PCloudVolumesApi.md#pcloud_v2_volumesclone_cancel_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone/{volumes_clone_id}/cancel | Cancel a volumes-clone request, initiates the Cleanup action Cleanup action performs the cleanup of the preparatory clones and snapshot volumes 
[**pcloud_v2_volumesclone_delete**](PCloudVolumesApi.md#pcloud_v2_volumesclone_delete) | **DELETE** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone/{volumes_clone_id} | Delete a volumes-clone request
[**pcloud_v2_volumesclone_execute_post**](PCloudVolumesApi.md#pcloud_v2_volumesclone_execute_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone/{volumes_clone_id}/execute | Initiate the Execute action for a volumes-clone request Execute action creates the cloned volumes using the volume snapshots 
[**pcloud_v2_volumesclone_get**](PCloudVolumesApi.md#pcloud_v2_volumesclone_get) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone/{volumes_clone_id} | Get the details for a volumes-clone request
[**pcloud_v2_volumesclone_getall**](PCloudVolumesApi.md#pcloud_v2_volumesclone_getall) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone | Get the list of volumes-clone request for a cloud instance
[**pcloud_v2_volumesclone_post**](PCloudVolumesApi.md#pcloud_v2_volumesclone_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone | Create a new volumes clone request and initiates the Prepare action   Requires a minimum of two volumes   Requires a minimum of one volume to be in the &#39;in-use&#39; state   Requires a unique volumes clone name   Prepare action does the preparatory work for creating the snapshot volumes 
[**pcloud_v2_volumesclone_start_post**](PCloudVolumesApi.md#pcloud_v2_volumesclone_start_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/volumes-clone/{volumes_clone_id}/start | Initiate the Start action for a volumes-clone request Start action starts the consistency group to initiate the flash copy 
[**pcloud_volumes_clone_post**](PCloudVolumesApi.md#pcloud_volumes_clone_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/clone | Create a volume clone for specified volumes


# **pcloud_cloudinstances_volumes_action_post**
> Object pcloud_cloudinstances_volumes_action_post(cloud_instance_id, volume_id, body)

Perform an action on a Volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volume_id = 'volume_id_example' # str | Volume ID
body = swagger_client.VolumeAction() # VolumeAction | Parameters for the desired action

try:
    # Perform an action on a Volume
    api_response = api_instance.pcloud_cloudinstances_volumes_action_post(cloud_instance_id, volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volume_id** | **str**| Volume ID | 
 **body** | [**VolumeAction**](VolumeAction.md)| Parameters for the desired action | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_volumes_delete**
> Object pcloud_cloudinstances_volumes_delete(cloud_instance_id, volume_id)

Delete a cloud instance volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Delete a cloud instance volume
    api_response = api_instance.pcloud_cloudinstances_volumes_delete(cloud_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_volumes_get**
> Volume pcloud_cloudinstances_volumes_get(cloud_instance_id, volume_id)

Detailed info of a volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Detailed info of a volume
    api_response = api_instance.pcloud_cloudinstances_volumes_get(cloud_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_volumes_getall**
> Volumes pcloud_cloudinstances_volumes_getall(cloud_instance_id, affinity=affinity)

List all volumes for this cloud instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
affinity = 'affinity_example' # str | A pvmInstance (id or name), limits a volumes list response to only volumes that have affinity to the pvmInstance (optional)

try:
    # List all volumes for this cloud instance
    api_response = api_instance.pcloud_cloudinstances_volumes_getall(cloud_instance_id, affinity=affinity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **affinity** | **str**| A pvmInstance (id or name), limits a volumes list response to only volumes that have affinity to the pvmInstance | [optional] 

### Return type

[**Volumes**](Volumes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_volumes_post**
> Volume pcloud_cloudinstances_volumes_post(cloud_instance_id, body)

Create a new data Volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.CreateDataVolume() # CreateDataVolume | Parameters for the creation of a new data volume

try:
    # Create a new data Volume
    api_response = api_instance.pcloud_cloudinstances_volumes_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**CreateDataVolume**](CreateDataVolume.md)| Parameters for the creation of a new data volume | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_volumes_put**
> Volume pcloud_cloudinstances_volumes_put(cloud_instance_id, volume_id, body)

Update a cloud instance volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volume_id = 'volume_id_example' # str | Volume ID
body = swagger_client.UpdateVolume() # UpdateVolume | Parameters to update a cloud instance volume

try:
    # Update a cloud instance volume
    api_response = api_instance.pcloud_cloudinstances_volumes_put(cloud_instance_id, volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_cloudinstances_volumes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volume_id** | **str**| Volume ID | 
 **body** | [**UpdateVolume**](UpdateVolume.md)| Parameters to update a cloud instance volume | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_delete**
> Object pcloud_pvminstances_volumes_delete(cloud_instance_id, pvm_instance_id, volume_id)

Detach a volume from a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Detach a volume from a PVMInstance
    api_response = api_instance.pcloud_pvminstances_volumes_delete(cloud_instance_id, pvm_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_get**
> Volume pcloud_pvminstances_volumes_get(cloud_instance_id, pvm_instance_id, volume_id)

Detailed info of a volume attached to a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Detailed info of a volume attached to a PVMInstance
    api_response = api_instance.pcloud_pvminstances_volumes_get(cloud_instance_id, pvm_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_getall**
> Volumes pcloud_pvminstances_volumes_getall(cloud_instance_id, pvm_instance_id)

List all volumes attached to a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID

try:
    # List all volumes attached to a PVMInstance
    api_response = api_instance.pcloud_pvminstances_volumes_getall(cloud_instance_id, pvm_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 

### Return type

[**Volumes**](Volumes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_post**
> Object pcloud_pvminstances_volumes_post(cloud_instance_id, pvm_instance_id, volume_id)

Attach a volume to a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Attach a volume to a PVMInstance
    api_response = api_instance.pcloud_pvminstances_volumes_post(cloud_instance_id, pvm_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_put**
> Object pcloud_pvminstances_volumes_put(cloud_instance_id, pvm_instance_id, volume_id, body)

Update a volume attached to a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
volume_id = 'volume_id_example' # str | Volume ID
body = swagger_client.PVMInstanceVolumeUpdate() # PVMInstanceVolumeUpdate | Parameters to update a volume attached to a PVMInstance

try:
    # Update a volume attached to a PVMInstance
    api_response = api_instance.pcloud_pvminstances_volumes_put(cloud_instance_id, pvm_instance_id, volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **volume_id** | **str**| Volume ID | 
 **body** | [**PVMInstanceVolumeUpdate**](PVMInstanceVolumeUpdate.md)| Parameters to update a volume attached to a PVMInstance | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_pvminstances_volumes_setboot_put**
> Object pcloud_pvminstances_volumes_setboot_put(cloud_instance_id, pvm_instance_id, volume_id)

Set the PVMInstance volume as the boot volume

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
volume_id = 'volume_id_example' # str | Volume ID

try:
    # Set the PVMInstance volume as the boot volume
    api_response = api_instance.pcloud_pvminstances_volumes_setboot_put(cloud_instance_id, pvm_instance_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_pvminstances_volumes_setboot_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **volume_id** | **str**| Volume ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_pvminstances_volumes_post**
> VolumesAttachmentResponse pcloud_v2_pvminstances_volumes_post(cloud_instance_id, pvm_instance_id, body)

Attach all volumes to a PVMInstance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
pvm_instance_id = 'pvm_instance_id_example' # str | PCloud PVM Instance ID
body = swagger_client.VolumesAttach() # VolumesAttach | Parameter to attach volumes to a PVMInstance

try:
    # Attach all volumes to a PVMInstance
    api_response = api_instance.pcloud_v2_pvminstances_volumes_post(cloud_instance_id, pvm_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_pvminstances_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **pvm_instance_id** | **str**| PCloud PVM Instance ID | 
 **body** | [**VolumesAttach**](VolumesAttach.md)| Parameter to attach volumes to a PVMInstance | 

### Return type

[**VolumesAttachmentResponse**](VolumesAttachmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumes_clone_post_v2**
> CloneTaskReference pcloud_v2_volumes_clone_post_v2(cloud_instance_id, body)

Create a volume clone for specified volumes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.VolumesCloneAsyncRequest() # VolumesCloneAsyncRequest | Parameters for the cloning of volumes

try:
    # Create a volume clone for specified volumes
    api_response = api_instance.pcloud_v2_volumes_clone_post_v2(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumes_clone_post_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**VolumesCloneAsyncRequest**](VolumesCloneAsyncRequest.md)| Parameters for the cloning of volumes | 

### Return type

[**CloneTaskReference**](CloneTaskReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumes_clonetasks_get**
> CloneTaskStatus pcloud_v2_volumes_clonetasks_get(cloud_instance_id, clone_task_id)

Get the status of a volumes clone request for the specified clone task ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
clone_task_id = 'clone_task_id_example' # str | Volumes Clone Task ID

try:
    # Get the status of a volumes clone request for the specified clone task ID
    api_response = api_instance.pcloud_v2_volumes_clonetasks_get(cloud_instance_id, clone_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumes_clonetasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **clone_task_id** | **str**| Volumes Clone Task ID | 

### Return type

[**CloneTaskStatus**](CloneTaskStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumes_post**
> Volumes pcloud_v2_volumes_post(cloud_instance_id, body)

Create multiple data volumes from a single definition

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.MultiVolumesCreate() # MultiVolumesCreate | Parameters for creating multiple volumes

try:
    # Create multiple data volumes from a single definition
    api_response = api_instance.pcloud_v2_volumes_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**MultiVolumesCreate**](MultiVolumesCreate.md)| Parameters for creating multiple volumes | 

### Return type

[**Volumes**](Volumes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_cancel_post**
> VolumesClone pcloud_v2_volumesclone_cancel_post(cloud_instance_id, volumes_clone_id, body=body)

Cancel a volumes-clone request, initiates the Cleanup action Cleanup action performs the cleanup of the preparatory clones and snapshot volumes 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volumes_clone_id = 'volumes_clone_id_example' # str | Volumes Clone ID
body = swagger_client.VolumesCloneCancel() # VolumesCloneCancel | Parameters for cancelling a volumes-clone request (optional)

try:
    # Cancel a volumes-clone request, initiates the Cleanup action Cleanup action performs the cleanup of the preparatory clones and snapshot volumes 
    api_response = api_instance.pcloud_v2_volumesclone_cancel_post(cloud_instance_id, volumes_clone_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volumes_clone_id** | **str**| Volumes Clone ID | 
 **body** | [**VolumesCloneCancel**](VolumesCloneCancel.md)| Parameters for cancelling a volumes-clone request | [optional] 

### Return type

[**VolumesClone**](VolumesClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_delete**
> Object pcloud_v2_volumesclone_delete(cloud_instance_id, volumes_clone_id)

Delete a volumes-clone request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volumes_clone_id = 'volumes_clone_id_example' # str | Volumes Clone ID

try:
    # Delete a volumes-clone request
    api_response = api_instance.pcloud_v2_volumesclone_delete(cloud_instance_id, volumes_clone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volumes_clone_id** | **str**| Volumes Clone ID | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_execute_post**
> VolumesClone pcloud_v2_volumesclone_execute_post(cloud_instance_id, volumes_clone_id, body)

Initiate the Execute action for a volumes-clone request Execute action creates the cloned volumes using the volume snapshots 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volumes_clone_id = 'volumes_clone_id_example' # str | Volumes Clone ID
body = swagger_client.VolumesCloneExecute() # VolumesCloneExecute | Parameters for the cloning of volumes

try:
    # Initiate the Execute action for a volumes-clone request Execute action creates the cloned volumes using the volume snapshots 
    api_response = api_instance.pcloud_v2_volumesclone_execute_post(cloud_instance_id, volumes_clone_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volumes_clone_id** | **str**| Volumes Clone ID | 
 **body** | [**VolumesCloneExecute**](VolumesCloneExecute.md)| Parameters for the cloning of volumes | 

### Return type

[**VolumesClone**](VolumesClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_get**
> VolumesCloneDetail pcloud_v2_volumesclone_get(cloud_instance_id, volumes_clone_id)

Get the details for a volumes-clone request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volumes_clone_id = 'volumes_clone_id_example' # str | Volumes Clone ID

try:
    # Get the details for a volumes-clone request
    api_response = api_instance.pcloud_v2_volumesclone_get(cloud_instance_id, volumes_clone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volumes_clone_id** | **str**| Volumes Clone ID | 

### Return type

[**VolumesCloneDetail**](VolumesCloneDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_getall**
> VolumesClones pcloud_v2_volumesclone_getall(cloud_instance_id, filter=filter)

Get the list of volumes-clone request for a cloud instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
filter = 'filter_example' # str | volumes-clone filter to limit list items:   prepare - includes status values (preparing, prepared)   start   - includes status values (starting, available)   execute - includes status values (executing, available-rollback)   cancel  - includes status values (cancelling)   completed - includes status values (completed)   failed - includes status values (failed)   cancelled - includes status values (cancelled)   finalized - included status values (completed, failed, cancelled)  (optional)

try:
    # Get the list of volumes-clone request for a cloud instance
    api_response = api_instance.pcloud_v2_volumesclone_getall(cloud_instance_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **filter** | **str**| volumes-clone filter to limit list items:   prepare - includes status values (preparing, prepared)   start   - includes status values (starting, available)   execute - includes status values (executing, available-rollback)   cancel  - includes status values (cancelling)   completed - includes status values (completed)   failed - includes status values (failed)   cancelled - includes status values (cancelled)   finalized - included status values (completed, failed, cancelled)  | [optional] 

### Return type

[**VolumesClones**](VolumesClones.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_post**
> VolumesClone pcloud_v2_volumesclone_post(cloud_instance_id, body)

Create a new volumes clone request and initiates the Prepare action   Requires a minimum of two volumes   Requires a minimum of one volume to be in the 'in-use' state   Requires a unique volumes clone name   Prepare action does the preparatory work for creating the snapshot volumes 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.VolumesCloneCreate() # VolumesCloneCreate | Parameters for preparing a set of volumes to be cloned

try:
    # Create a new volumes clone request and initiates the Prepare action   Requires a minimum of two volumes   Requires a minimum of one volume to be in the 'in-use' state   Requires a unique volumes clone name   Prepare action does the preparatory work for creating the snapshot volumes 
    api_response = api_instance.pcloud_v2_volumesclone_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**VolumesCloneCreate**](VolumesCloneCreate.md)| Parameters for preparing a set of volumes to be cloned | 

### Return type

[**VolumesClone**](VolumesClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_volumesclone_start_post**
> VolumesClone pcloud_v2_volumesclone_start_post(cloud_instance_id, volumes_clone_id)

Initiate the Start action for a volumes-clone request Start action starts the consistency group to initiate the flash copy 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volumes_clone_id = 'volumes_clone_id_example' # str | Volumes Clone ID

try:
    # Initiate the Start action for a volumes-clone request Start action starts the consistency group to initiate the flash copy 
    api_response = api_instance.pcloud_v2_volumesclone_start_post(cloud_instance_id, volumes_clone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_v2_volumesclone_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volumes_clone_id** | **str**| Volumes Clone ID | 

### Return type

[**VolumesClone**](VolumesClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_volumes_clone_post**
> VolumesCloneResponse pcloud_volumes_clone_post(cloud_instance_id, body)

Create a volume clone for specified volumes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudVolumesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.VolumesCloneRequest() # VolumesCloneRequest | Parameters for the cloning of volumes

try:
    # Create a volume clone for specified volumes
    api_response = api_instance.pcloud_volumes_clone_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumesApi->pcloud_volumes_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**VolumesCloneRequest**](VolumesCloneRequest.md)| Parameters for the cloning of volumes | 

### Return type

[**VolumesCloneResponse**](VolumesCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


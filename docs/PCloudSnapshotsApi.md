# ip4g.PCloudSnapshotsApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_snapshots_delete**](PCloudSnapshotsApi.md#pcloud_cloudinstances_snapshots_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/snapshots/{snapshot_id} | Delete a PVM instance snapshot of a cloud instance
[**pcloud_cloudinstances_snapshots_get**](PCloudSnapshotsApi.md#pcloud_cloudinstances_snapshots_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/snapshots/{snapshot_id} | Get the detail of a snapshot
[**pcloud_cloudinstances_snapshots_getall**](PCloudSnapshotsApi.md#pcloud_cloudinstances_snapshots_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/snapshots | List all PVM instance snapshots for this cloud instance
[**pcloud_cloudinstances_snapshots_put**](PCloudSnapshotsApi.md#pcloud_cloudinstances_snapshots_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/snapshots/{snapshot_id} | Update a PVM instance snapshot


# **pcloud_cloudinstances_snapshots_delete**
> Object pcloud_cloudinstances_snapshots_delete(cloud_instance_id, snapshot_id)

Delete a PVM instance snapshot of a cloud instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudSnapshotsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
snapshot_id = 'snapshot_id_example' # str | PVM Instance snapshot id

try:
    # Delete a PVM instance snapshot of a cloud instance
    api_response = api_instance.pcloud_cloudinstances_snapshots_delete(cloud_instance_id, snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudSnapshotsApi->pcloud_cloudinstances_snapshots_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **snapshot_id** | **str**| PVM Instance snapshot id |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_snapshots_get**
> Snapshot pcloud_cloudinstances_snapshots_get(cloud_instance_id, snapshot_id)

Get the detail of a snapshot

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudSnapshotsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
snapshot_id = 'snapshot_id_example' # str | PVM Instance snapshot id

try:
    # Get the detail of a snapshot
    api_response = api_instance.pcloud_cloudinstances_snapshots_get(cloud_instance_id, snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudSnapshotsApi->pcloud_cloudinstances_snapshots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **snapshot_id** | **str**| PVM Instance snapshot id |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_snapshots_getall**
> Snapshots pcloud_cloudinstances_snapshots_getall(cloud_instance_id)

List all PVM instance snapshots for this cloud instance

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudSnapshotsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List all PVM instance snapshots for this cloud instance
    api_response = api_instance.pcloud_cloudinstances_snapshots_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudSnapshotsApi->pcloud_cloudinstances_snapshots_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_snapshots_put**
> Object pcloud_cloudinstances_snapshots_put(cloud_instance_id, snapshot_id, body)

Update a PVM instance snapshot

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudSnapshotsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
snapshot_id = 'snapshot_id_example' # str | PVM Instance snapshot id
body = ip4g.SnapshotUpdate() # SnapshotUpdate | Parameters for the update of a  PVM instance snapshot

try:
    # Update a PVM instance snapshot
    api_response = api_instance.pcloud_cloudinstances_snapshots_put(cloud_instance_id, snapshot_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudSnapshotsApi->pcloud_cloudinstances_snapshots_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **snapshot_id** | **str**| PVM Instance snapshot id |
 **body** | [**SnapshotUpdate**](SnapshotUpdate.md)| Parameters for the update of a  PVM instance snapshot |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

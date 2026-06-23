# ip4g.PCloudVolumeReplicationApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_v1_volume_replication_action_post**](PCloudVolumeReplicationApi.md#pcloud_v1_volume_replication_action_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-replication/{volume_id}/action | Toggle replication for a volume


# **pcloud_v1_volume_replication_action_post**
> Object pcloud_v1_volume_replication_action_post(cloud_instance_id, volume_id, body)

Toggle replication for a volume

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
api_instance = ip4g.PCloudVolumeReplicationApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
volume_id = 'volume_id_example' # str | Volume ID
body = ip4g.VolumeReplicationToggle() # VolumeReplicationToggle | Parameters for toggling volume replication

try:
    # Toggle replication for a volume
    api_response = api_instance.pcloud_v1_volume_replication_action_post(cloud_instance_id, volume_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudVolumeReplicationApi->pcloud_v1_volume_replication_action_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **volume_id** | **str**| Volume ID | 
 **body** | [**VolumeReplicationToggle**](VolumeReplicationToggle.md)| Parameters for toggling volume replication | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


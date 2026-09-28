# ip4g.VolumeTransferApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_volumetransfer_accept**](VolumeTransferApi.md#pcloud_volumetransfer_accept) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-transfers/{transfer_id}/accept | Accept volume transfer
[**pcloud_volumetransfer_delete**](VolumeTransferApi.md#pcloud_volumetransfer_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-transfers/{transfer_id} | Delete volume transfer
[**pcloud_volumetransfer_get**](VolumeTransferApi.md#pcloud_volumetransfer_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-transfers/{transfer_id} | Get volume transfer
[**pcloud_volumetransfer_getall**](VolumeTransferApi.md#pcloud_volumetransfer_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-transfers | List volume transfers
[**pcloud_volumetransfer_post**](VolumeTransferApi.md#pcloud_volumetransfer_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volume-transfers | Create a volume transfer


# **pcloud_volumetransfer_accept**
> VolumeTransfer pcloud_volumetransfer_accept(cloud_instance_id, transfer_id, body)

Accept volume transfer

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
api_instance = ip4g.VolumeTransferApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
transfer_id = 'transfer_id_example' # str | The unique identifier for a volume transfer
body = ip4g.VolumeTransferAccept() # VolumeTransferAccept | Parameters for accepting a volume transfer

try:
    # Accept volume transfer
    api_response = api_instance.pcloud_volumetransfer_accept(cloud_instance_id, transfer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeTransferApi->pcloud_volumetransfer_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **transfer_id** | **str**| The unique identifier for a volume transfer | 
 **body** | [**VolumeTransferAccept**](VolumeTransferAccept.md)| Parameters for accepting a volume transfer | 

### Return type

[**VolumeTransfer**](VolumeTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_volumetransfer_delete**
> pcloud_volumetransfer_delete(cloud_instance_id, transfer_id)

Delete volume transfer

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
api_instance = ip4g.VolumeTransferApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
transfer_id = 'transfer_id_example' # str | The unique identifier for a volume transfer

try:
    # Delete volume transfer
    api_instance.pcloud_volumetransfer_delete(cloud_instance_id, transfer_id)
except ApiException as e:
    print("Exception when calling VolumeTransferApi->pcloud_volumetransfer_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **transfer_id** | **str**| The unique identifier for a volume transfer | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_volumetransfer_get**
> VolumeTransfer pcloud_volumetransfer_get(cloud_instance_id, transfer_id)

Get volume transfer

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
api_instance = ip4g.VolumeTransferApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
transfer_id = 'transfer_id_example' # str | The unique identifier for a volume transfer

try:
    # Get volume transfer
    api_response = api_instance.pcloud_volumetransfer_get(cloud_instance_id, transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeTransferApi->pcloud_volumetransfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **transfer_id** | **str**| The unique identifier for a volume transfer | 

### Return type

[**VolumeTransfer**](VolumeTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_volumetransfer_getall**
> VolumeTransfers pcloud_volumetransfer_getall(cloud_instance_id)

List volume transfers

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
api_instance = ip4g.VolumeTransferApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List volume transfers
    api_response = api_instance.pcloud_volumetransfer_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeTransferApi->pcloud_volumetransfer_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**VolumeTransfers**](VolumeTransfers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_volumetransfer_post**
> VolumeTransfer pcloud_volumetransfer_post(cloud_instance_id, body)

Create a volume transfer

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
api_instance = ip4g.VolumeTransferApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.VolumeTransferCreate() # VolumeTransferCreate | Parameters for creating a volume transfer

try:
    # Create a volume transfer
    api_response = api_instance.pcloud_volumetransfer_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeTransferApi->pcloud_volumetransfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**VolumeTransferCreate**](VolumeTransferCreate.md)| Parameters for creating a volume transfer | 

### Return type

[**VolumeTransfer**](VolumeTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


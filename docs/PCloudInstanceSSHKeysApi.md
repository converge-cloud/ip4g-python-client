# ip4g.PCloudInstanceSSHKeysApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_sshkeys_delete**](PCloudInstanceSSHKeysApi.md#pcloud_cloudinstances_sshkeys_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/sshkeys/{sshkey_name} | Delete a CloudInstance&#39;s SSH key by name
[**pcloud_cloudinstances_sshkeys_get**](PCloudInstanceSSHKeysApi.md#pcloud_cloudinstances_sshkeys_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/sshkeys/{sshkey_name} | Get a CloudInstance&#39;s SSH Key by name
[**pcloud_cloudinstances_sshkeys_getall**](PCloudInstanceSSHKeysApi.md#pcloud_cloudinstances_sshkeys_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/sshkeys | List a CloudInstance&#39;s SSH Keys
[**pcloud_cloudinstances_sshkeys_post**](PCloudInstanceSSHKeysApi.md#pcloud_cloudinstances_sshkeys_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/sshkeys | Add a new SSH key to Cloud Instance
[**pcloud_cloudinstances_sshkeys_put**](PCloudInstanceSSHKeysApi.md#pcloud_cloudinstances_sshkeys_put) | **PUT** /pcloud/v1/cloud-instances/{cloud_instance_id}/sshkeys/{sshkey_name} | Update an SSH Key by SSH name


# **pcloud_cloudinstances_sshkeys_delete**
> Object pcloud_cloudinstances_sshkeys_delete(cloud_instance_id, sshkey_name)

Delete a CloudInstance's SSH key by name

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
api_instance = ip4g.PCloudInstanceSSHKeysApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant

try:
    # Delete a CloudInstance's SSH key by name
    api_response = api_instance.pcloud_cloudinstances_sshkeys_delete(cloud_instance_id, sshkey_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstanceSSHKeysApi->pcloud_cloudinstances_sshkeys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **sshkey_name** | **str**| SSH key name for a pcloud tenant | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_sshkeys_get**
> SSHKey pcloud_cloudinstances_sshkeys_get(cloud_instance_id, sshkey_name)

Get a CloudInstance's SSH Key by name

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
api_instance = ip4g.PCloudInstanceSSHKeysApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant

try:
    # Get a CloudInstance's SSH Key by name
    api_response = api_instance.pcloud_cloudinstances_sshkeys_get(cloud_instance_id, sshkey_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstanceSSHKeysApi->pcloud_cloudinstances_sshkeys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **sshkey_name** | **str**| SSH key name for a pcloud tenant | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_sshkeys_getall**
> SSHKeys pcloud_cloudinstances_sshkeys_getall(cloud_instance_id)

List a CloudInstance's SSH Keys

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
api_instance = ip4g.PCloudInstanceSSHKeysApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List a CloudInstance's SSH Keys
    api_response = api_instance.pcloud_cloudinstances_sshkeys_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstanceSSHKeysApi->pcloud_cloudinstances_sshkeys_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**SSHKeys**](SSHKeys.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_sshkeys_post**
> SSHKey pcloud_cloudinstances_sshkeys_post(cloud_instance_id, body)

Add a new SSH key to Cloud Instance

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
api_instance = ip4g.PCloudInstanceSSHKeysApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.SSHKey() # SSHKey | Parameters for the creation of a new SSH key in Cloud Instance

try:
    # Add a new SSH key to Cloud Instance
    api_response = api_instance.pcloud_cloudinstances_sshkeys_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstanceSSHKeysApi->pcloud_cloudinstances_sshkeys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**SSHKey**](SSHKey.md)| Parameters for the creation of a new SSH key in Cloud Instance | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_sshkeys_put**
> SSHKey pcloud_cloudinstances_sshkeys_put(cloud_instance_id, sshkey_name, body)

Update an SSH Key by SSH name

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
api_instance = ip4g.PCloudInstanceSSHKeysApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant
body = ip4g.SSHKey() # SSHKey | Parameters for updating a CloudInstance's SSH Key by name

try:
    # Update an SSH Key by SSH name
    api_response = api_instance.pcloud_cloudinstances_sshkeys_put(cloud_instance_id, sshkey_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudInstanceSSHKeysApi->pcloud_cloudinstances_sshkeys_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **sshkey_name** | **str**| SSH key name for a pcloud tenant | 
 **body** | [**SSHKey**](SSHKey.md)| Parameters for updating a CloudInstance&#39;s SSH Key by name | 

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


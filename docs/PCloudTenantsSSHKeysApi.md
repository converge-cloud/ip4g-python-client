# ip4g.PCloudTenantsSSHKeysApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_tenants_sshkeys_delete**](PCloudTenantsSSHKeysApi.md#pcloud_tenants_sshkeys_delete) | **DELETE** /pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name} | Delete a Tenant&#39;s SSH key
[**pcloud_tenants_sshkeys_get**](PCloudTenantsSSHKeysApi.md#pcloud_tenants_sshkeys_get) | **GET** /pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name} | Get a Tenant&#39;s SSH Key by name
[**pcloud_tenants_sshkeys_getall**](PCloudTenantsSSHKeysApi.md#pcloud_tenants_sshkeys_getall) | **GET** /pcloud/v1/tenants/{tenant_id}/sshkeys | List a Tenant&#39;s SSH Keys
[**pcloud_tenants_sshkeys_post**](PCloudTenantsSSHKeysApi.md#pcloud_tenants_sshkeys_post) | **POST** /pcloud/v1/tenants/{tenant_id}/sshkeys | Add a new SSH key to the Tenant
[**pcloud_tenants_sshkeys_put**](PCloudTenantsSSHKeysApi.md#pcloud_tenants_sshkeys_put) | **PUT** /pcloud/v1/tenants/{tenant_id}/sshkeys/{sshkey_name} | Update an SSH Key


# **pcloud_tenants_sshkeys_delete**
> Object pcloud_tenants_sshkeys_delete(tenant_id, sshkey_name)

Delete a Tenant's SSH key

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudTenantsSSHKeysApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant

try:
    # Delete a Tenant's SSH key
    api_response = api_instance.pcloud_tenants_sshkeys_delete(tenant_id, sshkey_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTenantsSSHKeysApi->pcloud_tenants_sshkeys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |
 **sshkey_name** | **str**| SSH key name for a pcloud tenant |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_tenants_sshkeys_get**
> SSHKey pcloud_tenants_sshkeys_get(tenant_id, sshkey_name)

Get a Tenant's SSH Key by name

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudTenantsSSHKeysApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant

try:
    # Get a Tenant's SSH Key by name
    api_response = api_instance.pcloud_tenants_sshkeys_get(tenant_id, sshkey_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTenantsSSHKeysApi->pcloud_tenants_sshkeys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |
 **sshkey_name** | **str**| SSH key name for a pcloud tenant |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_tenants_sshkeys_getall**
> SSHKeys pcloud_tenants_sshkeys_getall(tenant_id)

List a Tenant's SSH Keys

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudTenantsSSHKeysApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant

try:
    # List a Tenant's SSH Keys
    api_response = api_instance.pcloud_tenants_sshkeys_getall(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTenantsSSHKeysApi->pcloud_tenants_sshkeys_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |

### Return type

[**SSHKeys**](SSHKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_tenants_sshkeys_post**
> SSHKey pcloud_tenants_sshkeys_post(tenant_id, body)

Add a new SSH key to the Tenant

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudTenantsSSHKeysApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant
body = ip4g.SSHKey() # SSHKey | Parameters for the creation of a new SSH key

try:
    # Add a new SSH key to the Tenant
    api_response = api_instance.pcloud_tenants_sshkeys_post(tenant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTenantsSSHKeysApi->pcloud_tenants_sshkeys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |
 **body** | [**SSHKey**](SSHKey.md)| Parameters for the creation of a new SSH key |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_tenants_sshkeys_put**
> SSHKey pcloud_tenants_sshkeys_put(tenant_id, sshkey_name, body)

Update an SSH Key

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudTenantsSSHKeysApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant
sshkey_name = 'sshkey_name_example' # str | SSH key name for a pcloud tenant
body = ip4g.SSHKey() # SSHKey | Parameters for updating a Tenant's SSH Key

try:
    # Update an SSH Key
    api_response = api_instance.pcloud_tenants_sshkeys_put(tenant_id, sshkey_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudTenantsSSHKeysApi->pcloud_tenants_sshkeys_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |
 **sshkey_name** | **str**| SSH key name for a pcloud tenant |
 **body** | [**SSHKey**](SSHKey.md)| Parameters for updating a Tenant&#39;s SSH Key |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ip4g.IaasServiceBrokerApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_broker_health**](IaasServiceBrokerApi.md#service_broker_health) | **GET** /broker/v1/health | Get current server health
[**service_broker_health_head**](IaasServiceBrokerApi.md#service_broker_health_head) | **HEAD** /broker/v1/health | Get current server health
[**service_broker_test_timeout**](IaasServiceBrokerApi.md#service_broker_test_timeout) | **GET** /broker/v1/test/timeout | Get current server version
[**service_broker_version**](IaasServiceBrokerApi.md#service_broker_version) | **GET** /broker/v1/version | Get current server version


# **service_broker_health**
> Health service_broker_health()

Get current server health

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.IaasServiceBrokerApi()

try:
    # Get current server health
    api_response = api_instance.service_broker_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IaasServiceBrokerApi->service_broker_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_health_head**
> Health service_broker_health_head()

Get current server health

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.IaasServiceBrokerApi()

try:
    # Get current server health
    api_response = api_instance.service_broker_health_head()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IaasServiceBrokerApi->service_broker_health_head: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_test_timeout**
> Object service_broker_test_timeout(t)

Get current server version

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.IaasServiceBrokerApi()
t = 56 # int | seconds

try:
    # Get current server version
    api_response = api_instance.service_broker_test_timeout(t)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IaasServiceBrokerApi->service_broker_test_timeout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| seconds |

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_version**
> Version service_broker_version()

Get current server version

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.IaasServiceBrokerApi()

try:
    # Get current server version
    api_response = api_instance.service_broker_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IaasServiceBrokerApi->service_broker_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

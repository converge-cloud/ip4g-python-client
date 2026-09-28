# ip4g.SwaggerSpecApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_broker_swaggerspec**](SwaggerSpecApi.md#service_broker_swaggerspec) | **GET** /v1/swagger.json | Get swagger json spec


# **service_broker_swaggerspec**
> Object service_broker_swaggerspec()

Get swagger json spec

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.SwaggerSpecApi()

try:
    # Get swagger json spec
    api_response = api_instance.service_broker_swaggerspec()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SwaggerSpecApi->service_broker_swaggerspec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


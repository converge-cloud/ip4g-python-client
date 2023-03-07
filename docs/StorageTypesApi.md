# ip4g.StorageTypesApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_broker_storagetypes_get**](StorageTypesApi.md#service_broker_storagetypes_get) | **GET** /broker/v1/storage-types | Available storage types in a region


# **service_broker_storagetypes_get**
> StorageTypes service_broker_storagetypes_get()

Available storage types in a region

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.StorageTypesApi()

try:
    # Available storage types in a region
    api_response = api_instance.service_broker_storagetypes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageTypesApi->service_broker_storagetypes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageTypes**](StorageTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

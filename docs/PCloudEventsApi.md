# ip4g.PCloudEventsApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_events_get**](PCloudEventsApi.md#pcloud_events_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/events/{event_id} | Get a single event
[**pcloud_events_getquery**](PCloudEventsApi.md#pcloud_events_getquery) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/events | Get events from this cloud instance since a specific timestamp


# **pcloud_events_get**
> Event pcloud_events_get(cloud_instance_id, event_id, accept_language=accept_language)

Get a single event

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudEventsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
event_id = 'event_id_example' # str | Event ID
accept_language = 'accept_language_example' # str | The language requested for the return document (optional)

try:
    # Get a single event
    api_response = api_instance.pcloud_events_get(cloud_instance_id, event_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudEventsApi->pcloud_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **event_id** | **str**| Event ID |
 **accept_language** | **str**| The language requested for the return document | [optional]

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_events_getquery**
> Events pcloud_events_getquery(cloud_instance_id, time=time, from_time=from_time, to_time=to_time, accept_language=accept_language)

Get events from this cloud instance since a specific timestamp

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.PCloudEventsApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
time = 'time_example' # str | (deprecated - use from_time) A time in either ISO 8601 or unix epoch format (optional)
from_time = 'from_time_example' # str | A from query time in either ISO 8601 or unix epoch format (optional)
to_time = 'to_time_example' # str | A to query time in either ISO 8601 or unix epoch format (optional)
accept_language = 'accept_language_example' # str | The language requested for the return document (optional)

try:
    # Get events from this cloud instance since a specific timestamp
    api_response = api_instance.pcloud_events_getquery(cloud_instance_id, time=time, from_time=from_time, to_time=to_time, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudEventsApi->pcloud_events_getquery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance |
 **time** | **str**| (deprecated - use from_time) A time in either ISO 8601 or unix epoch format | [optional]
 **from_time** | **str**| A from query time in either ISO 8601 or unix epoch format | [optional]
 **to_time** | **str**| A to query time in either ISO 8601 or unix epoch format | [optional]
 **accept_language** | **str**| The language requested for the return document | [optional]

### Return type

[**Events**](Events.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

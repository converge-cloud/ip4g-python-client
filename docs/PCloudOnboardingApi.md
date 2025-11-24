# ip4g.PCloudOnboardingApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_v1_volume_onboarding_get**](PCloudOnboardingApi.md#pcloud_v1_volume_onboarding_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/onboarding | Describe onboard jobs
[**pcloud_v1_volume_onboarding_post**](PCloudOnboardingApi.md#pcloud_v1_volume_onboarding_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/volumes/onboarding | Onboard volumes to target site


# **pcloud_v1_volume_onboarding_get**
> VolumeAuxOnboarding pcloud_v1_volume_onboarding_get(cloud_instance_id)

Describe onboard jobs

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
api_instance = ip4g.PCloudOnboardingApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # Describe onboard jobs
    api_response = api_instance.pcloud_v1_volume_onboarding_get(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudOnboardingApi->pcloud_v1_volume_onboarding_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**VolumeAuxOnboarding**](VolumeAuxOnboarding.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v1_volume_onboarding_post**
> Object pcloud_v1_volume_onboarding_post(cloud_instance_id, body=body)

Onboard volumes to target site

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
api_instance = ip4g.PCloudOnboardingApi(ip4g.ApiClient(configuration))
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = ip4g.VolumeOnboarding() # VolumeOnboarding | Paremeters for onboarding aux volumes (optional)

try:
    # Onboard volumes to target site
    api_response = api_instance.pcloud_v1_volume_onboarding_post(cloud_instance_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudOnboardingApi->pcloud_v1_volume_onboarding_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**VolumeOnboarding**](VolumeOnboarding.md)| Paremeters for onboarding aux volumes | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


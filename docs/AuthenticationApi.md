# ip4g.AuthenticationApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_broker_auth_callback**](AuthenticationApi.md#service_broker_auth_callback) | **GET** /auth/v1/callback | Returns an accessToken (and set cookie)
[**service_broker_auth_device_code_post**](AuthenticationApi.md#service_broker_auth_device_code_post) | **POST** /auth/v1/device/code | Request a authorization device code
[**service_broker_auth_device_token_post**](AuthenticationApi.md#service_broker_auth_device_token_post) | **POST** /auth/v1/device/token | Poll for authorization device token
[**service_broker_auth_info_token**](AuthenticationApi.md#service_broker_auth_info_token) | **GET** /auth/v1/info/token | Information about current access token
[**service_broker_auth_info_user**](AuthenticationApi.md#service_broker_auth_info_user) | **GET** /auth/v1/info/user | Information about current user
[**service_broker_auth_login**](AuthenticationApi.md#service_broker_auth_login) | **GET** /auth/v1/login | Login
[**service_broker_auth_logout**](AuthenticationApi.md#service_broker_auth_logout) | **GET** /auth/v1/logout | Logout
[**service_broker_auth_registration**](AuthenticationApi.md#service_broker_auth_registration) | **GET** /auth/v1/registration | Registration of a new Tenant and Login
[**service_broker_auth_registration_callback**](AuthenticationApi.md#service_broker_auth_registration_callback) | **GET** /auth/v1/callback-registration | Associates the user with a tenant and returns an accessToken
[**service_broker_auth_token_post**](AuthenticationApi.md#service_broker_auth_token_post) | **POST** /auth/v1/token | Request a new token from a refresh token


# **service_broker_auth_callback**
> AccessToken service_broker_auth_callback()

Returns an accessToken (and set cookie)

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Returns an accessToken (and set cookie)
    api_response = api_instance.service_broker_auth_callback()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_callback: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_device_code_post**
> DeviceCode service_broker_auth_device_code_post()

Request a authorization device code

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Request a authorization device code
    api_response = api_instance.service_broker_auth_device_code_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_device_code_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceCode**](DeviceCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_device_token_post**
> Token service_broker_auth_device_token_post(body)

Poll for authorization device token

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()
body = ip4g.Body() # Body | Parameters for polling authorization device code

try:
    # Poll for authorization device token
    api_response = api_instance.service_broker_auth_device_token_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_device_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| Parameters for polling authorization device code |

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_info_token**
> TokenExtra service_broker_auth_info_token()

Information about current access token

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Information about current access token
    api_response = api_instance.service_broker_auth_info_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_info_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenExtra**](TokenExtra.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_info_user**
> UserInfo service_broker_auth_info_user()

Information about current user

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Information about current user
    api_response = api_instance.service_broker_auth_info_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_info_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_login**
> AccessToken service_broker_auth_login(user_id=user_id, redirect_url=redirect_url, access_type=access_type)

Login

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()
user_id = 'user_id_example' # str | The user id of the user (optional)
redirect_url = 'redirect_url_example' # str | The URL to redirect to after login/registration (optional)
access_type = 'online' # str | Determines if a refresh token is returned (optional) (default to online)

try:
    # Login
    api_response = api_instance.service_broker_auth_login(user_id=user_id, redirect_url=redirect_url, access_type=access_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id of the user | [optional]
 **redirect_url** | **str**| The URL to redirect to after login/registration | [optional]
 **access_type** | **str**| Determines if a refresh token is returned | [optional] [default to online]

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_logout**
> Object service_broker_auth_logout()

Logout

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Logout
    api_response = api_instance.service_broker_auth_logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_logout: %s\n" % e)
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

# **service_broker_auth_registration**
> AccessToken service_broker_auth_registration(tenant_id, entitlement_id, plan, icn, regions, redirect_url=redirect_url)

Registration of a new Tenant and Login

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()
tenant_id = 'tenant_id_example' # str | Tenant ID of a pcloud tenant
entitlement_id = 'entitlement_id_example' # str | Entitlement ID of for this tenant
plan = 'plan_example' # str | Plan for this tenant and entitlement
icn = 'icn_example' # str | IBM Customer Number (ICN) for this tenant
regions = ['regions_example'] # list[str] | An array of regions matching the number of cloud-instances in the plan
redirect_url = 'redirect_url_example' # str | The URL to redirect to after login/registration (optional)

try:
    # Registration of a new Tenant and Login
    api_response = api_instance.service_broker_auth_registration(tenant_id, entitlement_id, plan, icn, regions, redirect_url=redirect_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant ID of a pcloud tenant |
 **entitlement_id** | **str**| Entitlement ID of for this tenant |
 **plan** | **str**| Plan for this tenant and entitlement |
 **icn** | **str**| IBM Customer Number (ICN) for this tenant |
 **regions** | [**list[str]**](str.md)| An array of regions matching the number of cloud-instances in the plan |
 **redirect_url** | **str**| The URL to redirect to after login/registration | [optional]

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_registration_callback**
> AccessToken service_broker_auth_registration_callback()

Associates the user with a tenant and returns an accessToken

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()

try:
    # Associates the user with a tenant and returns an accessToken
    api_response = api_instance.service_broker_auth_registration_callback()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_registration_callback: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_token_post**
> Token service_broker_auth_token_post(body)

Request a new token from a refresh token

### Example
```python
from __future__ import print_function
import time
import ip4g
from ip4g.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ip4g.AuthenticationApi()
body = ip4g.TokenRequest() # TokenRequest | Parameters for requesting a new Token from a Refresh Token

try:
    # Request a new token from a refresh token
    api_response = api_instance.service_broker_auth_token_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequest**](TokenRequest.md)| Parameters for requesting a new Token from a Refresh Token |

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

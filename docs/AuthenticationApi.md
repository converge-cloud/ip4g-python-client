# ip4g.AuthenticationApi

All URIs are relative to *https://service-broker-api.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_broker_auth_info_token**](AuthenticationApi.md#service_broker_auth_info_token) | **GET** /auth/v1/info/token | Information about current access token
[**service_broker_auth_info_user**](AuthenticationApi.md#service_broker_auth_info_user) | **GET** /auth/v1/info/user | Information about current user
[**service_broker_auth_login**](AuthenticationApi.md#service_broker_auth_login) | **GET** /auth/v1/login | Login
[**service_broker_auth_logout**](AuthenticationApi.md#service_broker_auth_logout) | **GET** /auth/v1/logout | Logout
[**service_broker_auth_sa_delete**](AuthenticationApi.md#service_broker_auth_sa_delete) | **DELETE** /auth/sa/{client_id} | Delete service account
[**service_broker_auth_sa_get**](AuthenticationApi.md#service_broker_auth_sa_get) | **GET** /auth/sa/{client_id} | Describe service account
[**service_broker_auth_sa_getall**](AuthenticationApi.md#service_broker_auth_sa_getall) | **GET** /auth/sa | List service accounts
[**service_broker_auth_sa_post**](AuthenticationApi.md#service_broker_auth_sa_post) | **POST** /auth/sa/{client_id} | Add service account
[**service_broker_auth_sa_put**](AuthenticationApi.md#service_broker_auth_sa_put) | **PUT** /auth/sa/{client_id} | Edit service account


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

# Configure API key authorization: bearerAuth
configuration = ip4g.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
configuration = ip4g.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))

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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

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

# Configure API key authorization: bearerAuth
configuration = ip4g.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
configuration = ip4g.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))

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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

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

# Configure API key authorization: bearerAuth
configuration = ip4g.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
configuration = ip4g.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))

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

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_sa_delete**
> Object service_broker_auth_sa_delete(client_id)

Delete service account

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
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))
client_id = 'client_id_example' # str | SA client ID

try:
    # Delete service account
    api_response = api_instance.service_broker_auth_sa_delete(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_sa_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| SA client ID | 

### Return type

[**Object**](Object.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_sa_get**
> ServiceAccount service_broker_auth_sa_get(client_id)

Describe service account

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
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))
client_id = 'client_id_example' # str | SA client ID

try:
    # Describe service account
    api_response = api_instance.service_broker_auth_sa_get(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_sa_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| SA client ID | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_sa_getall**
> ServiceAccounts service_broker_auth_sa_getall()

List service accounts

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
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))

try:
    # List service accounts
    api_response = api_instance.service_broker_auth_sa_getall()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_sa_getall: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceAccounts**](ServiceAccounts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_sa_post**
> ServiceAccount service_broker_auth_sa_post(client_id, body)

Add service account

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
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))
client_id = 'client_id_example' # str | SA client ID
body = ip4g.ServiceAccountRequest() # ServiceAccountRequest | Parameters for adding service account

try:
    # Add service account
    api_response = api_instance.service_broker_auth_sa_post(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_sa_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| SA client ID | 
 **body** | [**ServiceAccountRequest**](ServiceAccountRequest.md)| Parameters for adding service account | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_broker_auth_sa_put**
> ServiceAccount service_broker_auth_sa_put(client_id, body)

Edit service account

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
api_instance = ip4g.AuthenticationApi(ip4g.ApiClient(configuration))
client_id = 'client_id_example' # str | SA client ID
body = ip4g.ServiceAccountRequest() # ServiceAccountRequest | Parameters for updating service account

try:
    # Edit service account
    api_response = api_instance.service_broker_auth_sa_put(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->service_broker_auth_sa_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| SA client ID | 
 **body** | [**ServiceAccountRequest**](ServiceAccountRequest.md)| Parameters for updating service account | 

### Return type

[**ServiceAccount**](ServiceAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.PCloudImagesApi

All URIs are relative to *https://service-broker-api.staging.gpcloudtest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pcloud_cloudinstances_images_delete**](PCloudImagesApi.md#pcloud_cloudinstances_images_delete) | **DELETE** /pcloud/v1/cloud-instances/{cloud_instance_id}/images/{image_id} | Delete an Image from a Cloud Instance
[**pcloud_cloudinstances_images_export_post**](PCloudImagesApi.md#pcloud_cloudinstances_images_export_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/images/{image_id}/export | Export an image
[**pcloud_cloudinstances_images_get**](PCloudImagesApi.md#pcloud_cloudinstances_images_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/images/{image_id} | Detailed info of an image
[**pcloud_cloudinstances_images_getall**](PCloudImagesApi.md#pcloud_cloudinstances_images_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/images | List all images for this cloud instance
[**pcloud_cloudinstances_images_post**](PCloudImagesApi.md#pcloud_cloudinstances_images_post) | **POST** /pcloud/v1/cloud-instances/{cloud_instance_id}/images | Create a new Image (from available images)
[**pcloud_cloudinstances_stockimages_get**](PCloudImagesApi.md#pcloud_cloudinstances_stockimages_get) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images/{image_id} | Detailed info of an available stock image
[**pcloud_cloudinstances_stockimages_getall**](PCloudImagesApi.md#pcloud_cloudinstances_stockimages_getall) | **GET** /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images | List all available stock images
[**pcloud_images_get**](PCloudImagesApi.md#pcloud_images_get) | **GET** /pcloud/v1/images/{image_id} | Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images/{image_id} - Detailed info of an available stock image
[**pcloud_images_getall**](PCloudImagesApi.md#pcloud_images_getall) | **GET** /pcloud/v1/images | Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images - List all available stock images
[**pcloud_v2_images_export_get**](PCloudImagesApi.md#pcloud_v2_images_export_get) | **GET** /pcloud/v2/cloud-instances/{cloud_instance_id}/images/{image_id}/export | Get detail of last image export job
[**pcloud_v2_images_export_post**](PCloudImagesApi.md#pcloud_v2_images_export_post) | **POST** /pcloud/v2/cloud-instances/{cloud_instance_id}/images/{image_id}/export | Add image export job to the jobs queue


# **pcloud_cloudinstances_images_delete**
> Object pcloud_cloudinstances_images_delete(cloud_instance_id, image_id)

Delete an Image from a Cloud Instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image

try:
    # Delete an Image from a Cloud Instance
    api_response = api_instance.pcloud_cloudinstances_images_delete(cloud_instance_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_images_export_post**
> Object pcloud_cloudinstances_images_export_post(cloud_instance_id, image_id, body)

Export an image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image
body = swagger_client.ExportImage() # ExportImage | Parameters for exporting an image

try:
    # Export an image
    api_response = api_instance.pcloud_cloudinstances_images_export_post(cloud_instance_id, image_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_images_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 
 **body** | [**ExportImage**](ExportImage.md)| Parameters for exporting an image | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_images_get**
> Image pcloud_cloudinstances_images_get(cloud_instance_id, image_id)

Detailed info of an image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image

try:
    # Detailed info of an image
    api_response = api_instance.pcloud_cloudinstances_images_get(cloud_instance_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_images_getall**
> Images pcloud_cloudinstances_images_getall(cloud_instance_id)

List all images for this cloud instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance

try:
    # List all images for this cloud instance
    api_response = api_instance.pcloud_cloudinstances_images_getall(cloud_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_images_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 

### Return type

[**Images**](Images.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_images_post**
> Image pcloud_cloudinstances_images_post(cloud_instance_id, body)

Create a new Image (from available images)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
body = swagger_client.CreateImage() # CreateImage | Parameters for the creation of a new image from available images

try:
    # Create a new Image (from available images)
    api_response = api_instance.pcloud_cloudinstances_images_post(cloud_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **body** | [**CreateImage**](CreateImage.md)| Parameters for the creation of a new image from available images | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_stockimages_get**
> Image pcloud_cloudinstances_stockimages_get(cloud_instance_id, image_id)

Detailed info of an available stock image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image

try:
    # Detailed info of an available stock image
    api_response = api_instance.pcloud_cloudinstances_stockimages_get(cloud_instance_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_stockimages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_cloudinstances_stockimages_getall**
> Images pcloud_cloudinstances_stockimages_getall(cloud_instance_id, sap=sap, vtl=vtl)

List all available stock images

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
sap = true # bool | Include SAP images with get available stock images (optional)
vtl = true # bool | Include VTL images with get available stock images (optional)

try:
    # List all available stock images
    api_response = api_instance.pcloud_cloudinstances_stockimages_getall(cloud_instance_id, sap=sap, vtl=vtl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_cloudinstances_stockimages_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **sap** | **bool**| Include SAP images with get available stock images | [optional] 
 **vtl** | **bool**| Include VTL images with get available stock images | [optional] 

### Return type

[**Images**](Images.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_images_get**
> Image pcloud_images_get(image_id)

Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images/{image_id} - Detailed info of an available stock image

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
image_id = 'image_id_example' # str | Image ID of a image

try:
    # Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images/{image_id} - Detailed info of an available stock image
    api_response = api_instance.pcloud_images_get(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID of a image | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_images_getall**
> Images pcloud_images_getall(sap=sap, vtl=vtl)

Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images - List all available stock images

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
sap = true # bool | Include SAP images with get available stock images (optional)
vtl = true # bool | Include VTL images with get available stock images (optional)

try:
    # Deprecated for /pcloud/v1/cloud-instances/{cloud_instance_id}/stock-images - List all available stock images
    api_response = api_instance.pcloud_images_getall(sap=sap, vtl=vtl)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_images_getall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sap** | **bool**| Include SAP images with get available stock images | [optional] 
 **vtl** | **bool**| Include VTL images with get available stock images | [optional] 

### Return type

[**Images**](Images.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_images_export_get**
> Job pcloud_v2_images_export_get(cloud_instance_id, image_id)

Get detail of last image export job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image

try:
    # Get detail of last image export job
    api_response = api_instance.pcloud_v2_images_export_get(cloud_instance_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_v2_images_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pcloud_v2_images_export_post**
> JobReference pcloud_v2_images_export_post(cloud_instance_id, image_id, body)

Add image export job to the jobs queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PCloudImagesApi()
cloud_instance_id = 'cloud_instance_id_example' # str | Cloud Instance ID of a PCloud Instance
image_id = 'image_id_example' # str | Image ID of a image
body = swagger_client.ExportImage() # ExportImage | Parameters for the export

try:
    # Add image export job to the jobs queue
    api_response = api_instance.pcloud_v2_images_export_post(cloud_instance_id, image_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PCloudImagesApi->pcloud_v2_images_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_instance_id** | **str**| Cloud Instance ID of a PCloud Instance | 
 **image_id** | **str**| Image ID of a image | 
 **body** | [**ExportImage**](ExportImage.md)| Parameters for the export | 

### Return type

[**JobReference**](JobReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


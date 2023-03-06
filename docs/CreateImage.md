# CreateImage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | Name to give created image; required for import image | [optional] 
**region** | **str** | Cloud Storage Region; only required to access IBM Cloud Storage | [optional] 
**secret_key** | **str** | Cloud Storage secret key; required for import image | [optional] 
**access_key** | **str** | Cloud Storage access key; required for import image | [optional] 
**image_id** | **str** | Image ID of existing source image; required for copy image | [optional] 
**image_filename** | **str** | Cloud Storage image filename; required for import image | [optional] 
**image_path** | **str** | (deprecated - replaced by region, imageFilename and bucketName) Path to image starting with service endpoint and ending with image filename | [optional] 
**os_type** | **str** | Image OS Type, required if importing a raw image; raw images can only be imported using the command line interface | [optional] 
**source** | **str** | Source of the image | 
**storage_affinity** | [**StorageAffinity**](StorageAffinity.md) | The storage affinity data; ignored if storagePool is provided; Used only when importing an image from cloud storage. | [optional] 
**storage_pool** | **str** | Storage pool where the image will be loaded; if provided then storageAffinity and diskType will be ignored; Used only when importing an image from cloud storage. | [optional] 
**bucket_name** | **str** | Cloud Storage bucket name; bucket-name[/optional/folder]; required for import image | [optional] 
**disk_type** | **str** | Type of Disk; will be ignored if storagePool or affinityPolicy is provided; Used only when importing an image from cloud storage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateCosImageImportJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | Cloud Object Storage access key; required for buckets with private access | [optional] 
**bucket_access** | **str** | indicates if the bucket has public or private access public access require no authentication keys private access requires hmac authentication keys (access,secret) | [optional] [default to 'private']
**bucket_name** | **str** | Cloud Object Storage bucket name; bucket-name[/optional/folder] | 
**image_filename** | **str** | Cloud Object Storage image filename | 
**image_name** | **str** | Name for the image that will be loaded into the boot image catalog | 
**os_type** | **str** | Image OS Type, required if importing a raw image; raw images can only be imported using the command line interface | [optional] 
**region** | **str** | Cloud Object Storage region | 
**secret_key** | **str** | Cloud Object Storage secret key; required for buckets with private access | [optional] 
**storage_affinity** | [**StorageAffinity**](StorageAffinity.md) | Storage affinity data used for storage pool selection | [optional] 
**storage_pool** | **str** | Storage pool where the image will be loaded, if provided then storageType and storageAffinity will be ignored | [optional] 
**storage_type** | **str** | Type of storage; will be ignored if storagePool or storageAffinity is provided. If only using storageType for storage selection then the storage pool with the most available space will be selected | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



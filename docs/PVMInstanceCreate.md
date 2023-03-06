# PVMInstanceCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicant_affinity_policy** | **str** | Affinity policy for replicants being created; affinity for the same host, anti-affinity for different hosts, none for no preference | [optional] [default to 'none']
**storage_pool** | **str** | Storage Pool for server deployment; if provided then storageAffinity and storageType will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**volume_ids** | **list[str]** | List of volume IDs | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**migratable** | **bool** | Indicates if the server is allowed to migrate between hosts | [optional] [default to True]
**pin_policy** | [**PinPolicy**](PinPolicy.md) |  | [optional] 
**server_name** | **str** | Name of the server to create | 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**storage_connection** | **str** | The storage connection type | [optional] 
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 
**image_id** | **str** | Image ID of the image to use for the server | 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [default to 'dedicated']
**replicant_naming_scheme** | **str** | How to name the created vms | [optional] [default to 'suffix']
**replicants** | **float** | Number of duplicate instances to create in this request | [optional] 
**storage_type** | **str** | Storage type for server deployment; will be ignored if storagePool or storageAffinity is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**user_data** | **str** | Cloud init user defined data | [optional] 
**network_ids** | **list[str]** | (deprecated - replaced by networks) List of Network IDs | [optional] 
**networks** | [**list[PVMInstanceAddNetwork]**](PVMInstanceAddNetwork.md) | The pvm instance networks information | [optional] 
**placement_group** | **str** | The placement group for the server | [optional] 
**processors** | **float** | Number of processors allocated | 
**storage_affinity** | [**StorageAffinity**](StorageAffinity.md) | The storage affinity data; ignored if storagePool is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**sys_type** | **str** | System type used to host the instance | [optional] 
**key_pair_name** | **str** | The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant&#39;s list of keys) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



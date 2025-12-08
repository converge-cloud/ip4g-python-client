# PVMInstanceCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | Image ID of the image to use for the server | 
**key_pair_name** | **str** | The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant&#39;s list of keys) | [optional] 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | 
**migratable** | **bool** | Indicates if the server is allowed to migrate between hosts | [optional] [default to True]
**network_ids** | **list[str]** | (deprecated - replaced by networks) List of Network IDs | [optional] 
**networks** | [**list[PVMInstanceAddNetwork]**](PVMInstanceAddNetwork.md) | The pvm instance networks information | [optional] 
**pin_policy** | [**PinPolicy**](PinPolicy.md) |  | [optional] 
**placement_group** | **str** | The placement group for the server | [optional] 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [default to 'dedicated']
**processors** | **float** | Number of processors allocated | 
**replicant_affinity_policy** | **str** | Affinity policy for replicants being created; affinity for the same host, anti-affinity for different hosts, none for no preference | [optional] [default to 'none']
**replicant_naming_scheme** | **str** | How to name the created vms | [optional] [default to 'suffix']
**replicants** | **float** | Number of duplicate instances to create in this request | [optional] 
**server_name** | **str** | Name of the server to create | 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**spp_name_or_id** | **str** | Assign this newly created compute instance to the given Shared Processor Pool [SPP] (as identified by either name or ID).  You may not assign the new instance to an SPP and also assign it to a PlacementGroup and/or with an affinityPolicy.  | [optional] 
**storage_affinity** | [**StorageAffinity**](StorageAffinity.md) | The storage affinity data; ignored if storagePool is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**storage_connection** | **str** | The storage connection type | [optional] 
**storage_pool** | **str** | Storage Pool for server deployment; if provided then storageAffinity and storageType will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**storage_type** | **str** | Storage type for server deployment; will be ignored if storagePool or storageAffinity is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in | [optional] 
**sys_type** | **str** | System type used to host the instance | [optional] 
**user_data** | **str** | Cloud init user defined data | [optional] 
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 
**volume_ids** | **list[str]** | List of volume IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PVMInstanceUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | [optional] 
**migratable** | **bool** | Indicates if the server is allowed to migrate between hosts | [optional] [default to True]
**pin_policy** | [**PinPolicy**](PinPolicy.md) |  | [optional] 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [optional] 
**processors** | **float** | Number of processors allocated | [optional] 
**sap_profile_id** | **str** | If an SAP pvm-instance, the SAP profile ID to switch to (only while shutdown) | [optional] 
**server_name** | **str** | Name of the server to create | [optional] 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**storage_pool_affinity** | **bool** | Indicates if all volumes attached to the server must reside in the same storage pool; If set to false then volumes from any storage type and pool can be attached to the PVMInstance; Impacts PVMInstance snapshot, capture, and clone, for capture and clone - only data volumes that are of the same storage type and in the same storage pool of the PVMInstance&#39;s boot volume can be included; for snapshot - all data volumes to be included in the snapshot must reside in the same storage type and pool. Once set to false, cannot be set back to true unless all volumes attached reside in the same storage type and pool. | [optional] [default to True]
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



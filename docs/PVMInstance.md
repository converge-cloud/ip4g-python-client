# PVMInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys_type** | **str** | System type used to host the instance | [optional] 
**minmem** | **float** | Minimum amount of memory that can be allocated (in GB, for resize) | [optional] 
**operating_system** | **str** | OS system information (usually version and build) | [optional] 
**pin_policy** | **str** | VM pinning policy to use [none, soft, hard] | [optional] 
**storage_pool** | **str** | Storage Pool where server is deployed | [optional] 
**storage_type** | **str** | Storage type where server is deployed | 
**progress** | **float** | The progress of an operation | [optional] 
**sap_profile** | [**SAPProfileReference**](SAPProfileReference.md) | If this is an SAP pvm-instance the profile reference will link to the SAP profile | [optional] 
**status** | **str** | The status of the instance | 
**addresses** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | (deprecated - replaced by networks) The list of addresses and their network information | [optional] 
**host_id** | **int** | The PVM Instance Host ID (Internal Use Only) | [optional] 
**image_id** | **str** | The ImageID used by the server | 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**maxproc** | **float** | Maximum number of processors that can be allocated (for resize) | [optional] 
**creation_date** | **datetime** | Date/Time of PVM creation | [optional] 
**fault** | [**PVMInstanceFault**](PVMInstanceFault.md) |  | [optional] 
**migratable** | **bool** | whether the instance can be migrated | [optional] [default to True]
**maxmem** | **float** | Maximum amount of memory that can be allocated (in GB, for resize) | [optional] 
**minproc** | **float** | Minimum number of processors that can be allocated (for resize) | [optional] 
**os_type** | **str** | Type of the OS [aix, ibmi, rhel, sles, vtl] | 
**placement_group** | **str** | The placement group of the server | [optional] [default to 'none']
**console_language** | [**ConsoleLanguage**](ConsoleLanguage.md) | Console language and code | [optional] 
**disk_size** | **float** | Size of allocated disk (in GB) | 
**health** | [**PVMInstanceHealth**](PVMInstanceHealth.md) |  | [optional] 
**network_ids** | **list[str]** | (deprecated - replaced by networks) List of Network IDs | 
**storage_pool_affinity** | **bool** | Indicates if all volumes attached to the server must reside in the same storage pool; Defaults to true when initially deploying a PVMInstance | [optional] [default to True]
**memory** | **float** | Amount of memory allocated (in GB) | 
**networks** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | The pvm instance networks information | [optional] 
**pvm_instance_id** | **str** | PCloud PVM Instance ID | 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [default to 'dedicated']
**server_name** | **str** | Name of the server | 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**updated_date** | **datetime** | Date/Time of PVM last update | [optional] 
**volume_ids** | **list[str]** | List of volume IDs | 
**processors** | **float** | Number of processors allocated | 
**srcs** | **list[list[SRC]]** | The pvm instance SRC lists | [optional] 
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



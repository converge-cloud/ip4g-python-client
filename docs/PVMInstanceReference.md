# PVMInstanceReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_pool** | **str** | Storage Pool where server is deployed | [optional] 
**updated_date** | **datetime** | Date/Time of PVM last update | [optional] 
**disk_size** | **float** | Size of allocated disk (in GB) | 
**fault** | [**PVMInstanceFault**](PVMInstanceFault.md) |  | [optional] 
**srcs** | **list[list[SRC]]** | The pvm instance SRC lists | [optional] 
**status** | **str** | The status of the instance | 
**minmem** | **float** | Minimum amount of memory that can be allocated (in GB, for resize) | [optional] 
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 
**networks** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | The list of addresses and their network information | [optional] 
**addresses** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | (deprecated - replaced by networks) The list of addresses and their network information | [optional] 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**maxproc** | **float** | Maximum number of processors that can be allocated (for resize) | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | 
**processors** | **float** | Number of processors allocated | 
**storage_type** | **str** | Storage type of the deployment storage pool | [optional] 
**href** | **str** | Link to Cloud Instance resource | 
**image_id** | **str** | The ImageID used by the server | 
**operating_system** | **str** | OS system information (usually version and build) | [optional] 
**placement_group** | **str** | The placement group of the server | [optional] [default to 'none']
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**storage_pool_affinity** | **bool** | Indicates if all volumes attached to the server must reside in the same storage pool | [optional] [default to True]
**sys_type** | **str** | System type used to host the instance | [optional] 
**console_language** | [**ConsoleLanguage**](ConsoleLanguage.md) | Console language and code | [optional] 
**os_type** | **str** | Type of the OS [aix, ibmi, rhel, sles, vtl] | 
**progress** | **float** | The progress of an operation | [optional] 
**sap_profile** | [**SAPProfileReference**](SAPProfileReference.md) | If this is an SAP pvm-instance the profile reference will link to the SAP profile | [optional] 
**minproc** | **float** | Minimum number of processors that can be allocated (for resize) | [optional] 
**creation_date** | **datetime** | Date/Time of PVM creation | [optional] 
**maxmem** | **float** | Maximum amount of memory that can be allocated (in GB, for resize) | [optional] 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [default to 'dedicated']
**pvm_instance_id** | **str** | PCloud PVM Instance ID | 
**health** | [**PVMInstanceHealth**](PVMInstanceHealth.md) |  | [optional] 
**host_id** | **int** | The PVM Instance Host ID (Internal Use Only) | [optional] 
**pin_policy** | **str** | VM pinning policy to use [none, soft, hard] | [optional] 
**server_name** | **str** | Name of the server | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



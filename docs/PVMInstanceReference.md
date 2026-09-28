# PVMInstanceReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | (deprecated - replaced by networks) The list of addresses and their network information | [optional] 
**console_language** | [**ConsoleLanguage**](ConsoleLanguage.md) | Console language and code | [optional] 
**creation_date** | **datetime** | Date/Time of PVM creation | [optional] 
**disk_size** | **float** | Size of allocated disk (in GB) | 
**fault** | [**PVMInstanceFault**](PVMInstanceFault.md) |  | [optional] 
**health** | [**PVMInstanceHealth**](PVMInstanceHealth.md) |  | [optional] 
**host_id** | **int** | The PVM Instance Host ID (Internal Use Only) | [optional] 
**href** | **str** | Link to Cloud Instance resource | 
**image_id** | **str** | The ImageID used by the server | 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**maxmem** | **float** | Maximum amount of memory that can be allocated (in GB, for resize) | [optional] 
**maxproc** | **float** | Maximum number of processors that can be allocated (for resize) | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | 
**minmem** | **float** | Minimum amount of memory that can be allocated (in GB, for resize) | [optional] 
**minproc** | **float** | Minimum number of processors that can be allocated (for resize) | [optional] 
**networks** | [**list[PVMInstanceNetwork]**](PVMInstanceNetwork.md) | The list of addresses and their network information | [optional] 
**operating_system** | **str** | OS system information (usually version and build) | [optional] 
**os_type** | **str** | Type of the OS [aix, ibmi, rhel, sles, vtl, rhcos] | 
**pin_policy** | **str** | VM pinning policy to use [none, soft, hard] | [optional] 
**placement_group** | **str** | The placement group of the server | [optional] [default to 'none']
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [default to 'dedicated']
**processors** | **float** | Number of processors allocated | 
**progress** | **float** | The progress of an operation | [optional] 
**pvm_instance_id** | **str** | PCloud PVM Instance ID | 
**sap_profile** | [**SAPProfileReference**](SAPProfileReference.md) | If this is an SAP pvm-instance the profile reference will link to the SAP profile | [optional] 
**server_name** | **str** | Name of the server | 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**srcs** | **list[list[SRC]]** | The pvm instance SRC lists | [optional] 
**status** | **str** | The status of the instance | 
**storage_pool** | **str** | Storage Pool where server is deployed | [optional] 
**storage_pool_affinity** | **bool** | Indicates if all volumes attached to the server must reside in the same storage pool | [optional] [default to True]
**storage_type** | **str** | Storage type of the deployment storage pool | [optional] 
**sys_type** | **str** | System type used to host the instance | [optional] 
**task_state** | **str** | Intermediate task status | [optional] 
**updated_date** | **datetime** | Date/Time of PVM last update | [optional] 
**virtual_cores** | [**VirtualCores**](VirtualCores.md) | The pvm instance virtual CPU information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



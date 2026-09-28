# Spp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_cores** | **float** | The amount of allocated processor cores for the Shared Processor Pool  | 
**available_cores** | **float** | The amount of available processor cores for the Shared Processor Pool  | 
**host_group** | **str** | The host group the host belongs to | [optional] 
**host_id** | **int** | The ID of the host where the Shared Processor Pool resides | [optional] 
**id** | **str** | The id of the Shared Processor Pool | 
**name** | **str** | The name of the Shared Processor Pool | 
**pvm_instances** | [**list[SppServer]**](SppServer.md) | list of Power Virtual Machines (PVM) instances that are in the SPP.  | [optional] 
**reserved_cores** | **int** | The amount of reserved processor cores for the Shared Processor Pool  | 
**shared_processor_pool_placement_groups** | [**list[SppPlacementGroup]**](SppPlacementGroup.md) | list of Shared Processor Pool Placement Groups | [optional] 
**status** | **str** | The status of the Shared Processor Pool | [optional] 
**status_detail** | **str** | The status details of the Shared Processor Pool | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SystemPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**System**](System.md) | Advertised capacity cores and memory (GB) | [optional] 
**core_memory_ratio** | **float** | Processor to Memory (GB) Ratio | [optional] 
**max_available** | [**System**](System.md) | Maximum configurable cores and memory (GB) (aggregated from all hosts) | [optional] 
**max_cores_available** | [**System**](System.md) | Maximum configurable cores available combined with available memory of that host | [optional] 
**max_memory_available** | [**System**](System.md) | Maximum configurable memory available combined with available cores of that host | [optional] 
**shared_core_ratio** | [**MinMaxDefault**](MinMaxDefault.md) | min-max-default allocation percentage of shared core per vCPU | [optional] 
**systems** | [**list[System]**](System.md) | The DataCenter list of servers and their available resources | [optional] 
**type** | **str** | Type of system hardware | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



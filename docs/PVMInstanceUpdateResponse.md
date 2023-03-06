# PVMInstanceUpdateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin_policy** | [**PinPolicy**](PinPolicy.md) |  | [optional] 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [optional] 
**processors** | **float** | Number of processors allocated | [optional] 
**server_name** | **str** | Name of the server to create | [optional] 
**status_url** | **str** | URL to check for status of the operation (for now, just the URL for the GET on the server, which has status information from powervc) | [optional] 
**license_repository_capacity** | **int** | The VTL license repository capacity TB value | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



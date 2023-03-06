# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | ID of the Activity | 
**level** | **str** | Level of the event (notice, info, warning, error) | 
**resource** | **str** | Type of resource for this event | 
**time** | **datetime** | Time of activity in ISO 8601 - RFC3339 | 
**user** | [**EventUser**](EventUser.md) |  | [optional] 
**action** | **str** | Type of action for this event | 
**message** | **str** | The (translated) message of the event | 
**metadata** | **object** | Any metadata associated with the event | [optional] 
**timestamp** | **int** | Time of activity in unix epoch | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



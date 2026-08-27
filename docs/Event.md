# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Type of action for this event | 
**event_id** | **str** | ID of the Activity | 
**level** | **str** | Level of the event (notice, info, warning, error) | 
**message** | **str** | The (translated) message of the event | 
**metadata** | **object** | Any metadata associated with the event | [optional] 
**resource** | **str** | Type of resource for this event | 
**time** | **datetime** | Time of activity in ISO 8601 - RFC3339 | 
**timestamp** | **int** | Time of activity in unix epoch | 
**user** | [**EventUser**](EventUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** | Notes for development (not used internally) | [optional] 
**id** | **str** | User ID | [optional] 
**rev** | **str** |  | [optional] 
**base_role** | **str** | Base Role for this User | [optional] [default to 'user-readonly']
**cloud_instances** | [**UserAccessCloudInstanceMap**](UserAccessCloudInstanceMap.md) | A map of cloudInstanceID to role | [optional] 
**member_of** | **list[str]** | Member of (Tenants) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserAccess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | [optional] 
**rev** | **str** |  | [optional] 
**base_role** | **str** | Base Role for this User | [optional] [default to 'user-readonly']
**can_create_sa** | **bool** | Flag denoting permission to add SA UserAccess record | [optional] [default to False]
**cloud_instances** | [**UserAccessCloudInstanceMap**](UserAccessCloudInstanceMap.md) | A map of cloudInstanceID to role | [optional] 
**is_type_sa** | **bool** | Flag denoting SA UserAccess record | [optional] [default to False]
**member_of** | **list[str]** | Member of (Tenants) | [optional] 
**notes** | **str** | Notes for development (not used internally) | [optional] 
**sa_metadata** | **str** | SA related metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



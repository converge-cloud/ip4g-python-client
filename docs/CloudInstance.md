# CloudInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **list[str]** | Cloud Instance Capabilities | [optional] 
**cloud_instance_id** | **str** | Cloud Instance ID | 
**enabled** | **bool** | Indicates if the cloud instance is enabled | 
**initialized** | **bool** | Indicates if the cloud instance is initialized and ready for use | 
**limits** | [**CloudInstanceUsageLimits**](CloudInstanceUsageLimits.md) | Limits on the cloud instance | 
**name** | **str** | Cloud Instance Name | 
**openstack_id** | **str** | The open stack ID that controls this cloud instance | 
**pvm_instances** | [**list[PVMInstanceReference]**](PVMInstanceReference.md) | PVM instances owned by the Cloud Instance | 
**region** | **str** | The region the cloud instance lives | 
**tenant_id** | **str** | The tenant ID that owns this cloud instance | 
**usage** | [**CloudInstanceUsageLimits**](CloudInstanceUsageLimits.md) | Current usage on the cloud instance | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



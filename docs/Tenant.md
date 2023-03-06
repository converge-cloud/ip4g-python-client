# Tenant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_keys** | [**list[SSHKey]**](SSHKey.md) | Tenant SSH Keys | [optional] 
**tenant_id** | **str** | Tenant ID | 
**cloud_instances** | [**list[CloudInstanceReference]**](CloudInstanceReference.md) | Cloud Instances owned by the Tenant | 
**creation_date** | **datetime** | Date of Tenant creation | 
**enabled** | **bool** | Indicates if the tenant is enabled | 
**icn** | **str** | IBM Customer Number | [optional] 
**peering_networks** | [**list[PeeringNetwork]**](PeeringNetwork.md) | Peering Network Information (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



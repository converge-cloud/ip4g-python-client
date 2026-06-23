# PrivateConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | [**Bandwidth**](Bandwidth.md) |  | [optional] 
**enabled** | **bool** | Indicates whether the private connection is enabled or disabled. | [optional] 
**id** | **str** | Immutable identifier for the Private Connection | [optional] 
**name** | [**PrivateConnectionName**](PrivateConnectionName.md) |  | [optional] 
**primary_state** | **str** | State of primary attachment, see https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/patch for range, with the addition of DISABLED indicating that the overall connection has been disabled. | [optional] 
**region** | **str** | Region in which we’re creating primary and secondary VLAN attachments | [optional] 
**secondary_state** | **str** | State of secondary attachment, see https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/patch for range, with the addition of DISABLED indicating that the overall connection has been disabled. | [optional] 
**tenant_id** | **str** | Tenant ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



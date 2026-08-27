# VPNConnectionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_policy** | **str** | unique identifier of IKEPolicy selected for this VPNConnection | 
**ip_sec_policy** | **str** | unique identifier of IPSecPolicy selected for this VPNConnection | 
**mode** | **str** | Mode used by this VPNConnection, either policy-based, or route-based, this attribute is set at the creation and cannot be updated later. | 
**name** | **str** | VPN Connection name | 
**networks** | **list[str]** | an array of network IDs to attach to this VPNConnection | 
**peer_gateway_address** | [**PeerGatewayAddress**](PeerGatewayAddress.md) |  | 
**peer_subnets** | **list[str]** | an array of strings containing CIDR of peer subnets | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VPNConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dead_peer_detection** | [**DeadPeerDetection**](DeadPeerDetection.md) |  | 
**id** | **str** | unique identifier for VPN Connection | 
**ike_policy** | [**IKEPolicyRef**](IKEPolicyRef.md) |  | 
**ip_sec_policy** | [**IPSecPolicyRef**](IPSecPolicyRef.md) |  | 
**local_gateway_address** | **str** | local Gateway address, only in &#39;route&#39; mode. | 
**mode** | **str** | Mode used by this VPNConnection, either policy-based, or route-based, this attribute is set at the creation and cannot be updated later. | 
**name** | **str** | VPN Connection name | 
**network_ids** | **list[str]** | an array of network IDs | 
**peer_gateway_address** | [**PeerGatewayAddress**](PeerGatewayAddress.md) |  | 
**peer_subnets** | **list[str]** | an array of strings containing CIDR of peer subnets | 
**status** | **str** | status of the VPN connection | 
**vpn_gateway_address** | **str** | public IP address of the VPN Gateway (vSRX) attached to this VPNConnection | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



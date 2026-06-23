# Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | Network in CIDR notation (192.168.0.0/24) | 
**cloud_connections** | [**list[NetworkCloudConnections]**](NetworkCloudConnections.md) | (currently not available) cloud connections this network is attached | [optional] 
**dhcp_managed** | **bool** | DHCP Managed Network | [optional] 
**dns_servers** | **list[str]** | DNS Servers | 
**gateway** | **str** | Gateway IP Address | [optional] 
**ip_address_metrics** | [**NetworkIpAddressMetrics**](NetworkIpAddressMetrics.md) |  | 
**ip_address_ranges** | [**list[IPAddressRange]**](IPAddressRange.md) | IP Address Ranges | 
**jumbo** | **bool** | MTU Jumbo Network enabled | 
**name** | **str** | Network Name | 
**network_id** | **str** | Unique Network ID | 
**public_ip_address_ranges** | [**list[IPAddressRange]**](IPAddressRange.md) | Public IP Address Ranges (for pub-vlan networks) | [optional] 
**type** | **str** | Type of Network {vlan, pub-vlan} | [default to 'vlan']
**vlan_id** | **float** | VLAN ID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



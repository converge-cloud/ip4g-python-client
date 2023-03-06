# Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address_metrics** | [**NetworkIpAddressMetrics**](NetworkIpAddressMetrics.md) |  | 
**ip_address_ranges** | [**list[IPAddressRange]**](IPAddressRange.md) | IP Address Ranges | 
**jumbo** | **bool** | MTU Jumbo Network enabled | 
**cidr** | **str** | Network in CIDR notation (192.168.0.0/24) | 
**gateway** | **str** | Gateway IP Address | [optional] 
**name** | **str** | Network Name | 
**network_id** | **str** | Unique Network ID | 
**public_ip_address_ranges** | [**list[IPAddressRange]**](IPAddressRange.md) | Public IP Address Ranges (for pub-vlan networks) | [optional] 
**type** | **str** | Type of Network {vlan, pub-vlan} | [default to 'vlan']
**vlan_id** | **float** | VLAN ID | 
**dns_servers** | **list[str]** | DNS Servers | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



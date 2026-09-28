# NetworkCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | Network in CIDR notation (192.168.0.0/24) | [optional] 
**dns_servers** | **list[str]** | DNS Servers | [optional] 
**gateway** | **str** | Gateway IP Address | [optional] 
**ip_address_ranges** | [**list[IPAddressRange]**](IPAddressRange.md) | IP Address Ranges | [optional] 
**jumbo** | **bool** | Enable MTU Jumbo Network | [optional] 
**name** | **str** | Network Name | [optional] 
**type** | **str** | Type of Network - &#39;vlan&#39; (private network) &#39;pub-vlan&#39; (public network) | [default to 'vlan']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PVMInstanceClone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_pair_name** | **str** | The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant&#39;s list of keys) | [optional] 
**memory** | **float** | Amount of memory allocated (in GB) | [optional] 
**name** | **str** | Name of the server to create | 
**networks** | [**list[PVMInstanceAddNetwork]**](PVMInstanceAddNetwork.md) | The pvm instance networks information | 
**proc_type** | **str** | Processor type (dedicated, shared, capped) | [optional] [default to 'dedicated']
**processors** | **float** | Number of processors allocated | [optional] 
**software_licenses** | [**SoftwareLicenses**](SoftwareLicenses.md) | The pvm instance Software Licenses | [optional] 
**volume_ids** | **list[str]** | List of volume IDs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



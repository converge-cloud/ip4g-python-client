# StorageAffinity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity_pvm_instance** | **str** | PVM Instance (ID or Name) to base storage affinity policy against; required if requesting storage affinity and affinityVolume is not provided | [optional] 
**affinity_policy** | **str** | Affinity policy for storage pool selection; ignored if storagePool provided; for policy &#39;affinity&#39; requires one of affinityPVMInstance or affinityVolume to be specified; for policy &#39;anti-affinity&#39; requires one of antiAffinityPVMInstances or antiAffinityVolumes to be specified | [optional] 
**affinity_volume** | **str** | Volume (ID or Name) to base storage affinity policy against; required if requesting storage affinity and affinityPVMInstance is not provided | [optional] 
**anti_affinity_pvm_instances** | **list[str]** | List of pvmInstances to base storage anti-affinity policy against; required if requesting storage anti-affinity and antiAffinityVolumes is not provided | [optional] 
**anti_affinity_volumes** | **list[str]** | List of volumes to base storage anti-affinity policy against; required if requesting storage anti-affinity and antiAffinityPVMInstances is not provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



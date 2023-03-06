# MultiVolumesCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shareable** | **bool** | Indicates if the volume is shareable between VMs | [optional] 
**affinity_volume** | **str** | Volume (ID or Name) to base volume affinity policy against; required if requesting affinity and affinityPVMInstance is not provided | [optional] 
**anti_affinity_pvm_instances** | **list[str]** | List of pvmInstances to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityVolumes is not provided | [optional] 
**anti_affinity_volumes** | **list[str]** | List of volumes to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityPVMInstances is not provided | [optional] 
**count** | **int** | Number of volumes to create | [optional] 
**name** | **str** | Base name of the volume(s) | 
**replication_enabled** | **bool** | Indicates if the volume should be replication enabled or not | [optional] 
**affinity_pvm_instance** | **str** | PVM Instance (ID or Name)to base volume affinity policy against; required if requesting affinity and affinityVolume is not provided | [optional] 
**affinity_policy** | **str** | Affinity policy for data volume being created; ignored if volumePool provided; for policy &#39;affinity&#39; requires one of affinityPVMInstance or affinityVolume to be specified; for policy &#39;anti-affinity&#39; requires one of antiAffinityPVMInstances or antiAffinityVolumes to be specified | [optional] 
**disk_type** | **str** | Type of Disk, required if affinityPolicy and volumePool not provided, otherwise ignored | [optional] 
**size** | **int** | Volume Size (GB) | 
**volume_pool** | **str** | Volume pool where the volume will be created; if provided then diskType and affinityPolicy values will be ignored | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VolumeReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wwn** | **str** | Volume world wide name | 
**boot_volume** | **bool** | Indicates if the volume is the server&#39;s boot volume | [optional] 
**disk_type** | **str** | Type of Disk | 
**href** | **str** | Link to Volume resource | 
**state** | **str** | Volume State | 
**volume_pool** | **str** | Volume pool, name of storage pool where the volume is located | [optional] 
**group_id** | **str** | Volume Group ID | [optional] 
**pvm_instance_ids** | **list[str]** | List of PCloud PVM Instance attached to the volume | [optional] 
**replication_status** | **str** | shows the replication status of a volume | [optional] 
**shareable** | **bool** | Indicates if the volume is shareable between VMs | 
**creation_date** | **datetime** | Creation Date | 
**last_update_date** | **datetime** | Last Update Date | 
**size** | **float** | Volume Size | 
**volume_type** | **str** | Volume type, name of storage template used to create the volume | [optional] 
**name** | **str** | Volume Name | 
**volume_id** | **str** | Volume ID | 
**bootable** | **bool** | Indicates if the volume is boot capable | 
**consistency_group_name** | **str** | Consistency Group Name if volume is a part of volume group | [optional] 
**delete_on_termination** | **bool** | Indicates if the volume should be deleted when the server terminates | [optional] 
**mirroring_state** | **str** | mirroring state for replication enabled volume | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



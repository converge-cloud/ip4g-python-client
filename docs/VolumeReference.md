# VolumeReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_volume** | **bool** | Indicates if the volume is the server&#39;s boot volume | [optional] 
**bootable** | **bool** | Indicates if the volume is boot capable | 
**consistency_group_name** | **str** | Consistency Group Name if volume is a part of volume group | [optional] 
**creation_date** | **datetime** | Creation Date | 
**delete_on_termination** | **bool** | Indicates if the volume should be deleted when the server terminates | [optional] 
**disk_type** | **str** | Type of Disk | 
**group_id** | **str** | Volume Group ID | [optional] 
**href** | **str** | Link to Volume resource | 
**io_throttle_rate** | **str** | IOps limit for the volume | [optional] 
**last_update_date** | **datetime** | Last Update Date | 
**mirroring_state** | **str** | mirroring state for replication enabled volume | [optional] 
**name** | **str** | Volume Name | 
**pvm_instance_ids** | **list[str]** | List of PCloud PVM Instance attached to the volume | [optional] 
**replication_status** | **str** | shows the replication status of a volume | [optional] 
**shareable** | **bool** | Indicates if the volume is shareable between VMs | 
**size** | **float** | Volume Size | 
**state** | **str** | Volume State | 
**volume_id** | **str** | Volume ID | 
**volume_pool** | **str** | Volume pool, name of storage pool where the volume is located | [optional] 
**volume_type** | **str** | Volume type, name of storage template used to create the volume | [optional] 
**wwn** | **str** | Volume world wide name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



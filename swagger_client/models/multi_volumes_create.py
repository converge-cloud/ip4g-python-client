# coding: utf-8

"""
    IBM Power Systems for Google Cloud API

    IBM Power Systems for Google Cloud API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: ip4g@convergetp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class MultiVolumesCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'shareable': 'bool',
        'affinity_volume': 'str',
        'anti_affinity_pvm_instances': 'list[str]',
        'anti_affinity_volumes': 'list[str]',
        'count': 'int',
        'name': 'str',
        'replication_enabled': 'bool',
        'affinity_pvm_instance': 'str',
        'affinity_policy': 'str',
        'disk_type': 'str',
        'size': 'int',
        'volume_pool': 'str'
    }

    attribute_map = {
        'shareable': 'shareable',
        'affinity_volume': 'affinityVolume',
        'anti_affinity_pvm_instances': 'antiAffinityPVMInstances',
        'anti_affinity_volumes': 'antiAffinityVolumes',
        'count': 'count',
        'name': 'name',
        'replication_enabled': 'replicationEnabled',
        'affinity_pvm_instance': 'affinityPVMInstance',
        'affinity_policy': 'affinityPolicy',
        'disk_type': 'diskType',
        'size': 'size',
        'volume_pool': 'volumePool'
    }

    def __init__(self, shareable=None, affinity_volume=None, anti_affinity_pvm_instances=None, anti_affinity_volumes=None, count=None, name=None, replication_enabled=None, affinity_pvm_instance=None, affinity_policy=None, disk_type=None, size=None, volume_pool=None, _configuration=None):  # noqa: E501
        """MultiVolumesCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._shareable = None
        self._affinity_volume = None
        self._anti_affinity_pvm_instances = None
        self._anti_affinity_volumes = None
        self._count = None
        self._name = None
        self._replication_enabled = None
        self._affinity_pvm_instance = None
        self._affinity_policy = None
        self._disk_type = None
        self._size = None
        self._volume_pool = None
        self.discriminator = None

        if shareable is not None:
            self.shareable = shareable
        if affinity_volume is not None:
            self.affinity_volume = affinity_volume
        if anti_affinity_pvm_instances is not None:
            self.anti_affinity_pvm_instances = anti_affinity_pvm_instances
        if anti_affinity_volumes is not None:
            self.anti_affinity_volumes = anti_affinity_volumes
        if count is not None:
            self.count = count
        self.name = name
        if replication_enabled is not None:
            self.replication_enabled = replication_enabled
        if affinity_pvm_instance is not None:
            self.affinity_pvm_instance = affinity_pvm_instance
        if affinity_policy is not None:
            self.affinity_policy = affinity_policy
        if disk_type is not None:
            self.disk_type = disk_type
        self.size = size
        if volume_pool is not None:
            self.volume_pool = volume_pool

    @property
    def shareable(self):
        """Gets the shareable of this MultiVolumesCreate.  # noqa: E501

        Indicates if the volume is shareable between VMs  # noqa: E501

        :return: The shareable of this MultiVolumesCreate.  # noqa: E501
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this MultiVolumesCreate.

        Indicates if the volume is shareable between VMs  # noqa: E501

        :param shareable: The shareable of this MultiVolumesCreate.  # noqa: E501
        :type: bool
        """

        self._shareable = shareable

    @property
    def affinity_volume(self):
        """Gets the affinity_volume of this MultiVolumesCreate.  # noqa: E501

        Volume (ID or Name) to base volume affinity policy against; required if requesting affinity and affinityPVMInstance is not provided  # noqa: E501

        :return: The affinity_volume of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._affinity_volume

    @affinity_volume.setter
    def affinity_volume(self, affinity_volume):
        """Sets the affinity_volume of this MultiVolumesCreate.

        Volume (ID or Name) to base volume affinity policy against; required if requesting affinity and affinityPVMInstance is not provided  # noqa: E501

        :param affinity_volume: The affinity_volume of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """

        self._affinity_volume = affinity_volume

    @property
    def anti_affinity_pvm_instances(self):
        """Gets the anti_affinity_pvm_instances of this MultiVolumesCreate.  # noqa: E501

        List of pvmInstances to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityVolumes is not provided  # noqa: E501

        :return: The anti_affinity_pvm_instances of this MultiVolumesCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._anti_affinity_pvm_instances

    @anti_affinity_pvm_instances.setter
    def anti_affinity_pvm_instances(self, anti_affinity_pvm_instances):
        """Sets the anti_affinity_pvm_instances of this MultiVolumesCreate.

        List of pvmInstances to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityVolumes is not provided  # noqa: E501

        :param anti_affinity_pvm_instances: The anti_affinity_pvm_instances of this MultiVolumesCreate.  # noqa: E501
        :type: list[str]
        """

        self._anti_affinity_pvm_instances = anti_affinity_pvm_instances

    @property
    def anti_affinity_volumes(self):
        """Gets the anti_affinity_volumes of this MultiVolumesCreate.  # noqa: E501

        List of volumes to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityPVMInstances is not provided  # noqa: E501

        :return: The anti_affinity_volumes of this MultiVolumesCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._anti_affinity_volumes

    @anti_affinity_volumes.setter
    def anti_affinity_volumes(self, anti_affinity_volumes):
        """Sets the anti_affinity_volumes of this MultiVolumesCreate.

        List of volumes to base volume anti-affinity policy against; required if requesting anti-affinity and antiAffinityPVMInstances is not provided  # noqa: E501

        :param anti_affinity_volumes: The anti_affinity_volumes of this MultiVolumesCreate.  # noqa: E501
        :type: list[str]
        """

        self._anti_affinity_volumes = anti_affinity_volumes

    @property
    def count(self):
        """Gets the count of this MultiVolumesCreate.  # noqa: E501

        Number of volumes to create  # noqa: E501

        :return: The count of this MultiVolumesCreate.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MultiVolumesCreate.

        Number of volumes to create  # noqa: E501

        :param count: The count of this MultiVolumesCreate.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def name(self):
        """Gets the name of this MultiVolumesCreate.  # noqa: E501

        Base name of the volume(s)  # noqa: E501

        :return: The name of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MultiVolumesCreate.

        Base name of the volume(s)  # noqa: E501

        :param name: The name of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def replication_enabled(self):
        """Gets the replication_enabled of this MultiVolumesCreate.  # noqa: E501

        Indicates if the volume should be replication enabled or not  # noqa: E501

        :return: The replication_enabled of this MultiVolumesCreate.  # noqa: E501
        :rtype: bool
        """
        return self._replication_enabled

    @replication_enabled.setter
    def replication_enabled(self, replication_enabled):
        """Sets the replication_enabled of this MultiVolumesCreate.

        Indicates if the volume should be replication enabled or not  # noqa: E501

        :param replication_enabled: The replication_enabled of this MultiVolumesCreate.  # noqa: E501
        :type: bool
        """

        self._replication_enabled = replication_enabled

    @property
    def affinity_pvm_instance(self):
        """Gets the affinity_pvm_instance of this MultiVolumesCreate.  # noqa: E501

        PVM Instance (ID or Name)to base volume affinity policy against; required if requesting affinity and affinityVolume is not provided  # noqa: E501

        :return: The affinity_pvm_instance of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._affinity_pvm_instance

    @affinity_pvm_instance.setter
    def affinity_pvm_instance(self, affinity_pvm_instance):
        """Sets the affinity_pvm_instance of this MultiVolumesCreate.

        PVM Instance (ID or Name)to base volume affinity policy against; required if requesting affinity and affinityVolume is not provided  # noqa: E501

        :param affinity_pvm_instance: The affinity_pvm_instance of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """

        self._affinity_pvm_instance = affinity_pvm_instance

    @property
    def affinity_policy(self):
        """Gets the affinity_policy of this MultiVolumesCreate.  # noqa: E501

        Affinity policy for data volume being created; ignored if volumePool provided; for policy 'affinity' requires one of affinityPVMInstance or affinityVolume to be specified; for policy 'anti-affinity' requires one of antiAffinityPVMInstances or antiAffinityVolumes to be specified  # noqa: E501

        :return: The affinity_policy of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._affinity_policy

    @affinity_policy.setter
    def affinity_policy(self, affinity_policy):
        """Sets the affinity_policy of this MultiVolumesCreate.

        Affinity policy for data volume being created; ignored if volumePool provided; for policy 'affinity' requires one of affinityPVMInstance or affinityVolume to be specified; for policy 'anti-affinity' requires one of antiAffinityPVMInstances or antiAffinityVolumes to be specified  # noqa: E501

        :param affinity_policy: The affinity_policy of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["affinity", "anti-affinity"]  # noqa: E501
        if (self._configuration.client_side_validation and
                affinity_policy not in allowed_values):
            raise ValueError(
                "Invalid value for `affinity_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(affinity_policy, allowed_values)
            )

        self._affinity_policy = affinity_policy

    @property
    def disk_type(self):
        """Gets the disk_type of this MultiVolumesCreate.  # noqa: E501

        Type of Disk, required if affinityPolicy and volumePool not provided, otherwise ignored  # noqa: E501

        :return: The disk_type of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this MultiVolumesCreate.

        Type of Disk, required if affinityPolicy and volumePool not provided, otherwise ignored  # noqa: E501

        :param disk_type: The disk_type of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """

        self._disk_type = disk_type

    @property
    def size(self):
        """Gets the size of this MultiVolumesCreate.  # noqa: E501

        Volume Size (GB)  # noqa: E501

        :return: The size of this MultiVolumesCreate.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MultiVolumesCreate.

        Volume Size (GB)  # noqa: E501

        :param size: The size of this MultiVolumesCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def volume_pool(self):
        """Gets the volume_pool of this MultiVolumesCreate.  # noqa: E501

        Volume pool where the volume will be created; if provided then diskType and affinityPolicy values will be ignored  # noqa: E501

        :return: The volume_pool of this MultiVolumesCreate.  # noqa: E501
        :rtype: str
        """
        return self._volume_pool

    @volume_pool.setter
    def volume_pool(self, volume_pool):
        """Sets the volume_pool of this MultiVolumesCreate.

        Volume pool where the volume will be created; if provided then diskType and affinityPolicy values will be ignored  # noqa: E501

        :param volume_pool: The volume_pool of this MultiVolumesCreate.  # noqa: E501
        :type: str
        """

        self._volume_pool = volume_pool

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MultiVolumesCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiVolumesCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiVolumesCreate):
            return True

        return self.to_dict() != other.to_dict()

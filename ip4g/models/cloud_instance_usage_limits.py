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

from ip4g.configuration import Configuration


class CloudInstanceUsageLimits(object):
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
        'peering_bandwidth': 'int',
        'proc_units': 'float',
        'processors': 'float',
        'storage_ssd': 'float',
        'storage_standard': 'float',
        'storage': 'float',
        'instance_memory': 'float',
        'instance_proc_units': 'float',
        'instances': 'float',
        'memory': 'float',
        'peering_networks': 'int'
    }

    attribute_map = {
        'peering_bandwidth': 'peeringBandwidth',
        'proc_units': 'procUnits',
        'processors': 'processors',
        'storage_ssd': 'storageSSD',
        'storage_standard': 'storageStandard',
        'storage': 'storage',
        'instance_memory': 'instanceMemory',
        'instance_proc_units': 'instanceProcUnits',
        'instances': 'instances',
        'memory': 'memory',
        'peering_networks': 'peeringNetworks'
    }

    def __init__(self, peering_bandwidth=None, proc_units=None, processors=None, storage_ssd=None, storage_standard=None, storage=None, instance_memory=None, instance_proc_units=None, instances=None, memory=None, peering_networks=None, _configuration=None):  # noqa: E501
        """CloudInstanceUsageLimits - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._peering_bandwidth = None
        self._proc_units = None
        self._processors = None
        self._storage_ssd = None
        self._storage_standard = None
        self._storage = None
        self._instance_memory = None
        self._instance_proc_units = None
        self._instances = None
        self._memory = None
        self._peering_networks = None
        self.discriminator = None

        if peering_bandwidth is not None:
            self.peering_bandwidth = peering_bandwidth
        self.proc_units = proc_units
        self.processors = processors
        if storage_ssd is not None:
            self.storage_ssd = storage_ssd
        if storage_standard is not None:
            self.storage_standard = storage_standard
        self.storage = storage
        if instance_memory is not None:
            self.instance_memory = instance_memory
        if instance_proc_units is not None:
            self.instance_proc_units = instance_proc_units
        self.instances = instances
        self.memory = memory
        if peering_networks is not None:
            self.peering_networks = peering_networks

    @property
    def peering_bandwidth(self):
        """Gets the peering_bandwidth of this CloudInstanceUsageLimits.  # noqa: E501

        Maximum network bandwidth to GCP Mbps  # noqa: E501

        :return: The peering_bandwidth of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: int
        """
        return self._peering_bandwidth

    @peering_bandwidth.setter
    def peering_bandwidth(self, peering_bandwidth):
        """Sets the peering_bandwidth of this CloudInstanceUsageLimits.

        Maximum network bandwidth to GCP Mbps  # noqa: E501

        :param peering_bandwidth: The peering_bandwidth of this CloudInstanceUsageLimits.  # noqa: E501
        :type: int
        """

        self._peering_bandwidth = peering_bandwidth

    @property
    def proc_units(self):
        """Gets the proc_units of this CloudInstanceUsageLimits.  # noqa: E501

        Number of processor units allowed  # noqa: E501

        :return: The proc_units of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._proc_units

    @proc_units.setter
    def proc_units(self, proc_units):
        """Sets the proc_units of this CloudInstanceUsageLimits.

        Number of processor units allowed  # noqa: E501

        :param proc_units: The proc_units of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and proc_units is None:
            raise ValueError("Invalid value for `proc_units`, must not be `None`")  # noqa: E501

        self._proc_units = proc_units

    @property
    def processors(self):
        """Gets the processors of this CloudInstanceUsageLimits.  # noqa: E501

        Number of processors allowed  # noqa: E501

        :return: The processors of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this CloudInstanceUsageLimits.

        Number of processors allowed  # noqa: E501

        :param processors: The processors of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and processors is None:
            raise ValueError("Invalid value for `processors`, must not be `None`")  # noqa: E501

        self._processors = processors

    @property
    def storage_ssd(self):
        """Gets the storage_ssd of this CloudInstanceUsageLimits.  # noqa: E501

        Amount of SSD storage allowed (TB)  # noqa: E501

        :return: The storage_ssd of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._storage_ssd

    @storage_ssd.setter
    def storage_ssd(self, storage_ssd):
        """Sets the storage_ssd of this CloudInstanceUsageLimits.

        Amount of SSD storage allowed (TB)  # noqa: E501

        :param storage_ssd: The storage_ssd of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """

        self._storage_ssd = storage_ssd

    @property
    def storage_standard(self):
        """Gets the storage_standard of this CloudInstanceUsageLimits.  # noqa: E501

        Amount of standard (HDD) storage allowed (TB)  # noqa: E501

        :return: The storage_standard of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._storage_standard

    @storage_standard.setter
    def storage_standard(self, storage_standard):
        """Sets the storage_standard of this CloudInstanceUsageLimits.

        Amount of standard (HDD) storage allowed (TB)  # noqa: E501

        :param storage_standard: The storage_standard of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """

        self._storage_standard = storage_standard

    @property
    def storage(self):
        """Gets the storage of this CloudInstanceUsageLimits.  # noqa: E501

        Amount of storage allowed (TB)  # noqa: E501

        :return: The storage of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CloudInstanceUsageLimits.

        Amount of storage allowed (TB)  # noqa: E501

        :param storage: The storage of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and storage is None:
            raise ValueError("Invalid value for `storage`, must not be `None`")  # noqa: E501

        self._storage = storage

    @property
    def instance_memory(self):
        """Gets the instance_memory of this CloudInstanceUsageLimits.  # noqa: E501

        Maximum memory (in GB) per PVMInstance  # noqa: E501

        :return: The instance_memory of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._instance_memory

    @instance_memory.setter
    def instance_memory(self, instance_memory):
        """Sets the instance_memory of this CloudInstanceUsageLimits.

        Maximum memory (in GB) per PVMInstance  # noqa: E501

        :param instance_memory: The instance_memory of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """

        self._instance_memory = instance_memory

    @property
    def instance_proc_units(self):
        """Gets the instance_proc_units of this CloudInstanceUsageLimits.  # noqa: E501

        Maximum proc units per PVMInstance  # noqa: E501

        :return: The instance_proc_units of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._instance_proc_units

    @instance_proc_units.setter
    def instance_proc_units(self, instance_proc_units):
        """Sets the instance_proc_units of this CloudInstanceUsageLimits.

        Maximum proc units per PVMInstance  # noqa: E501

        :param instance_proc_units: The instance_proc_units of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """

        self._instance_proc_units = instance_proc_units

    @property
    def instances(self):
        """Gets the instances of this CloudInstanceUsageLimits.  # noqa: E501

        Number of power instances allowed  # noqa: E501

        :return: The instances of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this CloudInstanceUsageLimits.

        Number of power instances allowed  # noqa: E501

        :param instances: The instances of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and instances is None:
            raise ValueError("Invalid value for `instances`, must not be `None`")  # noqa: E501

        self._instances = instances

    @property
    def memory(self):
        """Gets the memory of this CloudInstanceUsageLimits.  # noqa: E501

        Amount of memory allowed  # noqa: E501

        :return: The memory of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this CloudInstanceUsageLimits.

        Amount of memory allowed  # noqa: E501

        :param memory: The memory of this CloudInstanceUsageLimits.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def peering_networks(self):
        """Gets the peering_networks of this CloudInstanceUsageLimits.  # noqa: E501

        Amount of peering networks allowed  # noqa: E501

        :return: The peering_networks of this CloudInstanceUsageLimits.  # noqa: E501
        :rtype: int
        """
        return self._peering_networks

    @peering_networks.setter
    def peering_networks(self, peering_networks):
        """Sets the peering_networks of this CloudInstanceUsageLimits.

        Amount of peering networks allowed  # noqa: E501

        :param peering_networks: The peering_networks of this CloudInstanceUsageLimits.  # noqa: E501
        :type: int
        """

        self._peering_networks = peering_networks

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
        if issubclass(CloudInstanceUsageLimits, dict):
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
        if not isinstance(other, CloudInstanceUsageLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudInstanceUsageLimits):
            return True

        return self.to_dict() != other.to_dict()
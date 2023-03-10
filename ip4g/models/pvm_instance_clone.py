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


class PVMInstanceClone(object):
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
        'volume_ids': 'list[str]',
        'key_pair_name': 'str',
        'memory': 'float',
        'name': 'str',
        'networks': 'list[PVMInstanceAddNetwork]',
        'proc_type': 'str',
        'processors': 'float',
        'software_licenses': 'SoftwareLicenses'
    }

    attribute_map = {
        'volume_ids': 'volumeIDs',
        'key_pair_name': 'keyPairName',
        'memory': 'memory',
        'name': 'name',
        'networks': 'networks',
        'proc_type': 'procType',
        'processors': 'processors',
        'software_licenses': 'softwareLicenses'
    }

    def __init__(self, volume_ids=None, key_pair_name=None, memory=None, name=None, networks=None, proc_type='dedicated', processors=None, software_licenses=None, _configuration=None):  # noqa: E501
        """PVMInstanceClone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._volume_ids = None
        self._key_pair_name = None
        self._memory = None
        self._name = None
        self._networks = None
        self._proc_type = None
        self._processors = None
        self._software_licenses = None
        self.discriminator = None

        if volume_ids is not None:
            self.volume_ids = volume_ids
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if memory is not None:
            self.memory = memory
        self.name = name
        self.networks = networks
        if proc_type is not None:
            self.proc_type = proc_type
        if processors is not None:
            self.processors = processors
        if software_licenses is not None:
            self.software_licenses = software_licenses

    @property
    def volume_ids(self):
        """Gets the volume_ids of this PVMInstanceClone.  # noqa: E501

        List of volume IDs  # noqa: E501

        :return: The volume_ids of this PVMInstanceClone.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this PVMInstanceClone.

        List of volume IDs  # noqa: E501

        :param volume_ids: The volume_ids of this PVMInstanceClone.  # noqa: E501
        :type: list[str]
        """

        self._volume_ids = volume_ids

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this PVMInstanceClone.  # noqa: E501

        The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant's list of keys)  # noqa: E501

        :return: The key_pair_name of this PVMInstanceClone.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this PVMInstanceClone.

        The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant's list of keys)  # noqa: E501

        :param key_pair_name: The key_pair_name of this PVMInstanceClone.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def memory(self):
        """Gets the memory of this PVMInstanceClone.  # noqa: E501

        Amount of memory allocated (in GB)  # noqa: E501

        :return: The memory of this PVMInstanceClone.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this PVMInstanceClone.

        Amount of memory allocated (in GB)  # noqa: E501

        :param memory: The memory of this PVMInstanceClone.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def name(self):
        """Gets the name of this PVMInstanceClone.  # noqa: E501

        Name of the server to create  # noqa: E501

        :return: The name of this PVMInstanceClone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PVMInstanceClone.

        Name of the server to create  # noqa: E501

        :param name: The name of this PVMInstanceClone.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def networks(self):
        """Gets the networks of this PVMInstanceClone.  # noqa: E501

        The pvm instance networks information  # noqa: E501

        :return: The networks of this PVMInstanceClone.  # noqa: E501
        :rtype: list[PVMInstanceAddNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this PVMInstanceClone.

        The pvm instance networks information  # noqa: E501

        :param networks: The networks of this PVMInstanceClone.  # noqa: E501
        :type: list[PVMInstanceAddNetwork]
        """
        if self._configuration.client_side_validation and networks is None:
            raise ValueError("Invalid value for `networks`, must not be `None`")  # noqa: E501

        self._networks = networks

    @property
    def proc_type(self):
        """Gets the proc_type of this PVMInstanceClone.  # noqa: E501

        Processor type (dedicated, shared, capped)  # noqa: E501

        :return: The proc_type of this PVMInstanceClone.  # noqa: E501
        :rtype: str
        """
        return self._proc_type

    @proc_type.setter
    def proc_type(self, proc_type):
        """Sets the proc_type of this PVMInstanceClone.

        Processor type (dedicated, shared, capped)  # noqa: E501

        :param proc_type: The proc_type of this PVMInstanceClone.  # noqa: E501
        :type: str
        """
        allowed_values = ["dedicated", "shared", "capped"]  # noqa: E501
        if (self._configuration.client_side_validation and
                proc_type not in allowed_values):
            raise ValueError(
                "Invalid value for `proc_type` ({0}), must be one of {1}"  # noqa: E501
                .format(proc_type, allowed_values)
            )

        self._proc_type = proc_type

    @property
    def processors(self):
        """Gets the processors of this PVMInstanceClone.  # noqa: E501

        Number of processors allocated  # noqa: E501

        :return: The processors of this PVMInstanceClone.  # noqa: E501
        :rtype: float
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this PVMInstanceClone.

        Number of processors allocated  # noqa: E501

        :param processors: The processors of this PVMInstanceClone.  # noqa: E501
        :type: float
        """

        self._processors = processors

    @property
    def software_licenses(self):
        """Gets the software_licenses of this PVMInstanceClone.  # noqa: E501

        The pvm instance Software Licenses  # noqa: E501

        :return: The software_licenses of this PVMInstanceClone.  # noqa: E501
        :rtype: SoftwareLicenses
        """
        return self._software_licenses

    @software_licenses.setter
    def software_licenses(self, software_licenses):
        """Sets the software_licenses of this PVMInstanceClone.

        The pvm instance Software Licenses  # noqa: E501

        :param software_licenses: The software_licenses of this PVMInstanceClone.  # noqa: E501
        :type: SoftwareLicenses
        """

        self._software_licenses = software_licenses

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
        if issubclass(PVMInstanceClone, dict):
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
        if not isinstance(other, PVMInstanceClone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PVMInstanceClone):
            return True

        return self.to_dict() != other.to_dict()

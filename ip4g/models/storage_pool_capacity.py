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


class StoragePoolCapacity(object):
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
        'pool_name': 'str',
        'storage_type': 'str',
        'total_capacity': 'int',
        'max_allocation_size': 'int'
    }

    attribute_map = {
        'pool_name': 'poolName',
        'storage_type': 'storageType',
        'total_capacity': 'totalCapacity',
        'max_allocation_size': 'maxAllocationSize'
    }

    def __init__(self, pool_name=None, storage_type=None, total_capacity=None, max_allocation_size=None, _configuration=None):  # noqa: E501
        """StoragePoolCapacity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pool_name = None
        self._storage_type = None
        self._total_capacity = None
        self._max_allocation_size = None
        self.discriminator = None

        if pool_name is not None:
            self.pool_name = pool_name
        if storage_type is not None:
            self.storage_type = storage_type
        if total_capacity is not None:
            self.total_capacity = total_capacity
        self.max_allocation_size = max_allocation_size

    @property
    def pool_name(self):
        """Gets the pool_name of this StoragePoolCapacity.  # noqa: E501

        Pool name  # noqa: E501

        :return: The pool_name of this StoragePoolCapacity.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this StoragePoolCapacity.

        Pool name  # noqa: E501

        :param pool_name: The pool_name of this StoragePoolCapacity.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

    @property
    def storage_type(self):
        """Gets the storage_type of this StoragePoolCapacity.  # noqa: E501

        Storage type of the storage pool  # noqa: E501

        :return: The storage_type of this StoragePoolCapacity.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this StoragePoolCapacity.

        Storage type of the storage pool  # noqa: E501

        :param storage_type: The storage_type of this StoragePoolCapacity.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def total_capacity(self):
        """Gets the total_capacity of this StoragePoolCapacity.  # noqa: E501

        Total pool capacity (GB)  # noqa: E501

        :return: The total_capacity of this StoragePoolCapacity.  # noqa: E501
        :rtype: int
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this StoragePoolCapacity.

        Total pool capacity (GB)  # noqa: E501

        :param total_capacity: The total_capacity of this StoragePoolCapacity.  # noqa: E501
        :type: int
        """

        self._total_capacity = total_capacity

    @property
    def max_allocation_size(self):
        """Gets the max_allocation_size of this StoragePoolCapacity.  # noqa: E501

        Maximum allocation storage size (GB)  # noqa: E501

        :return: The max_allocation_size of this StoragePoolCapacity.  # noqa: E501
        :rtype: int
        """
        return self._max_allocation_size

    @max_allocation_size.setter
    def max_allocation_size(self, max_allocation_size):
        """Sets the max_allocation_size of this StoragePoolCapacity.

        Maximum allocation storage size (GB)  # noqa: E501

        :param max_allocation_size: The max_allocation_size of this StoragePoolCapacity.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and max_allocation_size is None:
            raise ValueError("Invalid value for `max_allocation_size`, must not be `None`")  # noqa: E501

        self._max_allocation_size = max_allocation_size

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
        if issubclass(StoragePoolCapacity, dict):
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
        if not isinstance(other, StoragePoolCapacity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoragePoolCapacity):
            return True

        return self.to_dict() != other.to_dict()

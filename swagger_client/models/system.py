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


class System(object):
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
        'memory': 'int',
        'cores': 'float',
        'id': 'int'
    }

    attribute_map = {
        'memory': 'memory',
        'cores': 'cores',
        'id': 'id'
    }

    def __init__(self, memory=None, cores=None, id=None, _configuration=None):  # noqa: E501
        """System - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._memory = None
        self._cores = None
        self._id = None
        self.discriminator = None

        self.memory = memory
        self.cores = cores
        if id is not None:
            self.id = id

    @property
    def memory(self):
        """Gets the memory of this System.  # noqa: E501

        The host available RAM memory in GiB  # noqa: E501

        :return: The memory of this System.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this System.

        The host available RAM memory in GiB  # noqa: E501

        :param memory: The memory of this System.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def cores(self):
        """Gets the cores of this System.  # noqa: E501

        The host available Processor units  # noqa: E501

        :return: The cores of this System.  # noqa: E501
        :rtype: float
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this System.

        The host available Processor units  # noqa: E501

        :param cores: The cores of this System.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and cores is None:
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501

        self._cores = cores

    @property
    def id(self):
        """Gets the id of this System.  # noqa: E501

        The host identifier  # noqa: E501

        :return: The id of this System.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this System.

        The host identifier  # noqa: E501

        :param id: The id of this System.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(System, dict):
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
        if not isinstance(other, System):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, System):
            return True

        return self.to_dict() != other.to_dict()

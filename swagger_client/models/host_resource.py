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


class HostResource(object):
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
        'free': 'float',
        'total': 'float',
        'used': 'float'
    }

    attribute_map = {
        'free': 'free',
        'total': 'total',
        'used': 'used'
    }

    def __init__(self, free=None, total=None, used=None, _configuration=None):  # noqa: E501
        """HostResource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._free = None
        self._total = None
        self._used = None
        self.discriminator = None

        self.free = free
        self.total = total
        self.used = used

    @property
    def free(self):
        """Gets the free of this HostResource.  # noqa: E501

        Free  # noqa: E501

        :return: The free of this HostResource.  # noqa: E501
        :rtype: float
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this HostResource.

        Free  # noqa: E501

        :param free: The free of this HostResource.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and free is None:
            raise ValueError("Invalid value for `free`, must not be `None`")  # noqa: E501

        self._free = free

    @property
    def total(self):
        """Gets the total of this HostResource.  # noqa: E501

        Total  # noqa: E501

        :return: The total of this HostResource.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this HostResource.

        Total  # noqa: E501

        :param total: The total of this HostResource.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def used(self):
        """Gets the used of this HostResource.  # noqa: E501

        Used  # noqa: E501

        :return: The used of this HostResource.  # noqa: E501
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this HostResource.

        Used  # noqa: E501

        :param used: The used of this HostResource.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and used is None:
            raise ValueError("Invalid value for `used`, must not be `None`")  # noqa: E501

        self._used = used

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
        if issubclass(HostResource, dict):
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
        if not isinstance(other, HostResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostResource):
            return True

        return self.to_dict() != other.to_dict()

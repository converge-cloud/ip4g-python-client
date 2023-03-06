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


class NetworkPorts(object):
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
        'ports': 'list[NetworkPort]'
    }

    attribute_map = {
        'ports': 'ports'
    }

    def __init__(self, ports=None, _configuration=None):  # noqa: E501
        """NetworkPorts - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ports = None
        self.discriminator = None

        self.ports = ports

    @property
    def ports(self):
        """Gets the ports of this NetworkPorts.  # noqa: E501

        Network Ports  # noqa: E501

        :return: The ports of this NetworkPorts.  # noqa: E501
        :rtype: list[NetworkPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NetworkPorts.

        Network Ports  # noqa: E501

        :param ports: The ports of this NetworkPorts.  # noqa: E501
        :type: list[NetworkPort]
        """
        if self._configuration.client_side_validation and ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports

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
        if issubclass(NetworkPorts, dict):
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
        if not isinstance(other, NetworkPorts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkPorts):
            return True

        return self.to_dict() != other.to_dict()

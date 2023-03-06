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


class PVMInstanceConsole(object):
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
        'console_url': 'str'
    }

    attribute_map = {
        'console_url': 'consoleURL'
    }

    def __init__(self, console_url=None, _configuration=None):  # noqa: E501
        """PVMInstanceConsole - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._console_url = None
        self.discriminator = None

        self.console_url = console_url

    @property
    def console_url(self):
        """Gets the console_url of this PVMInstanceConsole.  # noqa: E501

        The URL to the noVNC console for the PVM Instance  # noqa: E501

        :return: The console_url of this PVMInstanceConsole.  # noqa: E501
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this PVMInstanceConsole.

        The URL to the noVNC console for the PVM Instance  # noqa: E501

        :param console_url: The console_url of this PVMInstanceConsole.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and console_url is None:
            raise ValueError("Invalid value for `console_url`, must not be `None`")  # noqa: E501

        self._console_url = console_url

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
        if issubclass(PVMInstanceConsole, dict):
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
        if not isinstance(other, PVMInstanceConsole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PVMInstanceConsole):
            return True

        return self.to_dict() != other.to_dict()

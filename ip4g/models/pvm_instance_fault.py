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


class PVMInstanceFault(object):
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
        'message': 'str',
        'code': 'float',
        'created': 'datetime',
        'details': 'str'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'created': 'created',
        'details': 'details'
    }

    def __init__(self, message=None, code=None, created=None, details=None, _configuration=None):  # noqa: E501
        """PVMInstanceFault - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._code = None
        self._created = None
        self._details = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if created is not None:
            self.created = created
        if details is not None:
            self.details = details

    @property
    def message(self):
        """Gets the message of this PVMInstanceFault.  # noqa: E501

        The fault message of the server, if any  # noqa: E501

        :return: The message of this PVMInstanceFault.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PVMInstanceFault.

        The fault message of the server, if any  # noqa: E501

        :param message: The message of this PVMInstanceFault.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this PVMInstanceFault.  # noqa: E501

        The fault status of the server, if any  # noqa: E501

        :return: The code of this PVMInstanceFault.  # noqa: E501
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PVMInstanceFault.

        The fault status of the server, if any  # noqa: E501

        :param code: The code of this PVMInstanceFault.  # noqa: E501
        :type: float
        """

        self._code = code

    @property
    def created(self):
        """Gets the created of this PVMInstanceFault.  # noqa: E501

        The date and time the fault occurred  # noqa: E501

        :return: The created of this PVMInstanceFault.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PVMInstanceFault.

        The date and time the fault occurred  # noqa: E501

        :param created: The created of this PVMInstanceFault.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def details(self):
        """Gets the details of this PVMInstanceFault.  # noqa: E501

        The fault details of the server, if any  # noqa: E501

        :return: The details of this PVMInstanceFault.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PVMInstanceFault.

        The fault details of the server, if any  # noqa: E501

        :param details: The details of this PVMInstanceFault.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(PVMInstanceFault, dict):
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
        if not isinstance(other, PVMInstanceFault):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PVMInstanceFault):
            return True

        return self.to_dict() != other.to_dict()
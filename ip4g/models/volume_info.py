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


class VolumeInfo(object):
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
        'name': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'volume_id': 'volumeID'
    }

    def __init__(self, name=None, volume_id=None, _configuration=None):  # noqa: E501
        """VolumeInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._volume_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def name(self):
        """Gets the name of this VolumeInfo.  # noqa: E501

        Name of the volume  # noqa: E501

        :return: The name of this VolumeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeInfo.

        Name of the volume  # noqa: E501

        :param name: The name of this VolumeInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeInfo.  # noqa: E501

        ID of the volume  # noqa: E501

        :return: The volume_id of this VolumeInfo.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeInfo.

        ID of the volume  # noqa: E501

        :param volume_id: The volume_id of this VolumeInfo.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

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
        if issubclass(VolumeInfo, dict):
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
        if not isinstance(other, VolumeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeInfo):
            return True

        return self.to_dict() != other.to_dict()

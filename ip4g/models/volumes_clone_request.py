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


class VolumesCloneRequest(object):
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
        'display_name': 'str',
        'volume_ids': 'list[str]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'volume_ids': 'volumeIDs'
    }

    def __init__(self, display_name=None, volume_ids=None, _configuration=None):  # noqa: E501
        """VolumesCloneRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._volume_ids = None
        self.discriminator = None

        self.display_name = display_name
        self.volume_ids = volume_ids

    @property
    def display_name(self):
        """Gets the display_name of this VolumesCloneRequest.  # noqa: E501

        Display name for the new cloned volumes. Cloned Volume names will be prefixed with 'clone-'. If multiple volumes cloned they will be suffix with a '-' and an incremental number starting with 1.   Example volume names using displayName=\"volume-abcdef\"     single volume clone will be named \"clone-volume-abcdef\"     multi volume clone will be named \"clone-volume-abcdef-1\", \"clone-volume-abcdef-2\", ...   # noqa: E501

        :return: The display_name of this VolumesCloneRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this VolumesCloneRequest.

        Display name for the new cloned volumes. Cloned Volume names will be prefixed with 'clone-'. If multiple volumes cloned they will be suffix with a '-' and an incremental number starting with 1.   Example volume names using displayName=\"volume-abcdef\"     single volume clone will be named \"clone-volume-abcdef\"     multi volume clone will be named \"clone-volume-abcdef-1\", \"clone-volume-abcdef-2\", ...   # noqa: E501

        :param display_name: The display_name of this VolumesCloneRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def volume_ids(self):
        """Gets the volume_ids of this VolumesCloneRequest.  # noqa: E501

        List of volumes to be cloned  # noqa: E501

        :return: The volume_ids of this VolumesCloneRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this VolumesCloneRequest.

        List of volumes to be cloned  # noqa: E501

        :param volume_ids: The volume_ids of this VolumesCloneRequest.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and volume_ids is None:
            raise ValueError("Invalid value for `volume_ids`, must not be `None`")  # noqa: E501

        self._volume_ids = volume_ids

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
        if issubclass(VolumesCloneRequest, dict):
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
        if not isinstance(other, VolumesCloneRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumesCloneRequest):
            return True

        return self.to_dict() != other.to_dict()

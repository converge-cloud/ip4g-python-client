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


class VolumesCloneResponse(object):
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
        'additional_properties': 'str',
        'cloned_volumes': 'object'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'cloned_volumes': 'clonedVolumes'
    }

    def __init__(self, additional_properties=None, cloned_volumes=None, _configuration=None):  # noqa: E501
        """VolumesCloneResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_properties = None
        self._cloned_volumes = None
        self.discriminator = None

        if additional_properties is not None:
            self.additional_properties = additional_properties
        if cloned_volumes is not None:
            self.cloned_volumes = cloned_volumes

    @property
    def additional_properties(self):
        """Gets the additional_properties of this VolumesCloneResponse.  # noqa: E501

        ID of the new cloned volume  # noqa: E501

        :return: The additional_properties of this VolumesCloneResponse.  # noqa: E501
        :rtype: str
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """Sets the additional_properties of this VolumesCloneResponse.

        ID of the new cloned volume  # noqa: E501

        :param additional_properties: The additional_properties of this VolumesCloneResponse.  # noqa: E501
        :type: str
        """

        self._additional_properties = additional_properties

    @property
    def cloned_volumes(self):
        """Gets the cloned_volumes of this VolumesCloneResponse.  # noqa: E501

        A map of volume IDs to cloned volume IDs  # noqa: E501

        :return: The cloned_volumes of this VolumesCloneResponse.  # noqa: E501
        :rtype: object
        """
        return self._cloned_volumes

    @cloned_volumes.setter
    def cloned_volumes(self, cloned_volumes):
        """Sets the cloned_volumes of this VolumesCloneResponse.

        A map of volume IDs to cloned volume IDs  # noqa: E501

        :param cloned_volumes: The cloned_volumes of this VolumesCloneResponse.  # noqa: E501
        :type: object
        """

        self._cloned_volumes = cloned_volumes

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
        if issubclass(VolumesCloneResponse, dict):
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
        if not isinstance(other, VolumesCloneResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumesCloneResponse):
            return True

        return self.to_dict() != other.to_dict()

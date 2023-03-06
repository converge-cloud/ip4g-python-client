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


class SAPProfileReference(object):
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
        'href': 'str',
        'profile_id': 'str'
    }

    attribute_map = {
        'href': 'href',
        'profile_id': 'profileID'
    }

    def __init__(self, href=None, profile_id=None, _configuration=None):  # noqa: E501
        """SAPProfileReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._profile_id = None
        self.discriminator = None

        self.href = href
        self.profile_id = profile_id

    @property
    def href(self):
        """Gets the href of this SAPProfileReference.  # noqa: E501

        Link to SAP profile resource  # noqa: E501

        :return: The href of this SAPProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SAPProfileReference.

        Link to SAP profile resource  # noqa: E501

        :param href: The href of this SAPProfileReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def profile_id(self):
        """Gets the profile_id of this SAPProfileReference.  # noqa: E501

        SAP Profile ID  # noqa: E501

        :return: The profile_id of this SAPProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this SAPProfileReference.

        SAP Profile ID  # noqa: E501

        :param profile_id: The profile_id of this SAPProfileReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and profile_id is None:
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

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
        if issubclass(SAPProfileReference, dict):
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
        if not isinstance(other, SAPProfileReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SAPProfileReference):
            return True

        return self.to_dict() != other.to_dict()

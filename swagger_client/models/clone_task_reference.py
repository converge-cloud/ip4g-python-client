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


class CloneTaskReference(object):
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
        'clone_task_id': 'str'
    }

    attribute_map = {
        'href': 'href',
        'clone_task_id': 'cloneTaskID'
    }

    def __init__(self, href=None, clone_task_id=None, _configuration=None):  # noqa: E501
        """CloneTaskReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._clone_task_id = None
        self.discriminator = None

        self.href = href
        self.clone_task_id = clone_task_id

    @property
    def href(self):
        """Gets the href of this CloneTaskReference.  # noqa: E501

        Link to PowerVC clone task resource  # noqa: E501

        :return: The href of this CloneTaskReference.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CloneTaskReference.

        Link to PowerVC clone task resource  # noqa: E501

        :param href: The href of this CloneTaskReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def clone_task_id(self):
        """Gets the clone_task_id of this CloneTaskReference.  # noqa: E501

        ID of a long running PowerVC clone task  # noqa: E501

        :return: The clone_task_id of this CloneTaskReference.  # noqa: E501
        :rtype: str
        """
        return self._clone_task_id

    @clone_task_id.setter
    def clone_task_id(self, clone_task_id):
        """Sets the clone_task_id of this CloneTaskReference.

        ID of a long running PowerVC clone task  # noqa: E501

        :param clone_task_id: The clone_task_id of this CloneTaskReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and clone_task_id is None:
            raise ValueError("Invalid value for `clone_task_id`, must not be `None`")  # noqa: E501

        self._clone_task_id = clone_task_id

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
        if issubclass(CloneTaskReference, dict):
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
        if not isinstance(other, CloneTaskReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloneTaskReference):
            return True

        return self.to_dict() != other.to_dict()

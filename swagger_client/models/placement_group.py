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


class PlacementGroup(object):
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
        'policy': 'str',
        'id': 'str',
        'members': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'policy': 'policy',
        'id': 'id',
        'members': 'members'
    }

    def __init__(self, name=None, policy=None, id=None, members=None, _configuration=None):  # noqa: E501
        """PlacementGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._policy = None
        self._id = None
        self._members = None
        self.discriminator = None

        self.name = name
        self.policy = policy
        self.id = id
        self.members = members

    @property
    def name(self):
        """Gets the name of this PlacementGroup.  # noqa: E501

        The name of the Placement Group  # noqa: E501

        :return: The name of this PlacementGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlacementGroup.

        The name of the Placement Group  # noqa: E501

        :param name: The name of this PlacementGroup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this PlacementGroup.  # noqa: E501

        The Placement Group Policy  # noqa: E501

        :return: The policy of this PlacementGroup.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PlacementGroup.

        The Placement Group Policy  # noqa: E501

        :param policy: The policy of this PlacementGroup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501
        allowed_values = ["affinity", "anti-affinity"]  # noqa: E501
        if (self._configuration.client_side_validation and
                policy not in allowed_values):
            raise ValueError(
                "Invalid value for `policy` ({0}), must be one of {1}"  # noqa: E501
                .format(policy, allowed_values)
            )

        self._policy = policy

    @property
    def id(self):
        """Gets the id of this PlacementGroup.  # noqa: E501

        The id of the Placement Group  # noqa: E501

        :return: The id of this PlacementGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlacementGroup.

        The id of the Placement Group  # noqa: E501

        :param id: The id of this PlacementGroup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def members(self):
        """Gets the members of this PlacementGroup.  # noqa: E501

        The List of PVM Instance IDs associated with the Placement Group  # noqa: E501

        :return: The members of this PlacementGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this PlacementGroup.

        The List of PVM Instance IDs associated with the Placement Group  # noqa: E501

        :param members: The members of this PlacementGroup.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

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
        if issubclass(PlacementGroup, dict):
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
        if not isinstance(other, PlacementGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlacementGroup):
            return True

        return self.to_dict() != other.to_dict()

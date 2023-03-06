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


class Principal(object):
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
        'credential_type': 'str',
        'crn': 'str',
        'region': 'str',
        'resource_group_crn': 'str',
        'token': 'Token',
        'user_access': 'UserAccess',
        'user_email': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'credential_type': 'credentialType',
        'crn': 'crn',
        'region': 'region',
        'resource_group_crn': 'resourceGroupCRN',
        'token': 'token',
        'user_access': 'userAccess',
        'user_email': 'userEmail',
        'user_id': 'userID'
    }

    def __init__(self, credential_type=None, crn=None, region=None, resource_group_crn=None, token=None, user_access=None, user_email=None, user_id=None, _configuration=None):  # noqa: E501
        """Principal - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._credential_type = None
        self._crn = None
        self._region = None
        self._resource_group_crn = None
        self._token = None
        self._user_access = None
        self._user_email = None
        self._user_id = None
        self.discriminator = None

        if credential_type is not None:
            self.credential_type = credential_type
        if crn is not None:
            self.crn = crn
        if region is not None:
            self.region = region
        if resource_group_crn is not None:
            self.resource_group_crn = resource_group_crn
        if token is not None:
            self.token = token
        if user_access is not None:
            self.user_access = user_access
        if user_email is not None:
            self.user_email = user_email
        if user_id is not None:
            self.user_id = user_id

    @property
    def credential_type(self):
        """Gets the credential_type of this Principal.  # noqa: E501

        Workaround for AT event tracker  # noqa: E501

        :return: The credential_type of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """Sets the credential_type of this Principal.

        Workaround for AT event tracker  # noqa: E501

        :param credential_type: The credential_type of this Principal.  # noqa: E501
        :type: str
        """

        self._credential_type = credential_type

    @property
    def crn(self):
        """Gets the crn of this Principal.  # noqa: E501

        Workaround for AT event tracker  # noqa: E501

        :return: The crn of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._crn

    @crn.setter
    def crn(self, crn):
        """Sets the crn of this Principal.

        Workaround for AT event tracker  # noqa: E501

        :param crn: The crn of this Principal.  # noqa: E501
        :type: str
        """

        self._crn = crn

    @property
    def region(self):
        """Gets the region of this Principal.  # noqa: E501

        Workaround for API's not having region in their context (only works in IBM Cloud)  # noqa: E501

        :return: The region of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Principal.

        Workaround for API's not having region in their context (only works in IBM Cloud)  # noqa: E501

        :param region: The region of this Principal.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def resource_group_crn(self):
        """Gets the resource_group_crn of this Principal.  # noqa: E501

        Workaround for AT event tracker  # noqa: E501

        :return: The resource_group_crn of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_crn

    @resource_group_crn.setter
    def resource_group_crn(self, resource_group_crn):
        """Sets the resource_group_crn of this Principal.

        Workaround for AT event tracker  # noqa: E501

        :param resource_group_crn: The resource_group_crn of this Principal.  # noqa: E501
        :type: str
        """

        self._resource_group_crn = resource_group_crn

    @property
    def token(self):
        """Gets the token of this Principal.  # noqa: E501

        OAuth2 Token  # noqa: E501

        :return: The token of this Principal.  # noqa: E501
        :rtype: Token
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Principal.

        OAuth2 Token  # noqa: E501

        :param token: The token of this Principal.  # noqa: E501
        :type: Token
        """

        self._token = token

    @property
    def user_access(self):
        """Gets the user_access of this Principal.  # noqa: E501

        User Access  # noqa: E501

        :return: The user_access of this Principal.  # noqa: E501
        :rtype: UserAccess
        """
        return self._user_access

    @user_access.setter
    def user_access(self, user_access):
        """Sets the user_access of this Principal.

        User Access  # noqa: E501

        :param user_access: The user_access of this Principal.  # noqa: E501
        :type: UserAccess
        """

        self._user_access = user_access

    @property
    def user_email(self):
        """Gets the user_email of this Principal.  # noqa: E501

        Email of User  # noqa: E501

        :return: The user_email of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this Principal.

        Email of User  # noqa: E501

        :param user_email: The user_email of this Principal.  # noqa: E501
        :type: str
        """

        self._user_email = user_email

    @property
    def user_id(self):
        """Gets the user_id of this Principal.  # noqa: E501

        ID of User  # noqa: E501

        :return: The user_id of this Principal.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Principal.

        ID of User  # noqa: E501

        :param user_id: The user_id of this Principal.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(Principal, dict):
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
        if not isinstance(other, Principal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Principal):
            return True

        return self.to_dict() != other.to_dict()

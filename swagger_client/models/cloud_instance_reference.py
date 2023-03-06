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


class CloudInstanceReference(object):
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
        'initialized': 'bool',
        'limits': 'CloudInstanceUsageLimits',
        'name': 'str',
        'region': 'str',
        'capabilities': 'list[str]',
        'cloud_instance_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'href': 'href',
        'initialized': 'initialized',
        'limits': 'limits',
        'name': 'name',
        'region': 'region',
        'capabilities': 'capabilities',
        'cloud_instance_id': 'cloudInstanceID',
        'enabled': 'enabled'
    }

    def __init__(self, href=None, initialized=None, limits=None, name=None, region=None, capabilities=None, cloud_instance_id=None, enabled=None, _configuration=None):  # noqa: E501
        """CloudInstanceReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._href = None
        self._initialized = None
        self._limits = None
        self._name = None
        self._region = None
        self._capabilities = None
        self._cloud_instance_id = None
        self._enabled = None
        self.discriminator = None

        self.href = href
        self.initialized = initialized
        self.limits = limits
        self.name = name
        self.region = region
        if capabilities is not None:
            self.capabilities = capabilities
        self.cloud_instance_id = cloud_instance_id
        self.enabled = enabled

    @property
    def href(self):
        """Gets the href of this CloudInstanceReference.  # noqa: E501

        Link to Cloud Instance resource  # noqa: E501

        :return: The href of this CloudInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CloudInstanceReference.

        Link to Cloud Instance resource  # noqa: E501

        :param href: The href of this CloudInstanceReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def initialized(self):
        """Gets the initialized of this CloudInstanceReference.  # noqa: E501

        Indicates if the cloud instance is initialized and ready for use  # noqa: E501

        :return: The initialized of this CloudInstanceReference.  # noqa: E501
        :rtype: bool
        """
        return self._initialized

    @initialized.setter
    def initialized(self, initialized):
        """Sets the initialized of this CloudInstanceReference.

        Indicates if the cloud instance is initialized and ready for use  # noqa: E501

        :param initialized: The initialized of this CloudInstanceReference.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and initialized is None:
            raise ValueError("Invalid value for `initialized`, must not be `None`")  # noqa: E501

        self._initialized = initialized

    @property
    def limits(self):
        """Gets the limits of this CloudInstanceReference.  # noqa: E501

        Limits on the cloud instance  # noqa: E501

        :return: The limits of this CloudInstanceReference.  # noqa: E501
        :rtype: CloudInstanceUsageLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this CloudInstanceReference.

        Limits on the cloud instance  # noqa: E501

        :param limits: The limits of this CloudInstanceReference.  # noqa: E501
        :type: CloudInstanceUsageLimits
        """
        if self._configuration.client_side_validation and limits is None:
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def name(self):
        """Gets the name of this CloudInstanceReference.  # noqa: E501

        Cloud Instance Name  # noqa: E501

        :return: The name of this CloudInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudInstanceReference.

        Cloud Instance Name  # noqa: E501

        :param name: The name of this CloudInstanceReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def region(self):
        """Gets the region of this CloudInstanceReference.  # noqa: E501

        The region the cloud instance lives  # noqa: E501

        :return: The region of this CloudInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudInstanceReference.

        The region the cloud instance lives  # noqa: E501

        :param region: The region of this CloudInstanceReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def capabilities(self):
        """Gets the capabilities of this CloudInstanceReference.  # noqa: E501

        Cloud Instance Capabilities  # noqa: E501

        :return: The capabilities of this CloudInstanceReference.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this CloudInstanceReference.

        Cloud Instance Capabilities  # noqa: E501

        :param capabilities: The capabilities of this CloudInstanceReference.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def cloud_instance_id(self):
        """Gets the cloud_instance_id of this CloudInstanceReference.  # noqa: E501

        Cloud Instance ID  # noqa: E501

        :return: The cloud_instance_id of this CloudInstanceReference.  # noqa: E501
        :rtype: str
        """
        return self._cloud_instance_id

    @cloud_instance_id.setter
    def cloud_instance_id(self, cloud_instance_id):
        """Sets the cloud_instance_id of this CloudInstanceReference.

        Cloud Instance ID  # noqa: E501

        :param cloud_instance_id: The cloud_instance_id of this CloudInstanceReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cloud_instance_id is None:
            raise ValueError("Invalid value for `cloud_instance_id`, must not be `None`")  # noqa: E501

        self._cloud_instance_id = cloud_instance_id

    @property
    def enabled(self):
        """Gets the enabled of this CloudInstanceReference.  # noqa: E501

        Indicates if the cloud instance is enabled  # noqa: E501

        :return: The enabled of this CloudInstanceReference.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudInstanceReference.

        Indicates if the cloud instance is enabled  # noqa: E501

        :param enabled: The enabled of this CloudInstanceReference.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if issubclass(CloudInstanceReference, dict):
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
        if not isinstance(other, CloudInstanceReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudInstanceReference):
            return True

        return self.to_dict() != other.to_dict()

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


class NetworkCreate(object):
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
        'type': 'str',
        'cidr': 'str',
        'dns_servers': 'list[str]',
        'gateway': 'str',
        'ip_address_ranges': 'list[IPAddressRange]',
        'jumbo': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'cidr': 'cidr',
        'dns_servers': 'dnsServers',
        'gateway': 'gateway',
        'ip_address_ranges': 'ipAddressRanges',
        'jumbo': 'jumbo'
    }

    def __init__(self, name=None, type='vlan', cidr=None, dns_servers=None, gateway=None, ip_address_ranges=None, jumbo=None, _configuration=None):  # noqa: E501
        """NetworkCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._type = None
        self._cidr = None
        self._dns_servers = None
        self._gateway = None
        self._ip_address_ranges = None
        self._jumbo = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.type = type
        if cidr is not None:
            self.cidr = cidr
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if gateway is not None:
            self.gateway = gateway
        if ip_address_ranges is not None:
            self.ip_address_ranges = ip_address_ranges
        if jumbo is not None:
            self.jumbo = jumbo

    @property
    def name(self):
        """Gets the name of this NetworkCreate.  # noqa: E501

        Network Name  # noqa: E501

        :return: The name of this NetworkCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkCreate.

        Network Name  # noqa: E501

        :param name: The name of this NetworkCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this NetworkCreate.  # noqa: E501

        Type of Network - 'vlan' (private network) 'pub-vlan' (public network)  # noqa: E501

        :return: The type of this NetworkCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkCreate.

        Type of Network - 'vlan' (private network) 'pub-vlan' (public network)  # noqa: E501

        :param type: The type of this NetworkCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["vlan", "pub-vlan"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def cidr(self):
        """Gets the cidr of this NetworkCreate.  # noqa: E501

        Network in CIDR notation (192.168.0.0/24)  # noqa: E501

        :return: The cidr of this NetworkCreate.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NetworkCreate.

        Network in CIDR notation (192.168.0.0/24)  # noqa: E501

        :param cidr: The cidr of this NetworkCreate.  # noqa: E501
        :type: str
        """

        self._cidr = cidr

    @property
    def dns_servers(self):
        """Gets the dns_servers of this NetworkCreate.  # noqa: E501

        DNS Servers  # noqa: E501

        :return: The dns_servers of this NetworkCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this NetworkCreate.

        DNS Servers  # noqa: E501

        :param dns_servers: The dns_servers of this NetworkCreate.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def gateway(self):
        """Gets the gateway of this NetworkCreate.  # noqa: E501

        Gateway IP Address  # noqa: E501

        :return: The gateway of this NetworkCreate.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NetworkCreate.

        Gateway IP Address  # noqa: E501

        :param gateway: The gateway of this NetworkCreate.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def ip_address_ranges(self):
        """Gets the ip_address_ranges of this NetworkCreate.  # noqa: E501

        IP Address Ranges  # noqa: E501

        :return: The ip_address_ranges of this NetworkCreate.  # noqa: E501
        :rtype: list[IPAddressRange]
        """
        return self._ip_address_ranges

    @ip_address_ranges.setter
    def ip_address_ranges(self, ip_address_ranges):
        """Sets the ip_address_ranges of this NetworkCreate.

        IP Address Ranges  # noqa: E501

        :param ip_address_ranges: The ip_address_ranges of this NetworkCreate.  # noqa: E501
        :type: list[IPAddressRange]
        """

        self._ip_address_ranges = ip_address_ranges

    @property
    def jumbo(self):
        """Gets the jumbo of this NetworkCreate.  # noqa: E501

        Enable MTU Jumbo Network  # noqa: E501

        :return: The jumbo of this NetworkCreate.  # noqa: E501
        :rtype: bool
        """
        return self._jumbo

    @jumbo.setter
    def jumbo(self, jumbo):
        """Sets the jumbo of this NetworkCreate.

        Enable MTU Jumbo Network  # noqa: E501

        :param jumbo: The jumbo of this NetworkCreate.  # noqa: E501
        :type: bool
        """

        self._jumbo = jumbo

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
        if issubclass(NetworkCreate, dict):
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
        if not isinstance(other, NetworkCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkCreate):
            return True

        return self.to_dict() != other.to_dict()

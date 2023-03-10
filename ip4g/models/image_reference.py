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


class ImageReference(object):
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
        'last_update_date': 'datetime',
        'description': 'str',
        'href': 'str',
        'name': 'str',
        'specifications': 'ImageSpecifications',
        'state': 'str',
        'storage_pool': 'str',
        'storage_type': 'str',
        'creation_date': 'datetime',
        'image_id': 'str'
    }

    attribute_map = {
        'last_update_date': 'lastUpdateDate',
        'description': 'description',
        'href': 'href',
        'name': 'name',
        'specifications': 'specifications',
        'state': 'state',
        'storage_pool': 'storagePool',
        'storage_type': 'storageType',
        'creation_date': 'creationDate',
        'image_id': 'imageID'
    }

    def __init__(self, last_update_date=None, description=None, href=None, name=None, specifications=None, state=None, storage_pool=None, storage_type=None, creation_date=None, image_id=None, _configuration=None):  # noqa: E501
        """ImageReference - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_update_date = None
        self._description = None
        self._href = None
        self._name = None
        self._specifications = None
        self._state = None
        self._storage_pool = None
        self._storage_type = None
        self._creation_date = None
        self._image_id = None
        self.discriminator = None

        self.last_update_date = last_update_date
        self.description = description
        self.href = href
        self.name = name
        self.specifications = specifications
        self.state = state
        self.storage_pool = storage_pool
        self.storage_type = storage_type
        self.creation_date = creation_date
        self.image_id = image_id

    @property
    def last_update_date(self):
        """Gets the last_update_date of this ImageReference.  # noqa: E501

        Last Update Date  # noqa: E501

        :return: The last_update_date of this ImageReference.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this ImageReference.

        Last Update Date  # noqa: E501

        :param last_update_date: The last_update_date of this ImageReference.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def description(self):
        """Gets the description of this ImageReference.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageReference.

        Description  # noqa: E501

        :param description: The description of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def href(self):
        """Gets the href of this ImageReference.  # noqa: E501

        Link to Image resource  # noqa: E501

        :return: The href of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ImageReference.

        Link to Image resource  # noqa: E501

        :param href: The href of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def name(self):
        """Gets the name of this ImageReference.  # noqa: E501

        Image Name  # noqa: E501

        :return: The name of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageReference.

        Image Name  # noqa: E501

        :param name: The name of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def specifications(self):
        """Gets the specifications of this ImageReference.  # noqa: E501


        :return: The specifications of this ImageReference.  # noqa: E501
        :rtype: ImageSpecifications
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this ImageReference.


        :param specifications: The specifications of this ImageReference.  # noqa: E501
        :type: ImageSpecifications
        """
        if self._configuration.client_side_validation and specifications is None:
            raise ValueError("Invalid value for `specifications`, must not be `None`")  # noqa: E501

        self._specifications = specifications

    @property
    def state(self):
        """Gets the state of this ImageReference.  # noqa: E501

        Image State  # noqa: E501

        :return: The state of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ImageReference.

        Image State  # noqa: E501

        :param state: The state of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def storage_pool(self):
        """Gets the storage_pool of this ImageReference.  # noqa: E501

        Storage pool where image resides  # noqa: E501

        :return: The storage_pool of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._storage_pool

    @storage_pool.setter
    def storage_pool(self, storage_pool):
        """Sets the storage_pool of this ImageReference.

        Storage pool where image resides  # noqa: E501

        :param storage_pool: The storage_pool of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_pool is None:
            raise ValueError("Invalid value for `storage_pool`, must not be `None`")  # noqa: E501

        self._storage_pool = storage_pool

    @property
    def storage_type(self):
        """Gets the storage_type of this ImageReference.  # noqa: E501

        Storage type for image  # noqa: E501

        :return: The storage_type of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ImageReference.

        Storage type for image  # noqa: E501

        :param storage_type: The storage_type of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_type is None:
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501

        self._storage_type = storage_type

    @property
    def creation_date(self):
        """Gets the creation_date of this ImageReference.  # noqa: E501

        Creation Date  # noqa: E501

        :return: The creation_date of this ImageReference.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ImageReference.

        Creation Date  # noqa: E501

        :param creation_date: The creation_date of this ImageReference.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def image_id(self):
        """Gets the image_id of this ImageReference.  # noqa: E501

        Image ID  # noqa: E501

        :return: The image_id of this ImageReference.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageReference.

        Image ID  # noqa: E501

        :param image_id: The image_id of this ImageReference.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

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
        if issubclass(ImageReference, dict):
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
        if not isinstance(other, ImageReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageReference):
            return True

        return self.to_dict() != other.to_dict()

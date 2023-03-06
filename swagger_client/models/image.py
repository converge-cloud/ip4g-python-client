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


class Image(object):
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
        'name': 'str',
        'servers': 'list[str]',
        'size': 'float',
        'storage_pool': 'str',
        'volumes': 'list[ImageVolume]',
        'taskref': 'TaskReference',
        'creation_date': 'datetime',
        'description': 'str',
        'image_id': 'str',
        'specifications': 'ImageSpecifications',
        'state': 'str',
        'storage_type': 'str'
    }

    attribute_map = {
        'last_update_date': 'lastUpdateDate',
        'name': 'name',
        'servers': 'servers',
        'size': 'size',
        'storage_pool': 'storagePool',
        'volumes': 'volumes',
        'taskref': 'taskref',
        'creation_date': 'creationDate',
        'description': 'description',
        'image_id': 'imageID',
        'specifications': 'specifications',
        'state': 'state',
        'storage_type': 'storageType'
    }

    def __init__(self, last_update_date=None, name=None, servers=None, size=None, storage_pool=None, volumes=None, taskref=None, creation_date=None, description=None, image_id=None, specifications=None, state=None, storage_type=None, _configuration=None):  # noqa: E501
        """Image - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_update_date = None
        self._name = None
        self._servers = None
        self._size = None
        self._storage_pool = None
        self._volumes = None
        self._taskref = None
        self._creation_date = None
        self._description = None
        self._image_id = None
        self._specifications = None
        self._state = None
        self._storage_type = None
        self.discriminator = None

        self.last_update_date = last_update_date
        self.name = name
        if servers is not None:
            self.servers = servers
        self.size = size
        self.storage_pool = storage_pool
        if volumes is not None:
            self.volumes = volumes
        if taskref is not None:
            self.taskref = taskref
        self.creation_date = creation_date
        if description is not None:
            self.description = description
        self.image_id = image_id
        if specifications is not None:
            self.specifications = specifications
        if state is not None:
            self.state = state
        self.storage_type = storage_type

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Image.  # noqa: E501

        Last Update Date  # noqa: E501

        :return: The last_update_date of this Image.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Image.

        Last Update Date  # noqa: E501

        :param last_update_date: The last_update_date of this Image.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def name(self):
        """Gets the name of this Image.  # noqa: E501

        Image Name  # noqa: E501

        :return: The name of this Image.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Image.

        Image Name  # noqa: E501

        :param name: The name of this Image.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def servers(self):
        """Gets the servers of this Image.  # noqa: E501

        List of Servers that have deployed the image  # noqa: E501

        :return: The servers of this Image.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this Image.

        List of Servers that have deployed the image  # noqa: E501

        :param servers: The servers of this Image.  # noqa: E501
        :type: list[str]
        """

        self._servers = servers

    @property
    def size(self):
        """Gets the size of this Image.  # noqa: E501

        Image Size  # noqa: E501

        :return: The size of this Image.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Image.

        Image Size  # noqa: E501

        :param size: The size of this Image.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def storage_pool(self):
        """Gets the storage_pool of this Image.  # noqa: E501

        Storage pool where the image resides  # noqa: E501

        :return: The storage_pool of this Image.  # noqa: E501
        :rtype: str
        """
        return self._storage_pool

    @storage_pool.setter
    def storage_pool(self, storage_pool):
        """Sets the storage_pool of this Image.

        Storage pool where the image resides  # noqa: E501

        :param storage_pool: The storage_pool of this Image.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_pool is None:
            raise ValueError("Invalid value for `storage_pool`, must not be `None`")  # noqa: E501

        self._storage_pool = storage_pool

    @property
    def volumes(self):
        """Gets the volumes of this Image.  # noqa: E501

        Image Volumes  # noqa: E501

        :return: The volumes of this Image.  # noqa: E501
        :rtype: list[ImageVolume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Image.

        Image Volumes  # noqa: E501

        :param volumes: The volumes of this Image.  # noqa: E501
        :type: list[ImageVolume]
        """

        self._volumes = volumes

    @property
    def taskref(self):
        """Gets the taskref of this Image.  # noqa: E501


        :return: The taskref of this Image.  # noqa: E501
        :rtype: TaskReference
        """
        return self._taskref

    @taskref.setter
    def taskref(self, taskref):
        """Sets the taskref of this Image.


        :param taskref: The taskref of this Image.  # noqa: E501
        :type: TaskReference
        """

        self._taskref = taskref

    @property
    def creation_date(self):
        """Gets the creation_date of this Image.  # noqa: E501

        Creation Date  # noqa: E501

        :return: The creation_date of this Image.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Image.

        Creation Date  # noqa: E501

        :param creation_date: The creation_date of this Image.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def description(self):
        """Gets the description of this Image.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this Image.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Image.

        Description  # noqa: E501

        :param description: The description of this Image.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image_id(self):
        """Gets the image_id of this Image.  # noqa: E501

        Image ID  # noqa: E501

        :return: The image_id of this Image.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Image.

        Image ID  # noqa: E501

        :param image_id: The image_id of this Image.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def specifications(self):
        """Gets the specifications of this Image.  # noqa: E501


        :return: The specifications of this Image.  # noqa: E501
        :rtype: ImageSpecifications
        """
        return self._specifications

    @specifications.setter
    def specifications(self, specifications):
        """Sets the specifications of this Image.


        :param specifications: The specifications of this Image.  # noqa: E501
        :type: ImageSpecifications
        """

        self._specifications = specifications

    @property
    def state(self):
        """Gets the state of this Image.  # noqa: E501

        Image State  # noqa: E501

        :return: The state of this Image.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Image.

        Image State  # noqa: E501

        :param state: The state of this Image.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def storage_type(self):
        """Gets the storage_type of this Image.  # noqa: E501

        Storage type for image  # noqa: E501

        :return: The storage_type of this Image.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this Image.

        Storage type for image  # noqa: E501

        :param storage_type: The storage_type of this Image.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and storage_type is None:
            raise ValueError("Invalid value for `storage_type`, must not be `None`")  # noqa: E501

        self._storage_type = storage_type

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
        if issubclass(Image, dict):
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
        if not isinstance(other, Image):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Image):
            return True

        return self.to_dict() != other.to_dict()

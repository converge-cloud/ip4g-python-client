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


class VolumesClone(object):
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
        'percent_complete': 'int',
        'status': 'str',
        'volumes_clone_id': 'str',
        'action': 'str',
        'creation_date': 'datetime',
        'failure_message': 'str',
        'last_update_date': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'percent_complete': 'percentComplete',
        'status': 'status',
        'volumes_clone_id': 'volumesCloneID',
        'action': 'action',
        'creation_date': 'creationDate',
        'failure_message': 'failureMessage',
        'last_update_date': 'lastUpdateDate'
    }

    def __init__(self, name=None, percent_complete=None, status=None, volumes_clone_id=None, action=None, creation_date=None, failure_message=None, last_update_date=None, _configuration=None):  # noqa: E501
        """VolumesClone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._percent_complete = None
        self._status = None
        self._volumes_clone_id = None
        self._action = None
        self._creation_date = None
        self._failure_message = None
        self._last_update_date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.percent_complete = percent_complete
        if status is not None:
            self.status = status
        if volumes_clone_id is not None:
            self.volumes_clone_id = volumes_clone_id
        if action is not None:
            self.action = action
        if creation_date is not None:
            self.creation_date = creation_date
        if failure_message is not None:
            self.failure_message = failure_message
        if last_update_date is not None:
            self.last_update_date = last_update_date

    @property
    def name(self):
        """Gets the name of this VolumesClone.  # noqa: E501

        Name assigned to a volumes-clone request  # noqa: E501

        :return: The name of this VolumesClone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumesClone.

        Name assigned to a volumes-clone request  # noqa: E501

        :param name: The name of this VolumesClone.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def percent_complete(self):
        """Gets the percent_complete of this VolumesClone.  # noqa: E501

        The percent completion for the current action  # noqa: E501

        :return: The percent_complete of this VolumesClone.  # noqa: E501
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this VolumesClone.

        The percent completion for the current action  # noqa: E501

        :param percent_complete: The percent_complete of this VolumesClone.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and percent_complete is None:
            raise ValueError("Invalid value for `percent_complete`, must not be `None`")  # noqa: E501

        self._percent_complete = percent_complete

    @property
    def status(self):
        """Gets the status of this VolumesClone.  # noqa: E501

        Current status of the volumes-clone request  # noqa: E501

        :return: The status of this VolumesClone.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VolumesClone.

        Current status of the volumes-clone request  # noqa: E501

        :param status: The status of this VolumesClone.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def volumes_clone_id(self):
        """Gets the volumes_clone_id of this VolumesClone.  # noqa: E501

        ID assigned to a volumes-clone request  # noqa: E501

        :return: The volumes_clone_id of this VolumesClone.  # noqa: E501
        :rtype: str
        """
        return self._volumes_clone_id

    @volumes_clone_id.setter
    def volumes_clone_id(self, volumes_clone_id):
        """Sets the volumes_clone_id of this VolumesClone.

        ID assigned to a volumes-clone request  # noqa: E501

        :param volumes_clone_id: The volumes_clone_id of this VolumesClone.  # noqa: E501
        :type: str
        """

        self._volumes_clone_id = volumes_clone_id

    @property
    def action(self):
        """Gets the action of this VolumesClone.  # noqa: E501

        Current action performed for the volumes-clone request  # noqa: E501

        :return: The action of this VolumesClone.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this VolumesClone.

        Current action performed for the volumes-clone request  # noqa: E501

        :param action: The action of this VolumesClone.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def creation_date(self):
        """Gets the creation_date of this VolumesClone.  # noqa: E501

        Creation Date  # noqa: E501

        :return: The creation_date of this VolumesClone.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this VolumesClone.

        Creation Date  # noqa: E501

        :param creation_date: The creation_date of this VolumesClone.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def failure_message(self):
        """Gets the failure_message of this VolumesClone.  # noqa: E501

        Failure reason for a failed volumes-clone request  # noqa: E501

        :return: The failure_message of this VolumesClone.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this VolumesClone.

        Failure reason for a failed volumes-clone request  # noqa: E501

        :param failure_message: The failure_message of this VolumesClone.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def last_update_date(self):
        """Gets the last_update_date of this VolumesClone.  # noqa: E501

        Last Update Date  # noqa: E501

        :return: The last_update_date of this VolumesClone.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this VolumesClone.

        Last Update Date  # noqa: E501

        :param last_update_date: The last_update_date of this VolumesClone.  # noqa: E501
        :type: datetime
        """

        self._last_update_date = last_update_date

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
        if issubclass(VolumesClone, dict):
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
        if not isinstance(other, VolumesClone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumesClone):
            return True

        return self.to_dict() != other.to_dict()
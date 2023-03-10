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


class Task(object):
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
        'component_type': 'str',
        'creation_date': 'datetime',
        'last_update_date': 'datetime',
        'task_id': 'str',
        'cloud_instance_id': 'str',
        'component_id': 'str',
        'operation': 'str',
        'status': 'str',
        'status_detail': 'str'
    }

    attribute_map = {
        'component_type': 'componentType',
        'creation_date': 'creationDate',
        'last_update_date': 'lastUpdateDate',
        'task_id': 'taskID',
        'cloud_instance_id': 'cloudInstanceID',
        'component_id': 'componentID',
        'operation': 'operation',
        'status': 'status',
        'status_detail': 'statusDetail'
    }

    def __init__(self, component_type=None, creation_date=None, last_update_date=None, task_id=None, cloud_instance_id=None, component_id=None, operation=None, status=None, status_detail=None, _configuration=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._component_type = None
        self._creation_date = None
        self._last_update_date = None
        self._task_id = None
        self._cloud_instance_id = None
        self._component_id = None
        self._operation = None
        self._status = None
        self._status_detail = None
        self.discriminator = None

        self.component_type = component_type
        self.creation_date = creation_date
        self.last_update_date = last_update_date
        self.task_id = task_id
        self.cloud_instance_id = cloud_instance_id
        self.component_id = component_id
        self.operation = operation
        self.status = status
        self.status_detail = status_detail

    @property
    def component_type(self):
        """Gets the component_type of this Task.  # noqa: E501

        the component type of the task  # noqa: E501

        :return: The component_type of this Task.  # noqa: E501
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this Task.

        the component type of the task  # noqa: E501

        :param component_type: The component_type of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and component_type is None:
            raise ValueError("Invalid value for `component_type`, must not be `None`")  # noqa: E501

        self._component_type = component_type

    @property
    def creation_date(self):
        """Gets the creation_date of this Task.  # noqa: E501

        Creation Date  # noqa: E501

        :return: The creation_date of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Task.

        Creation Date  # noqa: E501

        :param creation_date: The creation_date of this Task.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and creation_date is None:
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Task.  # noqa: E501

        Last Update Date  # noqa: E501

        :return: The last_update_date of this Task.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Task.

        Last Update Date  # noqa: E501

        :param last_update_date: The last_update_date of this Task.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def task_id(self):
        """Gets the task_id of this Task.  # noqa: E501

        Pcloud Task ID  # noqa: E501

        :return: The task_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Task.

        Pcloud Task ID  # noqa: E501

        :param task_id: The task_id of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

    @property
    def cloud_instance_id(self):
        """Gets the cloud_instance_id of this Task.  # noqa: E501

        Cloud Instance ID of task owner  # noqa: E501

        :return: The cloud_instance_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._cloud_instance_id

    @cloud_instance_id.setter
    def cloud_instance_id(self, cloud_instance_id):
        """Sets the cloud_instance_id of this Task.

        Cloud Instance ID of task owner  # noqa: E501

        :param cloud_instance_id: The cloud_instance_id of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cloud_instance_id is None:
            raise ValueError("Invalid value for `cloud_instance_id`, must not be `None`")  # noqa: E501

        self._cloud_instance_id = cloud_instance_id

    @property
    def component_id(self):
        """Gets the component_id of this Task.  # noqa: E501

        the component id of the task  # noqa: E501

        :return: The component_id of this Task.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this Task.

        the component id of the task  # noqa: E501

        :param component_id: The component_id of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and component_id is None:
            raise ValueError("Invalid value for `component_id`, must not be `None`")  # noqa: E501

        self._component_id = component_id

    @property
    def operation(self):
        """Gets the operation of this Task.  # noqa: E501

        Task Operation  # noqa: E501

        :return: The operation of this Task.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Task.

        Task Operation  # noqa: E501

        :param operation: The operation of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501

        status code of the task  # noqa: E501

        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        status code of the task  # noqa: E501

        :param status: The status of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this Task.  # noqa: E501

        status detail of the task  # noqa: E501

        :return: The status_detail of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this Task.

        status detail of the task  # noqa: E501

        :param status_detail: The status_detail of this Task.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status_detail is None:
            raise ValueError("Invalid value for `status_detail`, must not be `None`")  # noqa: E501

        self._status_detail = status_detail

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
        if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Task):
            return True

        return self.to_dict() != other.to_dict()

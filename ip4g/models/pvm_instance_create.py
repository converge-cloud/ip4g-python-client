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


class PVMInstanceCreate(object):
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
        'replicant_affinity_policy': 'str',
        'storage_pool': 'str',
        'volume_ids': 'list[str]',
        'memory': 'float',
        'license_repository_capacity': 'int',
        'migratable': 'bool',
        'pin_policy': 'PinPolicy',
        'server_name': 'str',
        'software_licenses': 'SoftwareLicenses',
        'storage_connection': 'str',
        'virtual_cores': 'VirtualCores',
        'image_id': 'str',
        'proc_type': 'str',
        'replicant_naming_scheme': 'str',
        'replicants': 'float',
        'storage_type': 'str',
        'user_data': 'str',
        'network_ids': 'list[str]',
        'networks': 'list[PVMInstanceAddNetwork]',
        'placement_group': 'str',
        'processors': 'float',
        'storage_affinity': 'StorageAffinity',
        'sys_type': 'str',
        'key_pair_name': 'str'
    }

    attribute_map = {
        'replicant_affinity_policy': 'replicantAffinityPolicy',
        'storage_pool': 'storagePool',
        'volume_ids': 'volumeIDs',
        'memory': 'memory',
        'license_repository_capacity': 'licenseRepositoryCapacity',
        'migratable': 'migratable',
        'pin_policy': 'pinPolicy',
        'server_name': 'serverName',
        'software_licenses': 'softwareLicenses',
        'storage_connection': 'storageConnection',
        'virtual_cores': 'virtualCores',
        'image_id': 'imageID',
        'proc_type': 'procType',
        'replicant_naming_scheme': 'replicantNamingScheme',
        'replicants': 'replicants',
        'storage_type': 'storageType',
        'user_data': 'userData',
        'network_ids': 'networkIDs',
        'networks': 'networks',
        'placement_group': 'placementGroup',
        'processors': 'processors',
        'storage_affinity': 'storageAffinity',
        'sys_type': 'sysType',
        'key_pair_name': 'keyPairName'
    }

    def __init__(self, replicant_affinity_policy='none', storage_pool=None, volume_ids=None, memory=None, license_repository_capacity=None, migratable=True, pin_policy=None, server_name=None, software_licenses=None, storage_connection=None, virtual_cores=None, image_id=None, proc_type='dedicated', replicant_naming_scheme='suffix', replicants=None, storage_type=None, user_data=None, network_ids=None, networks=None, placement_group=None, processors=None, storage_affinity=None, sys_type=None, key_pair_name=None, _configuration=None):  # noqa: E501
        """PVMInstanceCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._replicant_affinity_policy = None
        self._storage_pool = None
        self._volume_ids = None
        self._memory = None
        self._license_repository_capacity = None
        self._migratable = None
        self._pin_policy = None
        self._server_name = None
        self._software_licenses = None
        self._storage_connection = None
        self._virtual_cores = None
        self._image_id = None
        self._proc_type = None
        self._replicant_naming_scheme = None
        self._replicants = None
        self._storage_type = None
        self._user_data = None
        self._network_ids = None
        self._networks = None
        self._placement_group = None
        self._processors = None
        self._storage_affinity = None
        self._sys_type = None
        self._key_pair_name = None
        self.discriminator = None

        if replicant_affinity_policy is not None:
            self.replicant_affinity_policy = replicant_affinity_policy
        if storage_pool is not None:
            self.storage_pool = storage_pool
        if volume_ids is not None:
            self.volume_ids = volume_ids
        self.memory = memory
        if license_repository_capacity is not None:
            self.license_repository_capacity = license_repository_capacity
        if migratable is not None:
            self.migratable = migratable
        if pin_policy is not None:
            self.pin_policy = pin_policy
        self.server_name = server_name
        if software_licenses is not None:
            self.software_licenses = software_licenses
        if storage_connection is not None:
            self.storage_connection = storage_connection
        if virtual_cores is not None:
            self.virtual_cores = virtual_cores
        self.image_id = image_id
        self.proc_type = proc_type
        if replicant_naming_scheme is not None:
            self.replicant_naming_scheme = replicant_naming_scheme
        if replicants is not None:
            self.replicants = replicants
        if storage_type is not None:
            self.storage_type = storage_type
        if user_data is not None:
            self.user_data = user_data
        if network_ids is not None:
            self.network_ids = network_ids
        if networks is not None:
            self.networks = networks
        if placement_group is not None:
            self.placement_group = placement_group
        self.processors = processors
        if storage_affinity is not None:
            self.storage_affinity = storage_affinity
        if sys_type is not None:
            self.sys_type = sys_type
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name

    @property
    def replicant_affinity_policy(self):
        """Gets the replicant_affinity_policy of this PVMInstanceCreate.  # noqa: E501

        Affinity policy for replicants being created; affinity for the same host, anti-affinity for different hosts, none for no preference  # noqa: E501

        :return: The replicant_affinity_policy of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._replicant_affinity_policy

    @replicant_affinity_policy.setter
    def replicant_affinity_policy(self, replicant_affinity_policy):
        """Sets the replicant_affinity_policy of this PVMInstanceCreate.

        Affinity policy for replicants being created; affinity for the same host, anti-affinity for different hosts, none for no preference  # noqa: E501

        :param replicant_affinity_policy: The replicant_affinity_policy of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["affinity", "anti-affinity", "none"]  # noqa: E501
        if (self._configuration.client_side_validation and
                replicant_affinity_policy not in allowed_values):
            raise ValueError(
                "Invalid value for `replicant_affinity_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(replicant_affinity_policy, allowed_values)
            )

        self._replicant_affinity_policy = replicant_affinity_policy

    @property
    def storage_pool(self):
        """Gets the storage_pool of this PVMInstanceCreate.  # noqa: E501

        Storage Pool for server deployment; if provided then storageAffinity and storageType will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :return: The storage_pool of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._storage_pool

    @storage_pool.setter
    def storage_pool(self, storage_pool):
        """Sets the storage_pool of this PVMInstanceCreate.

        Storage Pool for server deployment; if provided then storageAffinity and storageType will be ignored; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :param storage_pool: The storage_pool of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._storage_pool = storage_pool

    @property
    def volume_ids(self):
        """Gets the volume_ids of this PVMInstanceCreate.  # noqa: E501

        List of volume IDs  # noqa: E501

        :return: The volume_ids of this PVMInstanceCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this PVMInstanceCreate.

        List of volume IDs  # noqa: E501

        :param volume_ids: The volume_ids of this PVMInstanceCreate.  # noqa: E501
        :type: list[str]
        """

        self._volume_ids = volume_ids

    @property
    def memory(self):
        """Gets the memory of this PVMInstanceCreate.  # noqa: E501

        Amount of memory allocated (in GB)  # noqa: E501

        :return: The memory of this PVMInstanceCreate.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this PVMInstanceCreate.

        Amount of memory allocated (in GB)  # noqa: E501

        :param memory: The memory of this PVMInstanceCreate.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def license_repository_capacity(self):
        """Gets the license_repository_capacity of this PVMInstanceCreate.  # noqa: E501

        The VTL license repository capacity TB value  # noqa: E501

        :return: The license_repository_capacity of this PVMInstanceCreate.  # noqa: E501
        :rtype: int
        """
        return self._license_repository_capacity

    @license_repository_capacity.setter
    def license_repository_capacity(self, license_repository_capacity):
        """Sets the license_repository_capacity of this PVMInstanceCreate.

        The VTL license repository capacity TB value  # noqa: E501

        :param license_repository_capacity: The license_repository_capacity of this PVMInstanceCreate.  # noqa: E501
        :type: int
        """

        self._license_repository_capacity = license_repository_capacity

    @property
    def migratable(self):
        """Gets the migratable of this PVMInstanceCreate.  # noqa: E501

        Indicates if the server is allowed to migrate between hosts  # noqa: E501

        :return: The migratable of this PVMInstanceCreate.  # noqa: E501
        :rtype: bool
        """
        return self._migratable

    @migratable.setter
    def migratable(self, migratable):
        """Sets the migratable of this PVMInstanceCreate.

        Indicates if the server is allowed to migrate between hosts  # noqa: E501

        :param migratable: The migratable of this PVMInstanceCreate.  # noqa: E501
        :type: bool
        """

        self._migratable = migratable

    @property
    def pin_policy(self):
        """Gets the pin_policy of this PVMInstanceCreate.  # noqa: E501


        :return: The pin_policy of this PVMInstanceCreate.  # noqa: E501
        :rtype: PinPolicy
        """
        return self._pin_policy

    @pin_policy.setter
    def pin_policy(self, pin_policy):
        """Sets the pin_policy of this PVMInstanceCreate.


        :param pin_policy: The pin_policy of this PVMInstanceCreate.  # noqa: E501
        :type: PinPolicy
        """

        self._pin_policy = pin_policy

    @property
    def server_name(self):
        """Gets the server_name of this PVMInstanceCreate.  # noqa: E501

        Name of the server to create  # noqa: E501

        :return: The server_name of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this PVMInstanceCreate.

        Name of the server to create  # noqa: E501

        :param server_name: The server_name of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and server_name is None:
            raise ValueError("Invalid value for `server_name`, must not be `None`")  # noqa: E501

        self._server_name = server_name

    @property
    def software_licenses(self):
        """Gets the software_licenses of this PVMInstanceCreate.  # noqa: E501

        The pvm instance Software Licenses  # noqa: E501

        :return: The software_licenses of this PVMInstanceCreate.  # noqa: E501
        :rtype: SoftwareLicenses
        """
        return self._software_licenses

    @software_licenses.setter
    def software_licenses(self, software_licenses):
        """Sets the software_licenses of this PVMInstanceCreate.

        The pvm instance Software Licenses  # noqa: E501

        :param software_licenses: The software_licenses of this PVMInstanceCreate.  # noqa: E501
        :type: SoftwareLicenses
        """

        self._software_licenses = software_licenses

    @property
    def storage_connection(self):
        """Gets the storage_connection of this PVMInstanceCreate.  # noqa: E501

        The storage connection type  # noqa: E501

        :return: The storage_connection of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._storage_connection

    @storage_connection.setter
    def storage_connection(self, storage_connection):
        """Sets the storage_connection of this PVMInstanceCreate.

        The storage connection type  # noqa: E501

        :param storage_connection: The storage_connection of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["vSCSI"]  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_connection not in allowed_values):
            raise ValueError(
                "Invalid value for `storage_connection` ({0}), must be one of {1}"  # noqa: E501
                .format(storage_connection, allowed_values)
            )

        self._storage_connection = storage_connection

    @property
    def virtual_cores(self):
        """Gets the virtual_cores of this PVMInstanceCreate.  # noqa: E501

        The pvm instance virtual CPU information  # noqa: E501

        :return: The virtual_cores of this PVMInstanceCreate.  # noqa: E501
        :rtype: VirtualCores
        """
        return self._virtual_cores

    @virtual_cores.setter
    def virtual_cores(self, virtual_cores):
        """Sets the virtual_cores of this PVMInstanceCreate.

        The pvm instance virtual CPU information  # noqa: E501

        :param virtual_cores: The virtual_cores of this PVMInstanceCreate.  # noqa: E501
        :type: VirtualCores
        """

        self._virtual_cores = virtual_cores

    @property
    def image_id(self):
        """Gets the image_id of this PVMInstanceCreate.  # noqa: E501

        Image ID of the image to use for the server  # noqa: E501

        :return: The image_id of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this PVMInstanceCreate.

        Image ID of the image to use for the server  # noqa: E501

        :param image_id: The image_id of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def proc_type(self):
        """Gets the proc_type of this PVMInstanceCreate.  # noqa: E501

        Processor type (dedicated, shared, capped)  # noqa: E501

        :return: The proc_type of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._proc_type

    @proc_type.setter
    def proc_type(self, proc_type):
        """Sets the proc_type of this PVMInstanceCreate.

        Processor type (dedicated, shared, capped)  # noqa: E501

        :param proc_type: The proc_type of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and proc_type is None:
            raise ValueError("Invalid value for `proc_type`, must not be `None`")  # noqa: E501
        allowed_values = ["dedicated", "shared", "capped"]  # noqa: E501
        if (self._configuration.client_side_validation and
                proc_type not in allowed_values):
            raise ValueError(
                "Invalid value for `proc_type` ({0}), must be one of {1}"  # noqa: E501
                .format(proc_type, allowed_values)
            )

        self._proc_type = proc_type

    @property
    def replicant_naming_scheme(self):
        """Gets the replicant_naming_scheme of this PVMInstanceCreate.  # noqa: E501

        How to name the created vms  # noqa: E501

        :return: The replicant_naming_scheme of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._replicant_naming_scheme

    @replicant_naming_scheme.setter
    def replicant_naming_scheme(self, replicant_naming_scheme):
        """Sets the replicant_naming_scheme of this PVMInstanceCreate.

        How to name the created vms  # noqa: E501

        :param replicant_naming_scheme: The replicant_naming_scheme of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["prefix", "suffix"]  # noqa: E501
        if (self._configuration.client_side_validation and
                replicant_naming_scheme not in allowed_values):
            raise ValueError(
                "Invalid value for `replicant_naming_scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(replicant_naming_scheme, allowed_values)
            )

        self._replicant_naming_scheme = replicant_naming_scheme

    @property
    def replicants(self):
        """Gets the replicants of this PVMInstanceCreate.  # noqa: E501

        Number of duplicate instances to create in this request  # noqa: E501

        :return: The replicants of this PVMInstanceCreate.  # noqa: E501
        :rtype: float
        """
        return self._replicants

    @replicants.setter
    def replicants(self, replicants):
        """Sets the replicants of this PVMInstanceCreate.

        Number of duplicate instances to create in this request  # noqa: E501

        :param replicants: The replicants of this PVMInstanceCreate.  # noqa: E501
        :type: float
        """

        self._replicants = replicants

    @property
    def storage_type(self):
        """Gets the storage_type of this PVMInstanceCreate.  # noqa: E501

        Storage type for server deployment; will be ignored if storagePool or storageAffinity is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :return: The storage_type of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this PVMInstanceCreate.

        Storage type for server deployment; will be ignored if storagePool or storageAffinity is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :param storage_type: The storage_type of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._storage_type = storage_type

    @property
    def user_data(self):
        """Gets the user_data of this PVMInstanceCreate.  # noqa: E501

        Cloud init user defined data  # noqa: E501

        :return: The user_data of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this PVMInstanceCreate.

        Cloud init user defined data  # noqa: E501

        :param user_data: The user_data of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def network_ids(self):
        """Gets the network_ids of this PVMInstanceCreate.  # noqa: E501

        (deprecated - replaced by networks) List of Network IDs  # noqa: E501

        :return: The network_ids of this PVMInstanceCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_ids

    @network_ids.setter
    def network_ids(self, network_ids):
        """Sets the network_ids of this PVMInstanceCreate.

        (deprecated - replaced by networks) List of Network IDs  # noqa: E501

        :param network_ids: The network_ids of this PVMInstanceCreate.  # noqa: E501
        :type: list[str]
        """

        self._network_ids = network_ids

    @property
    def networks(self):
        """Gets the networks of this PVMInstanceCreate.  # noqa: E501

        The pvm instance networks information  # noqa: E501

        :return: The networks of this PVMInstanceCreate.  # noqa: E501
        :rtype: list[PVMInstanceAddNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this PVMInstanceCreate.

        The pvm instance networks information  # noqa: E501

        :param networks: The networks of this PVMInstanceCreate.  # noqa: E501
        :type: list[PVMInstanceAddNetwork]
        """

        self._networks = networks

    @property
    def placement_group(self):
        """Gets the placement_group of this PVMInstanceCreate.  # noqa: E501

        The placement group for the server  # noqa: E501

        :return: The placement_group of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this PVMInstanceCreate.

        The placement group for the server  # noqa: E501

        :param placement_group: The placement_group of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._placement_group = placement_group

    @property
    def processors(self):
        """Gets the processors of this PVMInstanceCreate.  # noqa: E501

        Number of processors allocated  # noqa: E501

        :return: The processors of this PVMInstanceCreate.  # noqa: E501
        :rtype: float
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this PVMInstanceCreate.

        Number of processors allocated  # noqa: E501

        :param processors: The processors of this PVMInstanceCreate.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and processors is None:
            raise ValueError("Invalid value for `processors`, must not be `None`")  # noqa: E501

        self._processors = processors

    @property
    def storage_affinity(self):
        """Gets the storage_affinity of this PVMInstanceCreate.  # noqa: E501

        The storage affinity data; ignored if storagePool is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :return: The storage_affinity of this PVMInstanceCreate.  # noqa: E501
        :rtype: StorageAffinity
        """
        return self._storage_affinity

    @storage_affinity.setter
    def storage_affinity(self, storage_affinity):
        """Sets the storage_affinity of this PVMInstanceCreate.

        The storage affinity data; ignored if storagePool is provided; Only valid when you deploy one of the IBM supplied stock images. Storage type and pool for a custom image (an imported image or an image that is created from a PVMInstance capture) defaults to the storage type and pool the image was created in  # noqa: E501

        :param storage_affinity: The storage_affinity of this PVMInstanceCreate.  # noqa: E501
        :type: StorageAffinity
        """

        self._storage_affinity = storage_affinity

    @property
    def sys_type(self):
        """Gets the sys_type of this PVMInstanceCreate.  # noqa: E501

        System type used to host the instance  # noqa: E501

        :return: The sys_type of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._sys_type

    @sys_type.setter
    def sys_type(self, sys_type):
        """Sets the sys_type of this PVMInstanceCreate.

        System type used to host the instance  # noqa: E501

        :param sys_type: The sys_type of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._sys_type = sys_type

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this PVMInstanceCreate.  # noqa: E501

        The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant's list of keys)  # noqa: E501

        :return: The key_pair_name of this PVMInstanceCreate.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this PVMInstanceCreate.

        The name of the SSH key pair provided to the server for authenticating users (looked up in the tenant's list of keys)  # noqa: E501

        :param key_pair_name: The key_pair_name of this PVMInstanceCreate.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

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
        if issubclass(PVMInstanceCreate, dict):
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
        if not isinstance(other, PVMInstanceCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PVMInstanceCreate):
            return True

        return self.to_dict() != other.to_dict()

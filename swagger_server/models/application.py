# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Application(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, program_id: int=None, user_id: int=None, status: str=None, created_at: datetime=None):  # noqa: E501
        """Application - a model defined in Swagger

        :param id: The id of this Application.  # noqa: E501
        :type id: int
        :param program_id: The program_id of this Application.  # noqa: E501
        :type program_id: int
        :param user_id: The user_id of this Application.  # noqa: E501
        :type user_id: int
        :param status: The status of this Application.  # noqa: E501
        :type status: str
        :param created_at: The created_at of this Application.  # noqa: E501
        :type created_at: datetime
        """
        self.swagger_types = {
            'id': int,
            'program_id': int,
            'user_id': int,
            'status': str,
            'created_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'program_id': 'program_id',
            'user_id': 'user_id',
            'status': 'status',
            'created_at': 'created_at'
        }
        self._id = id
        self._program_id = program_id
        self._user_id = user_id
        self._status = status
        self._created_at = created_at

    @classmethod
    def from_dict(cls, dikt) -> 'Application':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Application of this Application.  # noqa: E501
        :rtype: Application
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Application.


        :return: The id of this Application.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Application.


        :param id: The id of this Application.
        :type id: int
        """

        self._id = id

    @property
    def program_id(self) -> int:
        """Gets the program_id of this Application.


        :return: The program_id of this Application.
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id: int):
        """Sets the program_id of this Application.


        :param program_id: The program_id of this Application.
        :type program_id: int
        """

        self._program_id = program_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Application.


        :return: The user_id of this Application.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Application.


        :param user_id: The user_id of this Application.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def status(self) -> str:
        """Gets the status of this Application.


        :return: The status of this Application.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Application.


        :param status: The status of this Application.
        :type status: str
        """

        self._status = status

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this Application.


        :return: The created_at of this Application.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this Application.


        :param created_at: The created_at of this Application.
        :type created_at: datetime
        """

        self._created_at = created_at

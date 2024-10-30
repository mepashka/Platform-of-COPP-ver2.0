# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApplicationInput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, program_id: int=None, user_id: int=None, status: str=None):  # noqa: E501
        """ApplicationInput - a model defined in Swagger

        :param program_id: The program_id of this ApplicationInput.  # noqa: E501
        :type program_id: int
        :param user_id: The user_id of this ApplicationInput.  # noqa: E501
        :type user_id: int
        :param status: The status of this ApplicationInput.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'program_id': int,
            'user_id': int,
            'status': str
        }

        self.attribute_map = {
            'program_id': 'program_id',
            'user_id': 'user_id',
            'status': 'status'
        }
        self._program_id = program_id
        self._user_id = user_id
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApplicationInput of this ApplicationInput.  # noqa: E501
        :rtype: ApplicationInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def program_id(self) -> int:
        """Gets the program_id of this ApplicationInput.


        :return: The program_id of this ApplicationInput.
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id: int):
        """Sets the program_id of this ApplicationInput.


        :param program_id: The program_id of this ApplicationInput.
        :type program_id: int
        """
        if program_id is None:
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ApplicationInput.


        :return: The user_id of this ApplicationInput.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ApplicationInput.


        :param user_id: The user_id of this ApplicationInput.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def status(self) -> str:
        """Gets the status of this ApplicationInput.


        :return: The status of this ApplicationInput.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ApplicationInput.


        :param status: The status of this ApplicationInput.
        :type status: str
        """

        self._status = status
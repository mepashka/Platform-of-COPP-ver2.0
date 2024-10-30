# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UserInput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, email: str=None, password: str=None, role: str=None):  # noqa: E501
        """UserInput - a model defined in Swagger

        :param name: The name of this UserInput.  # noqa: E501
        :type name: str
        :param email: The email of this UserInput.  # noqa: E501
        :type email: str
        :param password: The password of this UserInput.  # noqa: E501
        :type password: str
        :param role: The role of this UserInput.  # noqa: E501
        :type role: str
        """
        self.swagger_types = {
            'name': str,
            'email': str,
            'password': str,
            'role': str
        }

        self.attribute_map = {
            'name': 'name',
            'email': 'email',
            'password': 'password',
            'role': 'role'
        }
        self._name = name
        self._email = email
        self._password = password
        self._role = role

    @classmethod
    def from_dict(cls, dikt) -> 'UserInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserInput of this UserInput.  # noqa: E501
        :rtype: UserInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this UserInput.


        :return: The name of this UserInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserInput.


        :param name: The name of this UserInput.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this UserInput.


        :return: The email of this UserInput.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserInput.


        :param email: The email of this UserInput.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this UserInput.


        :return: The password of this UserInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserInput.


        :param password: The password of this UserInput.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def role(self) -> str:
        """Gets the role of this UserInput.


        :return: The role of this UserInput.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this UserInput.


        :param role: The role of this UserInput.
        :type role: str
        """

        self._role = role

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_input import ApplicationInput  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.program_input import ProgramInput  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_input import UserInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_applications_get(self):
        """Test case for applications_get

        Получить список всех заявок
        """
        response = self.client.open(
            '/v1/applications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_post(self):
        """Test case for applications_post

        Создать новую заявку
        """
        body = ApplicationInput()
        response = self.client.open(
            '/v1/applications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_get(self):
        """Test case for programs_get

        Получить список всех программ
        """
        response = self.client.open(
            '/v1/programs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_programs_post(self):
        """Test case for programs_post

        Создать новую программу
        """
        body = ProgramInput()
        response = self.client.open(
            '/v1/programs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Получить список всех пользователей
        """
        response = self.client.open(
            '/v1/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_delete(self):
        """Test case for users_id_delete

        Удалить пользователя
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_get(self):
        """Test case for users_id_get

        Получить информацию о конкретном пользователе
        """
        response = self.client.open(
            '/v1/users/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_id_put(self):
        """Test case for users_id_put

        Обновить данные пользователя
        """
        body = UserInput()
        response = self.client.open(
            '/v1/users/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Создать нового пользователя
        """
        body = UserInput()
        response = self.client.open(
            '/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

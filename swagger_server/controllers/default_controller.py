import connexion
import six

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.application_input import ApplicationInput  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.program import Program  # noqa: E501
from swagger_server.models.program_input import ProgramInput  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_input import UserInput  # noqa: E501
from swagger_server import util


def applications_get():  # noqa: E501
    """Получить список всех заявок

     # noqa: E501


    :rtype: List[Application]
    """
    return 'do some magic!'


def applications_post(body):  # noqa: E501
    """Создать новую заявку

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Application
    """
    if connexion.request.is_json:
        body = ApplicationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def programs_get():  # noqa: E501
    """Получить список всех программ

     # noqa: E501


    :rtype: List[Program]
    """
    return 'do some magic!'


def programs_post(body):  # noqa: E501
    """Создать новую программу

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Program
    """
    if connexion.request.is_json:
        body = ProgramInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_get():  # noqa: E501
    """Получить список всех пользователей

     # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_id_delete(id):  # noqa: E501
    """Удалить пользователя

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def users_id_get(id):  # noqa: E501
    """Получить информацию о конкретном пользователе

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def users_id_put(body, id):  # noqa: E501
    """Обновить данные пользователя

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Создать нового пользователя

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

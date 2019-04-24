from app import sessionStorage
import logging


def set_status(session_id, status):
    sessionStorage[session_id]['status'] = status


def old_user_start(**kwargs):
    response = kwargs['response']
    response['response']['text'] = 'Добро пожаловать обратно!'
    logging.info('User logged in<br>')


def new_user_start(**kwargs):
    response = kwargs['response']
    response['response']['text'] = 'Добро пожаловать в систему Умный Дом! Если вам требуется помощь, напишите "помощь"'
    logging.info('New user registered<br>')


def no_session(**kwargs):
    response = kwargs['response']
    response['response']['text'] = 'Извините, ваша сессия закончилась. Перезагрузите навык'
    response['response']['end_session'] = True
    logging.warning('Not found user session<br>')


def unexpected_error(**kwargs):
    response = kwargs['response']
    response['response']['text'] = 'Неизвестная ошибка. Перезагрузите навык'
    response['response']['end_session'] = True
    logging.error('Unexpected error: {}<br>'.format(str(kwargs['error'])))


def main_menu(**kwargs):
    response = kwargs['response']
    response['response']['text'] = 'Main menu'
    response['response']['end_session'] = True
    logging.warning('Not found user session<br>')


def enter_name(**kwargs):
    request = kwargs['request']['request']
    pass


def enter_smarthome_webhook(**kwargs):
    webhook = kwargs['request']['request']['original_utterance']
    pass


def enter_smarthome_password(**kwargs):
    pass

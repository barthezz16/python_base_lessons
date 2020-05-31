from copy import deepcopy
from pprint import pprint
from unittest import TestCase
from unittest.mock import patch, Mock
import datetime as DT

from vk_api.bot_longpoll import VkBotEvent

import settings
from bot import Bot


class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {'date': 1561646823, 'from_id': 550207343, 'id': 119, 'out': 0, 'peer_id': 550207343,
                   'text': 'привет bot', 'coversation_message_id': 119, 'fwd_messages': [], 'important': False,
                   'random_id': 0, 'attachments': [], 'is_hidde': False},
        'group_id': 183721469}

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    date = DT.datetime.now().strftime('%d.%m.%Y')

    INPUTS = [
        '\\ticket',
        'moscow',
        'berlin',
        date,
        date,
        '5',
        'ok',
        'yes',
        '9179631309',
    ]
    EXPECTED_OUTPUTS = [
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        "Вы ищите рейс из Moscow в Berlin?.\n Пять ближайших рейсов из Moscow в Berlin: "
        "{'31.05.2020, 05.06.2020, 10.06.2020, 14.06.2020, 19.06.2020'}."
        "\n\n\nВведите желаемую дату вылета в формате DD.MM.YYYY.",
        "Выберите желаемую дату вылета из ближайших к желаемой дате вылета "
        "['31.05.2020', '05.06.2020', '10.06.2020', '14.06.2020', '19.06.2020'].",
        settings.SCENARIOS['registration']['steps']['step5']['text'],
        settings.SCENARIOS['registration']['steps']['step6']['text'],
        'Проверьте пожалуйста введенные данные, если все верно, введите "Да".\nГород вылета: Moscow. '
        '\nГород прилета: Berlin.\nДата: 31.05.2020. \nКоличество мест: 5.\nКомментарий: ok.',
        settings.SCENARIOS['registration']['steps']['step8']['text'],
        'Спасибо за покупку, мы свяжемся с вами по указанному номеру (9179631309)..',
    ]  # TODO неужели надо вот так расписать, чтобы тест прошел?

    def test_tun_ok(self):
        print('-' * 84)
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['text'] = input_text
            events.append(VkBotEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()
        print(send_mock.call_count, len(self.INPUTS))
        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        print(real_outputs)
        print(self.EXPECTED_OUTPUTS)
        assert real_outputs == self.EXPECTED_OUTPUTS

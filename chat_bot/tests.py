from unittest import TestCase
from unittest.mock import Mock

from requests import patch

from vk_bot import Bot


class Test1(TestCase):
    def test_ok(self):
        count = 5
        events = [{}] * count
        long_poller_mock = Mock(retun_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
        with patch('vk_bot.vk_api.VkApi'):
            with patch('vk_bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                vk_bot = Bot('', '')
                vk_bot.on_event = Mock()
                vk_bot.run()

                vk_bot.on_event.assert_colled()
                vk_bot.on_event.assert_any_call({})
                vk_bot.on_event.call_count == count

import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
from handlers import dates_creator

import handlers

try:
    import settings
except ImportError:
    exit('settings.py.default settings.py and set toke.')

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler('bot.log', mode='a', encoding='UTF8', delay=False)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s', "%d-%m-%Y %H:%M"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


class Bot:
    """
    Echo bot для vk.com

    Use python 3.8.1
    """

    def __init__(self, group_id, token):
        """

        :param group_id: group id из группы vk.com
        :param token: серкретный токен
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        self.user_states = dict()
        self.flights = dates_creator()

    def run(self):
        """ Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception("ошибка в обработке события")

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст.

        :param event: VkBotMessageEvent object
        :return: None
        """
        answer = str(event.object.text)
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('мы пока не умеем обрабатывать события такого типа %s', event.type)
            return

        user_id = event.object.peer_id
        text = event.object.text

        if user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            for intent in settings.INTENTS:
                log.debug(f'User get {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(
            message=text_to_send,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id,
        )

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]
        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):
            next_step = steps[step['next_step']]  # Обратите внимание, что для указания следующего шага
            # Нужно после этого действия сделать ещё и другие
            text_to_send = next_step['text'].format(**state.context)
            if next_step['next_step']:
                state.step_name = step['next_step']
                next_step = steps[step['failure_step']]# В частности вот это.
                # TODO да и тут что то не пойму что надо дальше...
            else:
                self.user_states.pop(user_id)
                log.info('Билет из {city_departure} в {city_arrival} на {date} куплен.'.format(**state.context))
        else:
            next_step = steps[step['failure_step']]
            text_to_send = step['failure_text'].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()

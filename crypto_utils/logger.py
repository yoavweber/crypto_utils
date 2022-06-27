from crypto_utils.utils import is_development  
import logging
from dotenv import load_dotenv
from os import environ, path
import urllib.parse
import logging.config
from logging import StreamHandler
import requests


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'telegram': {
            'class': 'telegram_handler.TelegramHandler',
            'token': environ.get('TELEGRAM_BOT'),
            'chat_id': environ.get('GROUP_ID')
        }
    },
    'loggers': {
        'my_logger': {
            'handlers': ['telegram'],
            'level': 'DEBUG'
        }
    }
}



class Telegram:
    def __init__(self, group_id) -> None:
        self.bot_key = environ.get('TELEGRAM_BOT')
        self.group_id = group_id

    def _format_message(self, message):
        encoded_message = urllib.parse.quote_plus(message)
        endpoint = f"https://api.telegram.org/bot{self.bot_key}/sendMessage?chat_id=-{self.group_id}&text={encoded_message}"
        return endpoint

    def send_message(self, message):
        print(message, "!!")
        url = self._format_message(message)
        requests.post(url)


class TelegramErrorHandler(StreamHandler):
    def __init__(self, group_id):
        StreamHandler.__init__(self)
        self.telegram = Telegram(group_id)

    def emit(self, record):
        msg = self.format(record)
        self.telegram.send_message(msg)


logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S '
)

logger = logging.getLogger('simple_example')
formatter = logging.Formatter(
    '%(asctime)s  - %(message)s')
tl_error = TelegramErrorHandler(environ.get('GROUP_ID'))
tl_error.setFormatter(formatter)
tl_error.setLevel(logging.ERROR)

tl_log = TelegramErrorHandler(environ.get('LOG_GROUP_ID'))
tl_log.setFormatter(formatter)
tl_log.setLevel(logging.DEBUG)


if is_development():
    logger.addHandler(StreamHandler())
else:
    logger.addHandler(tl_error)
    logger.addHandler(tl_log)

import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "23237740"))
    API_HASH = os.environ.get("API_HASH", "690d9c8bc9a28338d59216e3ea0501c4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6951958770:AAEyTj58WQWRUZ9G2wMT1uhpmI9_OVvN6WE")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ufoxx_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]

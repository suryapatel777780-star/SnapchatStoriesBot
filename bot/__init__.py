import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "36221865"))
    API_HASH = os.environ.get("API_HASH", "bf67875147c03982e57599fcb43f5b40")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","9032331403:AAG7TvulMJE7ufK_qFjmQjB-RIS46WESyn8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","snap_stories_download_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]

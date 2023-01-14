import os

class Config(object):

    # get a token from @BotFather

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5945346287:AAE3gmyeGs-oK2UxcgbTDWjr48an4iv-oSY")

    # The Telegram API things

    APP_ID = int(os.environ.get("APP_ID", 22681384))

    API_HASH = os.environ.get("API_HASH", "14ae45755537c723aab0564a80d723a9")

    # Get these values from my.telegram.org

    # Banned Unwanted Members..

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size

    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000

    # chunk size that should be used with requests

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess

    PROCESS_MAX_TIMEOUT = 3600

    # watermark file

    DEF_WATER_MARK_FILE = ""

    # your telegram id

    OWNER_ID = int(os.environ.get("OWNER_ID", "5468192421"))

    # Update channel for Force Subscribe

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001523739263")

    # database session name, example: xurluploader

    SESSION_NAME = os.environ.get("SESSION_NAME", "uptoniyt")

    # database uri (mongodb)

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")

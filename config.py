import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "17713634"))
API_HASH = getenv("API_HASH", "a8c943a69022fef3ac66accc7ba8ce6b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6671586333:AAE9lmQLng_vwnQ0VH-UpDEixaXdd5WSWJA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://moni2002:moni2002@cluster0.uorma4o.mongodb.net/?retryWrites=true&w=majority")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "⌜ꜱᴡᴇᴇᴛy ✘ ᴍᴜsɪᴄ 🕊⃝‌⌟")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "True")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9000000000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001891375171"))

# Get this value from @PiyushXManagerBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5854691181"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MoniSandy0204/SweetyMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TMK_MUSICCHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TMK_MUSICSUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @String_SessionRobot on Telegram
STRING1 = getenv("STRING_SESSION", "BQCP7n8RWza-1GEfxCj9XwdHsUgQy2UacCLmGYx4mfnj7JIFhVIQb8WG9T_aDY2aMsYljNqBns5kfO6kPniMwQGEmm-Oe5toI_vyjK57UVsnepA7zxbzP0EppZDcy_e4IbnCQUIWWzquHb7zPwdjmk8nj-nVvbIEtaJZZm9oeqXoVXmN216j7vHsGcY0GAYeMtGGZmvLUuaE_qnJLFnodolpHtLPSYIsYxGj5p8sX8GTOxtvFC8tNV4uBcAjAyKec9hHAdBPllmdmYnR6AsiB6lut-YVzTbcWyECnzC5KvPXgb4EBrWq7xwog3nY0_211MkYj1efLJI0FSZG5QqhFdl6AAAAAXn9mXgA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/3d010ee2c59464f6c6705.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/efbf0fedf841bf3f5c953.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/68120737e37cae7520c7b.jpg"
STATS_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/afe528670b99930e7f66d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

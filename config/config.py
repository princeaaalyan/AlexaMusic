# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
Alexa is a Telegram Audio and video streaming bot
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# === Your Fixed Credentials ===
API_ID = int(getenv("API_ID", "28142579"))
API_HASH = getenv("API_HASH", "f3dcd1e8dedf35e513b59c0ad01f33be")
BOT_TOKEN = getenv("BOT_TOKEN", "8238506745:AAGoZtm2kceFcJAPC0VkFzzvL5kx4MiXBVI")

OWNER_ID = int(getenv("OWNER_ID", "7618637244"))
SESSION = getenv("SESSION", "AQFk39kAhjZcHuD4YJmtD6IhgTwq_5YXw7zDpsDZevtzQgoRtdNDR2tysPwnMIpZ09jC9mBWZ_7msws_gclXvBuziE9WzA3yGBMUkf99O3YnTb_6BhdCf91K5uDNZIlr8mgmzr7C8rQTk3jUzQQVPv_BKGSSZszRGoxarfOR11kAr7hi8H8-SmWqdBSp9Aj7tr1xXxJLHMk2m_6OmRVwPiYFWOFLb_s26PSk9E05DVB9GLYKGsops4JHeCZ6eYgroCSfpNtASV_dObxqon0qKCq8JhTycmEqMSF4yOp39RfLJ3wP0cAWCfp0-aCJD4StzVY7XXVZtvGFMrTBO02Y9M_BTVAqeQAAAAHGGy28AA")

# === Other Configurations ===
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "0"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Alexa Music")

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
BOT_ID = getenv("BOT_ID", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Alexa_BotUpdates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alexa_Help")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

COOKIES = getenv("COOKIES", None)

STRING1 = getenv("STRING_SESSION", SESSION)  # default = your session
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"

adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []

# === Default Image URLs ===
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/d593c6064ff7657d0c714.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "assets/Ping.jpeg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "assets/Playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "assets/Global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "assets/Stats.jpeg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "assets/Audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "assets/Video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "assets/Stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "assets/Soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "assets/Youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "assets/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "assets/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "assets/SpotifyPlaylist.jpeg")

# === Duration Settings ===
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

# === URL Checks ===
for name, value in {
    "SUPPORT_CHANNEL": SUPPORT_CHANNEL,
    "SUPPORT_GROUP": SUPPORT_GROUP,
    "UPSTREAM_REPO": UPSTREAM_REPO,
    "GITHUB_REPO": GITHUB_REPO,
    "PING_IMG_URL": PING_IMG_URL,
    "PLAYLIST_IMG_URL": PLAYLIST_IMG_URL,
    "GLOBAL_IMG_URL": GLOBAL_IMG_URL,
    "STATS_IMG_URL": STATS_IMG_URL,
    "TELEGRAM_AUDIO_URL": TELEGRAM_AUDIO_URL,
    "TELEGRAM_VIDEO_URL": TELEGRAM_VIDEO_URL,
    "STREAM_IMG_URL": STREAM_IMG_URL,
    "SOUNCLOUD_IMG_URL": SOUNCLOUD_IMG_URL,
    "YOUTUBE_IMG_URL": YOUTUBE_IMG_URL,
}.items():
    if value and not re.match("(?:http|https)://", value) and not value.startswith("assets/"):
        print(f"[ERROR] - Your {name} url is wrong. Please ensure that it starts with https://")
        sys.exit()

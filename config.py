from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16782655"))
API_HASH = getenv("API_HASH", "86c15289ada86db4c53a0b57470f9a50")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𓆩𝗦𝗣𝗢𝗥𝗧𝗙𝗬 ✘ 𝗠𝗨𝗦𝗜𝗖𓆪")
BOT_USERNAME = getenv("BOT_USERNAME", "SPORTFY_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SHRIYANSHCHAT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/13f6591189b9df22269f8.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/13f6591189b9df22269f8.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))

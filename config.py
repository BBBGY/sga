## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDFhFw814pbes49RyXoLqh_pmzvy5DnH09ZFG-xQnZThh4DMkZbfsTbmXt-wGvumEnQYOLDyh2U26FT_KQ6S40Dc8MvbCtwmFDDM-xXr5FYY2iv-oeEOy9p6zkq3hSFb74o7S9f176zD9rq_QoAPT11osa0mqlsLZYrWip6RwzhuhB6TivPOInHbUCA6F-hrdXBAkk_g3-i894q-jAwFZIIfkkLZeXN3hyGVInEGjcbpZQeNwU4ux-NwuA0iGzA3oYXm6f4u6r4DAek2h3zweP4fOMAGHVATvUq1h5U2v5xVKmQMCRLdMqcjZKZu5pR2xoA8Jho36R3ZXo6iw52Q40mAAAAATtJ9AIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5156913565:AAE1tQ1ojwOZ83tI77iUP7PIZFSNmJXJDSc")
BOT_NAME = getenv("BOT_NAME", "Nelover")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "taha")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ttttz9")
ALIVE_NAME = getenv("ALIVE_NAME", "taha")
BOT_USERNAME = getenv("BOT_USERNAME", "en_9bot")
OWNER_ID = getenv("OWNER_ID", "5564738618")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "een6e")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "tttp9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tttp9")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5564738618").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

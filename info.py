import re
from os import environ
from ast import literal_eval as eval
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 7475759
API_HASH = "9a0128b1396fb0c1e0e2af0267a44a29"
BOT_TOKEN = "2146623895:AAGV5zzGJe0BmPkMoW5zkn9Fpuxf2i-y8O8"

# Bot settings
CACHE_TIME = "300"
USE_CAPTION_FILTER = False        
PICS = [
  "https://telegra.ph/file/6c3e0994e3d8f0d6d5b8d.jpg",
  "https://telegra.ph/file/112378346f55f1bf332b0.jpg",
  "https://telegra.ph/file/d9dc44f2d938df975d4e6.jpg",
  "https://telegra.ph/file/2dbb2278089fee7078c85.jpg",
  "https://telegra.ph/file/0faa6ca4f27522c5104b2.jpg",
  "https://telegra.ph/file/8cdf0c1c64b2807605435.jpg",
  "https://telegra.ph/file/662f41ef8fa2d45114700.jpg",
  "https://telegra.ph/file/61e5dd43220097e7bea57.jpg",
  "https://telegra.ph/file/d75221819b317e4d06598.jpg",
  "https://telegra.ph/file/a5f4eab0445da6d3d4720.jpg",
  "https://telegra.ph/file/5a7ab02ce1f53ecc1098f.jpg",
  "https://telegra.ph/file/31f833975728d83a66567.jpg",
]

# Admins, Channels & Users
ADMINS = [1103647866]
CHANNELS = [-1001485668506]
AUTH_USERS = ADMINS
AUTH_CHANNEL = -1001485668506
AUTH_GROUPS = -1001498025340
# MongoDB information
DATABASE_URI = "mongodb+srv://evamaria2:evamaria2@cluster0.tx3ho.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = -1001500220248
SUPPORT_CHAT = "PrimeFlix_Movies"
P_TTTI_SHOW_OFF = "True"
IMDB = "True"
MAX_LIST_ELM = 4
SINGLE_BUTTON = eval((environ.get('SINGLE_BUTTON', "True")))
CUSTOM_FILE_CAPTION = "`{file_name}`"


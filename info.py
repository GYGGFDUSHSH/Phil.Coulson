import re
from os import environ
from ast import literal_eval as eval
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 3020564
API_HASH = "91c026fadfdc442f504a0bd3e5c8cd18"
BOT_TOKEN = "1651274124:AAGL8ZRwA5D3EcNskAmKxx7aRokWBn26L98"

# Bot settings
CACHE_TIME = "300"
USE_CAPTION_FILTER = False
PICS = "https://telegra.ph/file/d32169a517600a90812a9.jpg"        

# Admins, Channels & Users
ADMINS = [1560645285]
CHANNELS = [-1001462830769]
AUTH_USERS = ADMINS
AUTH_CHANNEL = None
AUTH_GROUPS = -1001277599754

# MongoDB information
DATABASE_URI = "mongodb+srv://Wafikh:wafikh@cluster0.sjzmu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = -1001716242007
SUPPORT_CHAT = "MGMOVIEGRAM"
P_TTTI_SHOW_OFF = "True"
IMDB = "True"
SINGLE_BUTTON = bool((environ.get('SINGLE_BUTTON', False)))
CUSTOM_FILE_CAPTION = "`{file_name}`"

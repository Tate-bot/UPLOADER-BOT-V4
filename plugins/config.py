import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7824090160:AAGZ17TUz4pPvl-YIRA2HLwHxlXdf4JYiHk")
    
    API_ID = int(os.environ.get("API_ID", "28810170"))
    
    API_HASH = os.environ.get("API_HASH", "d8fa6697eb16406d15015179aa641fee")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = ""
    
    FREE_USER_MAX_FILE_SIZE = 2097152000

    MAX_SPLIT_SIZE = 4187407334
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "Tateurl_uploader_bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://muktarhussainff5:3ChQSSJmaCri2LLi@cluster0.pykyf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "Tateurl_uploader_bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002291255801"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002098980021")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5560200410"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tateurl_uploader_bot")
                                  

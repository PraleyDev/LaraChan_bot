#(©)Codeflix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7387239953:AAEPoYNdZNWJ4eELPaYZs88DQcNueV-N7ls")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22281455"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dc3bf5521f4cd885f20e1fdd6aadd0ba")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002094207998"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5652322516"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "larachan_bot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002439585405"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002323962743"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002393105826"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002494281614"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention} ⚡,\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/RyumaHindiSubAnime'>𝐑ʏᴜᴍᴀ 𝐀ɴɪᴍᴇ</a></b>")
try:
    ADMINS=[5652322516]
    for x in (os.environ.get("ADMINS", "5652322516").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention},\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ • ᴛʀʏ ᴀɢᴀɪɴ • ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/RyumaHindiSubAnime'>𝐑ʏᴜᴍᴀ 𝐀ɴɪᴍᴇ</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Praley_dev"

ADMINS.append(OWNER_ID)
ADMINS.append(5652322516)

LOG_FILE_NAME = "urrsanji.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ OWNER : <a href='tg://user?id={OWNER_ID}'>Praley</a>\n○ MAIN CHANNEL : <a href='https://t.me/RyumaHindiSubAnime'>RYUMA ANIME</a>\n○ ONGOING CHANNEL : <a href='https://t.me/RyumaOngoingAnime'>ONGOING RYUMA</a>\n○ OUR COMMUNITY : <a href='https://t.me/+d6UkrNV0bxc4NjVl'>CLICK HERE</a>\n○ DEVELOPER : <a href='https://t.me/RyumaHindiSubAnime'>PRALEY DEV</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ CLOSE", callback_data = "close"),
                    InlineKeyboardButton('🍁 MAIN CHANNEL', url='https://t.me/RyumaHindiSubAnime')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

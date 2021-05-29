from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIZFWCquxoG_Ervt_4d61DnSF3YKLI9AALGAgAClA5RVUG4_pmGDtAXHwQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Imteyaz_king For Telegram voice chat's](https://t.me/Imteyaz_support).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Imteyazking/D3VILMUSICBOT")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/FRIENDS_FOREVER_OFFICIAL_CHAT"
                    ),
                    InlineKeyboardButton(
                        "♥️ INFORMATION", url="https://t.me/Imteyaz_info"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💗OwNeR💥", url="https://t.me/Imteyaz_king"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♥️CREATOR✨", url="https://t.me/Imteyaz_king")
                ]
            ]
        )
   )



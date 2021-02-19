from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "My Source 😒", url="https://github.com/odysseusmax/animated-lamp"
                    ),
                    InlineKeyboardButton("Base Source", url="https://github.com/odysseusmax/animated-lamp"),
                ],
                [InlineKeyboardButton("Join Channel", url="https://t.me/Infinity_Bots")],
            ]
        ),
    )

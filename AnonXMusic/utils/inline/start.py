from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="جروب الدعم", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="جروب الدعم", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الي مجموعتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر و المساعده", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="مطور السورس", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="جروب الدعم", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="قناة السورس", url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons

from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton(" sᴜᴩᴩᴏʀᴛ ", url="https://t.me/Mutualanrelaxed"),
         InlineKeyboardButton(" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", url="https://t.me/Jrsss777"),
        ],
    ]

    START = """
Hᴇʏ {},
Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
Sᴏᴜʀᴄᴇ 😱 : [ɢɪᴛʜᴜʙ](https://github.com/ELDRAZI-17/FEUR)
Mᴀᴅᴇ ᴡɪᴛʜ 😘 ʙʏ : [ᴊᴀʀsss](https://t.me/Jrsss777) !
    """

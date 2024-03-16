class Txt(object):

    PRIVATE_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴅᴏ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ɪɴ ɴᴇɢʟɪɢɪʙʟᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏss ᴏғ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ
"""
    GROUP_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ɴᴇɢʟɪɢɪʙʟᴇ sɪᴢᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏᴏsɪɴɢ ᴛʜᴇ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ

❗**Yᴏᴜ ʜᴀsɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴍᴇ ʏᴇᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ғɪʀsᴛ sᴛᴀʀᴛ ᴍᴇ sᴏ ɪ ᴄᴀɴ ᴡᴏʀᴋ ғʟᴀᴡʟᴇssʟʏ**
"""
    PROGRESS_BAR = """<b>
┏━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━•
┣ 🗃️ Sɪᴢᴇ: {1} | {2}
┣ ⏳️ Dᴏɴᴇ : {0}%
┣ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣ ⏰️ Eᴛᴀ: {4}
┗━━━━━━━━━━━━━━━• </b>"""

    SEND_FFMPEG_CODE = """
Send me the correct ffmpeg code

• Format

ffmpeg -i input.mp4 <code> -c:v libx264 -crf 23 </code> output.mp4

<code> -c:v libx264 -crf 23 </code> This is your FFMPEG code

"""

    SEND_METADATA ="""
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="My Video" -metadata author="John Doe" -metadata:s:s title="Subtitle Title" -metadata:s:a title="Audio Title" -metadata:s:v title="Video Title" </code>

"""

    
    HELP_MSG = """
Available commands:-

➜ start - Check Bot is Working or not
➜ set_ffmpeg - Set Your Custom FFMPEG Code
➜ see_ffmpeg - See Your Custom FFMPEG Code
➜ del_ffmpeg - Delete Your Current FFMPEG Code
➜ set_metadata - To set custom metadata code
➜ see_ffmpeg - View custom ffmpeg code
➜ set_caption - Set Your Caption
➜ see_caption - See Your Caption
➜ del_caption - Delete Your Caption
➜ del_thumb - Delete Thumbnail
➜ view_thumb - View Thumbnail
➜ stats - See Current Status of Bot and No of Users [ADMIN]
➜ broadcast - Broadcast Message To All The Users [ADMIN]
➜ ban_user - Ban Perticualr User To Use The Bot [ADMIN]
➜ unban_user - Unban The User [ADMIN]
➜ banned_users - List Of Banned Users [ADMIN]


"""

    ABOUT_TXT = """<b>┏• Creator : <a href='tg://settings'>yours truly</a>\n┣• Channel : <a href='https://t.me/AnimeXWrld'>Anime Wrld</a>\n┗• Support Group : <a href='https://t.me/AnimeXWrld_Chat'>Anime Wrld Chat</a></b> """

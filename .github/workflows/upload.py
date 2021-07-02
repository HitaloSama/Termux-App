import os
from glob import glob

import pyrogram

short_rev = os.getenv("SHORT_REV")
long_rev = os.getenv("LONG_REV")
branch = os.getenv("BRANCH")
time = os.getenv("TIME")
md5 = os.getenv("MD5")
sha256 = os.getenv("SHA256")


with pyrogram.Client(
    "bot", os.getenv("API_ID"), os.getenv("API_HASH"), bot_token=os.getenv("BOT_TOKEN")
) as client:
    for path in glob("**/*.apk", recursive=True):
        client.send_document(
            document=path,
            caption=f"""
**Branch:** [{branch}](https://github.com/termux/termux-app/tree/{branch})
APK Built with the [{short_rev}](https://github.com/termux/termux-app/commit/{long_rev}) commit (Commit made on {time}).

**MD5:** `{md5}`
**SHA256:** `{sha256}`
""",
            chat_id=os.getenv("CHAT_ID"),
            parse_mode="markdown",
        )

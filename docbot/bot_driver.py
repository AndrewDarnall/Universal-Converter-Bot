""" This module contains the code for the Bot """

from os.path import join
from os import getenv
from sys import exit as EXIT_FAILURE
from subprocess import run as subproc_run

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types.messages_and_media.message import Message

from docbot.utils import replace_file_extension, get_basename


env_path = join("config", ".env")
load_dotenv(dotenv_path=env_path)

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

if API_ID is None:
    print(" !!! Check the Bot API_ID, the one you chose is None !!! ")
    EXIT_FAILURE(-1)


if API_HASH is None:
    print(" !!! Check the Bot API_HASH, the one you chose is None !!! ")
    EXIT_FAILURE(-1)


def main() -> None:
    """
    main: Wrapper which acts as the driver that determines
          the behavior of the bot
    """

    app = Client(
        "account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
    )

    # /start handler
    @app.on_message(filters.command("start") & filters.private)
    async def start_command(client: Client, message: Message) -> None:
        await message.reply(
            "Hi, I am converterbot! 😁\n"
            "Send me any file you wich to have converted into PDF format 📋"
        )

    # Echo handler
    @app.on_message(filters.text & filters.private)
    async def greet(client: Client, message: Message) -> None:
        await message.reply(
            "Sorry, I am not a chatbot, please send me a file to convert 😆🗣🚫"
        )

    # File handler
    @app.on_message(filters.document & filters.private)
    async def convert_file(client: Client, message: Message) -> None:

        file_name = message.document.file_name
        file_path = await message.download(file_name)

        result = subproc_run(
            ["libreoffice", "--headless", "--convert-to", "pdf", file_path],
            capture_output=True,
            text=True,
            check=True,
        )

        print(f"Subprocess output:\t{result.stdout}")
        print(f"Subprocess exit code:\t{result.returncode}")
        print(f"Error:\t{result.stderr}")

        if result.returncode == 0:
            target_file_base = get_basename(file_path)
            target_file = replace_file_extension(target_file_base, ".pdf")
            await message.reply_document(target_file)
        else:
            await message.reply(
                "I'm sorry but this file is not supported,"
                " so I cannot convert it into a .pdf 😔"
            )

    app.run()

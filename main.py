""" Main Driver for the Telegram Bot """

from asyncio import run

from docbot.bot_driver import main


if __name__ == "__main__":
    print(" <-> Launching Telegram Python Bot <-> ")

    run(main())

    print(" <-> Quit Telegram Python Bot <-> ")

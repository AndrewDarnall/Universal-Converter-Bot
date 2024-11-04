# Anything to PDF Converter Bot

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Build Status](https://github.com/AndrewDarnall/XML-Editing-Tool/actions/workflows/lint.yml/badge.svg)

<!--
    ![CI/CD](https://github.com/username/telegram-bot/actions/workflows/deploy.yml/badge.svg)
    ![Bot Status](https://img.shields.io/uptimerobot/status/m1234567890-abcdef)
    ![Unit Tests](https://github.com/username/telegram-bot/actions/workflows/tests.yml/badge.svg)
-->


---

## Requirements

| Software      | Version  |
|---------------|----------|
| Python        | `3.12.2` |
| pip           | `23.3.1` |
| Docker        | `20.10.5`|
| LibreOffice   | `7.0.4.2`|


---

The bot is a very simple tool made to aid a simple and hassle-free conversion
of any type of `libreoffice` supported document into a `.pdf` file (without having to go through a sketchy website)

---

# Testing the bot

My bot is currently deployed on my remote server, you can [try it](https://t.me/Airport_Pookie_bot) if you'd like

---

# Running the bot locally

In order to run the bot functionality locally, simply follow the steps listed below

---

## Setup & Configuration

To run the same Telegram bot for youreself, you need to create a `Telegram Account` and then register
an app as a `Telegram Developer` following [this guide](https://core.telegram.org/api/obtaining_api_id)
<br>
After completing the previous tasks you will endup with an `API_ID` and `API_HASH` which are tied
to *your personal telegram account*
<br>
<br>
Finally register a new `Telegram Bot` via the [Bot Father](https://telegram.me/BotFather), after which
you will obtain the `BOT_TOKEN`

## Installation & Usage

1) Clone the git repository and change into the repository's directory

```bash
git clone https://github.com/AndrewDarnall/Universal-Converter-Bot.git
cd Universal-Converter-Bot
```

2) Populate the variables within the `./scripts/envs_setup.sh` script with your personal `API_ID`, `API_HASH` and `BOT_TOKEN` values, and run the following script

```bash
bash ./scripts/envs_setup.sh
```

3) Build the docker container from the `Dockerfile`

```bash
docker build -t converter-bot-py .
```

4) Run the docker container, which will in turn run the Telegram Bot and accept messages sent to it

```bash
docker run -d -e API_ID=$API_ID -e API_HASH=$API_HASH -e BOT_TOKEN=$BOT_TOKEN --name converter_bot_py converter-bot-py
```

5) Open a `Telegram Client` of choice and begin a chat with *your* telegram bot, after which
you will be able to send any document you wich, as long as it is smaller than `2GB` and it will
return a converted file into `.pdf` format, as long as `libreoffice` supports said conversion

---

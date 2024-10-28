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

| Software  | Version  |
|-----------|----------|
| Python    | `3.12.2` |
| pip       | `23.3.1` |
| Docker    | `20.10.5`|       


---

The bot is a very simple tool made to aid a simple and hassle-free conversion
of any type of `libreoffice` supported document into a `.pdf` file (without having to go through a sketchy website)

---

# Usage

To run the same Telegram bot, perform the following steps

1) Clone the git repository and change into the repository's directory

```bash
git clone https://github.com/AndrewDarnall/Universal-Converter-Bot.git
cd Universal-Converter-Bot
```

2) Build the docker container from the `Dockerfile`

```bash
docker build -t converter-bot-py .
```

3) Run the docker container, which will in turn run the Telegram Bot and accept messages sent to it

```bash
docker run -d --name converter_bot_py -e TELEGRAM_TOKEN=<your-telegram-bot-token> converter-bot-py
```

---
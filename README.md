# MIT Discord Pirate Bot

A small Discord bot for the optional Module 3 assignment. It responds to `$hello` and answers `$question` messages in a friendly pirate voice using OpenRouter.

## Setup

1. Create a Discord application and bot, turn on **Message Content Intent** in the bot settings, and invite the bot to your server with permission to view the channel, read messages, and send messages.
2. Create an OpenRouter API key. Copy `.env.example` to a new file named `.env`, then enter your Discord bot token and OpenRouter key there. Keep `.env` private; it is excluded from Git.
3. In a terminal (locally or in a GitHub Codespace), install the packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Run `python discord_only.py`, then type `$hello` in a channel the bot can access. Stop it with Ctrl+C.
5. Run `python mybot.py`, then try `$question What is the best treasure?` in Discord. The process must stay running for the bot to respond.

The bot uses OpenRouter's `openrouter/free` model router. Free model availability and rate limits can change. Messages sent with `$question` are sent to OpenRouter, so do not include private or sensitive information.

## Credits

Adapted for OpenRouter from the course starter project [avathuy/dbot](https://github.com/avathuy/dbot).

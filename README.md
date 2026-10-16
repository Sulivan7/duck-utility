# Duck-utility

A Discord bot that shows **Counter-Strike 2 utility lineups** (smokes, flashes, molotovs
and HE grenades) right in the chat.

> 🚧 **Work in progress** — the bot is under active development.

## ✨ Planned features

- `/smoke <map> <position>` — get a GIF showing exactly where to aim and how to throw
- Autocomplete for maps and positions while you type
- Support for smokes, flashes, molotovs and HE grenades
- Clean embed responses

## 🛠️ Tech stack

- [Python](https://www.python.org/) 3.14+
- [discord.py](https://discordpy.readthedocs.io/)

## 🚀 Getting started

### Prerequisites

- Python 3.14+
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

### Installation

```powershell
git clone https://github.com/Sulivan7/duck-utility.git
cd duck-utility
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### Environment variables

Create a `.env` file at the project root (it is already ignored by git):

```dotenv
DISCORD_TOKEN=your-bot-token-here
```

| Variable        | Required | Description                                                                                     |
| --------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `DISCORD_TOKEN` | Yes      | Your bot token from the [Discord Developer Portal](https://discord.com/developers/applications) |

### Running

```powershell
python -m duck_utility
```

## 💬 Commands

| Command | Description                |
| ------- | -------------------------- |
| `/ping` | Check if the bot is online |

## 🙏 Credits

Initial lineup GIFs from [Tactical Toss Tutor](https://github.com/bubfusion/Tactical-Toss-Tutor)
by [@bubfusion](https://github.com/bubfusion), licensed under MIT.
This project is an independent rewrite inspired by it.

## 📄 License

This project is licensed under the [MIT License](LICENSE)

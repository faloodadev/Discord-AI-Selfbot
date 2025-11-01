# Discord AI Selfbot

## Overview
This is a Python-based Discord selfbot that uses AI to automatically respond to messages. The bot runs on a real Discord user account and uses Groq API's Llama-3 or OpenAI's GPT models to generate responses. It can participate in conversations, recognize images, and provide various utility commands.

**⚠️ Important Warning**: Using selfbots violates Discord's Terms of Service and may result in account termination. Use at your own risk on an account you don't mind losing.

## Project Architecture

### Core Components
- **main.py**: Main bot file containing event handlers and conversation logic
- **cogs/**: Command modules (error_handler, general, management)
- **utils/**: Utility modules for AI, database, helpers, and error handling
- **config/**: Configuration files (.env, config.yaml, instructions.txt)

### Technology Stack
- **Python 3.11**: Runtime environment
- **discord.py-self 2.0.1**: Selfbot library for Discord integration
- **Groq API**: Free LLM API (Llama-3 models)
- **OpenAI API**: Optional GPT models
- **SQLite**: Local database for storing channel and user data
- **aiohttp**: Async HTTP client

## Setup Instructions

### Step 1: Configure Your Discord Token
1. Open `config/.env`
2. Add your Discord user token to `DISCORD_TOKEN=`
   - To get your token:
     - Open Discord in your browser
     - Press `Ctrl+Shift+I` (Windows) or `Cmd+Opt+I` (Mac)
     - Go to the Network tab
     - Send any message or change servers
     - Find headers like "messages?limit=50", "science", or "preview"
     - Copy the Authorization value (your token)

### Step 2: Configure API Keys
In `config/.env`, add one of these API keys:

**Option 1 - Groq (Free):**
- Go to https://console.groq.com/keys
- Sign up and get your free API key
- Add to `GROQ_API_KEY=`

**Option 2 - OpenAI (Paid):**
- Go to https://platform.openai.com/api-keys
- Get your API key
- Add to `OPENAI_API_KEY=`

### Step 3: Configure Bot Settings
Edit `config/config.yaml`:

**Required Settings:**
- `owner_id`: Your Discord user ID (NOT the bot account's ID)
  - Right-click your name in Discord → Copy User ID
  - Enable Developer Mode in Discord settings if needed
- `trigger`: Word(s) the bot responds to (e.g., "assistant", "bot")

**Optional Settings:**
- `prefix`: Command prefix (default: ~)
- `allow_dm`: Bot responds in DMs (default: true)
- `allow_gc`: Bot responds in group chats (default: true)
- `realistic_typing`: Simulates typing delay (default: false)
- `batch_messages`: Waits to collect multiple messages before responding (default: true)
- `hold_conversation`: Continues conversations without trigger word (default: true)

### Step 4: Customize AI Personality
Edit `config/instructions.txt` to change how the AI behaves. Example:
```
You are a helpful AI assistant. Be friendly, conversational, and engaging. Respond naturally to messages and maintain the flow of conversation.
```

### Step 5: Run the Bot
The bot will automatically start when you open this Repl. Check the Console tab to see if it's running properly.

## Using the Bot

### Activating Channels
1. The bot won't respond anywhere until you activate channels
2. In Discord, type: `~toggleactive <channelID>`
   - To get channel ID: Right-click channel → Copy Channel ID
   - Or use `~toggleactive` in the channel itself
3. The bot will now respond in that channel when mentioned or trigger word is used

### Available Commands
All commands use the `~` prefix by default:

- `~pause` - Pause/unpause AI responses
- `~analyse @user` - Analyze a user's message history
- `~wipe` - Clear conversation history
- `~ping` - Check bot latency
- `~toggleactive [channelID]` - Toggle channel activation
- `~toggledm` - Toggle DM responses
- `~togglegc` - Toggle group chat responses
- `~ignore @user` - Block a user from using the bot
- `~reload` - Reload all command modules
- `~prompt [text/clear]` - View/set/clear AI prompt
- `~restart` - Restart the bot
- `~shutdown` - Stop the bot
- `~help` - Show all commands

### How Conversations Work
The bot responds when:
- Someone uses the trigger word (set in config.yaml)
- Someone mentions the bot account
- Someone replies to the bot's message
- In DMs (if allowed)
- In group chats (if allowed)
- In active conversations (if hold_conversation is enabled)

## Features

### Anti-Spam Protection
- Limits: 5 messages per 10 seconds per user
- Cooldown: 60 seconds when exceeded
- Prevents API abuse

### Message Batching
When enabled, the bot waits 10 seconds to collect multiple messages from the same user before responding. This:
- Reduces API calls
- Makes responses more natural
- Handles rapid-fire messages better

### Image Recognition
The bot can analyze images sent in messages and incorporate them into responses using vision-capable models.

### Conversation History
- Maintains last 15 messages per user per channel
- Provides context for better responses
- Can be cleared with `~wipe` command

## Database

The bot uses SQLite to store:
- **Active channels**: Channels where the bot responds
- **Ignored users**: Users blocked from using the bot

Database location: `config/bot_data.db`

## Recent Changes

### 2024-11-01: Replit Setup
- Installed Python 3.11 and all dependencies
- Fixed discord.py-self integration (selfbot support)
- Created .env file from template
- Added default AI instructions
- Updated .gitignore for Python/Replit
- Configured workflow for automatic startup
- Set up proper selfbot initialization

## Troubleshooting

### Bot Not Responding
1. Check that you've activated channels with `~toggleactive`
2. Verify trigger word is being used
3. Check Console tab for errors
4. Ensure API keys are valid
5. Make sure the bot account isn't the same as owner_id

### Login Failure
- Verify Discord token in `.env` is correct
- Token format should be a long string with letters and numbers
- Don't include quotes around the token

### API Errors
- Check that API keys are valid
- Groq: Verify free tier limits haven't been exceeded
- OpenAI: Ensure billing is set up if using paid API

### Import Errors
- The bot uses `discord.py-self`, not regular `discord.py`
- If you see import errors, the workflow will handle reinstallation

## User Preferences
- None configured yet

## Security Notes
- Never share your Discord token or API keys
- The `.env` file is in `.gitignore` to prevent accidental commits
- Use a separate Discord account for the bot
- Be aware this violates Discord's Terms of Service

## Support
For issues or questions:
- Check the original project: https://github.com/Najmul190/Discord-AI-Selfbot
- Join the support Discord: https://discord.gg/yUWmzQBV4P

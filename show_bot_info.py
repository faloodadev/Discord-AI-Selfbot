import os
import discord
from dotenv import load_dotenv
from utils.helpers import get_env_path

env_path = get_env_path()
load_dotenv(dotenv_path=env_path, override=True)

TOKEN = os.getenv("DISCORD_TOKEN")

class InfoBot(discord.Client):
    async def on_ready(self):
        print(f"\n{'='*60}")
        print(f"🤖 SELFBOT CONNECTED SUCCESSFULLY!")
        print(f"{'='*60}")
        print(f"Username: {self.user.name}")
        print(f"User ID: {self.user.id}")
        print(f"Discriminator: #{self.user.discriminator}")
        print(f"{'='*60}")
        print(f"\nℹ️  CONFIGURATION INSTRUCTIONS:")
        print(f"1. Copy the User ID above: {self.user.id}")
        print(f"2. This is the bot account - you need YOUR user ID for owner_id")
        print(f"3. To get YOUR user ID:")
        print(f"   - Enable Developer Mode in Discord Settings > Advanced")
        print(f"   - Right-click your username and select 'Copy User ID'")
        print(f"4. Edit config/config.yaml and update:")
        print(f"   - owner_id: <your_user_id>")
        print(f"   - trigger: \"<word_to_trigger_bot>\"")
        print(f"{'='*60}\n")
        await self.close()

if __name__ == "__main__":
    client = InfoBot()
    client.run(TOKEN, log_handler=None)

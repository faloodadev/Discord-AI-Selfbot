from discord.ext import commands
import discord
from utils.mood import mood_manager

class OwnerRemote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="status", aliases=["stats", "info"])
    async def bot_status(self, ctx):
        if ctx.author.id != self.bot.owner_id:
            return
        
        status = f"**🤖 Cuss Status Report**\n\n"
        status += f"**Account:** {self.bot.user.name}#{self.bot.user.discriminator}\n"
        status += f"**User ID:** {self.bot.user.id}\n"
        status += f"**Current Mood:** {mood_manager.get_mood()}\n"
        status += f"**Active Channels:** {len(self.bot.active_channels)}\n"
        status += f"**Paused:** {'Yes' if self.bot.paused else 'No'}\n"
        status += f"**Allow DMs:** {'Yes' if self.bot.allow_dm else 'No'}\n"
        status += f"**Allow Group Chats:** {'Yes' if self.bot.allow_gc else 'No'}\n"
        status += f"**Realistic Typing:** {'Yes' if self.bot.realistic_typing else 'No'}\n"
        status += f"**Active Conversations:** {len(self.bot.active_conversations)}\n"
        
        await ctx.send(status)
    
    @commands.command(name="say")
    async def remote_say(self, ctx, channel_id: int = None, *, message: str):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not channel_id:
            await ctx.send("Usage: ~say <channel_id> <message>")
            return
        
        try:
            channel = self.bot.get_channel(channel_id)
            if not channel:
                await ctx.send(f"❌ Channel {channel_id} not found!")
                return
            
            await channel.send(message)
            await ctx.send(f"✅ Message sent to {channel.name if hasattr(channel, 'name') else 'DM'}!")
        except Exception as e:
            await ctx.send(f"❌ Error sending message: {e}")
    
    @commands.command(name="dm")
    async def remote_dm(self, ctx, user_id: int, *, message: str):
        if ctx.author.id != self.bot.owner_id:
            return
        
        try:
            user = await self.bot.fetch_user(user_id)
            if not user:
                await ctx.send(f"❌ User {user_id} not found!")
                return
            
            await user.send(message)
            await ctx.send(f"✅ DM sent to {user.name}!")
        except Exception as e:
            await ctx.send(f"❌ Error sending DM: {e}")
    
    @commands.command(name="channels", aliases=["activechannels"])
    async def list_channels(self, ctx):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not self.bot.active_channels:
            await ctx.send("No active channels configured. Use ~toggleactive to add channels.")
            return
        
        channel_list = "**Active Channels:**\n"
        for channel_id in self.bot.active_channels:
            try:
                channel = self.bot.get_channel(channel_id)
                if channel:
                    channel_list += f"• {channel.name} (ID: {channel_id})\n"
                else:
                    channel_list += f"• Unknown Channel (ID: {channel_id})\n"
            except:
                channel_list += f"• Unknown Channel (ID: {channel_id})\n"
        
        await ctx.send(channel_list)
    
    @commands.command(name="setpresence", aliases=["presence"])
    async def set_presence(self, ctx, status: str = None, *, activity: str = None):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not status:
            await ctx.send("**Usage:** ~setpresence <online/idle/dnd/invisible> [activity text]")
            return
        
        status_map = {
            'online': discord.Status.online,
            'idle': discord.Status.idle,
            'dnd': discord.Status.dnd,
            'invisible': discord.Status.invisible
        }
        
        discord_status = status_map.get(status.lower())
        if not discord_status:
            await ctx.send("❌ Invalid status! Use: online, idle, dnd, or invisible")
            return
        
        try:
            if activity:
                await self.bot.change_presence(
                    status=discord_status,
                    activity=discord.Game(name=activity)
                )
                await ctx.send(f"✅ Presence updated: {status} - {activity}")
            else:
                await self.bot.change_presence(status=discord_status)
                await ctx.send(f"✅ Status updated: {status}")
        except Exception as e:
            await ctx.send(f"❌ Error updating presence: {e}")
    
    @commands.command(name="toggletyping")
    async def toggle_typing(self, ctx):
        if ctx.author.id != self.bot.owner_id:
            return
        
        self.bot.realistic_typing = not self.bot.realistic_typing
        status = "enabled" if self.bot.realistic_typing else "disabled"
        await ctx.send(f"✅ Realistic typing {status}")
    
    @commands.command(name="conversations", aliases=["convos"])
    async def list_conversations(self, ctx):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not self.bot.active_conversations:
            await ctx.send("No active conversations")
            return
        
        import time
        current_time = time.time()
        convo_list = "**Active Conversations:**\n"
        
        for key, timestamp in self.bot.active_conversations.items():
            user_id, channel_id = key.split('-')
            time_ago = int(current_time - timestamp)
            
            try:
                user = await self.bot.fetch_user(int(user_id))
                channel = self.bot.get_channel(int(channel_id))
                
                user_name = user.name if user else f"User {user_id}"
                channel_name = channel.name if channel and hasattr(channel, 'name') else f"Channel {channel_id}"
                
                convo_list += f"• {user_name} in {channel_name} ({time_ago}s ago)\n"
            except:
                convo_list += f"• User {user_id} in Channel {channel_id} ({time_ago}s ago)\n"
        
        await ctx.send(convo_list)
    
    @commands.command(name="clearhistory")
    async def clear_history(self, ctx, user_id: int = None):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if user_id:
            cleared = 0
            keys_to_remove = [key for key in self.bot.message_history.keys() if key.startswith(f"{user_id}-")]
            for key in keys_to_remove:
                del self.bot.message_history[key]
                cleared += 1
            
            await ctx.send(f"✅ Cleared {cleared} conversation(s) with user {user_id}")
        else:
            count = len(self.bot.message_history)
            self.bot.message_history.clear()
            await ctx.send(f"✅ Cleared all {count} conversations from history")
    
    @commands.command(name="eval")
    async def evaluate_code(self, ctx, *, code: str):
        if ctx.author.id != self.bot.owner_id:
            return
        
        try:
            if code.startswith("```python"):
                code = code[9:-3]
            elif code.startswith("```"):
                code = code[3:-3]
            
            result = eval(code)
            await ctx.send(f"**Result:**\n```python\n{result}\n```")
        except Exception as e:
            await ctx.send(f"**Error:**\n```python\n{e}\n```")
    
    @commands.command(name="exec")
    async def execute_code(self, ctx, *, code: str):
        if ctx.author.id != self.bot.owner_id:
            return
        
        try:
            if code.startswith("```python"):
                code = code[9:-3]
            elif code.startswith("```"):
                code = code[3:-3]
            
            exec(code)
            await ctx.send("✅ Code executed successfully")
        except Exception as e:
            await ctx.send(f"**Error:**\n```python\n{e}\n```")
    
    @commands.command(name="getpfp", aliases=["avatar"])
    async def get_avatar(self, ctx, user_id: int = None):
        if ctx.author.id != self.bot.owner_id:
            return
        
        try:
            if user_id:
                user = await self.bot.fetch_user(user_id)
            else:
                user = self.bot.user
            
            avatar_url = user.display_avatar.url
            await ctx.send(f"**{user.name}'s Avatar:**\n{avatar_url}")
        except Exception as e:
            await ctx.send(f"❌ Error fetching avatar: {e}")
    
    @commands.command(name="setchannel")
    async def set_active_channel(self, ctx, channel_id: int = None):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not channel_id:
            channel_id = ctx.channel.id
        
        await ctx.invoke(self.bot.get_command('toggleactive'), channel_id)

async def setup(bot):
    await bot.add_cog(OwnerRemote(bot))

from discord.ext import commands
from utils.mood import mood_manager, MOODS

class MoodCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="setmood", aliases=["mood"])
    async def set_mood(self, ctx, mood: str = None):
        if ctx.author.id != self.bot.owner_id:
            return
        
        if not mood:
            current_mood = mood_manager.get_mood()
            available_moods = ", ".join(MOODS.keys())
            await ctx.send(f"Current mood: **{current_mood}**\nAvailable moods: {available_moods}")
            return
        
        mood = mood.lower()
        if mood_manager.set_mood(mood):
            await ctx.send(f"✨ Mood changed to: **{mood}**")
        else:
            available_moods = ", ".join(MOODS.keys())
            await ctx.send(f"❌ Invalid mood! Available: {available_moods}")
    
    @commands.command(name="moodinfo")
    async def mood_info(self, ctx):
        if ctx.author.id != self.bot.owner_id:
            return
        
        current_mood = mood_manager.get_mood()
        mood_data = MOODS.get(current_mood, {})
        
        info = f"**Current Mood:** {current_mood}\n"
        info += f"**Typing Speed:** {mood_data.get('typing_delay_multiplier', 1.0)}x\n"
        info += f"**Chattiness:** {mood_data.get('chattiness', 1.0)}x\n"
        info += f"**Common Responses:** {', '.join(mood_data.get('responses', []))}"
        
        await ctx.send(info)

async def setup(bot):
    await bot.add_cog(MoodCommands(bot))

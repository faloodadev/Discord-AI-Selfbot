import discord
import aiohttp
import io
from utils.mood import pfp_manager
from utils.ai import client, model

async def handle_pfp_change(message, image_url, bot):
    try:
        if message.author.id != bot.owner_id and len(message.attachments) > 0:
            likes_it, reason = await pfp_manager.analyze_image_for_pfp(image_url, client, model)
            
            if likes_it:
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as resp:
                        if resp.status == 200:
                            image_data = await resp.read()
                            
                            try:
                                await bot.user.edit(avatar=image_data)
                                pfp_manager.add_liked_pfp(image_url)
                                pfp_manager.set_current_pfp(image_url)
                                
                                await message.channel.send(f"omg i love this!! changed my pfp 💕")
                                return True
                            except discord.HTTPException as e:
                                if "avatar" in str(e).lower():
                                    await message.channel.send(f"tried to change it but discord being weird rn lol")
                                return False
        
        if pfp_manager.should_change_pfp_back():
            old_pfp = pfp_manager.get_random_old_pfp()
            if old_pfp and old_pfp != pfp_manager.pfp_history.get('current'):
                async with aiohttp.ClientSession() as session:
                    async with session.get(old_pfp) as resp:
                        if resp.status == 200:
                            image_data = await resp.read()
                            try:
                                await bot.user.edit(avatar=image_data)
                                pfp_manager.set_current_pfp(old_pfp)
                                return True
                            except:
                                pass
        
        return False
        
    except Exception as e:
        print(f"Error handling PFP: {e}")
        return False

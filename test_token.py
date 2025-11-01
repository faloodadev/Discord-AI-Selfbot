#!/usr/bin/env python3
"""
Token verification script for Discord AI Selfbot
This script helps you verify your Discord token is correct
"""

import os
from dotenv import load_dotenv

print("=" * 60)
print("Discord Token Verification Script")
print("=" * 60)

# Load .env file
load_dotenv(dotenv_path="config/.env", override=True)

token = os.getenv("DISCORD_TOKEN")

print(f"\n1. Token loaded from .env: {'✓ Yes' if token else '✗ No'}")

if token:
    print(f"2. Token length: {len(token)} characters")
    print(f"3. Token preview: {token[:20]}...{token[-10:] if len(token) > 30 else ''}")
    print(f"4. Has whitespace: {'✗ Yes (REMOVE IT!)' if token != token.strip() else '✓ No'}")
    has_quotes = '"' in token or "'" in token
    print(f"5. Has quotes: {'✗ Yes (REMOVE THEM!)' if has_quotes else '✓ No'}")
    print(f"6. Starts with 'Bot': {'✗ Yes (REMOVE IT! User tokens dont need Bot prefix)' if token.strip().startswith('Bot ') else '✓ No'}")
    
    # Check if it's still the placeholder
    if token == "TOKEN_GOES_HERE":
        print("\n⚠️  ERROR: You haven't replaced the placeholder token!")
        print("   Please edit config/.env and add your real Discord user token.")
    elif len(token) < 50:
        print("\n⚠️  WARNING: Token seems too short. Discord tokens are typically 59+ characters.")
        print("   Make sure you copied the entire token.")
    else:
        print("\n✓ Token format looks okay!")
        print("\nNext step: Testing Discord connection...")
        
        import asyncio
        import discord
        
        async def test_login():
            try:
                client = discord.Client()
                
                @client.event
                async def on_ready():
                    print(f"\n✓✓✓ SUCCESS! Logged in as {client.user.name} ({client.user.id})")
                    await client.close()
                
                await client.start(token.strip())
            except discord.errors.LoginFailure as e:
                print(f"\n✗✗✗ LOGIN FAILED: {e}")
                print("\nPossible causes:")
                print("1. Wrong token - Make sure you're copying the Authorization header value")
                print("2. Analytics token - Don't use tokens from 'science' or 'analytics' requests")
                print("3. Expired token - Try logging out and back in to get a fresh token")
                print("\nHow to get the CORRECT token:")
                print("- Open Discord in browser (discord.com/app)")
                print("- Open DevTools (F12) → Network tab")
                print("- Filter by 'messages' or 'gateway'")  
                print("- Send a message or reload")
                print("- Click on a request → Headers → Request Headers → Authorization")
                print("- Copy the ENTIRE value (no quotes, no 'Bot' prefix)")
            except Exception as e:
                print(f"\n✗✗✗ ERROR: {e}")
        
        try:
            asyncio.run(test_login())
        except KeyboardInterrupt:
            print("\n\nTest interrupted.")
else:
    print("\n✗ No token found in .env file!")
    print("   Please edit config/.env and add your Discord user token.")

print("\n" + "=" * 60)

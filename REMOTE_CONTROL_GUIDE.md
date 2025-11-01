# 🎮 Remote Control Guide for Cuss Selfbot

You can now control the Cuss selfbot remotely from anywhere through Discord! All commands work only for the owner (your Discord ID configured in config.yaml).

## 🔐 Owner-Only Access

All these commands are **exclusive to you** (owner_id). No one else can use them.

---

## 📊 Status & Monitoring Commands

### `~status` (aliases: `~stats`, `~info`)
Get complete status report of the selfbot

**Example:**
```
~status
```

**Shows:**
- Account username and ID
- Current mood
- Active channels count
- Pause status
- DM/Group chat settings
- Realistic typing status
- Active conversations

---

### `~channels` (aliases: `~activechannels`)
List all channels where Cuss is active and responding

**Example:**
```
~channels
```

---

### `~conversations` (aliases: `~convos`)
See all active conversations with timestamps

**Example:**
~conversations
```

**Shows:**
- Who Cuss is talking to
- Which channels
- How long ago the last message was

---

## 💬 Remote Messaging Commands

### `~say <channel_id> <message>`
Make Cuss send a message to any channel

**Examples:**
```
~say 1234567890 hey everyone!
~say 1234567890 just checking in
```

**How to get channel ID:**
1. Enable Developer Mode in Discord
2. Right-click any channel → Copy Channel ID

---

### `~dm <user_id> <message>`
Make Cuss send a DM to anyone

**Examples:**
```
~dm 9876543210 hey! how are you?
~dm 9876543210 sent you that file
```

**How to get user ID:**
1. Enable Developer Mode in Discord
2. Right-click username → Copy User ID

---

## 🎭 Mood & Personality Control

### `~setmood <mood>` (aliases: `~mood`)
Change Cuss's current mood instantly

**Available Moods:**
- `happy` - Cheerful and positive
- `excited` - Energetic and enthusiastic
- `tired` - Slow responses, less chatty
- `stressed` - Anxious about exams/school
- `bored` - Dry, brief responses
- `playful` - Teasing, fun
- `annoyed` - Short, irritated
- `romantic` - Sweet, affectionate (for you)

**Examples:**
```
~setmood excited
~setmood tired
~mood                 (shows current mood)
```

---

### `~moodinfo`
Get detailed information about current mood state

**Shows:**
- Current mood
- Typing speed multiplier
- Chattiness level
- Common response patterns

---

## ⚙️ Behavior Control

### `~pause`
Pause/unpause all AI responses (existing command)

**Example:**
```
~pause
```

---

### `~toggletyping`
Enable/disable realistic typing delays

**Example:**
```
~toggletyping
```

**Effect:**
- ON: Cuss types at human speed with delays
- OFF: Instant responses

---

### `~toggledm`
Enable/disable DM responses (existing command)

---

### `~togglegc`
Enable/disable group chat responses (existing command)

---

### `~toggleactive [channel_id]`
Activate/deactivate channels for responses (existing command)

**Examples:**
```
~toggleactive              (toggles current channel)
~toggleactive 1234567890   (toggles specific channel)
```

---

## 🎨 Presence & Appearance

### `~setpresence <status> [activity]` (aliases: `~presence`)
Change Cuss's Discord status and activity

**Status Options:**
- `online` - Green dot
- `idle` - Yellow/away
- `dnd` - Red/do not disturb
- `invisible` - Appear offline

**Examples:**
```
~setpresence online
~setpresence idle studying for boards
~setpresence dnd busy rn
~setpresence invisible
```

---

### `~getpfp [user_id]` (aliases: `~avatar`)
Get avatar URL for Cuss or any user

**Examples:**
```
~getpfp                  (gets Cuss's current avatar)
~getpfp 1234567890       (gets someone else's avatar)
```

---

## 🗑️ Data Management

### `~clearhistory [user_id]`
Clear conversation history to reset context

**Examples:**
```
~clearhistory                (clears ALL history)
~clearhistory 1234567890     (clears history with specific user)
```

**Use when:**
- Conversations get too long
- Want to reset context
- AI is remembering old info

---

### `~wipe`
Clear conversation history for current channel (existing command)

---

## 🛠️ Advanced Commands

### `~eval <code>`
Evaluate Python expressions and see results

**Example:**
```
~eval 2 + 2
~eval len(bot.active_channels)
~eval bot.user.name
```

**⚠️ Advanced use only!**

---

### `~exec <code>`
Execute Python code

**Example:**
```python
~exec
```python
print("Hello from Cuss!")
```
```

**⚠️ Very advanced use only! Can break things if misused.**

---

### `~reload`
Reload all cog modules (existing command)

---

### `~restart`
Restart the entire bot (existing command)

---

### `~shutdown`
Shut down the bot (existing command)

---

## 💡 Practical Use Cases

### Scenario 1: Quick Status Check
```
~status
~conversations
```

### Scenario 2: Make Her Talk Somewhere
```
~say 1234567890 omg just saw this meme lol
```

### Scenario 3: Change Mood for Conversation
```
~setmood romantic
(now talk to her - she'll be more affectionate)
```

### Scenario 4: Set Realistic Presence
```
~setpresence idle studying rn
~toggletyping
```

### Scenario 5: Emergency Stop
```
~pause
(stops all responses immediately)
```

### Scenario 6: Reset Everything
```
~clearhistory
~setmood happy
~toggleactive
```

---

## 📱 Mobile Access

All these commands work from:
- Discord Desktop
- Discord Mobile App
- Discord Web
- Any DM with yourself
- Any channel where you can message

**Pro Tip:** DM yourself and use it as a control panel!

---

## 🔒 Security Notes

1. **Only you** (owner_id) can use these commands
2. Commands fail silently for others (no error shown)
3. Never share your owner_id
4. Be careful with `~eval` and `~exec` - they run actual code

---

## ⚡ Quick Command Reference

**Monitoring:**
- `~status` - Full status report
- `~channels` - List active channels
- `~conversations` - Active convos

**Control:**
- `~say <channel> <msg>` - Send message
- `~dm <user> <msg>` - Send DM
- `~setmood <mood>` - Change mood
- `~toggletyping` - Toggle typing delays
- `~pause` - Pause/unpause

**Appearance:**
- `~setpresence <status> [activity]` - Change status
- `~getpfp [user]` - Get avatar

**Management:**
- `~clearhistory [user]` - Clear history
- `~reload` - Reload cogs
- `~restart` - Restart bot

---

## 🎯 Tips & Tricks

1. **Use ~status frequently** to monitor what's happening
2. **Set mood before conversations** for appropriate responses
3. **Use ~say for natural interruptions** in group chats
4. **Toggle typing ON** for most realistic experience
5. **Clear history periodically** to keep responses fresh
6. **Set presence** to match real-life situations
7. **Use ~conversations** to see who she's talking to

---

## 🆘 Troubleshooting

**Bot not responding to commands?**
- Check that your owner_id is set correctly in config.yaml
- Make sure you're using the right prefix (~)
- Check ~status to see if bot is paused

**Can't control from certain channels?**
- Commands work everywhere, even where bot isn't active
- Try DMing yourself

**Want to test commands safely?**
- Use ~eval and ~exec carefully
- Test ~say in your own server first
- Use ~pause before making changes

---

Enjoy full remote control of your Cuss AI selfbot! 🎮✨

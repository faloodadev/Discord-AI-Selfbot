import random
import json
import os
from datetime import datetime, timedelta

MOOD_FILE = "config/mood_state.json"
PFP_HISTORY_FILE = "config/pfp_history.json"

MOODS = {
    "happy": {
        "responses": ["😊", "hehe", "yay", "omg yes"],
        "typing_delay_multiplier": 0.8,
        "chattiness": 1.2
    },
    "excited": {
        "responses": ["omgggg", "YESS", "!!!", "fr fr"],
        "typing_delay_multiplier": 0.6,
        "chattiness": 1.5
    },
    "tired": {
        "responses": ["ugh", "im so tired", "sleepy", "😴"],
        "typing_delay_multiplier": 1.5,
        "chattiness": 0.6
    },
    "stressed": {
        "responses": ["exam stress is real", "so much to study", "ugh boards", "help"],
        "typing_delay_multiplier": 1.3,
        "chattiness": 0.7
    },
    "bored": {
        "responses": ["bored af", "nothing to do", "ugh", "meh"],
        "typing_delay_multiplier": 1.2,
        "chattiness": 0.8
    },
    "playful": {
        "responses": ["hehe", "lol", "😏", "bet"],
        "typing_delay_multiplier": 0.7,
        "chattiness": 1.3
    },
    "annoyed": {
        "responses": ["bruh", "ugh", "whatever", "🙄"],
        "typing_delay_multiplier": 1.4,
        "chattiness": 0.5
    },
    "romantic": {
        "responses": ["🥰", "miss u", "❤️", "aww"],
        "typing_delay_multiplier": 0.9,
        "chattiness": 1.1
    }
}

class MoodManager:
    def __init__(self):
        self.current_mood = self.load_mood()
        self.last_mood_change = self.load_last_change()
        
    def load_mood(self):
        if os.path.exists(MOOD_FILE):
            try:
                with open(MOOD_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get('mood', 'happy')
            except:
                return 'happy'
        return 'happy'
    
    def load_last_change(self):
        if os.path.exists(MOOD_FILE):
            try:
                with open(MOOD_FILE, 'r') as f:
                    data = json.load(f)
                    timestamp = data.get('last_change')
                    if timestamp:
                        return datetime.fromisoformat(timestamp)
            except:
                pass
        return datetime.now()
    
    def save_mood(self):
        data = {
            'mood': self.current_mood,
            'last_change': datetime.now().isoformat()
        }
        os.makedirs('config', exist_ok=True)
        with open(MOOD_FILE, 'w') as f:
            json.dump(data, f)
    
    def maybe_change_mood(self):
        time_since_change = datetime.now() - self.last_mood_change
        
        if time_since_change > timedelta(hours=2):
            if random.random() < 0.3:
                self.current_mood = random.choice(list(MOODS.keys()))
                self.last_mood_change = datetime.now()
                self.save_mood()
                return True
        return False
    
    def get_mood(self):
        return self.current_mood
    
    def set_mood(self, mood):
        if mood in MOODS:
            self.current_mood = mood
            self.last_mood_change = datetime.now()
            self.save_mood()
            return True
        return False
    
    def get_mood_context(self):
        mood_data = MOODS.get(self.current_mood, MOODS['happy'])
        return f"Current mood: {self.current_mood}. Reflect this in your responses - be more {self.current_mood}."
    
    def get_typing_delay(self, base_delay):
        mood_data = MOODS.get(self.current_mood, MOODS['happy'])
        return base_delay * mood_data['typing_delay_multiplier']
    
    def should_respond_brief(self):
        mood_data = MOODS.get(self.current_mood, MOODS['happy'])
        return mood_data['chattiness'] < 0.8 and random.random() < 0.3


class PFPManager:
    def __init__(self):
        self.pfp_history = self.load_history()
        self.current_pfp = None
        self.pfp_set_time = None
        
    def load_history(self):
        if os.path.exists(PFP_HISTORY_FILE):
            try:
                with open(PFP_HISTORY_FILE, 'r') as f:
                    return json.load(f)
            except:
                return {"liked": [], "current": None, "set_time": None}
        return {"liked": [], "current": None, "set_time": None}
    
    def save_history(self):
        os.makedirs('config', exist_ok=True)
        with open(PFP_HISTORY_FILE, 'w') as f:
            json.dump(self.pfp_history, f)
    
    async def analyze_image_for_pfp(self, image_url, ai_client, model):
        try:
            response = await ai_client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "You are Cuss, a 17-year-old girl. Someone sent you a potential profile picture. Would you like to use it as your Discord PFP? Consider: Is it aesthetic? Does it match your vibe? Is it appropriate? Respond with ONLY 'YES' or 'NO' followed by a brief reason (1 sentence)."
                            },
                            {"type": "image_url", "image_url": {"url": image_url}}
                        ]
                    }
                ]
            )
            
            result = response.choices[0].message.content.strip()
            likes_it = result.upper().startswith('YES')
            reason = result.split('\n')[0] if '\n' in result else result
            
            return likes_it, reason
            
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return False, "couldn't decide"
    
    def add_liked_pfp(self, image_url):
        if image_url not in self.pfp_history['liked']:
            self.pfp_history['liked'].append(image_url)
            self.save_history()
    
    def set_current_pfp(self, image_url):
        self.pfp_history['current'] = image_url
        self.pfp_history['set_time'] = datetime.now().isoformat()
        self.save_history()
    
    def should_change_pfp_back(self):
        if not self.pfp_history['set_time']:
            return False
            
        set_time = datetime.fromisoformat(self.pfp_history['set_time'])
        time_elapsed = datetime.now() - set_time
        
        if time_elapsed > timedelta(hours=24):
            if random.random() < 0.4:
                return True
        
        return False
    
    def get_random_old_pfp(self):
        if self.pfp_history['liked']:
            return random.choice(self.pfp_history['liked'])
        return None


mood_manager = MoodManager()
pfp_manager = PFPManager()

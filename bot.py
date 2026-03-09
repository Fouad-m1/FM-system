import discord
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── CONFIG ──────────────────────────────────────────
import os
TOKEN = os.environ.get("TOKEN")
WELCOME_CHANNEL_ID = 1465376495311651065  # Replace with your channel ID
RULES_CHANNEL_ID   = 1465353644592468138  # Replace with your rules channel ID
# ────────────────────────────────────────────────────

# Tiny web server to keep Render happy
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")
    def log_message(self, *args):
        pass

def run_server():
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# ── BOT ─────────────────────────────────────────────
intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Online as {bot.user}")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title=f"Welcome to {member.guild.name}! 🎉",
        description=(
            f"Hey {member.mention}, glad you're here!\n\n"
            f"📜 Check the rules in <#{RULES_CHANNEL_ID}>\n"
            f"🎮 Enjoy your stay!"
        ),
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=f"Member #{member.guild.member_count}")

    await channel.send(embed=embed)

bot.run(TOKEN)
```

**`requirements.txt`**
```
discord.py
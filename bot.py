import discord
from discord.ext import commands
from datetime import datetime
from collections import defaultdict

TOKEN = "Bot-token"
AUTHORIZED_ROLES = [123456789012345678, 987654321098765432]  # ID rolí, které mohou používat příkaz

# Nastavení intentů
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True  
intents.message_content = True  

# Prefix pro příkazy
bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} je připraven!")

@bot.command()
async def ping(ctx):
    """Zkontroluje odezvu bota."""
    await ctx.send(f"🏓 Pong! Latence: {round(bot.latency * 1000)}ms")

@bot.command()
async def vyhodnotit_vyzvu(ctx, channel: discord.TextChannel = None, vypis: str = "true", filtr: str = "", *odmeny):
    """Vyhodnotí aktivitu uživatelů v kanále a přidělí role podle zadaných podmínek."""
    try:
        # Kontrola oprávnění
        if not ctx.author.guild_permissions.administrator and not any(role.id in AUTHORIZED_ROLES for role in ctx.author.roles):
            await ctx.send("⛔ Nemáš oprávnění používat tento příkaz.")
            return

        if channel is None or channel == "-":
            channel = ctx.channel  # Pokud není zadaný kanál, vezme aktuální
        
        vypis = vypis.lower() != "false"
        filtr = None if filtr == "-" else filtr
        odmeny = [o for o in odmeny if o != "-"]

        status_message = await ctx.send(f"📊 Analyzuji zprávy v kanále {channel.mention}...")

        user_activity = defaultdict(set)

        async for message in channel.history(limit=None):
            if message.author.bot:
                continue  # Ignoruj zprávy od botů
            
            # Kontrola filtru zpráv
            if filtr:
                if filtr.lower() == "photo":
                    if not message.attachments:
                        continue  # Pokud filtr je "photo" a zpráva neobsahuje přílohu, přeskočíme
                elif filtr not in message.content and not any(str(emoji) in message.content for emoji in message.guild.emojis):
                    continue  # Pokud filtr není obsažen ve zprávě ani není emoji, přeskočíme
            
            date = message.created_at.date()
            user_activity[message.author.id].add(date)

        results = []
        activity_report = ["📋 **Aktivita uživatelů**:"]
        
        for user_id, days in user_activity.items():
            active_days = len(days)
            user = ctx.guild.get_member(user_id)

            if user:
                activity_report.append(f"👤 {user.display_name} – **{active_days} dní**")

                for i in range(0, len(odmeny), 2):
                    try:
                        threshold = int(odmeny[i])
                        role = discord.utils.get(ctx.guild.roles, name=odmeny[i + 1])
                        if active_days >= threshold and role and role not in user.roles:
                            await user.add_roles(role)
                            results.append(f"🏆 {user.mention} získal roli {role.name} ({active_days} dní)")
                    except (ValueError, IndexError):
                        continue  # Pokud je neplatný vstup, přeskočíme

        if vypis:
            activity_report_text = "\n".join(activity_report)
            if len(activity_report_text) > 2000:
                with open("activity_report.txt", "w", encoding="utf-8") as file:
                    file.write(activity_report_text)
                await ctx.send("📄 **Přehled aktivity je moc dlouhý, posílám jako soubor:**", file=discord.File("activity_report.txt"))
            else:
                await ctx.send(activity_report_text)

        if results:
            await ctx.send("\n".join(results))
        elif odmeny:  # Pouze zobrazit hlášku, pokud byly nějaké role specifikovány
            await ctx.send("ℹ️ Nikdo nesplnil podmínky pro získání role.")

        # Smazání zprávy s analýzou
        await status_message.delete()

    except Exception as e:
        print(f"❌ Chyba při vyhodnocení výzvy: {e}")
        await ctx.send(f"⚠️ Chyba: {e}")

bot.run(TOKEN)

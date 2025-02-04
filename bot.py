import discord
from discord.ext import commands
from datetime import datetime
from collections import defaultdict

TOKEN = ("MTIyNzI2OTU5OTk1MTU4OTUwOA.G9SX_P.uQQZh6QP_Vq3F_HUwmXngJyVS59dLQwO9z-2QI")

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
async def vyhodnotit_vyzvu(ctx, channel: discord.TextChannel):
    """Vyhodnotí aktivitu uživatelů v kanále a přidělí role."""
    try:
        await ctx.send(f"📊 Analyzuji zprávy v kanále {channel.mention}...")

        # Slovník pro ukládání aktivních dnů uživatelů
        user_activity = defaultdict(set)

        # Načtení historie zpráv
        async for message in channel.history(limit=None):
            if message.author.bot:
                continue  # Ignoruj zprávy od botů
            date = message.created_at.date()  # Ulož datum zprávy
            user_activity[message.author.id].add(date)

        # Výsledky
        results = []
        activity_report = ["📋 **Aktivita uživatelů**:"]
        for user_id, days in user_activity.items():
            active_days = len(days)
            user = ctx.guild.get_member(user_id)

            if user:
                activity_report.append(f"👤 {user.display_name} – **{active_days} dní**")

                # Udělení rolí
                role_15 = discord.utils.get(ctx.guild.roles, name="𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5")
                role_30 = discord.utils.get(ctx.guild.roles, name="𐌍𐌄𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5")

                if active_days >= 15 and role_15 and role_15 not in user.roles:
                    await user.add_roles(role_15)
                    results.append(f"✅ {user.mention} získal roli {role_15.name} ({active_days} dní)")

                if active_days >= 30 and role_30 and role_30 not in user.roles:
                    await user.add_roles(role_30)
                    results.append(f"🏆 {user.mention} získal roli {role_30.name} ({active_days} dní)")

        # Odeslání aktivity
        activity_report_text = "\n".join(activity_report)
        if len(activity_report_text) > 2000:
            with open("activity_report.txt", "w", encoding="utf-8") as file:
                file.write(activity_report_text)
            await ctx.send("📄 **Přehled aktivity je moc dlouhý, posílám jako soubor:**", file=discord.File("activity_report.txt"))
        else:
            await ctx.send(activity_report_text)

        # Odeslání informací o přidání rolí
        if results:
            await ctx.send("\n".join(results))
        else:
            await ctx.send("ℹ️ Nikdo nesplnil podmínky pro získání role.")

    except Exception as e:
        print(f"❌ Chyba při vyhodnocení výzvy: {e}")
        await ctx.send(f"⚠️ Chyba: {e}")

bot.run(TOKEN)

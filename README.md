# Discord Challenge Bot

---

## 🇬🇧 English Version

### **Discord Challenge Bot**

A Discord bot designed to help track and evaluate user activity in a specific channel, rewarding those who complete challenges for a certain number of days.

---

### **Features**

- **Tracks user activity** in the channel.
- **Calculates active days** for each user.
- **Assigns roles** for completing a challenge:
  - 15 active days: `𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5`
  - 30 active days: `𐌍𐌄𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5`
- **Displays a report** of user activity.
- Can handle a large number of messages and output.

---

### **Setup**

1. **Clone the repository or download the bot code.**

2. **Install the required packages:**
   ```bash
   pip install discord.py python-dotenv
Create a .env file to store your bot token:

ini
Zkopírovat
Upravit
DISCORD_BOT_TOKEN=your_token_here
Run the bot:

bash
Zkopírovat
Upravit
python bot.py
Invite the bot to your Discord server and give it the necessary permissions:

Manage Roles
Read Message History
Send Messages
Commands
*vyhodnotit_vyzvu #channel_name: Evaluates user activity in the specified channel and assigns roles based on activity.
Troubleshooting
Error: 403 Forbidden (Missing Permissions): Make sure the bot has the "Manage Roles" permission and that the bot's role is above the roles it needs to assign.
Error: 50013: Check if the bot has the necessary permissions on your server.
🇨🇿 Česká Verze
Discord Challenge Bot
Discord bot, který slouží k sledování a vyhodnocování aktivity uživatelů v určitém kanále a odměňuje ty, kteří splní výzvu po určitý počet dní.

Funkce
Sleduje aktivitu uživatelů v kanále.
Počítá aktivní dny pro každého uživatele.
Přiděluje role za splnění výzvy:
15 aktivních dní: 𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5
30 aktivních dní: 𐌍𐌄𐌋𐌄𐌃𐌍𐌀𐌂𐌄𐌊 ᘖ0ᘖ5
Zobrazuje přehled aktivity uživatelů.
Zvládá zpracovat velké množství zpráv a výstupu.
Nastavení
Naklonujte repozitář nebo stáhněte kód bota.

Nainstalujte požadované balíčky:

bash
Zkopírovat
Upravit
pip install discord.py python-dotenv
Vytvořte soubor .env pro uložení tokenu bota:

ini
Zkopírovat
Upravit
DISCORD_BOT_TOKEN=váš_token_zde
Spusťte bota:

bash
Zkopírovat
Upravit
python bot.py
Pozvěte bota na váš Discord server a dejte mu potřebná oprávnění:

Spravovat role
Číst historii zpráv
Posílat zprávy
Příkazy
*vyhodnotit_vyzvu #nazev-kanalu: Vyhodnotí aktivitu uživatelů v zadaném kanálu a přidělí role podle aktivity.
Řešení problémů
Chyba: 403 Forbidden (Missing Permissions): Ujistěte se, že bot má oprávnění „Spravovat role“ a že jeho role je nad rolemi, které potřebuje přidělit.
Chyba: 50013: Zkontrolujte, zda má bot na serveru potřebná oprávnění.

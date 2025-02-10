# Discord Bot - Vyhodnocení Aktivita

## Czech

Tento bot slouží k vyhodnocování aktivity uživatelů na Discord serveru. Na základě analýzy zpráv v kanálu přiděluje role uživatelům podle jejich aktivity.

### Funkce:
- **ping**: Zkontroluje latenci bota.
- **analyzovat**: Vyhodnocuje aktivitu uživatelů v kanálu a přiděluje role podle zadaných podmínek.

### Instalace:
1. Nainstalujte knihovnu `discord.py`:
   ```bash
   pip install discord.py
AUTHORIZED_ROLES.

Spusťte bota:


python bot.py
Příklady použití příkazů
*ping
Zkontroluje latenci bota.

Příklad:


*ping
Odpověď:


🏓 Pong! Latence: 50ms
*analyzovat
Vyhodnotí aktivitu uživatelů v kanálu a přidělí role podle zadaných podmínek.

Příklad 1:

*analyzovat #general vypis true photo 5 "Aktivní Uživatel"
Tento příkaz vyhodnotí aktivitu uživatelů v kanálu #general, vypíše aktivitu uživatelů a přidá roli "Aktivní Uživatel" těm, kteří připojili 5 a více obrázků.
Příklad 2:

*analyzovat #chat vypis false 3 "Častý Diskutér"
Tento příkaz vyhodnotí aktivitu uživatelů v kanálu #chat, nezobrazí souhrn aktivity (vypis false), a přidá roli "Častý Diskutér" těm, kteří napsali 3 a více zpráv.
Příklad 3:

*analyzovat #media vypis true - 10 "Fotograf"
Tento příkaz vyhodnotí aktivitu uživatelů v kanálu #media, zobrazí souhrn aktivity a přidá roli "Fotograf" těm, kteří připojili 10 a více příloh.
Příklad 4:

*analyzovat #game vypis true "good game" 7 "Hráč Měsíce"
Tento příkaz vyhodnotí aktivitu uživatelů v kanálu #game, zobrazí souhrn aktivity a přidá roli "Hráč Měsíce" těm, kteří použili frázi "good game" ve své zprávě alespoň 7krát.
Příklad 5:

*analyzovat #test vypis true - 0 "Nováček"
Tento příkaz vyhodnotí aktivitu uživatelů v kanálu #test, zobrazí souhrn aktivity a přidá roli "Nováček" těm, kteří napsali zprávu, ale nezadali žádné konkrétní kritérium pro filtr.
Parametry:
channel: Kanál pro analýzu zpráv (nepovinné, pokud není zadán, použije se aktuální kanál).
vypis: Zda má bot zobrazit souhrn aktivity uživatelů (defaultně "true").
filtr: Filtr pro zprávy (např. "photo", což znamená, že se budou hodnotit pouze zprávy s přílohami).
cas: Časový rámec pro analýzu zpráv (např. "3h", "7d", "1w", "3m", "1y").
odmeny: Seznam odměn, kde každé dvojice hodnot je počet dní aktivity a název role.
English
This bot is designed to evaluate user activity on a Discord server. Based on message analysis in a channel, it assigns roles to users according to their activity.

Features:
ping: Checks the bot's latency.
analyzovat: Evaluates user activity in a channel and assigns roles based on the specified conditions.
Installation:
Install the discord.py library:


pip install discord.py
Insert your bot token in the file and set the authorized roles in the AUTHORIZED_ROLES variable.

Run the bot:


python bot.py
Command Usage Examples
*ping
Checks the bot's latency.

Example:


*ping
Response:


🏓 Pong! Latency: 50ms
*analyzovat
Evaluates user activity in a channel and assigns roles based on the specified conditions.

Example 1:

*analyzovat #general vypis true photo 5 "Active User"
This command evaluates user activity in the #general channel, displays activity reports, and assigns the "Active User" role to users who posted 5 or more pictures.
Example 2:

*analyzovat #chat vypis false 3 "Frequent Poster"
This command evaluates user activity in the #chat channel, does not display a summary of activity (vypis false), and assigns the "Frequent Poster" role to users who sent 3 or more messages.
Example 3:

*analyzovat #media vypis true - 10 "Photographer"
This command evaluates user activity in the #media channel, displays activity reports, and assigns the "Photographer" role to users who posted 10 or more attachments.
Example 4:

*analyzovat #game vypis true "good game" 7 "Player of the Month"
This command evaluates user activity in the #game channel, displays activity reports, and assigns the "Player of the Month" role to users who mentioned the phrase "good game" at least 7 times.
Example 5:

*analyzovat #test vypis true - 0 "Newcomer"
This command evaluates user activity in the #test channel, displays activity reports, and assigns the "Newcomer" role to users who posted a message, with no specific filter.
Parameters:
channel: The channel for message analysis (optional, if not provided, the current channel is used).
vypis: Whether to display a summary of user activity (default is "true").
filtr: A filter for messages (e.g., "photo", meaning only messages with attachments will be considered).
cas: The time frame for message analysis (e.g., "3h", "7d", "1w", "3m", "1y").
odmeny: A list of rewards, where each pair of values represents the number of active days and the role name.

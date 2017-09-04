# NetBot
It's a Bot to manage some Ubiquiti Unifi functions with Telegram

<pre>
pip install -r dependencies.txt
</pre>

# How to install
<pre>
git clone https://github.com/warflop/netbot.git
Edit file conf.py and set token and rss news site.
Edit file bot.py set your iduser telegram and ubiquiti controller credentials.
</pre>

# Commands
<pre>
/news - Last 5 security news (Threatpost).
/speedtest - Test your internet speed.
/aps - Return your ap's name and mac.
/clients - List amount of users.
/list - List your connected clients.
/block 00:00:00:00:00:00 - Block mac address.
/unblock 00:00:00:00:00:00 - Unblock mac address.
/alerts - List alerts messages.
</pre>

# Thank's
<pre>
Thank's to <a href="https://github.com/sivel">@sivel</a> for create speedtest<a href="https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py"> api</a>.
Thank's to <a href="https://github.com/calmh">@calmh</a> for create unifi<a href="https://github.com/calmh/unifi-api"> api</a>.
</pre>


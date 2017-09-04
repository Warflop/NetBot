import telepot
from telepot.loop import MessageLoop
import time
import os
import feedparser
import speedtest
from unifi.controller import Controller
from conf import *

bot = telepot.Bot(token_bot)

def handle(msg):

	chat_id = '******USERID-CHAT-TELEGRAM********'
	command = msg['text']
	c = Controller('IP-UBIQUITI-CONTROLLER', 'USER-UBIQUITI-CONTROLLER', 'PASS-UBIQUITI-CONTROLLER', 'PORT-UBIQUITI', 'VERSION-UBIQUITI-CONTROLLER')	 

	if command == '/news':

		d = feedparser.parse(host_feed)
		for i in range(5):
			teste = d.entries[i].title +" : " +d.entries[i].link
			bot.sendMessage(chat_id, teste)

	elif command == '/speedtest':

		servers = []
		st = speedtest.Speedtest()
		st.get_servers(servers)
		st.get_best_server()
		download = st.download()/1000000
		upload = st.upload()/1000000
		bot.sendMessage(chat_id, "Download: " + str(download) + " Mbit/s \n" + "Upload: " + str(upload) + " Mbit/s")

	elif command == '/aps':

		for ap in c.get_aps():
			bot.sendMessage(chat_id, 'AP named %s with MAC %s' % (ap.get('name'), ap['mac']))


	elif command == '/clients':

		count = 0
		for client in c.get_clients():
			count = count + 1

		bot.sendMessage(chat_id, "We have " + str(count) + " users online!")

	elif command == '/list':

		for client in c.get_clients():

			name = client.get('hostname') or client.get('ip', 'Unknown')
			mac = client['mac']

			bot.sendMessage(chat_id, name + " " + mac)

	elif "/block" in command:

		mac_block = command[7:]
		c.block_client(mac_block)
		bot.sendMessage(chat_id, "User successfully blocked!")

	elif "/unblock" in command:

		mac_unblock = command[9:]
		c.unblock_client(mac_unblock)
		bot.sendMessage(chat_id, "User successfully unblocked!")

	elif command == "/alerts":
		count_alerts = 0
		for event in c.get_events():
			count_alerts = count_alerts + 1
			if count_alerts == 11:
				break
			else:
                bot.sendMessage(chat_id, event.get('msg'))

MessageLoop(bot, handle).run_as_thread()

while 1:
	time.sleep(10)

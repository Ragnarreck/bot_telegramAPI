from commands import CMD
from sourse import Bot

def main():
	bot = Bot()
	while True:
		answer = bot.get_message()
		if(answer!=None):
			bot.send_message(CMD(answer))
		else:
			continue

if(__name__ == '__main__'):
	main()

import requests
from token import get_token

class Bot:
	def __init__(self):
		self.TOKEN = get_token()
		self.URL = 'https://api.telegram.org/bot{0}/'.format(self.TOKEN)
		self.last_update_id = 0
	
	def update_json(self):
		url = self.URL + 'getupdates'
		response = requests.get(url)
		last_update = response.json()['result'][-1]
		json = {'chat_id':last_update['message']['chat']['id'],
				'update_id':last_update['update_id'],
				'message_text':last_update['message']['text'],
				'first_name':last_update['message']['from']['first_name'],
				'last_name':last_update['message']['from']['last_name']}

		return json
	
	def get_message(self):
		data = self.update_json()
		current_update_id = data['update_id']
		if(self.last_update_id != current_update_id):
			self.last_update_id = current_update_id
			message = {'text':data['message_text'],
					   'chat_id':data['chat_id'],
					   'first_name':data['first_name'],
					   'last_name':data['last_name']}
			return message
		else:
			return None
	
	def send_message(self,text):
		data = self.update_json()
		chat_id = data['chat_id']
		url = self.URL + 'sendmessage?chat_id={0}&text={1}'.format(chat_id, text)
		response = requests.get(url)
		return response
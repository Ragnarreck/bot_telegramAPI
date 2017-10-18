def CMD(answer):
	text = answer['text'].lower()
	if(text == '/start'):
		return ('Здравствуйте, {0}. Меня зовут Фестус, и я Ваш помощник.'.format(answer['first_name']))

	elif((text == '/lesson') or ('уроки' in text) or (('пары') in text)):
		return ('Вот Ваши пары на завтра.')

	elif(('спасибо' in text) or ('благодарю' in text)):
		return ('Пожалуйста.')

	else:
		return ('Вы ввели неправильную команду.')
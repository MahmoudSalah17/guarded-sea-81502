import sys, os
from flask import Flask, request
from utils import wit_response
from pymessenger import Bot

PAGE_ACCESS_TOKEN = "EAAZAnbdAPplsBAD4LANNjKuCx5EqzXIhmfDl1hZCGAzMST7RfjdO7p6bPZCMhfyys9Nqk8kzLYuAskGrAjzSBLNc29SAjnV8XrRZC01XWA1ALZBhdGKaDoGAb7c1CD8y0e7ZAqaUfwi0BbqloN2NZAZALmlrvZCQ9M7wqyxCjRzKzdwZDZD"
bot = Bot(PAGE_ACCESS_TOKEN)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
	#WEbhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200

	
@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)
	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					
					response = None
					
					entity, value = wit_response(messaging_text)
					if entity == "number":
						response = "3la wad3ak"
					elif entity == "location":
						response = "l2"
					else:
						response = "Sorry, I don't get it"
					print(response)
					bot.send_text_message(sender_id, response)

	return "ok", 200

def log(message):
	print(message)
	sys.stdout.flush()
		
if __name__ == "__main__":
	app.run(debug = True, port = 80)


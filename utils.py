from wit import Wit

access_token = "BYP3UZEPLSEUPQR6FFSBHXZT3WW53Y77"
client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	entity = None
	value = None
	
	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass
	return (entity, value)		

#print(wit_response("500"))
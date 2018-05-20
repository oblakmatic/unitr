import logging
from websocket_server import WebsocketServer
import json
from .models import *



def new_client(client, server):
	#server.send_message_to_all("Hey all, a new client has joined us")
    pass

def posljiMeetingLjudem(meet_id, message):
    Meeting.objects.get(meet_id=1)




def prejetoSporocilo(client, server, message):
    dzejson = json.loads(message)
    
    posljiMeetingLjudem(dzejson["meeting_id"],dzejson["message"])

    

def naredi_streznik():
    server = WebsocketServer(9001, host='127.0.0.1', loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(prejetoSporocilo)
    server.run_forever()



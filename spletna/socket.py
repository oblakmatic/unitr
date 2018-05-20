import logging
from websocket_server import WebsocketServer

def new_client(client, server):
	server.send_message_to_all("Hey all, a new client has joined us")


def naredi_streznik(request):
    print("enov")
    server = WebsocketServer(13254, host='127.0.0.1', loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(prejetoSporocilo)
    server.run_forever()


def prejetoSporocilo(client, server):
    server.send_message_to_all("jo jo jo kje ste ")
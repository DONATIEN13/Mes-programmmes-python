#lien youtube
https://youtu.be/AFUdjyBbsog


from multiprocessing import Process, Pipe
from time import sleep
import os
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/homehome")
def worker(conn):

	print('processus 1 - Initialisation du sommeil 1 seconde')
	sleep(1)

	a = os.getpid()
	b = 'processus 1, pid = ' + str(a)

	print(a)

	print('processus 1- envoi de donnée via le pipe')
	conn.send(b)

	print("processus 1 - reception de donnée via le pipe")
	print('processus 1: ' + conn.recv())

	print('processus 1 - fermeture du processus 1, fin de la connection')
	conn.close()
	print('processus 1- Terminé')
@app.get("/home")
def main():

	a = os.getpid()
	b = 'processus 2 pid = ' + str(a)

	print(a)

	print('processus 2 - Initialisation, creation du pipe')
	main_connection, worker_connection = Pipe()

	print('processus 2- mise en place du processus')
	p = Process(target = worker, args = [worker_connection])

	print('processus 2- Initialisation du processus')
	p.start()

	print('processus 2- en attente de la reponse du processus fils')

	print('\n')
	print('processus 2 - reception de donnée via le pipe')
	print('processus 2 : ' + main_connection.recv())

	print('\n')
	print('processus 2 - envoi de donnée via le pipe')
	main_connection.send(b)

	print('processus 2 - fermeture du main, fin de la de connection')
	main_connection.close()

	print('processus 2 - Terminé')
	print('\n\n')
	
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
	main()

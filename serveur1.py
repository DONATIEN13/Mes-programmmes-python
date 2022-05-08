import socket 
  
import threading 
  
PORT = 5000
  
SERVEUR = socket.gethostbyname(socket.gethostname()) 
  
ADDRESS = (SERVEUR, PORT) 
  
FORMAT = "utf-8"
  
clients, noms = [], [] 
  
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  
serveur.bind(ADDRESS) 
  
def conversation(): 
    
    print("Le serveur est en marche sur: " + SERVEUR) 
      
    
    serveur.listen(10) 
      
    while True: 
            
        conn, addr =  serveur.accept() 
        conn.send("NAME".encode(FORMAT)) 
              
        nom = conn.recv(1024).decode(FORMAT) 
          
        noms.append(nom) 
        clients.append(conn) 
          
        print("{} est en ligne".format(nom)) 
          
        diffuser(f"{nom} a rejoint le groupe!".encode(FORMAT)) 
          
        conn.send('Connexion étalie!'.encode(FORMAT)) 
          
        
        thread = threading.Thread(target = handle, 
                                  args = (conn, addr)) 
        thread.start() 
           
        print(f" connexions actives {threading.activeCount()-1}") 
  
def handle(conn, addr): 
    
    print(f" Nouvelle connexion: {addr}") 
    connected = True
      
    while connected: 
          
        message = conn.recv(1024) 
          
        diffuser(message) 

    conn.close() 
  
def diffuser(message): 
    for client in clients: 
        client.send(message) 

conversation() 

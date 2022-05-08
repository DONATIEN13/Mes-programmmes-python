from tkinter import *
import socket 
import threading 
from tkinter import font 
from tkinter import ttk 


PORT = 5000
SERVER = "127.0.0.1"
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(ADDRESS) 


class INTERFACE: 
    
    def __init__(self): 
        
        
        self.Window = Tk() 
        self.Window.withdraw() 
          
        
        self.login = Toplevel() 
        
        self.login.title(" INFORMATIONS DE CONNEXION..... ") 
        self.login.resizable(width = False,  
                             height = False) 
        self.login.geometry('400x300')
        self.login.configure(bg = 'ivory') 
        
        """self.pls = Label(self.login,  
                       text = "Infos de connexion", 
                       justify = CENTER,  
                       font = "Helvetica 14 bold")""" 
          
        #self.pls.place() 
        
        self.labelName1 = Label(self.login, 
                               text = "Pseudo: ", 
                               font = "Helvetica 12") 

        self.labelName1.place(x = 40, y = 40)

        self.labelName2 = Label(self.login, 
                               text = "Adresse: ", 
                               font = "Helvetica 12")
          
        self.labelName2.place(x = 40, y = 80)
        
        self.entryName1 = Entry(self.login,  
                             font = "Helvetica 14")

        self.entryName1.place(x = 110, y = 40)

        self.entryName2 = Entry(self.login,  
                             font = "Helvetica 14") 

        self.entryName2.place(x = 110, y = 80)
          
        """self.entryName1.focus()
        self.entryName2.focus()"""

        self.go = Button(self.login, 
                         text = "CONTINUER",  
                         font = "Helvetica 14 bold",  
                         command = lambda: self.ma_page1(self.entryName1.get(), self.entryName2.get())) 
          
        self.go.place(relx = 0.4, 
                      rely = 0.55) 
        self.Window.mainloop() 
  
    def ma_page1(self, name1, ADDRESS): 
        self.login.destroy() 
        self.ma_page(name1, ADDRESS) 
          
        
        rcv = threading.Thread(target = self.recevoir) 
        rcv.start()
  
    
    def ma_page2(self,name, ADDRESS): 
        
        self.name = name
        self.ADDRESS = ADDRESS
        
        self.Window.deiconify() 
        self.Window.title("MESSAGES") 
        self.Window.resizable(width = False, 
                              height = False) 
        self.Window.configure(width = 470, 
                              height = 550, 
                              bg = "#17202A") 
        self.labelHead = Label(self.Window, 
                            bg = "#17202A",  
                            fg = "#EAECEE", 
                            text = self.name, 
                            font = "Helvetica 13 bold",
                            pady = 5) 
          
        self.labelHead.place(relwidth = 1) 
        self.line = Label(self.Window, 
                          width = 450, 
                          bg = "#ABB2B9") 
          
        self.line.place(relwidth = 1, 
                        rely = 0.07, 
                        relheight = 0.012) 
          
        self.textCons = Text(self.Window, 
                             width = 20,  
                             height = 2, 
                             bg = "#17202A", 
                             fg = "#EAECEE", 
                             font = "Helvetica 14",  
                             padx = 5, 
                             pady = 5) 
          
        self.textCons.place(relheight = 0.745, 
                            relwidth = 1,  
                            rely = 0.08) 
          
        self.labelBottom = Label(self.Window, 
                                 bg = "#ABB2B9", 
                                 height = 80) 
          
        self.labelBottom.place(relwidth = 1, 
                               rely = 0.825) 
          
        self.entryMsg = Entry(self.labelBottom, 
                              bg = "#2C3E50", 
                              fg = "#EAECEE", 
                              font = "Helvetica 13") 
          
        self.entryMsg.place(relwidth = 0.74, 
                            relheight = 0.06, 
                            rely = 0.008, 
                            relx = 0.011) 
          
        self.entryMsg.focus() 
          
        
        self.buttonMsg = Button(self.labelBottom, 
                                text = "Envoyer", 
                                font = "Helvetica 10 bold",  
                                width = 20, 
                                bg = "#ABB2B9", 
                                command = lambda : self.boutton_envoi(self.entryMsg.get()))   
        self.buttonMsg.place(relx = 0.77, 
                             rely = 0.008, 
                             relheight = 0.06,  
                             relwidth = 0.22)   
        self.textCons.config(cursor = "arrow") 
          
        
        scrollbar = Scrollbar(self.textCons) 
          
        
        
        scrollbar.place(relheight = 1, 
                        relx = 0.974) 
          
        scrollbar.config(command = self.textCons.yview) 
          
        self.textCons.config(state = DISABLED) 
  
    
    def boutton_envoi(self, msg): 
        self.textCons.config(state = DISABLED) 
        self.msg=msg 
        self.entryMsg.delete(0, END) 
        snd= threading.Thread(target = self.envoyer_message) 
        snd.start() 
  
    
    def recevoir(self): 
        while True: 
            try: 
                message = client.recv(1024).decode(FORMAT) 
                  
                
                if message == 'NAME': 
                    client.send(self.name.encode(FORMAT)) 
                else: 
                    
                    self.textCons.config(state = NORMAL) 
                    self.textCons.insert(END, 
                                         message+"\n\n") 
                      
                    self.textCons.config(state = DISABLED) 
                    self.textCons.see(END) 
            except: 
                
                print("Une erreur est survenue !!!") 
                client.close() 
                break 
          
    
    def envoyer_message(self): 
        self.textCons.config(state = DISABLED) 
        while True: 
            message = (f"{self.name}: {self.msg}") 
            client.send(message.encode(FORMAT))     
            break

INTERFACE()
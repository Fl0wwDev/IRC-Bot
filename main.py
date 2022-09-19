import socket
from math import *

#setting
server = "irc.root-me.org"               
channel = "#root-me_challenge"
botnick = "Fl0ww-test"
botname = "Candy"
port = 6667


#defines the socket
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
irc.connect((server, port))



irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :python\n","UTF-8")) #user authentication
irc.send(bytes("NICK "+ botnick +"\n","UTF-8"))#sets nick #auth
irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :python\n","UTF-8")) #user authentication


while True:
    text = irc.recv(2040).decode("UTF-8")
    print(text)
    
    if "PING" in text:  #check if 'PING' is found
        irc.send(bytes('PONG ' + text.split() [1] + '\r\n',"UTF-8")) #returnes 'PONG' back to the server (prevents pinging out!)
        irc.send(bytes("JOIN "+ channel +"\n","UTF-8"))  #join the chan
    if ":End of /NAMES list." in text:
        irc.send(bytes("PRIVMSG " + botname + " !ep1 \r\n","UTF-8"))
    if ' / ' in text: 
        nombre = text.split()[3] #on coupe les nombres
        nombre1 = int(nombre.split(':')[1])
        nombre2 = int(text.split()[5])
        
        print(nombre1, nombre2)
        résultat = str(round(sqrt(nombre1) * nombre2,2))
        irc.send(bytes("PRIVMSG " + botname + " !ep1 -rep " + résultat + "\r\n","UTF-8"))  #on envoie le résultat
        
        



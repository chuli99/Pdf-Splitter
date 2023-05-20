import socket
import sys
import argparse
import time, sys

def client(h,p,f,t,nf):
    if h == 'localhost':
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Socket creation failed")
            sys.exit()
    if h == '::1':
        try:
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        except socket.error:
            print("Socket creation failed")
            sys.exit()
        
    #Recibe host por argumento
    host = h
    #Recibe port por argumento
    port = p
    print("Connecting..")
    time.sleep(2)
    s.connect((host,port))
    print("Handshake realizado")
    time.sleep(1)
    print("Esperando datos del server")
    while True:    
        #print("Cerrando conexion")
        msg = input("Ingrese comando a ejecutar:")
        s.send(msg.encode())
        print("Esperando datos del server")
        msg = s.recv(1024)
        print(msg.decode())
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-ht","--host",required=True,help="IP server")
    parser.add_argument("-p","--port", type=int,required=True,help="Server Port")
    
    #arguments for pages pdf
    parser.add_argument("-f","--fromm", type=int,required=True,help="From which page will you divide")
    parser.add_argument("-t","--to", type=int,required=True,help="Until which page divided")
    parser.add_argument("-nf","--namefile",required=True,help="Until which page divided")

    args = parser.parse_args()
    print(args.host,args.port)
    client(args.host,args.port,args.fromm,args.to,args.namefile)


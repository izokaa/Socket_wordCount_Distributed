import socket
import threading
import os
import pickle
from counter import mapreduce
Lock = False

clients = []
clients_queue =[] 
global_data={}


def waitData(conn,i):
    global global_data
    while True:
        data = conn.recv(1024) 
        if not data:
            continue
        print('data Received from user '+str(i))
        global_data=mapreduce.getReduce(global_data,pickle.loads(data))
        if(len(clients_queue)==1):
            file = open(os.path.join(os.path.dirname(__file__),'output/restult.txt'), 'w+')
            file.write(str(global_data))
            print(global_data)
            file.close()
            print('operation finished succesfully for results check out ./output/restult.txt')
            quit()
        else:
            clients_queue.remove(conn)

def send_andwait(lines):
    count = int(len(lines)/len(clients))
    for i in range(len(clients)):
        if(i==len(clients)-1):
            store= lines[i*count:]
            if(len(store)>0):                
                clients[i].send(pickle.dumps(store))
                # print(pickle.dumps(store))
                clients_queue.append( clients[i])
                x = threading.Thread(target=waitData, args=(clients[i],i))
                x.start()
        else:
            store=lines[i*count:i*count+count] 
            if(len(store)>0):                  
                clients[i].send(pickle.dumps(store))
                clients_queue.append( clients[i])
                x = threading.Thread(target=waitData, args=(clients[i],i))
                x.start()

def start_processing(path): 
    if(os.path.exists(path)):
        file = open(path,'r',encoding="utf8")
        lines=[]
        for line in file:
            if(len(line.strip())>0):
                lines.append(line)
        send_andwait(lines)     
    else:
        print('the path is invalid')

def acceptClients(server_socket): # thread function that accepts connected clients
    while Lock==False:
        conn, address = server_socket.accept()  # accept new connection
        clients.append(conn)
        print("Connection from: " + str(address))

    print('Server Ready To Process ')


def server_program(): # main program
    # set ip and port
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()      
    
    server_socket.bind((host, port))  # bind host address and port together    
    server_socket.listen(10)

    x = threading.Thread(target=acceptClients, args=(server_socket,))
    x.start()
    print('Server Started waiting for Machines to Connect ...')
    while True:
        global Lock

        data = input(' -> ')
        if(data.startswith('help')):
            print('Lock : to lock new users from connecting and start processing\nStart <filepath> : start processing with <filepath> the path to the file that contains content')
        elif(data.startswith('Start')):
            if(Lock==False):
                print('you need to execute Lock before starting to process')
            else:
                cmd = data.split(' ')
                if(len(cmd)<2):
                    print('Invalid params')
                else:
                    start_processing(' '.join(cmd[1:]))
        elif(data.startswith('Lock')):
            print('Locked')
            Lock=True


if __name__ == '__main__':
    server_program()


#listen to ip port
#get all clients
#lock from connecting
#get file location
#get file content
#split content by user
#send data to users 
#thread wait responces
#show responses
import socket
import threading
import pickle
from counter import mapreduce


def waitData(client_socket):
    while True:
          # send message
        data = client_socket.recv(1024)  # receive response
        if not data:
            continue
        
        print('data Received from server, processing data... \n')  # notify in terminal
        print('\n\n Recieved text : ')
        print(pickle.loads(data))
        countelems = mapreduce.getCountElements(''.join(pickle.loads(data)))
        print('\n\n Tansformed text : ')
        print(countelems)

        client_socket.send(pickle.dumps(countelems))
        
        print('Data Sent To The Server Successfully .....')
        input('press any key to exit .')
        quit()

def client_program():
    host = socket.gethostname()  
    port = 5000  

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    x = threading.Thread(target=waitData, args=(client_socket,))
    x.start()
    print('Wainting For Instructions')
    message = input(" -> ")  

    while message.lower().strip() != 'bye':
        

        message = input(" -> ")  

    client_socket.close()  


if __name__ == '__main__':
    client_program()
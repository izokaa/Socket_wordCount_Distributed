# Socket wordCount Distributed
This project is an implementation of map reduce "word Count" in a distributed system using sockets.
# How it works
the idea of this project is counting the number of words provided in a file from server.py
- **server.py** is the client that enables the user to connect with the distant machines and when ready provide with the data divided evenly to the number of server.py instances connected to it.
- **client.py** represent the machines that will recieve data from a single server.py then proccess and send the result to the server.py.
- **counter**  package used by client.py to process recieved data.
 - **counter/mapreduce.py** contains functions to process data.
# Command line
server.py commes with a command line.
Some basic  commands are:
```
- help // informs about the existing commands
- Lock // after the needed count of machines are connected it locks new machines from connecting  in order to not disturb the server.py when processing the data
- Start <filepath> // start processing with <filepath> the path to the file from the local machine, the file provided should contain the text that we want to process
```
# How run
- First we should configure server.py to host in the desired HOST and PORT (by default it listens to localhost:5000)
```
#server.py
def server_program(): # main program
    # set ip and port
    host = #host/ip adress here
    port = #port here
```
- After configuration we run server.py, if everything went well the server should show  this message 
```
Server Started waiting for Machines to Connect ...
```
 - in case the machines are connected by LAN we make sure that the port is allowed in the machine firewall
 - in case the machines are connected by internet make sure that the port is also allowed in the router's firewall
Now the server is set and ready to accept connections, we move on to clients(distributed machines)
-before we run client.py we should configure server ip and port (by default it points on localhost:5000)
 - in case the machines are connected by LAN we make sure that the port is allowed in the machine firewall
 - in case the machines are connected by internet make sure that the port is also allowed in the router's firewall
```
#client.py
def client_program():
    host = #server host/ip adress here
    port = #server port here  
```
- After configuration we should run client.py (we can run as many instances of client.py as we can)
  - client.py requires **counter** package (./counter/*) to run properly
- When the desired  number of machines are connected we run on server.py the following command line
  - ```Lock ```
- When we want to start processing a desired file we should run the following command line
  - ```Start <filePath> ``` <filePath> : path to the file containing the text
- the server.py should send the data to the connected client.py, when they finish we should get : ```operation finished succesfully for results check out ./output/restult.txt```
- the result are present in ./output/restult.txt

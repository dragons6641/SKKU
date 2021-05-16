#!usr/bin/python
#-*- coding : utf-8 -*-

# import socket
from socket import *

# [x, y] printing function
def position_print(x, y):
    print('[' + str(x) + ', ' + str(y) + ']\n');

    return;

# set ip address, port number and buffer size
host = '127.0.0.1';
port = 30000;
bufsize = 1024;

# set up listening socket
ds = socket(AF_INET, SOCK_STREAM);
ds.bind((host, port));
ds.listen(5);

# initial start point = [0, 0]
x = 0;
y = 0;

print('Drone starts at [' + str(x) + ', ' + str(y) + ']');
print('Waiting for the controller...\n');

# infinite loop
while True:
    # accept the controller socket
    ss, addr = ds.accept();
    
    print('Controller is connected');
    position_print(x, y);

    # send the current position of drone
    ss.send(str(x).encode());
    ss.send(str(y).encode());

    # infinite loop
    while True:
        # receive the command
        cmd = (ss.recv(bufsize)).decode();

        # if controller wants to be disconnected
        if(cmd == 'disconnect'):
            ss.close();

            print('Controller is disconnected\n');

            break;

        # else if controller wants to move the drone up
        elif(cmd == 'w'):
            print('Command arrived: MOVE_UP');
            
            y += 1;

        # else if controller wants to move the drone left
        elif(cmd == 'a'):
            print('Command arrived: MOVE_LEFT');
            
            x -= 1;

        # else if controller wants to move the drone down
        elif(cmd == 's'):
            print('Command arrived: MOVE_DOWN');
            
            y -= 1;

        # else if controller wants to move the drone right
        elif(cmd == 'd'):
            print('Command arrived: MOVE_RIGHT');
            
            x += 1;

        # else if controller reset the situation
        elif(cmd == 'reset'):
            print('Reset position');
            
            # initial start point = [0, 0]
            x = 0;
            y = 0;

        # moves to outside of the map is not allowed
        if(x > 9):
            x -= 1;

        elif(x < 0):
            x += 1;

        # moves to outside of the map is not allowed
        if(y > 9):
            y -= 1;

        elif(y < 0):
            y += 1;

        position_print(x, y);

        # send the current position of drone
        ss.send(str(x).encode());
        ss.send(str(y).encode());

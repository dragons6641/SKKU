#!usr/bin/python
#-*- coding : utf-8 -*-

# import socket
from socket import *

# [x, y] printing function
def position_print(x, y):
    print('[' + str(x) + ', ' + str(y) + ']\n');

    return;

print('Controller Starts\n');

# infinite loop
while True:
    msg = input('Enter Command: ');

    # if controller wants to be connected
    if(msg == 'connect'):
        # set ip address, port number and buffer size
        host = '127.0.0.1';
        port = 30000;
        bufsize = 1024;

        # connect to the drone socket
        cs = socket(AF_INET, SOCK_STREAM);
        cs.connect((host, port));

        print('Drone is connected');

        # receive the current position of drone
        x = (cs.recv(bufsize)).decode();
        y = (cs.recv(bufsize)).decode();

        position_print(x, y);

        # infinite loop
        while True:
            cmd = input('Enter Command: ');

            # if controller wants to be disconnected
            if(cmd == 'disconnect'):
                # send the command
                cs.send(str(cmd).encode());
                cs.close();

                print('Drone is disconnected\n');
                
                break;

            # else if controller wants to move the drone
            elif(cmd == 'w' or cmd == 'a' or cmd == 's' or cmd == 'd'):
                # send the command
                cs.send(str(cmd).encode());

                # receive the current position of drone
                x = (cs.recv(bufsize)).decode();
                y = (cs.recv(bufsize)).decode();                

                position_print(x, y);

            # else if controller reset the situation
            elif(cmd == 'reset'):
                # send the command
                cs.send(str(cmd).encode());

                print('Reset position');
                
                # receive the current position of drone
                x = (cs.recv(bufsize)).decode();
                y = (cs.recv(bufsize)).decode();                

                position_print(x, y);

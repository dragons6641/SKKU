MyController_V2.py
김

T
유형
텍스트
크기
2KB (2,110바이트)
사용된 저장용량
2KB (2,110바이트)
위치
Version2
소유자
나
수정한 날짜
내가 2020. 1. 31.에 수정함
열어본 날짜
내가 오후 9:04에 열어봄
생성한 날짜
Google Drive Web(으)로 2020. 1. 31.에 작성됨
설명 추가
뷰어가 다운로드할 수 있음
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

import RPi.GPIO as GPIO
import time
import threading
        
import socket
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)


host ='130.230.144.60'
port = 3010

mySocket = socket.socket()
mySocket.connect((host, port))



def sendMessage(message):
    

    #while message != 'q':
    mySocket.send(message.encode())
##    data = mySocket.recv(1024).decode()

##    print('Received from server: ' + data)

##        message = input(" -> ")

##    mySocket.close()


def sensor_room1():
    while True:
        room1 = GPIO.input(16)
        if room1==0:
            print("Room_1 is empty",room1)
            ##msgStr="Room_1:"+str(Room_1)
            msgStr="konetalo:room1:empty"
            sendMessage(msgStr)
            time.sleep(2)
            
        elif room1==1:
            print("Room_1 occupied",room1)
     ##       msgStr="Room_1:"+str(Room_1)
            msgStr="konetalo:room1:occupied"
            sendMessage(msgStr)
            time.sleep(2)

def sensor_room2():
        
    while True:
        room2 = GPIO.input(18)
        if room2==0:
            print("Room_2 is empty",room2)
            ##msgStr="Room_1:"+str(Room_1)
            msgStr="konetalo:room2:empty"
            sendMessage(msgStr)
            time.sleep(2)
            
        elif room2==1:
            print("Room_2 occupied",room2)
     ##       msgStr="Room_1:"+str(Room_1)
            msgStr="konetalo:room2:occupied"
            sendMessage(msgStr)
            time.sleep(2)



thread1=threading.Thread(target=sensor_room1)
thread1.start()

thread2=threading.Thread(target=sensor_room2)
thread2.start()
##
##
##def sendMessage(message):
##    host = '130.230.144.243'
##    port = 3010
##
##    mySocket = socket.socket()
##    mySocket.connect((host, port))
##
##    #message = input(" -> ")
##    
##
##    while message != 'q':
##        mySocket.send(message.encode())
##        data = mySocket.recv(1024).decode()
##
##        print('Received from server: ' + data)
##
####        message = input(" -> ")
##
##    mySocket.close()





##if __name__ == '__main__':
##    Main()
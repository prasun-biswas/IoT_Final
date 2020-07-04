# Project on IoT
includes code in: javascript, html, python

This Prototype project is part of my Minor studies(Master Degree in Automation Engineering). We developed a small project and presented it as if were a product. 

## Raspberry Pi, PIR sensor

It is a web-based occupancy checker where a web page shows if a room is occupied. PIR motion sensor was used to check if anyone stayed in a room based on movement. The sensors are interfaced with Raspberry PI. RPi also work as client side in a client-server system where main server is in a PC. The RPi uses Python to create client side of the application to read sensor data over an interval and send it to the server over socket connection where the main server is build with node.js. The node.js server also renders the webpage to show the occupancy status in real time using angular.js. 

<img src="IOT Project_Salman_Prasun/pb2.PNG" alt = "map of path and obstacles" width = 700>

* Python for RPI server
* Node.js for bacckend programming of main server
* Express.js for creating HTTP server
* HTML, CSS, Bootsstrap for frontend
* Socket for sending and receiving data from python.


<img src="IOT Project_Salman_Prasun/pb.PNG" alt = "map of path and obstacles" width = 610>
<img src="IOT Project_Salman_Prasun/pb1.PNG" alt = "map of path and obstacles" width = 610>


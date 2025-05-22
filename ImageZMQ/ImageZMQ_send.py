# run this program on each RPi to send a labelled image stream
# you can run it on multiple RPi's; 8 RPi's running in above example
import socket
import time
from picamera2 import Picamera2
import imagezmq
import cv2

sender = imagezmq.ImageSender(connect_to='tcp://Alexs-MacBook-Air.local:5560')

rpi_name = socket.gethostname() # send RPi hostname with each image
picam = Picamera2()
picam.start()
time.sleep(2)  # allow camera sensor to warm up


while True:  # send images as stream until Ctrl-C
    image = picam.capture_array()
    
    ret, jpg_buffer = cv2.imencode(".jpg", image)
    sender.send_jpg(rpi_name, jpg_buffer)

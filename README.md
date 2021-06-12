# LW-SI-Task3!


What is openCV-Python? 
OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
Python is a general purpose programming language started by Guido van Rossum that became very popular very quickly, mainly because of its simplicity and code readability. It enables the programmer to express ideas in fewer lines of code without reducing readability.


To know more about it , we can refer below article it will give you a great idea about openCV-python
https://www.linkedin.com/posts/nehal-ingole_task4-vimaldaga-righteducation-activity-6808377434438680576-eWXy


Reading a Video
In OpenCV, a video can be read either by using the feed from a camera connected to a computer or by reading a video file. The first step towards reading a video file is to create a VideoCapture object. Its argument can be either the device index or the name of the video file to be read.

In most cases, only one camera is connected to the system. So, all we do is pass ‘0’ and OpenCV uses the only camera attached to the computer. When more than one camera is connected to the computer, we can select the second camera by passing ‘1’, the third camera by passing ‘2’ and so on.



Installation of OpenCV .
Note: Since we are going to use OpenCV in the Python language, it is an implicit requirement that you already have Python (version 3) installed on your workstation. Depending upon your OS, execute one of the following commands to install OpenCV library on your system:

Windows

$ pip install opencv-python

MacOS

$ brew install opencv3 --with-contrib --with-python3
Linux

$ sudo apt-get install libopencv-dev python-opencv
To check if your installation was successful or not, run the following command in either a Python shell, or your command prompt/ terminal:

import cv2
If you do not get an error on importing cv2 then it was installed correctly.

Basic Image Operations
Now that we have installed OpenCV on our workstations, let's get our hands dirty with some of the functionalities that OpenCV offers.

Display an Image
Displaying an image using OpenCV is a two-step process; first, we have to load it, and then we can display it. Both operations are done in sequence using different functions.

To display an image, we need to know two things:

Image Path (both absolute and relative paths work)
Read Mode (read, write, etc.)

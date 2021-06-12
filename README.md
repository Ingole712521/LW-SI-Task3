# LW-SI-Task3!

[Uploading image.png…]()





Reading a Video
In OpenCV, a video can be read either by using the feed from a camera connected to a computer or by reading a video file. The first step towards reading a video file is to create a VideoCapture object. Its argument can be either the device index or the name of the video file to be read.

In most cases, only one camera is connected to the system. So, all we do is pass ‘0’ and OpenCV uses the only camera attached to the computer. When more than one camera is connected to the computer, we can select the second camera by passing ‘1’, the third camera by passing ‘2’ and so on.

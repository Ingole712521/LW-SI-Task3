import cv2,socket,struct,pickle
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",1234))
print("Connect Success")

cam = cv2.VideoCapture(0)
client_socket.settimeout(2)
img_counter = 0
encode_par=[0,90]
while True:
    ret, frame = cam.read()
    #Encodes an image into a memory buffer.
    #The function imencode compresses the image and stores it in the memory buffer that is resized to fit the result
    result, frame = cv2.imencode('.jpg', frame,encode_par)
    #The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
    #here 0 is a protocol
    #Protocol version 0 is the original “human-readable” protocol and is backwards compatible with earlier versions of Python.
    data = pickle.dumps(frame, 0)
    size = len(data)
    print("{}: {}".format(img_counter, size))
    try:
        client_socket.sendall(struct.pack(">L", size) + data)
    #This will raise a socket.timeout exception when no data has been recieved in timeout time.
    except socket.timeout:
        break        
    img_counter += 1
cam.release()
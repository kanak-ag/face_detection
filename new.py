import cv2
# print(cv2.__version__)
height=640
width=640
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS,30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    _ignore, frame=cam.read()
            #  mpDraw.draw_landmarks(frame,handlandmarks)
    cv2.imshow('mywebcam',frame)
    cv2.moveWindow('mywebcam',0,0)
    if cv2.waitKey(1)& 0xff  ==ord('q'):
        break
cam.release()
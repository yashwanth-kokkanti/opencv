import cv2
import numpy as np

cap = cv2.VideoCapture(0) ## 0 indicates first web cam

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read() ## returns true/false, frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## convertframe to gray

    out.write(frame)

    # Show Cameras  
    cv2.imshow('frame', frame) ## Color Format Default
    cv2.imshow('gray', gray)  ## Frame converted to grayscale 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() ## release Window
out.release()
cv2.destroyAllWindows()
    

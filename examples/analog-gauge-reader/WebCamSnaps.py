import numpy as np
import cv2
import time

#cap = cv2.VideoCapture(0)

while(True):
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    #start_time = time.time()
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    file = "gauge-100.jpg"
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, frame)


    #time.sleep(5.0 - time.time() + start_time) # Sleep for 1 second minus elapsed time
    time.sleep(5)
    cap.release()
    #cv2.destoryAllWindows()
# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()

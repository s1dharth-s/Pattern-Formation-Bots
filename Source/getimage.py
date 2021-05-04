
import cv2

cap = cv2.VideoCapture('http://10.0.0.14:8080/video')

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    res = cv2.aruco.detectMarkers(gray,dictionary)
#   print(res[0],res[1],len(res[2]))

    if len(res[0]) > 0:
        cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


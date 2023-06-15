
import cv2
import requests
import numpy as np
import imutils

#----------------------------------------- replace this url with one in the app
#--------------- append the /shot.jpg at the end of url
url = "http://100.135.63.48:8080/shot.jpg"
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow('camera feed', img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

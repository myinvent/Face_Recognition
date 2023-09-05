import cv2

name = 'Ariffin' #replace with your name

cam = cv2.VideoCapture(0)

cv2.namedWindow("Press Space to Take a Photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press Space to Take a Photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to Grab Frame")
        break
    cv2.imshow("Press Space to Take a Photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape Hit, Closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "images/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} Written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
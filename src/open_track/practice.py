import cv2
import numpy as np
import copy
IMAGE = "f73550_1295735436.jpg"

baseimg = cv2.imread(IMAGE, cv2.IMREAD_COLOR)
# cv2.IMREAD_COLOR | -1: loads a color image. any transparency will be ignored.
# cv2.IMREAD_GRAYSCALE | 0: loads in greyscale mode
# cv2.IMREAD_UNCHANGED | 1: loads color image. transparency will be respected.

img2 = cv2.resize(baseimg, (400, 400))
# hardcode image size

img = cv2.resize(baseimg, (0, 0), fx=0.5, fy=0.5)
# 50 percent scale

img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# rotate image


# cv2.imshow("window", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# response = input("would you like to save this image? ")
# if response == 'yes':
#     cv2.imwrite('new_img.jpg', img)

"""25 minutes"""

# print(img)
# img is stored as numpy array
print(type(img))

height, width, channels = img.shape
print((height, width, channels))

example =[
    [ [0,0,0], [0,0,0], [255, 255, 255] ],
    [ [0,0,0], [0,0,0], [255, 255, 255] ], ]
# this is a three dimensional array
# the length of dimension1 is height, len d2 is width, d3 is BGR
# open CV records pixel color values as Blue, Green, Red
# with a range of 0 to 255

blue = copy.copy(img)
for i in range(100):
    for j in range(blue.shape[1]):
        blue[i][j] = [255, 0, 0]  # make blue
# this changes the first 100 "lines" of the image to be blue

hair = img[500:700, 600:900]
img[100:300, 650:950] = hair
# this is copying a section of the image and pasting it
# in another section of the image

# cv2.imshow("window", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""15 minutes"""

cap = cv2.VideoCapture(0)
# the argument is the "number" of your video input device
# if there is only one video input device the number is zero

cap = cv2.VideoCapture("video.mp4")
# you can also load a video given its filename

# displays the input as is
# while True:
#     boolean, frame = cap.read()
#     # boolean indicates if the capture was successful or if there was an error
#
#     cv2.imshow("window", frame)
#
#     if cv2.waitKey(1) == ord('q'):
#         # waitkey(1) will wait for 1 millisecond
#         # if a key is pressed while waitkey is waiting, it will return
#         # the ordinal value of the pressed key
#         # the ordinal value of a key is the ASCII integer of that key
#         # in this example the loop will end when q is pressed
#         break

# fancy nonsense
# while True:
#     boolean, frame = cap.read()
#     # boolean indicates if the capture was successful or if there was an error
#
#     frame = cv2.resize(frame, (800, 800))
#     # square the image
#
#     image = np.zeros(frame.shape, np.uint8)
#     # this creates a numpy array with the same dimensions as our image filled with
#     # zeros, 8 bit unsigned integer zeroes
#
#     small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
#     # this resizes the frame
#
#     height, width, channels = frame.shape
#     # will need this for next step
#
#     top_left = cv2.rotate(small_frame, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
#     bottom_left = cv2.rotate(small_frame, cv2.cv2.ROTATE_90_CLOCKWISE)
#     top_right = cv2.rotate(small_frame, cv2.cv2.ROTATE_180)
#     bottom_right = small_frame
#     # spin the things
#
#     image[:height//2, :width//2] = top_left  # top left
#     image[height//2:, :width//2] = bottom_left  # bottom left
#     image[:height//2, width//2:] = top_right  # top right
#     image[height//2:, width//2:] = bottom_right  # bottom right
#     # copying the frame 4 times
#
#     cv2.imshow("window", image)
#
#     if cv2.waitKey(1) == ord('q'):
#         # waitkey(1) will wait for 1 millisecond
#         # if a key is pressed while waitkey is waiting, it will return
#         # the ordinal value of the pressed key
#         # the ordinal value of a key is the ASCII integer of that key
#         # in this example the loop will end when q is pressed
#         break


# cleanup
# cap.release()
# cv2.destroyAllWindows()

"""25 minutes"""

while True:
    boolean, frame = cap.read()
    height, width, channels = frame.shape

    start = (0, 0)
    end = (width, height)
    BGR = (255, 0, 0)
    line_thickness = 10

    # img = cv2.line(frame, start, end, BGR, line_thickness)
    # the origin of the coordinates is the top left
    # x and y increase as they move away from the origin
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (255, 0, 0), 10)

    top_left = (100, 100)
    bottom_right = (200, 200)
    color = (128, 128, 128)
    thickness = 5  # -1 to fill
    img = cv2.rectangle(frame, top_left, bottom_right, color, thickness)

    center = (300, 300)
    radius = 60
    color = (0, 0, 255)
    thickness = -1
    img = cv2.circle(frame, center, radius, color, thickness)

    font = cv2.FONT_HERSHEY_PLAIN
    text = "Hello World"
    font_size = 4
    location = (200, height-20)
    color = (0, 0, 0)
    thickness = 5
    anti_aliasing = cv2.LINE_AA
    img = cv2.putText(img, text, location, font, font_size,  color, thickness, anti_aliasing)
    # coordinates are backward here

    cv2.imshow("window", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()

""" 45 minutes"""


























































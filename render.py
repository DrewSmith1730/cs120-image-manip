# TODO: you will need to install cv2
# Run "pip3 install opencv-python" in CLI
import cv2
import sys
# Kaleidoscope requires numpy. Uncomment this line and install it if you need to.
import numpy as np

# Store command line arguments in variables
# TODO: change the next line to store the filename
filename = sys.argv[1]
manip = sys.argv[2]

# Open the image file
img = cv2.imread('../' + filename)
# Get the dimensions (in pixels) of the image
dimensions = img.shape
# Copy the original image into an image for manipulation
img_manip = cv2.resize(img, (dimensions[1], dimensions[0]))
# images used for the kalidascope part
img_manip_2 = cv2.resize(img, (dimensions[1], dimensions[0]))
img_manip_3 = cv2.resize(img, (dimensions[1], dimensions[0]))
img_manip_4 = cv2.resize(img, (dimensions[1], dimensions[0]))
# TODO: Store white in a list, where each of the three parts is on a scale of [0, 255]
white = [255, 255, 255]
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        if manip == 'flip':
            img_manip[x, y] = img[dimensions[0]-1-x, y]
            # for the kalidascope part
            img_manip_2[x, y] = img[x, dimensions[1]-1-y]
            img_manip_3[x, y] = img[dimensions[0]-1-x, dimensions[1]-1-y]

        elif manip == 'mirror':
            # TODO: mirror the image and store in img_manip[x, y]
            img_manip[x, y] = img[x, dimensions[1]-1-y]
            # for the kalidascope part
            img_manip_2[x, y] = img[dimensions[0]-1-x, y]
            img_manip_3[x, y] = img[dimensions[0]-1-x, dimensions[1]-1-y]

            pass
        elif manip == 'invert':
            # TODO: invert the image and store in img_manip[x, y]
            # Hint: img[x, y] returns the color of the pixel at that coordinate.
            # You can invert by subtracting that color from white.
            img_manip[x, y] = white - img[x, y]
            # for the kalidascope part
            img_manip_2[x, y] = img[dimensions[0]-1-x, y]
            img_manip_3[x, y] = img[x, dimensions[1]-1-y]
            img_manip_4[x, y] = img[dimensions[0]-1-x, dimensions[1]-1-y]

            pass

# Displays the original image in the top left corner of the screen.
image = 'Original image'
cv2.namedWindow(image)
cv2.moveWindow(image, 0, 0)
cv2.imshow(image, img)
# TODO: Display the manipulated image alongside the original image.
# for now just displayig the image at all
if manip == "flip":
    image_manip = 'Flipped image'
    cv2.namedWindow(image_manip)
    cv2.moveWindow(image_manip, 0, dimensions[0])
    cv2.imshow(image_manip, img_manip)
elif manip == "mirror":
    image_manip = 'Mirrored image'
    cv2.namedWindow(image_manip)
    cv2.moveWindow(image_manip, dimensions[1], 0)
    cv2.imshow(image_manip, img_manip)
elif manip == "invert":
    image_manip = 'Inverted image'
    cv2.namedWindow(image_manip)
    cv2.moveWindow(image_manip, 0, dimensions[0])
    cv2.imshow(image_manip, img_manip)


# TODO: Create a kaleidoscope image, display it, and save it to a file.
# This line puts two images side-by-side in one window.
# if the flipped is made first

if manip == 'flip':
    left_half = np.concatenate((img, img_manip), axis=0)
    right_half = np.concatenate((img_manip_2, img_manip_3), axis=0)
    kaleidoscope = np.concatenate((left_half, right_half), axis=1)
elif manip == 'mirror':
    left_half = np.concatenate((img, img_manip_2), axis=0)
    right_half = np.concatenate((img_manip, img_manip_3), axis=0)
    kaleidoscope = np.concatenate((left_half, right_half), axis=1)
elif manip == 'invert':
    left_half = np.concatenate((img, img_manip_2), axis=0)
    right_half = np.concatenate((img_manip_3, img_manip_4), axis=0)
    kaleidoscope = np.concatenate((left_half, right_half), axis=1)


# TODO: Save the image using the imwrite method from cv2
# TODO: Show the image
newfile = "D:/Kaleidoscope_" + filename
cv2.imshow('Kaleidoscope view of your Image!', kaleidoscope)
if cv2.imwrite(newfile, kaleidoscope):
    print("Your image has been saved")

# Infinite loop to keep the windows open until the escape key is pressed.
while True:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()


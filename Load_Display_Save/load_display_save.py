
##############################################################

USAGE : python load_display_save.py -i [Path to the image]
  
###############################################################

import cv2  # Importing computer vision library
import argparse   # used for command line arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
# To get image argument and its path in a dictionary
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args["image"])  # to read images
cv2.imshow("Image", image)  # to display images
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)  # to write into new images

# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#An arguement to specify the particular csv file
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
#An arguement to specify the particular image we are looking for; this one is necessary
ap.add_argument("-i", "--ref", required=True,
	help="path to input image")
#Dictionary with all command line inputted values
args = vars(ap.parse_args())







#Pull out the string that shows what image we are looking for
reference = args["ref"]
print ("The image we are looking for: ")
print(reference)







#load the binary of the image that corresponds to the string that we put in, taking this info from the saved image
binary = cv2.imread(args["ref"])





#Extrapolate the relevant values from the binary 
barcode_we_want = pyzbar.decode(binary)





#Using those values flat out decode the barcodes in the reference image to string.
for barcode in barcode_we_want:
	barcode_we_want_string = barcode.data.decode("utf-8")

print("The string we are looking for: ")
print(barcode_we_want_string)
	




# initialize the video stream and allow the camera sensor to warm up
print("Starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# open the output CSV file for writing 
#create an empty iterating variable to hold the set of strings found
csv = open(args["output"], "w")
found = set()











# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# find the barcodes in the frame and decode each of the barcodes
	barcodes_in_frame = pyzbar.decode(frame)

#loop over the detected barcodes
	for barcode in barcodes_in_frame:

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect

		#If the barcode string matches draw the box in green, if not, red
		if barcode_we_want_string == barcodeData:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		else:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)	

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)

		#If the barcode string matches output text in green, if not, red
		if barcode_we_want_string == barcodeData:
			cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		else:
			cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
			barcodeData))
			csv.flush()
			found.add(barcodeData)

	# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break







# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
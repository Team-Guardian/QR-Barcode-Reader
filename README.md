
This is the second version of the QR code scanner for machine vision. 

What the code does

Accesses your computers camera and reads QR codes from the individual frames. Highlights in green if the string encoded 
in the QR code matches the one inputted (this is inputted from the command line). Highlights in red if the string does not
match. All QR codes found within your camera's view are logged into a csv file named barcodes.csv. Two test qr codes have 
also been added, one says test,the other team_guardian.

What each file is for:

access_permissions.txt - a shortcut to the commands necessary to relay permissions, please use this after reading the links below, one or two installations are required first.

command.txt - a sample command to run the code

imreaderV3.py - the program file

team_guardian_qr_code - QR code that says team_guardian

test_qr_code - QR code that says test


Relevant links:

How to relay access permissions of camera into virutalbox - 
https://scribles.net/using-webcam-in-virtualbox-guest-os-on-windows-host/
https://richardstechnotes.com/2017/03/07/connecting-a-webcam-to-a-virtualbox-guest-os/

How to install opencv
https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/




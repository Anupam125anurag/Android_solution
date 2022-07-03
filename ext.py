from zipfile import ZipFile

with ZipFile('/var/lib/jenkins/workspace/Android_Framework_Pixel_git/android-cts-12.1_r2-linux_x86-arm.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

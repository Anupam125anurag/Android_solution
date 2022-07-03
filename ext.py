from zipfile import ZipFile

with ZipFile('android-cts-12_r4-linux_x86-arm.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
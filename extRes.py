from zipfile import ZipFile

with ZipFile('/var/lib/jenkins/workspace/Android_Framework_Pixel_git/cts_results.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
from datetime import datetime
import os
import pytz

#os.remove("/home/idm/Desktop/HDK855/cts_results.zip")

IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
d=datetime_ist.strftime('%Y.%m.%d_%H')
#print(d)
file2 = ''
for file in os.listdir("/var/lib/jenkins/workspace/Android_Framework_Pixel_git/android-cts/results"):
  if file.startswith(d):
    #print(file)
    file2=file
    break
        
     
  
old="/var/lib/jenkins/workspace/Android_Framework_Pixel_git/android-cts/results/" + file2
print(old)
new="/var/lib/jenkins/workspace/Android_Framework_Pixel_git/cts_results.zip"
os.rename(old,new)



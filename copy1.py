import shutil

original = r'/home/idm/Downloads/android-cts-12.1_r2-linux_x86-arm.zip'
target = r'/var/lib/jenkins/workspace/Android_Framework_Pixel_git/android-cts-12.1_r2-linux_x86-arm.zip'

shutil.copyfile(original, target)

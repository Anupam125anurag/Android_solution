*** Settings ***
Documentation    Sanity test
Suite Setup    Initialize Metadata

Library         ../library/base_lib.py
#Variables       ../locators/camera_locators.py
Library         ../library/camera_lib.py

Test Setup   START_TEST
Test Teardown  END_TEST

*** Keyword ***
Initialize Metadata
        #${devicename}       GET_DEVICE_NAME
        #Set suite metadata    Device Name    ${devicename}
        ${devicemodel}       GET_DEVICE_MODEL
        Set suite metadata    Device Model    ${devicemodel}
        ${Android_ver}       GET_ANDROID_VERSION
        Set suite metadata    OS Version    ${Android_ver}
        ${build_id}       GET_BUILD_ID
        Set suite metadata    Build ID    ${build_id}

*** Variable ***
${t}        10

*** Test Cases ***
Test_001 - Capture Image
    [tags]    Sanity
    #launch camera
    #${result}     LAUNCH_APP     ${appname}
    ${result}     LAUNCH_CAMERA
    ${result}     CAPTURE_IMAGE
    run keyword if  ${result}==False    Fail    Image_Capture_Failed    ELSE    LOG    PASS

 

#!/bin/bash
DIRECTORY_SCRIPT_MASS=/Users/dass/Tools/mobsf/Mobile-Security-Framework-MobSF/scripts
DIRECTORY_SCRIPTS=/Users/dass/Tools/Scripts
DIRECTORY_APKS=/Users/dass/Tools/Apks
SERVER_ADDRESS=127.0.0.1:8000

cd $DIRECTORY_SCRIPT_MASS

docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
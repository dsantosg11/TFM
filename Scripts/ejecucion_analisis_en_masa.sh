#!/bin/bash
DIRECTORY_SCRIPT_MASS=/Users/dass/Tools/mobsf/Mobile-Security-Framework-MobSF/scripts
DIRECTORY_SCRIPTS=/Users/dass/Tools/Scripts
DIRECTORY_PREP_APKS=/Users/dass/Tools/Preprocessed_Apks
SERVER_ADDRESS=127.0.0.1:8000

cd $DIRECTORY_SCRIPT_MASS

echo 'Por favor, inserte la API KEY: '
read API_KEY

python mass_static_analysis.py -d $DIRECTORY_PREP_APKS -s $SERVER_ADDRESS -k $API_KEY

cd $DIRECTORY_SCRIPTS

python get_reports_mobsf.py
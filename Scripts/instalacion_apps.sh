#!/bin/sh
DIRECTORY_APKS=/Users/dass/Tools/Preprocessed_Apks

cd $DIRECTORY_APKS
COUNTER=0

for i in $(ls | egrep -i '*\.apk'); do
    COUNTER=$((COUNTER+1))
    NOMBRE=${i%.*};
    adb -d install $i;
    echo "Aplicacion $NOMBRE instalada en el terminal via adb."
done

echo "$COUNTER aplicaciones instaladas en el terminal via adb. Instalación terminada"
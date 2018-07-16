#!/bin/sh
DIRECTORY_CODE=/Users/dass/Tools/IntelliDroid/AppAnalysis
DIRECTORY_SCRIPTS=/Users/dass/Tools/Scripts
DIRECTORY_JARS=/Users/dass/Tools/jars
DIRECTORY_PREP_APKS=/Users/dass/Tools/Preprocessed_Apks
DIRECTORY_RESULTS=/Users/dass/Tools/Results

cp -a $DIRECTORY_PREP_APKS/. $DIRECTORY_JARS
cd $DIRECTORY_JARS
COUNTER=0

find . -type f -name "* *.apk" -exec bash -c 'mv "$0" "${0// /_}"' {} \;

for i in $(ls | egrep -i '*\.apk'); do
    COUNTER=$((COUNTER+1))
    NOMBRE=${i%.*};
    if bash $DIRECTORY_CODE/preprocess/PreprocessAPK.sh $i >> $DIRECTORY_RESULTS/logs/log-$NOMBRE.txt; then
        echo ""
    else
        echo "Error al generar el archivo jar. No se ejecutará análisis con Intellidroid." && exit 1
    fi
    if bash $DIRECTORY_CODE/preprocess/PreprocessDataset.sh $NOMBRE >> $DIRECTORY_RESULTS/logs/log-$NOMBRE.txt; then
        echo ""
    else
        echo "Error al generar el archivo jar. No se ejecutará análisis con Intellidroid." && exit 1
    fi
done

echo "$COUNTER archivos procesados y convertidos en jars para Intellidroid. Comienza el análisis de Intellidroid..."

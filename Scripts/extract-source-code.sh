#!/bin/sh
DIRECTORY_SCRIPTS_DECOMPILE=/Users/dass/Tools/decompile-apk
DIRECTORY_OUTPUT=/Users/dass/Tools/decompile-apk/output
DIRECTORY_SCRIPTS=/Users/dass/Tools/Scripts
DIRECTORY_APKS=/Users/dass/Tools/Apks
DIRECTORY_PREP_APKS=/Users/dass/Tools/Preprocessed_Apks
DIRECTORY_SOURCE_CODE=/Users/dass/Tools/Results/Codigo_fuente_apps
DIRECTORY_LITERADAR=/Users/dass/Tools/LibRadar/LiteRadar/LiteRadar
DIRECTORY_RESULTS=/Users/dass/Tools/Results

cd $DIRECTORY_APKS
COUNTER=0

doalarm () { perl -e 'alarm shift; exec @ARGV' "$@"; } # define a helper function

find . -type f -name "* *.apk" -exec bash -c 'mv "$0" "${0// /_}"' {} \;

for i in $(ls | egrep -i '*\.apk'); do
    COUNTER=$((COUNTER+1))
    i=${i// /_}
    echo "Procesando la aplicación: $i"
    NOMBRE=${i%.*};
    cd $DIRECTORY_LITERADAR;
    python2 literadar.py $DIRECTORY_APKS/$i > $DIRECTORY_RESULTS/librerias/lista_completa/librerias_$NOMBRE.json;
    echo "Extraida lista de bibliotecas que utiliza"
    NOMBRE="$NOMBRE-jadx";
    cd $DIRECTORY_SCRIPTS_DECOMPILE;
    doalarm 600 sh ./jadx-apk.sh $DIRECTORY_APKS/$i &> $DIRECTORY_RESULTS/logs/log-$NOMBRE.txt;
    #expect -c 'set echo \"-noecho\"; set timeout $time; spawn -noecho $command; expect timeout { exit 1 } eof { exit 0 }'
    echo "Extraido el codigo fuente de la app"
    mv $DIRECTORY_OUTPUT/$NOMBRE $DIRECTORY_SOURCE_CODE/$NOMBRE;
    cd $DIRECTORY_SOURCE_CODE
    python $DIRECTORY_SCRIPTS/get_permissions.py $NOMBRE > $DIRECTORY_RESULTS/permisos/permisos_$NOMBRE.txt;
    echo "Extraida lista de permisos que necesita"
    echo "Se termina de pre-procesar la aplicacion $i. Se mueve el archivo a preprocesadas."
    cd $DIRECTORY_APKS
    mv $i $DIRECTORY_PREP_APKS;
done

echo "Procesadas $COUNTER aplicaciones y obtenido el código fuente, librerías y permisos. Pasando al análisis del código..."
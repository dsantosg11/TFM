#!/bin/sh
DIRECTORY_OUTPUT=/Users/dass/Tools/Results/intellidroid
DIRECTORY_SCRIPTS=/Users/dass/Tools/Scripts
DIRECTORY_JARS=/Users/dass/Tools/jars
DIRECTORY_CODE=/Users/dass/Tools/IntelliDroid/AppAnalysis
DIRECTORY_TARGETS=/Users/dass/Tools/Results/targets

cd $DIRECTORY_JARS
COUNTER=0

export JAVA_HOME=$(/usr/libexec/java_home -v 1.7)

# Funcion auxiliar para timeout
doalarm () {
    perl -e 'alarm shift; exec @ARGV' "$@";
    echo 'Proceso interrumpido por timeout. Generando archivo vacío de targets...';
    RUTA_JSON=$DIRECTORY_OUTPUT/$NOMBRE/appInfo.json
    [ -f $RUTA_JSON ] || echo "{}" > $RUTA_JSON
} 

for d in $(ls -d $DIRECTORY_JARS/*/) ; do
    cd $d
    NOMBRE=$(basename $d*/)
    echo $NOMBRE
    cd $DIRECTORY_CODE
    COUNTER=$((COUNTER+1))
    echo "Obteniendo los targets mediante el análisis de Intellidroid de la app $NOMBRE"
    mkdir $DIRECTORY_OUTPUT/$NOMBRE
    if doalarm 500 ./IntelliDroidAppAnalysis -o $DIRECTORY_OUTPUT/$NOMBRE -t taintdroidTargets.txt -y $d; then
        echo "Jar generado con éxito. Obteniendo targets."
    else
        echo 'Proceso interrumpido por error en el procesamiento de Intellidroid. Generando archivo vacío de targets...';
        RUTA_JSON=$DIRECTORY_OUTPUT/$NOMBRE/appInfo.json
        [ -f $RUTA_JSON ] || echo "{}" > $RUTA_JSON
    fi
    cd $DIRECTORY_JARS
done

echo "Procesadas $COUNTER aplicaciones. Moviendo targets a carpeta de resultados."

cd $DIRECTORY_OUTPUT

for dir in $(ls -d $DIRECTORY_OUTPUT/*/) ; do
    cd $dir
    for i in $(ls | egrep -i 'appInfo.json'); do
        NOMBRE="$(basename $dir).json"
        mv $i $NOMBRE
        cp $NOMBRE $DIRECTORY_TARGETS 
    done
done

echo "Proceso de Intellidroid finalizado."
exit
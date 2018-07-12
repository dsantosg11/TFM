#!/bin/sh
DIRECTORY_JADX=/Users/dass/Tools/jadx/build/jadx
DIRECTORY_SCRIPTS=/Users/dass/Tools/IntelliDroid/AppAnalysis
DIRECTORY_CODE=/Users/dass/Tools/Scripts
DIRECTORY_APKS=/Users/dass/Tools/Apks
DIRECTORY_PREP_APKS=/Users/dass/Tools/Preprocessed_Apks

cd $DIRECTORY_APKS
COUNTER=0

for i in $(ls | egrep -i '*\.apk'); do
    COUNTER=$((COUNTER+1))
    i=${i// /_}
    echo $i
    NOMBRE=${i%.*};
    bash $DIRECTORY_SCRIPTS/preprocess/PreprocessAPK.sh $i;
    bash $DIRECTORY_SCRIPTS/preprocess/PreprocessDataset.sh $NOMBRE;
    mv $NOMBRE $DIRECTORY_PREP_APKS/$NOMBRE
    echo 'Se comienza a analizar el Manifest de la aplicacion $NOMBRE'
    python $DIRECTORY_CODE/get_permissions.py $NOMBRE
    echo 'Se termina de analizar el Manifest de la aplicacion $NOMBRE'
done

echo "$COUNTER archivos procesados. Comprobando si queda algún archivo por descompilar..."

COUNTER=0
cd $DIRECTORY_PREP_APKS
for i in $(find . -name '*\.jar'); do
    COUNTER=$((COUNTER+1))
    i=${i// /_}
    echo $i
    NOMBRE=${i%.*};
    $DIRECTORY_JADX/bin/jadx -d . $i;
done

echo "$COUNTER archivos tratados extra. Descompilación terminada"
#!/bin/sh

filename='/Users/dass/Tools/Results/lista_paquetes.txt'

while read -r line
do
    name="$line"
    echo "Automatizando aplicación del paquete $name ... "
    adb -d shell monkey -p $name -v --pct-syskeys 0 5000
    echo "Se termina de automatizar la aplicación. Los resultados se mostraran en la app de Lumen."
done < "$filename"
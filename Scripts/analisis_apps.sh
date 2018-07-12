#!/bin/sh


analisis_lumen () {
    echo 'De acuerdo. Por favor, conecte su terminal vía adb a este ordenador. Iniciando el servidor adb...'; 
    adb start-server;
    echo 'Recuerde activar la depuración USB en las opciones de desarrollador de su terminal.';
    echo "Introduzca la dirección IP de su terminal: `echo $'\n> '`"
    read ipdir
    adb connect $ipdir
    echo 'A continuación debería figurar su dispositivo. Si no es así, revise su configuración:';
    adb devices;
    read -p "¿Está todo correcto? (y/n) `echo $'\n> '`" yn
    case $yn in
        [Yy]* ) echo "Instalando apps en el terminal. Espere..."; bash ./instalacion_apps.sh; break; echo 'Por favor, entre en la aplicación de Lumen Privacy Monitor de su teléfono y active la monitorización, otorgando los permisos necesarios';;
        [Nn]* ) echo 'No se realizará análisis con Lumen. Continuando con el proceso...'; break;;
        * ) echo "Por favor, conteste sí (y) o no (n).";;
    esac
    echo '¿Desea automatizar la ejecución de apps en su terminal para que Lumen las monitorice o desea realizarlo manualmente? (ATENCIÓN: Si no ha completado el proceso de configuración de su terminal, conteste que no (n)) (ATENCIÓN: El script de automatización genera gestos aleatorios en el terminal. Esto puede incurrir en desconfiguración de algún aspecto del mismo.';
    case $yn in
        [Yy]* ) echo "Automatizando el funcionamiento de las apps. Cuando terminen, abra Lumen para ver los resultados. Espere..."; bash ./automatizacion_apps_terminal.sh; break; echo 'Automatización finalizada. Continuando con el proceso...'; adb kill-server;;
        [Nn]* ) echo 'Use las aplicaciones instaladas para que Lumen recoja resultados. Continuando con el proceso...'; break;;
        * ) echo "Por favor, conteste sí (y) o no (n).";;
    esac
    
} 

# Carpeta de Scripts por si no estuvieramos
cd '/Users/dass/Tools/Scripts'

# Lista de app a procesar
python generate_list.py

[ -s /Users/dass/Tools/Results/fileslist.txt ] || echo "No hay apks que procesar en la carpeta."; exit

# Código fuente, librerías y permisos
bash ./extract-source-code.sh
python parse_results_libraries.py

# Ejecución del servidor mobsf en ventana nueva
osascript -e 'tell app "Terminal"
    do script "cd /Users/dass/Tools/Scripts; bash ./ejecucion_servidor_mobsf.sh"
end tell'

# Análisis con MobSF y recolección de resultados
bash ./ejecucion_analisis_en_masa.sh
python get_reports_mobsf.py
python get_results_mobsf.py

# Recolección de resultados de Intellidroid
bash ./generate-jar.sh
bash ./analisis_intellidroid.sh

#Preguntamos al usuario si desea realizar la parte de Lumen
while true; do
    read -p "¿Desea realizar análisis dinámico con Lumen? Necesitará un terminal físico configurado con adb y el SDK de Android en su terminal (y/n) `echo $'\n> '`" yn
    case $yn in
        [Yy]* ) analisis_lumen; break;;
        [Nn]* ) echo 'No se realizará análisis con Lumen. Continuando con el proceso...'; break;;
        * ) echo "Por favor, conteste sí (y) o no (n).";;
    esac
done

# Generación del informe detallado
python generate_word_document.py
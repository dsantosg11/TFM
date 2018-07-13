from xml.dom.minidom import parseString
import sys

file_name = sys.argv[1]

directory = '/Users/dass/Tools/Results/Codigo_fuente_apps/'+ file_name
paquetes = '/Users/dass/Tools/Results/lista_paquetes.txt'

data = ''
with open(directory+'/AndroidManifest.xml','r') as f:
    data = f.read()
dom = parseString(data)
manifest_element = dom.documentElement
package = manifest_element.getAttribute('package')
with open(paquetes,'a') as paq:
    paq.write(package+'\n')
nodes_permission = dom.getElementsByTagName('uses-permission')
nodes_feature = dom.getElementsByTagName('uses-feature')
permissions = []
features = []
for node in nodes_permission:
    permission = node.getAttribute('android:name')
    permissions.append(permission)
for node in nodes_feature:
    feature = node.getAttribute('android:name')
    features.append(feature)

# Permisos
if "android.permission.ACCESS_FINE_LOCATION" in permissions or "android.permission.ACCESS_COARSE_LOCATION" in permissions:
    print ("Esta app accede a la localizacion exacta y/o aproximada del terminal, lo cual puede construir una huella digital (fingerprint) sobre usted.")
if "android.permission.BLUETOOTH" in permissions or "android.permission.BLUETOOTH_ADMIN" in permissions:
    print("Esta app accede al Bluetooth, lo cual puede ser utilizado para fingerprinting sonoro.")
if "android.permission.BLUETOOTH_PRIVILEGED" in permissions:
    print("Esta app puede emparejar dispositivos Bluetooth sin autorizacion expresa, permiso muy peligroso y propicio para filtrar información privada")
if "android.permission.ACCESS_NETWORK_STATE" in permissions or "android.permission.ACCESS_WIFI_STATE" in permissions:
    print("Esta app accede al estado de la red y/o Wi-Fi, haciendo factible un posible fingerprinting basado en RSSI")
if "android.permission.CHANGE_NETWORK_STATE" in permissions or "android.permission.CHANGE_WIFI_STATE" in permissions:
    print("Esta app puede cambiar el estado de la conectividad de red y/o Wi-Fi, se trata de un permiso peligroso que puede provocar alteraciones en la red y realizar fingerprinting basado en RSSI.")
if "android.permission.CHANGE_WIFI_MULTICAST_STATE" in permissions:
    print("Esta app puede entrar en el modo multicast de Wi-Fi y realizar cambios, haciendo factible un posible fingerprinting basado en RSSI.")
if "android.permission.INTERNET" in permissions:
    print("Esta app puede abrir sockets de red, por donde puede filtrar información entre procesos o al exterior.")
if "android.permission.BODY_SENSORS" in permissions:
    print("Esta app puede acceder a datos de los sensores que utilice el usuario para medir acciones de su cuerpo, como la frecuencia cardíaca. Esto en combinación con otros factores, puede ser utilizado para identificarle.")
if "android.permission.CAPTURE_AUDIO_OUTPUT" in permissions:
    print("Esta app puede capturar el audio del terminal, posible fingerprinting sonoro")
if "android.permission.CAPTURE_VIDEO_OUTPUT" in permissions or "android.permission.CAPTURE_SECURE_VIDEO_OUTPUT" in permissions:
    print("Esta app puede capturar el video del terminal, posible fingerprinting visual.")
if "android.permission.CAMERA" in permissions:
    print("Esta app puede acceder a la cámara del dispositivo. Es posible que se lleve a cabo fingerprinting visual.")
if "android.permission.LOCATION_HARDWARE" in permissions:
    print("Esta app puede utilizar características de localización del Hardware, lo cual puede construir una huella digital (fingerprint) sobre usted..")
if "android.permission.NFC" in permissions or "android.permission.NFC_TRANSACTION_EVENT" in permissions:
    print("Esta app puede realizar operaciones NFC y/o recibir los eventos. Esto puede ser utilizado para construir una huella digital sobre usted o para realizar transacciones sin su permiso.")
if "android.permission.RECORD_AUDIO" in permissions:
    print("Esta app puede grabar audio, lo cual puede utilizarse para fingerprinting híbrido de sonido.")
if "android.permission.USE_BIOMETRIC" in permissions:
    print("Esta app puede utilizar las modalidades biométricas del dispositivo. Esto en combinación con otros factores, puede ser utilizado para identificarle.")

#Caracteristicas
if "android.hardware.sensor.accelerometer" in features:
    print("Esta app puede acceder al acelerómetro del dispositivo. Esto puede ser utilizado para construir una huella digital basada en el movimiento.")
if "android.hardware.sensor.gyroscope" in features:
    print("Esta app puede acceder al giroscopio del dispositivo. Esto puede ser utilizado para construir una huella digital basada en el movimiento.")
if "android.hardware.sensor.ambient_temperature" in features:
    print("Esta app puede acceder al sensor de temperatura ambiente del dispositivo. Esta información, combinada con otra de otro tipo (visual, sonora, de movimiento, RSSI...), puede utilizarse para realizar fingerprinting híbrido.")
if "android.hardware.sensor.barometer" in features:
    print("Esta app puede acceder al barómetro del dispositivo. Esta información, combinada con otra de otro tipo (visual, sonora, de movimiento, RSSI...), puede utilizarse para realizar fingerprinting híbrido.")
if "android.hardware.sensor.compass" in features:
    print("Esta app puede acceder a la brújula del dispositivo. Es posible que se esté realizando un fingerprinting basado en movimiento con esta información.")
if "android.hardware.sensor.hifi_sensors" in features:
    print("Esta app puede acceder a los sensores de alta fidelidad del dispositivo.")
if "android.hardware.sensor.heartrate" in features or "android.hardware.sensor.heartrate.ecg" in features:
    print("Esta app puede acceder al monitor de frecuencia cardíaca o al sensor de electrocardiograma del dispositivo. Esto en combinación con otros factores, puede ser utilizado para identificarle")
if "android.hardware.sensor.light" in features:
    print("Esta app puede acceder a los sensores de luz del dispositivo. Es posible que se esté realizando un fingerprinting visual")
if "android.hardware.sensor.proximity" in features:
    print("Esta app puede acceder a los sensores de proximidad del dispositivo. Es posible que sde esté realizando fingerprinting de movimiento.")
if "android.hardware.sensor.relative_humidity" in features:
    print("Esta app puede acceder a los sensores de humedad relativa del dispositivo. Esto en combinación con otros factores, puede ser utilizado para identificarle")
if "android.hardware.sensor.stepcounter" in features:
    print("Esta app puede utilizar el contador de pasos del dispositivo. Es posible que sde esté realizando fingerprinting de movimiento.")
if "android.hardware.sensor.stepdetector" in features:
    print("Esta app puede utilizar el detector de pasos del dispositivo. Es posible que sde esté realizando fingerprinting de movimiento.")

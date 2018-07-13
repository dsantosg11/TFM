import os
import shutil

path_jars='/Users/dass/Tools/jars'
path_prep_apks='/Users/dass/Tools/Preprocessed_Apks'
path_sourcecode='/Users/dass/Tools/Results/Codigo_fuente_apps'
path_enlacesmobsf='/Users/dass/Tools/Results/enlaces_mobsf'
path_intellidroid='/Users/dass/Tools/Results/intellidroid'
path_librerias='/Users/dass/Tools/Results/librerias'
path_permisos='/Users/dass/Tools/Results/permisos'
path_reportsmobsf='/Users/dass/Tools/Results/reports_mobsf'
path_df='/Users/dass/Tools/Results/tables_static/df'
path_logs='/Users/dass/Tools/Results/logs'
path_html='/Users/dass/Tools/Results/tables_static/html'
path_images='/Users/dass/Tools/Results/tables_static/images'
path_targets='/Users/dass/Tools/Results/targets'
lista_apps='/Users/dass/Tools/Results/fileslist.txt'
paquetes='/Users/dass/Tools/Results/lista_paquetes.txt'

def cleaning(folder_path):
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)


if __name__ == '__main__':
    print('Borrando archivos de análisis anteriores, sólo quedarán los informes.')
    if os.path.isfile(lista_apps):
        os.remove(lista_apps)
    if os.path.isfile(paquetes):
        os.remove(paquetes)
    cleaning(path_jars)
    cleaning(path_prep_apks)
    cleaning(path_logs)
    cleaning(path_sourcecode)
    cleaning(path_enlacesmobsf)
    cleaning(path_intellidroid)
    cleaning(path_librerias+'/lista_completa')
    cleaning(path_librerias+'/blacklist')
    cleaning(path_permisos)
    cleaning(path_reportsmobsf)
    cleaning(path_df)
    cleaning(path_html)
    cleaning(path_images)
    cleaning(path_targets)
    print('Terminada la limpieza')

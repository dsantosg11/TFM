import os
import csv
import sys
import shutil

directory_processing = '/Users/dass/Tools/Results/librerias/processing_info/'
directory_names = '/Users/dass/Tools/Results/librerias/processing_info/names'
directory_packages = '/Users/dass/Tools/Results/librerias/processing_info/packages'

blacklist_libraries = ['AdMob','AdWhirl','Flurry','Flurry SDK', 'InMobi','MoPub','AppLovin','Adgoji','Android Beacon Library', 'altbeacon', 'ZXing', 'ZXing ("Zebra Crossing")', 'Fluzo','GraceNote']

def search_blacklist(blacklist, list_to_check):
    coincidencias = []
    for element in blacklist:
        if element in list_to_check:
            if (element == "ALTBEACON"):
                element = "ANDROID BEACON LIBRARY"
            if(element == 'ZXING ("ZEBRA CROSSING")'):
                element = 'ZXING'
            coincidencias.append(element)
    return coincidencias

def treat_packages_names (list_to_treat):
    new_list=[i.split('/') for i in list_to_treat]
    def_list = []
    for element in new_list:
        def_list.extend(element)
    return list(set(def_list))

def check_files_directory (directory_to_check,filename):
    global blacklist_libraries
    file_libraries=directory_to_check+"/"+filename
    with open(file_libraries,'r', encoding='latin1') as f:
        reader = csv.reader(f)
        names = list(reader)[0]
    names_upper = [elem.upper() for elem in names]
    if (directory_to_check == directory_packages):
        names_upper = treat_packages_names(names_upper)
    blacklist_upper = [elem.upper() for elem in blacklist_libraries]
    f.close()
    return search_blacklist(blacklist_upper, names_upper)

            
if __name__ == '__main__':
    for filename in os.listdir(directory_names):
        if(filename==".DS_Store"):
            continue
        coincidencias_nombres = check_files_directory(directory_names, filename)
        coincidencias_paquetes = check_files_directory(directory_packages,filename)
        path_to_write= directory_processing+filename[:-4]+'.csv'
        with open(path_to_write,'w+') as fi:
            fi.write( ','.join(list((set(coincidencias_nombres+coincidencias_paquetes)))))
            fi.close()
    shutil.rmtree(directory_names)
    os.mkdir(directory_processing+'names')
    shutil.rmtree(directory_packages)
    os.mkdir(directory_processing+'packages')
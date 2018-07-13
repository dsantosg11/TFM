import os 

path = '/Users/dass/Tools/Apks'
path_textfile = '/Users/dass/Tools/Results/fileslist.txt'

print('Comienza el proceso. Obteniendo lista de aplicaciones a analizar...')

listaDir = os.listdir(path)

if '.DS_Store' in listaDir:
    listaDir.remove('.DS_Store')

listaDir = [s.strip('.apk') for s in listaDir]    

print('Se analizarán las siguientes apps:')
for element in listaDir:
    print(element+'\n')

with open(path_textfile, 'w') as f:
    f.write("\n".join(map(str, listaDir)))
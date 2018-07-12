import os 

path = '/Users/dass/Tools/Apks'
path_textfile = '/Users/dass/Tools/Results/fileslist.txt'

listaDir = os.listdir(path)

if '.DS_Store' in listaDir:
    listaDir.remove('.DS_Store')

listaDir = [s.strip('.apk') for s in listaDir]    

with open(path_textfile, 'w') as f:
    f.write("\n".join(map(str, listaDir)))
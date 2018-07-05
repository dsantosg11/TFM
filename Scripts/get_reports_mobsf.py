from urllib.request import urlopen
import urllib.error 

fichero_enlaces_analisis = '/Users/dass/Tools/Results/enlaces_mobsf/enlaces_analisis.txt'
fichero_enlaces_reports = '/Users/dass/Tools/Results/enlaces_mobsf/informes_analisis.txt'

def download_file(download_url,name):
    response = urlopen(download_url)
    file = open('/Users/dass/Tools/Results/reports_mobsf/'+name+".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed "+name)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        if last == '':
            return s[start:]
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def replace_name(file,string):
    with open(file) as fi:
        lineas = fi.readlines()
        lineas = [x.strip() for x in lineas]
        for linea in lineas:
            new_name = 'error'
            if linea == '':
                continue
            hashcode = find_between(linea,'&checksum=','')
            if hashcode == string:
                new_name = find_between(linea,'?name=','&type=')
                if(new_name[-5:]=='.appx'):
                    new_name=new_name[:-5]
                else:
                    new_name=new_name[:-4]
                break
        fi.close()
    return new_name

if __name__ == "__main__":
    with open(fichero_enlaces_reports) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        f.close()
    counter = 0
    for enlace in content:
        if (enlace == ''):
            continue
        try:
            counter = counter + 1
            hash_report = find_between(enlace,'?md5=','&type=')
            name_report = replace_name(fichero_enlaces_analisis,hash_report)
            download_file(enlace,name_report)
        except urllib.error.HTTPError:
            print("Error when taking file "+name_report+ ' from server.')
            pass
    print("Completed all "+str(counter)+ ' files.')
#!/usr/bin/env python
# Mass Static Analysis
import os
import urllib.request
import urllib.error
import urllib.parse
import argparse
import requests


def is_server_up(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.error.URLError:
        pass
    return False


def start_scan(directory, server_url, apikey, rescan='0'):
    print("\nLooking for Android/iOS/Windows binaries or source code in : " + directory)
    print("[INFO] Uploading to MobSF Server")
    uploaded = []
    MIME = {
        ".apk": 'application/octet-stream',
        ".ipa": 'application/octet-stream',
        ".appx": 'application/octet-stream',
        ".zip": 'application/zip'
    }
    fichero_enlaces_analisis = '/Users/dass/Tools/Results/enlaces_mobsf/enlaces_analisis.txt'
    fichero_enlaces_reports = '/Users/dass/Tools/Results/enlaces_mobsf/informes_analisis.txt'
    
    for filename in os.listdir(directory):
        fpath = os.path.join(directory, filename)
        _, ext = os.path.splitext(fpath)
        if ext in MIME:
            files = {'file': (filename, open(fpath, 'rb'),
                              MIME[ext], {'Expires': '0'})}
            response = requests.post(
                server_url + '/api/v1/upload', files=files, headers={'AUTHORIZATION': apikey})
            response_json = response.json()
            hash_app = response_json.get('hash')
            if(filename[-4:]=='.apk'):
                app_type='apk'
            elif(filename[-4:]=='.ipa'):
                app_type='ipa'
            elif(filename[-5:]=='.appx'):
                app_type='appx'
            elif(filename[-4:]=='.zip'):
                app_type='zip'
            else:
                app_type='unknown'
            if response.status_code == 200 and "hash" in response_json:
                print("[OK] Upload OK: " + filename)
                print("App hash code: " + hash_app)
                with open(fichero_enlaces_analisis, 'a+') as f:
                    print(server_url+'/StaticAnalyzer/?name='+filename+'&type='+app_type+'&checksum='+hash_app+'\n', file=f)
                with open(fichero_enlaces_reports, 'a+') as f:
                    print(server_url+'/PDF/?md5='+hash_app+'&type='+app_type.upper()+'\n', file=f)
                uploaded.append(response.json())
            else:
                print("[ERROR] Performing Upload: " + filename)

    print("[INFO] Running Static Analysis")
    for upl in uploaded:
        print("[INFO] Started Static Analysis on: ", upl["file_name"])
        if rescan == '1':
            upl["re_scan"] = 1
        response = requests.post(
            server_url + "/api/v1/scan", data=upl, headers={'AUTHORIZATION': apikey})
        if response.status_code == 200:
            print("[OK] Static Analysis Complete: " + upl["file_name"])
        else:
            print("[ERROR] Performing Static Analysis: " + upl["file_name"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory",
                        help="Path to the directory that contains mobile app binary/zipped source code")
    parser.add_argument(
        "-s", "--ipport", help="IP address and Port number of a running MobSF Server. (ex: 127.0.0.1:8000)")
    parser.add_argument(
        "-k", "--apikey", help="MobSF REST API Key")
    parser.add_argument(
        "-r", "--rescan", help="Run a fresh scan. Value can be 1 or 0 (Default: 0)")
    args = parser.parse_args()

    if args.directory and args.ipport and args.apikey:
        server = args.ipport
        directory = args.directory
        server_url = "http://" + server
        apikey = args.apikey
        rescan = args.rescan
        if is_server_up(server_url) == False:
            print("MobSF REST API Server is not running at " + server_url)
            print("Exiting!")
            exit(0)
        # MobSF is running, start scan
        start_scan(directory, server_url, apikey, rescan)
    else:
        parser.print_help()

import html2text
import urllib.request
from lxml import etree, objectify, html
import xml.etree.ElementTree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six
import imgkit
import random
import os

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def get_table(id,tree):
    string = '//section[@id="{}"]'.format(id)
    code = tree.xpath(string)
    result = ''
    for tabla in code:
        new = etree.tostring(tabla).decode('utf-8')
        result= result + new
    return result

def save_dataframe(df, file_name):
    df.to_csv(file_name, encoding='utf-8', index=False)

def DataFrame_to_image(data, css, outputfile, format="png"):
    #Code for this function from: https://medium.com/@andy.lane/convert-pandas-dataframes-to-images-using-imgkit-5da7e5108d55
    '''
    For rendering a Pandas DataFrame as an image.
    data: a pandas DataFrame
    css: a string containing rules for styling the output table. This must 
         contain both the opening an closing <style> tags.
    *outputimage: filename for saving of generated image
    *format: output format, as supported by IMGKit. Default is "png"
    '''
    fn = str(random.random()*100000000).split(".")[0] + ".html"
    
    try:
        os.remove(fn)
    except:
        None
    text_file = open(fn, "a")
    
    # write the CSS
    text_file.write(css)
    # write the HTML-ized Pandas DataFrame
    text_file.write(data.to_html())
    text_file.close()
    
    # See IMGKit options for full configuration,
    # e.g. cropping of final image
    imgkitoptions = {"format": format}
    
    imgkit.from_file(fn, outputfile, options=imgkitoptions)
    os.remove(fn)
    
def deleteContent(fName):
    with open(fName, "w"):
        pass
    
def get_content (url):
    
    # First we parse the url and get the etree, deleting line breaks if there are
    if url[-1]=='\n':
        url=url[:-1]
        
    mysite = urllib.request.urlopen(url).read()

    root = mysite.decode('utf-8')

    parser = etree.HTMLParser()
    tree   = etree.fromstring(mysite, parser)

    filename= find_between(url,'?name=','&type')
    print("Procesando el archivo "+filename)
    route_filename = "/Users/dass/Tools/Results/tables_static/html/"+filename+'.html'

    #Now we get all tables of our interest: android-api, browsable, manifest, code, url, email, file; and put them into html file.

    with open(route_filename, "w") as myfile:
        myfile.write(get_table('android-api',tree))
        myfile.write(get_table('browsable',tree))
        myfile.write(get_table('manifest',tree))
        myfile.write(get_table('code',tree))
        myfile.write(get_table('file',tree))
        myfile.write(get_table('url',tree))
        myfile.write(get_table('email',tree))
        myfile.close()

    #We turn each table into pandas dataframe, displaying all info.
    pd.set_option('display.max_colwidth', -1)
    df_list = pd.read_html(route_filename)

    for i, df in enumerate(df_list):
        #And we store them as a png image
        route_image = "/Users/dass/Tools/Results/tables_static/images/"+filename+'_table_'+str(i)+'.png'
        route_csv_df = "/Users/dass/Tools/Results/tables_static/df/"+filename+'_table_'+str(i)+'.csv'
        DataFrame_to_image(df,'',route_image)
        save_dataframe(df,route_csv_df)
        #print (df)
        #print(render_mpl_table(df, header_columns=0, col_width=3.0))
        #df.to_csv('table {}.csv'.format(i))


    #beautiful_html = html2text.html2text(result)

if __name__ == "__main__":
    links_file = '/Users/dass/Tools/Results/enlaces_mobsf/enlaces_analisis.txt'
    lista_enlaces = []
    with open(links_file) as f:
        x=f.readlines()
        x=list(filter(lambda a: a != '\n', x))
        f.close()
    for element in x:
        get_content(element)
    print('Procesados todos los archivos del análisis de MobSF')
    deleteContent(links_file)
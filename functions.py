import requests
import json
import urllib.request
import os, sys
import shutil
from bs4 import BeautifulSoup
from config import *


def retrieveImagesAll(_createFolderDepartment=0):
    departamentos=["Amazonas","Ancash","Apurimac","Arequipa","Ayacucho","Cajamarca",
            "Callao","Cusco","Huancavelica","Huanuco","Ica","Junin","La libertad",
            "Lambayeque","Lima","Loreto","Madre de Dios","Moquegua","Pasco","Piura",
            "Puno","San Martin","Tacna","Tumbes","Ucayali"
            ]
    ids_departamentos=["1","92","279","367","485","608","2026","749","871","973","1061","1110"
            ,"1243","1339","1381","1563","1622","1637","1661","1693","1766","1889","1977",
            "2009","2034"
    ]
    if os.path.isdir('imagenes-requisitoriados') and os.path.exists('imagenes-requisitoriados'):
        shutil.rmtree('imagenes-requisitoriados', ignore_errors=True)

    os.mkdir('imagenes-requisitoriados',755)
    for departamento,id in zip(departamentos,ids_departamentos):
        retrieveImagesByDepartment(id,departamento,_createFolderDepartment)


def pagesByDepartment(_departamento):
    _payload = payload(_departamento,'100')
    _headers=headers()
    r = requests.post("http://www.recompensas.pe/views/ajax", data=_payload,headers=_headers)
    data = r.json()[2]['data']
    soup = BeautifulSoup(data,"html.parser")
    paginas = soup.find("li",class_="pager-current last")
    if paginas is None:
        return 1
    else:
        return paginas.text

def retrieveImagesByDepartment(_id,_departamento,_createFolderDepartment=0):
    paginas = pagesByDepartment(_id)
    
    for i in range(0,int(paginas)):
        _payload = payload(_id,i)
        _headers=headers()
        r = requests.post("http://www.recompensas.pe/views/ajax", data=_payload,headers=_headers)
        data = r.json()[2]['data']
        soup = BeautifulSoup(data,"html.parser")
        nombres = list()
        url_imagenes=list()
        for nombre in soup.find_all('span',class_='field-content'):
            nombres.append(nombre.find('a').text.replace(" ","-").lower())

        for url in soup.find_all('img'):
            url_imagenes.append(url.get('src'))

        for nombre,url_imagen in zip(nombres,url_imagenes):
            
            if(_createFolderDepartment == 1):
                directorio_imagen='imagenes-requisitoriados/'+ _departamento +'/' + nombre+'/'
            else:
                directorio_imagen='imagenes-requisitoriados/'+'/'
            #if not os.path.exists(directorio_imagen):
                #os.makedirs(directorio_imagen)
                urllib.request.urlretrieve(url_imagen, directorio_imagen+nombre+'.jpg')



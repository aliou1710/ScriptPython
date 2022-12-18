import sys
import json
import requests
import re 
import os
import time
from flask import send_file,render_template,request

#les dossiers à sauvegarder
folder = [r"D:\\scripts\Analysevisuelle",r"D:\\scripts\Bureau_etudes"]
#les formats de fichiers qu'on veut stocker
formatsfile = [".txt",".cs",".png",".jpg"]

#recuperer un file
def getfile():
    resp = requests.get('http://192.168.1.51:5000/')
    file = request.files.get('getOneFile')

    td =open(file.filename.strip(),'wb')
    td.write(resp.content)
    td.close()

#envoyer les fichiers au serveur
def sendfiles(directories):
    url = "http://192.168.1.51:5000/sendfiles"
    listsdico={}
    dico = {}
    count = 0
    for it in directories:
        #l'ensemeble des fichiers qui ont ce formats ci
        path  = listofFiles(it,formatsfile)
        #on split pour recupererle nom du dossier
        stext =re.split(r'[\\]',it)
        #on met dans un dictionnaire le nom du dossier et le nombre de fichier
        datafolder = {'foldername':stext[-1].strip(),"filenumber":len(path)}
        print("###### foldername ###### ",datafolder,flush =True)
        
        for item in path:
         
            print("item " ,it,flush=True)
            #files = {'file': open(item,'rb')}
            
            listsdico["file"+str(count)]= open(item,'rb')
            count+=1

        res = requests.post(url,files=listsdico,data=datafolder)    
        
       
        
        print(res)
   
    

def listofFiles(directory,formatfiles):
    lists=[]
    for item in formatfiles:
        for root, dirs,files in os.walk(directory):
            print()
            for file in files:
                if file.endswith(item):
                    pathsource = os.path.join(root,file)
                    lists.append(pathsource)
    return lists
        

def createfolder(folders):
    
    for i in folders:
        stext =re.split(r'[\\]',i)
        print(stext)
        
        jsonfile = {"foldername":stext[-1].strip()}
        name =json.dumps(jsonfile)
        posted = requests.post('http://192.168.1.51:5000/create',json=name).json()
        print(posted["escalate"])


#while(True):
while(True):
    createfolder(folder)
    sendfiles(folder)
    time.sleep(60)

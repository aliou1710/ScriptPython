from socket import *
import http.server
import socketserver
import os;
import re;

from flask import Flask,request,Response,jsonify,json,send_file,send_from_directory,abort,render_template 
from werkzeug.utils import secure_filename


app = Flask(__name__)
currentdirectory =r"D:\\Cours_bloc_MA2\Langage script python\administration"
#recupere les fichiers 
@app.route("/sendfiles",methods=["GET","POST"])
def dowloadfiles():
    
    print("=============================================", flush=True)
    #on recupere le nom du dossier
    foldername = request.form.get("foldername")
    #on  recupere le nombre de fichiers à recevoir
    filenumber = request.form.get("filenumber")
    print("foldername: ",foldername, flush=True)
   
    #boucle pour permettre de recuperer le nombre de fichiers.
    for i in range(0,int(filenumber)):
        #on recupere le fichier dans le dico envoyé
        files = request.files.get("file"+str(i))
        #on stocke le fichier dans un dossier
        files.save(currentdirectory+"\\"+foldername+"\\"+files.filename.strip())
    
    print(request.headers,flush=True)
    print("=============================================", flush=True)
 
    print("foldername: ",foldername, flush=True)
    
    result = {'escalate': True}
    return json.dumps(result)
    

@app.route("/upload",methods=["POST"])
def uploadfile():
        if 'files[]' not in request.files:
            resp =jsonify({'message ':'No file part in the request'})
            resp.status_code=400
            return resp



@app.route('/determine', methods = ['POST'])
def determine_escalation():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    print(data)
    #stuff happens here that involves data to obtain a result
    result = {'escalate': True}
    return json.dumps(result)


#
@app.route('/create', methods = ['POST'])
def receiveFolderName():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
    print(data["foldername"])
    path = createFolder(data["foldername"])

    result = {'escalate': True}
    return json.dumps(result)


@app.route('/receiveFile', methods = ['POST'])
def receiveFileName():
    jsondata = request.get_json()
    data = json.loads(jsondata)
    
 
    createFilesfromclient(data["valuefile"])


    result = {'escalate': True}
    return json.dumps(result)



@app.route("/getOneFile",methods=["GET"])
def getOnefiles():
    files = open("index.html",'rb')
    return Response(files)
        


#method
def sendfolderZipped(foldername):
    path= os.path.join(os.getcwd(),foldername)
    return Response(path+".zip",'rb',mimetype='application/zip')

def createFolder(folderDirectoryname):
    
    print("************creation folder ************")  

    path = currentdirectory+"\\"+folderDirectoryname
    print("path : ",path)
    if (os.path.isdir(path)):
            print("exist déjà")        
    else:
          print("dossier à créer: ",path)
          os.mkdir(path)
    return path


#delete le backslash 
def deleteBackslashN(lists):
    modifiedList=[]
    for item in lists:
      #eviter la duplication
      if item not in modifiedList:
        if item[-1] == '\n':
            modifiedList.append(item[:-1])
        else:
            modifiedList.append(item)
    return modifiedList


def createFilesfromclient(createfile):

    currentdirectory =r"D:\\Cours_bloc_MA2\Langage script python\administration"
    path = currentdirectory+"\\"+createfile
    print("path : ",path)
       

    if os.path.exists(path):
        with open(createfile,'w',errors='ignore') as file_handler:
            
            content= file_handler.readlines()
            print(content)
            file_handler.write(content)
    else:
        td= open(createfile,'wb',errors='ignore') 
        td.write(content) 
        td.close() 




if __name__ =="__main__":
    app.run("192.168.1.51",debug=True)
    #app.run(host="192.168.1.51,por=8000,debug=True")



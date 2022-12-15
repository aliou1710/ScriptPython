import os;
import os.path;
import glob;
import shutil; 

formatsfiles= ("bmp","xlsx","docx","txt","png","jpg","pptx")
directory_src_one = r"D:\\Cours_bloc_MA2\test_Langage_Script\source"
directory_src_two = r"D:\\Cours_bloc_MA2\test_Langage_Script\sourcetwo"
destination_folder = r"D:\\Cours_bloc_MA2\test_Langage_Script\destination"
listOfFolder = (directory_src_one,directory_src_two)



def createFolder(listof_folder,destination):
    print("************creation folder ************")  
    for x in listof_folder:
        path = os.path.join(destination,x)
        if (os.path.isdir(path)):
            print("exist déjà")
            continue
            
        else:
          
          print(path)
          os.mkdir(path)




def conception(listOfFolders,formatsfiles_,destination):
 print("************move files ************")  
 for  item in listOfFolders:
    print()
    for  formats in formatsfiles_:
        for root, dirs, files in os.walk(item): 
            for file in files: 
                if file.endswith(formats):
                    print()
                    pathsource = os.path.join(root,file)
                    print("pathsource = "+pathsource)
                    pathdestination = os.path.join(destination,formats)
                    print("pathdestination = "+pathdestination)
                    pathfiles = os.path.join(pathdestination,file)
                    print("pathfiles = "+pathfiles)
                    try:
                        if os.path.exists(pathdestination) and os.path.exists(pathfiles) :
                            print("file existe deja")
                            continue
                        else:
                            shutil.move(pathsource,pathdestination)
                    except FileNotFoundError:
                        print("error")

createFolder(formatsfiles,destination_folder)
conception(listOfFolder,formatsfiles,destination_folder)
       

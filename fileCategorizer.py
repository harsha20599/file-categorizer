#This file is created by harsha20599 on 26th may 2018
from os import listdir
import os
from os.path import isfile, join

#mapping the files to specific folders based on the extensions (abc.txt - where txt is a extension)
fileDict = {
    'img' : 'images',
    'jpg' : 'images',
    'png' : 'images',
    'webp' : 'images',
    'gif' : 'images',
    'mp3' : 'music',
    'wav' : 'music',
    'm4a' : 'music',
    'doc' : 'documents',
    'txt' : 'documents',
    'csv' : 'documents',
    'docx' : 'documents',
    'xlsx' : 'documents',
    'pdf' : 'documents',
    'db': 'datbases',
    'py' : 'python files',
    'ttf' : 'fonts',
    'zip' : 'compressed',
    '7z' : 'compressed',
    'rar' : 'compressed',
    'exe' : 'setups',
    'msi' : 'setups',
    'mp4' : 'videos',
    'ai'  : 'illustrator',
    'psd' : 'photoshop',
    'pptm' : 'presentations',
    'pptx' : 'presentations',
    'htm' : 'html',
    'xd' : 'Prototypes',
    'pkg' : 'packages',
    'img' : 'ISO',
    'iso' : 'ISO',
    'isz' : 'ISO',
    'torrent' : 'torrent files'
}

#getting the working path where the file is going to excecute
mypath = os.getcwd()

#Taking all the files in the mypath into a list
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("************************************************************************\n")
print("                          Welcome to Auto File Categorizer                    ")
print("                            created by harsha20599 ")
print("\n\n You have ",len(onlyfiles)-1," files to categorize")
print("\n")

#promting the user to continue
choice = input("Press Y to continue, N to abort :")

print("Initializing the process, please wait")

if(choice == "Y" or choice == "y" ):
    #iterating over the each file in the list
    for i in onlyfiles:
        #getting the extension for the file
        filename, file_extension = os.path.splitext(i)
        #removing the . from the extension
        file_extension = file_extension[1:]
        #checking whether the key error occurs
        try:
            #searching the dictionary to take the corresponding folder name
            dictName = fileDict[file_extension]
            file_extension =  dictName
        #if there was an error, raise an exception
        except KeyError:
            pass
        #checking whether the folder is already exists or not
        if not os.path.exists(file_extension):
            try:
                #if the folder doesn't exist, create the folder
                os.makedirs(file_extension)
                print("Created ",file_extension," folder ..")
            except FileNotFoundError:
                #handling filenotfound exception
                print("Urgghhh !! That was a bitter taste by a file. Anyways, skipping it.")
                pass
        try:
            #moving the file to it's dedicated extension folder
            os.rename(i,file_extension+"/"+i)
        except PermissionError:
            #if the permissions is not sufficient to move, handle the error
            print("Johncena is blocking me to go. Permission issues, skipping although")
            pass
        except FileExistsError:
            #if the file is already exists in the folder, prepending the file with (1)
            os.rename(i,file_extension+"/(1)"+i)
                    
else:
    print("Hoping to see you again. Good bye !")  
    
print("Thanks for using the service\n Created by harsha20599")

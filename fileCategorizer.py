from os import listdir
import os
from os.path import isfile, join
fileDict = {
    'img' : 'images',
    'jpg' : 'images',
    'mp3' : 'music',
    'wav' : 'music',
    'm4a' : 'music',
    'doc' : 'documents',
    'txt' : 'documents',
    'csv' : 'documents',
    'xlsx' : 'documents',
    'pdf' : 'documents',
    'db': 'datbases',
    'py' : 'pythonFiles',
    'ttf' : 'fonts',
    'zip' : 'zips',
    '7z' : 'zips',
    'rar' : 'zips',
    'exe' : 'setups',
    'msi' : 'setups',
    'mp4' : 'videos',
    'ai'  : 'illustrator',
    'psd' : 'photoshop',
    'pptm' : 'presentations',
    'pptx' : 'presentations',
    'htm' : 'html'
}
cwd = os.getcwd()
mypath = cwd
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("************************************************************************\n")
print("                          Welcome to Auto File Categorizer                    ")
print("                            created by harsha20599 ")
print("\n\n You have ",len(onlyfiles)-1," files to categorize")
print("\n")

choice = input("Press Y to continue, N to abort :")

print("Initializing the process, please wait")

if(choice == "Y" or choice == "y" ):
    for i in onlyfiles:
        filename, file_extension = os.path.splitext(i)
        file_extension = file_extension[1:]
        try:
            dictName = fileDict[file_extension]
            file_extension =  dictName
        except KeyError:
            pass

        if not os.path.exists(file_extension):
            try:
                os.makedirs(file_extension)
                print("Created ",file_extension," folder ..")
            except FileNotFoundError:
                print("Urgghhh !! That was a bitter taste by a file. Anyways, skipping it.")
                pass
        try:
            os.rename(i,file_extension+"/"+i)
        except PermissionError:
            print("Johncena is blocking me to go. Permission issues, skipping although")
            pass
        except FileExistsError:
            os.rename(i,file_extension+"/(1)"+i)
                    
else:
    print("Hoping to see you again. Good bye !")  
    
print("Thanks for using the service\n Created by harsha20599")

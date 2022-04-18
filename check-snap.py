import requests
from colorama import *
print(Fore.BLUE+" [£] All Copy rights reserved© to @hxn_here << insta")
import os
try:
    import requests
    import socket as s
    import webbrowser
    from sys import platform
    import colorama

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install socket")
    os.system("pip install webbrowser")
    os.system("pip install sys")
    os.system("pip install platform")
    os.system("pip install colorama")
import webbrowser
url = "https://t.me/HEXiN1K"
webbrowser.open(url)
from sys import platform
from colorama import *
import socket
import requests

name = socket.gethostname()
myHostName = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n===========================================================")
name = ("""\n                    Hello sir """ +name+Style.RESET_ALL)
print(name)
host = ("""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)

api = "https://api.ipify.org/?format=json"
req = requests.get(api)
response = req.json()
a = response["ip"]

IP = ("""\n                Your Local iP is """+Fore.RED+a+Style.RESET_ALL)
print(IP)

v = (Fore.RED+"""\n                    Your iNFO PROXY is\n"""+Style.RESET_ALL)

print(v)
print(s)

print("\n===========================================================")

lib = input("""
\n  من صنع هيكسن انستجرام @hxn_here
\n  BY HEXiN INSTA @hxn_here
\n  tarafından yapılmış HEXiN Instagram @hxn_here
\n
===========================================================
\n   من صنع هيكسن تيليجرام @HEXiN 
\n  BY HEXiN TELeGRaM @HEXiN1K
\n  Bir telgraf HEXiN oluşturun @HEXiN1K
\n ===========================================================
 
 [1] DOWNLOAD LiP & UPDATE . تنزيل وتحديث المكاتب

\n [2] SKiP DOWNLOAD & UPDATE LiP . تخطي تنزيل وتحديث المكاتب 

\n [+] Please Choice >> """)

if lib == "1":
    try:
        os.system('pip install requests')
        os.system('pip install webbrowser')
        os.system('pip install socket')
        os.system('pip install sys')  
        os.system('pip install colorama')
        os.system('pip install time')
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except:
        pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
import requests
import colorama
import webbrowser
import socket
import time as mm
import sys as n
from colorama import *
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 75)
slow(Fore.RED+"""
 ...........................................................  

  Coded BY HEXiN inStAGrAm : @hxn_here
  
  TeLEGram programmer : @HEXiN1K 
  
  By @hxn_here ~ @7lm.py << instagram

...........................................................
                                                 """)
print("\n [~] Taken = مسحوب")
print("\n [~] Valid = متاح")
print("[+] احياناً يحدث خطأ يكون اليوزر غير متاح ويظهر انه متاح لان اليوزر مبند او محذوف")
user = input (Fore.CYAN+"\n [+] Enter Username to Check =>> : ")
api = "https://vodka-apis.herokuapp.com/SnapChat/Check/?user={user}"
req = requests.get(api)
response = req.json()

a = response["data"]
b = response ["loaded"]
print (a)
print (b)

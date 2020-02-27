import os
hostname="www.itmorelia.edu.mx"
respuesta=os.system("ping -c 1 "+hostname)
if respuesta==0:
    print(hostname+": está en funcionamiento! :D")
else:
    print(hostname+": no funciona! :(")  
red="200.33.171.0"
os.system("nmap -sP "+red)      

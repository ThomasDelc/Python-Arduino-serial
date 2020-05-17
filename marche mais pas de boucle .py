"""Importations des modules"""
import serial

"""Ouverture de la liaison série"""
try:
    arduino = serial.Serial("/dev/cu.usbmodem146101",timeout=1)
except:
    print('Please check the port')

"""Initialisation des variables"""
rawdata=[]
count=0

"""Réception et stockage des données"""
while count<4:
    rawdata.append(str(arduino.readline())) #données brutes
    count+=1
print(rawdata)



def clean(L):#L est une liste
    newl=[]#initialisation de la nouvelle liste
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl

cleandata=clean(rawdata)
print(cleandata)

def write(L):
    file=open("data.txt",mode='w')
    for i in range(len(L)):
        file.write(L[i]+'\n')
    file.close()

write(cleandata)
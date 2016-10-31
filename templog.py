'''
Created on Oct 30, 2016
@author: Timo 'sginne' Junolainen

'''
fileName='temperature.log'
hostName='ant-s9.home.gateway'
userName='root'
userPassword='root'

import datetime,time,sys
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPDigestAuth 



def currentTemperatures():
    soup=BeautifulSoup((requests.get("http://"+hostName+"/cgi-bin/minerStatus.cgi", auth=HTTPDigestAuth(userName,userPassword))).text,'html.parser')
    tchip=soup.findAll("div", {"id": "cbi-table-1-temp2"})
    out=[]
    for i in tchip:
        out.append(i.next)
        
    return ' '.join(out)

def log(inputString):
    with open(fileName,'a') as textFile:
        textFile.write(timeStamp()+' '+inputString+'\n')
def timeStamp():
    return('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now()))

lastHour=time.strftime("%H")
while True:
    print ('.',end="")
    currentHour=time.strftime("%H")
    sys.stdout.flush()
    time.sleep(6)
    if currentHour!=lastHour:
        lastHour=currentHour
        print('')
        print (lastHour)
        log(currentTemperatures())
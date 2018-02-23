import serial
import os, time
from decimal import *
import datetime
delay = 1
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
port.flush()
cd=1
def  get_gps():
    result = []
    ck=0
    result.append(str(datetime.datetime.now())[11:22].replace(":","").replace(".",""))
    #port = serial.Serial("/dev/ttyUSB0")
    #port.flush()	
    fd=''
    while ck <= 50:
        rcv = port.read(10)
 
        fd=fd+rcv
        ck=ck+1
    
    # print fd
    if '$GPRMC' in fd:
        ps=fd.find('$GPRMC')
        dif=len(fd)-ps
        #print dif
        if dif > 70:
            data=fd[ps:(ps+65)]
            #print data
            p=list(find(data, ","))
            lat=data[(p[2]+1):p[3]]
            lon=data[(p[4]+1):p[5]]
            time_gps=data[(p[0]+1):p[1]]
            #print time_gps
            date_gps=data[(p[8]+1):p[9]]
            #print date_gps
            s1=lat[2:len(lat)]
            s2=lon[3:len(lon)]
            try:
	            s1=Decimal(s1)
	            s2=Decimal(s2)
            except:
            	#print "No data received"
            	result = result + [0,0,0,0] 
            	return result
            s1=s1/60
            s11=int(lat[0:2])
            s1=s11+s1
            s2=s2/60
            s22=int(lon[0:3])
            s2=s22+s2
	    	
            #print s1
            #print s2
            result.append(time_gps)
            result.append(date_gps)
            result.append(str(s1))
            result.append(str(s2))
            return result   
 		
        else:
            #print "No sufficient data"
            result = result + [0,0,0,0] 
            return result
           
          	
    #cd=cd+1
    #os.system("python accel.py")	
    #print cd
    #port.close()
#get_gps()



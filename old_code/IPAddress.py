#!/usr/local/bin/python
"""
Author   : Sharad Talekar
Filename : IPAddress.py
Date     : 16-07-2016 : 16:21
Purpose  : To classify and check the validity of IP Address.
"""

stopper = 1
while stopper==1:
    IpAddr = raw_input('Enter the IP address: ')
    try:
        [oct1, oct2, oct3, oct4] = IpAddr.split('.')
        ip = int(oct1)
        print ip
        if (ip > 0 )and (ip < 127):
            print 'Class A'
        elif (ip >=128) and (ip < 192):
            print 'Class B'
        elif ip >= 192 and ip <224:
            print 'Class C'
        elif ip >= 224 and ip < 240:
            print 'Class D'
        elif ip >= 240 and ip <255:
            print 'Class E'
        stopper = input('Press 0 to stop, 1 to continue')
    except:
        print 'Invalid IP'


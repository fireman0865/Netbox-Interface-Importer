import requests as re
import napalm
import json
import time as t
import hostlist
import ip
from hostlist import hostliste
from ip import ips
from drivers import driver_list

for i,d,h in zip(ips,driver_list,hostliste):
    
    username=input("Enter username")
    pass=input("Enter Password")
    tokene=input("Enter your token")
    headers={'Authorization': ('Token %s' % tokene) ,'Content-type': 'application/json'}

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver(d)
    hostname=h
    # Connect:
    device = driver(
        hostname=i,
        username=username,
        
        password=pass,
    )

    print("Opening ...")
    device.open()
    
    interfaces=json.dumps(device.get_interfaces())
    print(interfaces)




    interfaces=json.loads(interfaces)


    keep = []
    for key,p in interfaces.items():
        p['device']=h
        p['name']=key
        p['type']='1000base-x-gbic'
        keep.append(p)

    data=json.dumps(keep)

    print(data)
    for x in keep:
        y=json.dumps(x)
        r=re.post("http://localhost:8000/api/dcim/interfaces/",data=y,headers=headers)
        print(r.status_code)
        t.sleep(4)
    device.close

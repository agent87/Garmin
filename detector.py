import pyudev
import psutil
import time
#from source.sync import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')




def port_scan():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                return device.device_node
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                print("Watch Removed!")    #remove this after debug
                


def async_scan():
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
            return device.device_node
        else:
            break
       

def mount_point(device_node):
    print(psutil.disk_partitions())
    for partitions in psutil.disk_partitions():
        if partitions.device == device_node:
            return partitions.mountpoint


#mount_point(async_scan())
if async_scan() == None:
    time.sleep(1)
    print(mount_point(port_scan()))
else:
    print(mount_point(async_scan()))
    

import pyudev
import psutil
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def async_scan():   #asynchronous port scan
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
            return device.device_node
        else:
            break

def sync_scan():   #synchronous port scan
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                print("SHOW")
                return async_scan()
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                print("Watch Removed!")    #remove this after debug
                break
                
def mount_point(device_node):
    for partitions in psutil.disk_partitions():
        if partitions.device == device_node:
            partitions.refreshDiskInfo()
            return partitions.mountpoint




if async_scan() == None:
    print(mount_point(sync_scan()))
else:
    print(mount_point(async_scan()))
    

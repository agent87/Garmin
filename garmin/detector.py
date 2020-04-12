import pyudev
from pyudev import Context, Monitor, MonitorObserver
import psutil
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def mount_point(device_node):
    for partitions in psutil.disk_partitions():
        if partitions.device == device_node:
            return partitions.mountpoint

def async_scan():   #asynchronous port scan
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
            return mount_point(device.device_node)
        else:
            break

def sync_scan():   #synchronous port scan
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                print(mount_point(device.device_node))
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL']:
                print("Watch Removed!")    #remove this after debug


def print_device_event(device):
    print('background event {0.action}: {0.device_path}'.format(device)) 



context = Context()
monitor = Monitor.from_netlink(context)
monitor.start()
monitor.filter_by(subsystem='block')
for action, device in monitor:
    print('{0}: {1}'.format(action, device.device_node))
    print(mount_point(device.device_node))


#if async_scan() == None:
#holla = mount_point(sync_scan())
#print(holla)
#else:
#    print(mount_point(async_scan()))
    

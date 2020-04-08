import pyudev
import psutil
#from source.sync import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')




def port_scan():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        print(device.device_node)
        if device.action == "add":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL'] :
                for p in psutil.disk_partitions():
                    print(' ')#p.device)# in device['DEVNAME']:
                    #    print("  {}: {}".format(p.device, p.mountpoint))
                print("Watch detected")
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == config['credential']['ID_FS_LABEL'] :
                print("Watch Removed!")
                break


def async_scan():
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        if device.device_node in psutil.disk_partitions():
            print("YES")


async_scan()



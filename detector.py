import pyudev 
from source.sync import *

watch_name = "GARMIN"
context = pyudev.Context()
forra = context.list_devices()
def port_scan(watch_name):
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch detected")
                return True
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch Removed!")
                break


def local_sync():
    print("this is the local sync")

def cloud_sync():
    print("This is the cloud sync")


if port_scan(watch_name) == True:
    sync.cloud_(watch_name)




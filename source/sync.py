import pyudev 

watch_name = "GARMIN"
context = pyudev.Context()


def port_scan(watch_name):
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('block')
    for device in iter(monitor.poll, None):
        if device.action == "add":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch detected")
        elif device.action == "remove":
            if device.get('ID_FS_LABEL') == watch_name :
                print("Watch Removed!")

port_scan(watch_name)

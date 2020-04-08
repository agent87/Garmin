from dirsync import sync



class synchronise():
    def local_(garmin, back_folder_name): #Include Garmin watch mount point, back-up folder location
        print("this is the local sync function")
        sync(garmin, back_folder_name, 'sync', purge = True, create=True)

    def cloud_(self):
        print("This is the cloud sync function")
    
    def rasp_(self):
        print("This is the raspberyy sync function")



synchronise.local_("/media/sangman/GARMIN","")

"""
A class that creates objects to represent each root Drive that holds your
video files, focusing on TV shows & episodes specifically. ShowDrive objects should be
manually created to ensure correct file paths are used. Make sure your
ShowDrive & MovieDrive objects for a specific drive are created
in the same order, as they are appended to a list that is referenced elsewhere.
"""


from PlexShowClass import*

class ShowDrive:

    dirlist = []
    drives = []


    def __init__(self, name, root_path):
        self.name = name
        self.root_path = r'{}'.format(root_path)
        self.number_of_files = self.get_number_of_files()
        self.number_of_shows = self.get_show_count()
        self.drive_list = self.get_names()
        ShowDrive.drives.append(self)


    #Goes through the drive's root path to retrieve the names of each subfolder,
    #these are then appended as strings to ShowDrive object's "drive_list" attribute.
    #drive_lists are then referenced to name TV show (PlexShow) objects.
    def get_names(self):
        path = r'{}'.format(self.root_path)
        dirlist=[]
        for item in os.listdir(path):
            dirlist.append(item)
        return dirlist


    #Retrieves the number of TV show episodes on drive.
    def get_number_of_files(self):
        path = self.root_path
        file_count = 0
        for root, dirs, files in os.walk(path, topdown=True):
            for item in files:
                if not item.startswith("desktop.ini"):
                    file_count+=1
        return file_count
    

    #Counts the subfolders of root path to determine total number of TV shows on drive.
    def get_show_count(self):
        show_count = len(next(os.walk(self.root_path))[1])
        return show_count
    

    def __str__(self):
        return ("Name: " + self.name + "\n" +
                "Number of TV Shows on drive: " + str(self.number_of_shows) + "\n" +
                "Number of episodes on drive: " + str(self.number_of_files) + "\n")


"""
NOTE!!

Create your Show Drive & Movie Drive objects for a drive in the same order--
so the write.file methods point to the correct information!

For example, if you create a ShowDrive object for Drive C: first, then
make sure your first MovieDrive object is for Drive C: as well.

"""

Drive_F_Shows = ShowDrive("F:",r"F:\Plex\TV Shows")
Drive_H_Shows = ShowDrive("H:",r"H:\Plex\TV Shows")


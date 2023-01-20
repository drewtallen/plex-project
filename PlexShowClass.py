"""
Plex Project
Drew Allen
10/31/2021
"""

"""
This is a class to represent individual TV shows. It includes several attributes
to be displayed in the text file when main() is executed. Several class methods
are called in initialization to retrieve these attributes. There is also a method
that allows you to backup the entire folder for a TV show, including all folders
and files within it, to a new destination.
"""


import os, sys
import shutil
import cv2
import textwrap
from ShowDriveClass import*
import datetime
now = datetime.datetime.now()


class PlexShow:


    #Keeps track of total # of shows & episodes and how many are standard & high def.
    total_shows = 0
    episode_count = 0
    show_list = []
    SD_count = 0
    HD_count = 0

    
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = r'{}'.format(file_path)
        self.root_drive = self.get_drive()
        self.number_of_files = self.get_number_of_files()
        self.show_size = self.get_folder_size()
        self.number_of_seasons = self.get_number_of_seasons()
        self.video_dimensions = ""
        self.video_definition = self.get_definition()
        PlexShow.total_shows+=1
        PlexShow.episode_count+=self.number_of_files
        
    
    #Retrieves the size of an entire individual TV show in GBs.
    def get_folder_size(self):
        path = self.file_path
        totalSize = 0
        for root, dirs, files in os.walk(path, topdown=True):
            for item in files:
                if not item.startswith("desktop.ini"):
                    filePath=os.path.join(root,item)
                    totalSize+=os.path.getsize(filePath)
        gig_size = (totalSize/1073741824)
        new_size = (format(gig_size,'.2f'))
        return new_size
    
    
    #Retrieves root drive of a show's files.
    def get_drive(self):
        path = self.file_path
        drive = os.path.splitdrive(path)
        return drive[0]
    
    
    #Retrieves the total number of files of a show through all subfolders.
    def get_number_of_files(self):
        path = self.file_path
        file_count = 0
        for root, dirs, files in os.walk(path, topdown=True):
            for item in files:
                if not item.startswith("desktop.ini"):
                    file_count+=1
        return file_count
    

    #Retrieves the number of seasons of a show by tallying subfolders of the show's main folder.
    def get_number_of_seasons(self):
        path = self.file_path
        season_count = 0
        for root, dirs, files in os.walk(path, topdown=True):
            for item in dirs:
                if not item.startswith("desktop.ini"):
                    season_count += 1
        return season_count
        

    #Once main is called and objects are created for all shows, this method allows you to-
    #backup an entire TV show to a new destination.
    #Call this method on the show's index using PlexShow.show_list[index].backup_folders()
    #A backup folder will be created in the destination. Change destination below as needed.
    def backup_folders(self):
        source = self.file_path
        destination = r"C:\Users\drews\Documents\\" + self.name + "_backup" ## change to allow destination folder to update to showname
        print("Copying files from " + source + " \nto " + destination + ".")
        print("This may take several minutes...")
        files = os.listdir(source)
        shutil.copytree(src=source,dst=destination)
        print("Copying complete!")


    #Retrieves the width & height of pixel measurements of video files.
    def get_dimensions(self):
        try:
            source = self.file_path
            folder_list = []
            file_list = []
            for root, dirs, files in os.walk(source, topdown=True):
                for folder in dirs:
                    folder_list.append(folder)
                for item in files:
                    file_list.append(item)
            test_path = os.path.join(source,folder_list[0],file_list[0])
            vid = cv2.VideoCapture(test_path)
            height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            if height == 0:
                print()
                print(textwrap.dedent("""\
                         ERROR:\n
                         Unable to retrieve dimensions from video file for """ + self.name + "."))
                print(textwrap.dedent("""\
                         Please make sure that files are correctly placed within season folders and that the
                         first folder in the show directory is not empty."""))
                sys.exit(1)
        except IndexError:
            print()
            print(self.name + " contains files outside of Season folders!!")
            sys.exit(1)
        return width,height


    #Calls the get_dimensions() method above and uses the measurements to determine video resolution.
    #Standard def has a width around 480 and high def has a width around 720 or higher.
    def get_definition(self):
        self.width,self.height = self.get_dimensions()
        self.video_dimensions = str(int(self.width))+ " x " + str(int(self.height))
        if (self.height > 0) & (self.height <= 500):
            PlexShow.SD_count+=1
            return "SD"
        elif (self.height > 500):
            PlexShow.HD_count+=1
            return "HD"
        

    #String method to display useful information. Also used when writing info to file in main().
    def __str__(self):
        return  ("Name: " + self.name + "\n" +
                "Root drive: " + str(self.root_drive) + "\n" +
                "Path of Plex files: " + self.file_path + "\n" +
                "Numer of seasons: " + str(self.number_of_seasons) + "\n" +
                "Number of files: " + str(self.number_of_files) + "\n" +
                "Dimensions of video file: " + self.video_dimensions + "\n" +
                "Resolution of video file: " + self.video_definition + "\n" +
                "Folder size of show: " + str(self.show_size) + " gigabytes\n")


    #Creates objects for each TV show by iterating through the show names retrieved for each drive
    #in the "ShowDriveClass". Uses the root paths and indices of drive_lists of the ShowDrive objects
    #as arguments for the PlexShow constructor. This way the PlexShow (TV show) objects maintain
    #their file paths and names. Each object is then appended to PlexShow.show_list.
    @staticmethod
    def create_shows():
        for drive in ShowDrive.drives:
            for i in range(len(drive.drive_list)):
                print("Creating object for: " + str(drive.drive_list[i]))
                file_path = os.path.join(drive.root_path,drive.drive_list[i])
                temp_string=drive.drive_list[i]
                temp_string.replace(" ","")
                temp_string = PlexShow(drive.drive_list[i],file_path)
                PlexShow.show_list.append(temp_string)


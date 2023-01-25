"""
A class that creates objects to represent each root Drive that holds your
video files, focusing on movies specifically. This class inherits from ShowDrive,
but most attributes & methods were overwritten. MovieDrive objects should be
manually created to ensure correct file paths are used. Make sure your
ShowDrive & MovieDrive objects for a specific drive are created
in the same order, as they are appended to a list that is referenced elsewhere.
"""


from PlexShowClass import*
from ShowDriveClass import*

class MovieDrive(ShowDrive):

    dirlist = []
    drives = []
    movie_count = 0
    

    def __init__(self, name, root_path):
        self.name = name
        self.root_path = root_path
        self.drive_list = self.get_names()
        self.number_of_files = self.get_number_of_files()
        MovieDrive.movie_count+=1
        MovieDrive.drives.append(self)
        

    #Retrieves the number of movies on drive.
    def get_number_of_files(self):
        count = 0
        for item in self.drive_list:
            count+=1
        return count
        

    #Goes through drive's movie file folder and retrieves the names of files.
    #These names are then appended to MovieDrive object's "drive_list" attribute.
    #MovieDrive "drive_lists" are then referenced in PlexMovie object creation.
    def get_names(self):
        movie_list = []
        path = self.root_path
        for root, dirs, files in os.walk(self.root_path):
            for movie in files:
                movie_list.append(movie)
        return movie_list
  

    def __str__(self):
        return ("Drive: " + self.name + "\n" +
                "Path of plex files: " + self.root_path + "\n" +
                "Number of movies on drive: " + str(self.number_of_files))


"""
NOTE!!

Create your Show Drive & Movie Drive objects for a drive in the same order--
so the write.file methods point to the correct information!

For example, if you create a MovieDrive object for Drive C: first, then
make sure your first ShowDrive object is for Drive C: as well.

"""


Drive_F_Movies = MovieDrive("F:",r"H:\Plex\Movies")
Drive_H_Movies = MovieDrive("H:",r"F:\Plex\Movies")

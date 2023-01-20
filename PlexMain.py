#Drew Allen
#Final Project

"""
This program calls the appropriate methods to create PlexShow & PlexMovie objects
for all TV shows and movies. These objects are then sorted alphabetically and
written to text files using appropriate __str__ methods. The purpose of this program
is to create detailed text files containing useful information for all shows & movies
currently in use by a user's Plex media server.
"""

from PlexShowClass import*
from ShowDriveClass import*
from MovieDriveClass import*
from PlexMovieClass import*

def main():

    i=0
    h=0
    j=0
    
    PlexShow.create_shows()
    PlexMovie.create_movies()

    PlexShow.show_list.sort(key=lambda x: x.name)
    PlexMovie.movie_list.sort(key=lambda x: x.name)


    #The first text file created is called "Plex Status" and it includes every TV show and movie,
    #along with their respective information using __str__ methods. An up-to-date timestamp
    #is included at the top of the file.
    with open("Plex Status.txt", 'w') as file1:
        file1.write("Plex Status as of: " + str(now) + "\n\n\n\n")
        file1.write("Total number of TV shows: " + str(PlexShow.total_shows) + "\n")
        file1.write("Number of standard definition TV shows: " + str(PlexShow.SD_count) + "\n")
        file1.write("Number of high definition TV shows: " + str(PlexShow.HD_count) + "\n")
        file1.write("Total number of episodes: " + str(PlexShow.episode_count) + "\n\n")
        file1.write("Total number of movies: " + str(len(PlexMovie.movie_list)) + "\n")
        file1.write("Number of standard definition movies: " + str(PlexMovie.SD_count) + "\n")
        file1.write("Number of high definition movies: " + str(PlexMovie.HD_count) + "\n\n\n\n")
        file1.write("Current drives with plex files:\n\n")
        for item in ShowDrive.drives:
            file1.write(str(item))
            file1.write("Number of movies on drive: " + str(MovieDrive.drives[i].number_of_files) + "\n\n")
            i+=1
        file1.write("\n\nTV Shows:\n\n")
        for item in PlexShow.show_list:
            file1.write(str(item))
            file1.write("PlexShow.show_list index # = " + str(h) + "\n\n")
            h+=1
        file1.write("\n\n\n\n")
        file1.write("Movies:\n\n")
        for item in PlexMovie.movie_list:
            file1.write(str(item))
            file1.write("PlexMovie.movie_list index # = " + str(j) + "\n\n")
            j+=1
        file1.close()
        
        
    #This second file contains lists of just the names of the TV shows & movies on a
    #particular drive. This is useful if you are using multiple drives and want a quick
    #reference for what a drive contains. The code below does not iterate through anything,
    #so it must be manually edited to reference the appropriate drives.
    with open("Drive F Contents.txt", 'w') as file2:
        file2.write("TV shows on Drive F: \n\n")
        for item in Drive_F_Shows.drive_list:
            file2.write(item + "\n")
        file2.write("\n\n\n\nMovies on Drive F: \n\n")
        for item in Drive_F_Movies.drive_list:
            file2.write(item + "\n")
        file2.close()


      
    with open("Drive H Contents.txt", 'w') as file3:
        file3.write("TV shows on Drive H: \n\n")
        for item in Drive_H_Shows.drive_list:
            file3.write(item + "\n")
        file3.write("\n\n\n\nMovies on Drive H: \n\n")
        for item in Drive_H_Movies.drive_list:
            file3.write(item + "\n")
        file3.close()

main()





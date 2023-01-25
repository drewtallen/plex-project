"""
This class works for individual movie objects and inherits from PlexShow.
Most methods and attributes were overwritten as it became apparent that
unique code was required. Very similar information is retrieved in this class
to that retrieved for the TV shows in PlexShow.
"""


from PlexShowClass import*
from MovieDriveClass import*


class PlexMovie(PlexShow):

    #Keeps track of total # of movies and how many are standard & high def.
    #movie_list holds all PlexMovie objects after creation.
    SD_count = 0
    HD_count = 0
    movie_list = []


    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        self.root_drive = self.get_drive()
        self.file_size = 0
        self.video_dimensions = ""
        self.video_definition = ""


    def __str__(self):
        return  ("Name: " + self.name + "\n" +
                 "Drive: " + self.root_drive + "\n" +
                 "Dimensions of video file: " + self.video_dimensions + "\n" +
                 "Resolution of video file: " + self.video_definition + "\n" +
                 "Size of movie file: " + str(float(self.file_size)) + " gigabytes\n")


    #Here, because only one folder is being iterated through for all movies,
    #a single staticmethod was created that creates the movie objects and retrieves
    #attribute information including file size, dimensions, and definition in one call.
    @staticmethod
    def create_movies():
        for item in MovieDrive.drives:
            i=0
            for i in range(len(item.drive_list)):
                if not item.drive_list[i].endswith('.srt'):
                    print("Creating object for: " + item.drive_list[i])
                    try:
                        source = item.root_path
                        test_path = os.path.join(source,item.drive_list[i])
                        temp_size = os.path.getsize(test_path)
                        file_size = (format(temp_size/1073741824,'.2f'))
                        vid = cv2.VideoCapture(test_path)
                        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
                        if height == 0:
                            print()
                            print(textwrap.dedent("""\
                                ERROR:\n
                                Unable to retrieve dimensions from video file for """ + item.drive_list[i] + "."))
                            print(textwrap.dedent("""\
                                Please make sure that the files being scanned are video files."""))
                            sys.exit(1)
                    except IndexError:
                        print()
                        print("Index Error")
                        sys.exit(1)
                    new_movie = PlexMovie(item.drive_list[i],item.root_path)
                    new_movie.file_size = file_size
                    new_movie.video_dimensions = str(width) + " x " + str(height)
                    if (height > 0) & (height <= 500):
                        PlexMovie.SD_count+=1
                        new_movie.video_definition = "SD"
                    elif (height > 500):
                        PlexMovie.HD_count+=1
                        new_movie.video_definition = "HD"
                    PlexMovie.movie_list.append(new_movie)
                    




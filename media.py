import webbrowser

#New class Movie which containes data regarding the movie.
#The class has an init function which recives 4 parameters and adds them to the instance of the movie class
#The class also contains a finction showtriler which plays the trailer in the webbrowser
class Movie():
    def __init__(self, movie_title, story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

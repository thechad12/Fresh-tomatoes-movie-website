import webbrowser

# Creates the class "Movie" that contains relevant information
# about a movie


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, actors):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actors = actors

# Creates the function show_trailer to open the trailer in the 
# webbrowser when clicked. 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

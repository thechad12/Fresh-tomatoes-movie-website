Fresh Tomatoes Version 3 9/21/2015 

-This is a website that contains 6 of my favorite movies.

-Media.py creates the class Media, which contains the functions 
"Movie", and "show_trailer." Show_trailer will open the youtube trailer in the webbrowser. The Movie function allows you to input a movie's title, storyline, url of the poster image, url of the youtube trailer, and main actors in the movie.

-entertainment_center.py contains instances of the class media, which are 6 of my favorite movies currently. To create another instance or edit one, the code would look like this:
		
			movie_title = media.Movie("move_title", "storyline", "Poster image url", "youtube trailer url", "actors")

-Once all of the movies have been created, create an array of the movies titled "movies." Below that, open the webbrowser by calling "fresh_tomatoes.open_movie_page(movies)." All the html and css editing is located in the file fresh_tomatoes.html, which is the file that will open the webpage. 

-To execute the program, make sure all the files are located in the same folder. You can execute the program by opening fresh_tomatoes.py in python and clicking "Run," or you can go to your command line and navigate to the folder, and run "python fresh_tomatoes.py" on a windows, or just "fresh_tomatoes.py" on a mac. 
import fresh_tomatoes
import media

# Creates new instances of the class Movie from the file media.py
toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys \
                        that come to life",
                        "http://cdn.gowatchit.com/posters/original/ToyStory-Poster.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "Tom Hanks, Tim Allen")

the_martian = media.Movie("The Martian",
                          "When astronauts blast off from Mars,\
                           they leave behind Mark Watney,\
                            presumed dead after a fierce storm.",
                          "http://cdn.traileraddict.com/content/20th-century-fox/martian2015.jpg",
                          "www.youtube.com/watch?v=Ue4PCI0NamI",
                          "Matt Damon")

apollo_13 = media.Movie("Apollo 13",
                        "Based on the events \
                         of the Apollo 13 lunar mission",
                        "https://s-media-cache-ak0.pinimg.com/736x/83/c2/05/83c205bec008fff44ff37cae9b11fa47.jpg",
                        "https://www.youtube.com/watch?v=nEl0NsYn1fU",
                        "Tom Hanks, Kevin Bacon, Bill Paxton, \
                        Gary Sinise")

cars = media.Movie("Cars",
                   "While traveling to California,\
                    Lightning McQueen becomes lost\
                     after falling out of his trailer",
                   "https://alualuna.files.wordpress.com/2011/12/cars.jpg",
                   "www.youtube.com/watch?v=WGByijP0Leo",
                   "Owen Wilson, Paul Newman")

caddyshack = media.Movie("Caddyshack",
                         "Danny Noonan works as a\
                          caddy at the snob-infested Bushwoord\
                           Country Club",
                         "http://www.chungkong.nl/wp-content/uploads/2013/12/No013-My-Caddyshack-minimal-movie-poster-720px.jpg",
                         "www.youtube.com/watch?v=zrTqenN1SqQ",
                         "Bill Murray, Chevy Chase, Rodney Dangerfield")

inside_out = media.Movie("Inside Out",
                         "Riley's world is turned upside-down when she\
                          and her parents move to San Francisco",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                         "www.youtube.com/watch?v=_MC3XuMvsD",
                         "Mandy Kaling, Lewis Black, Amy Schumer")

# Creates an array of the movies
movies = [toy_story, the_martian, apollo_13, cars, caddyshack, 
          inside_out]

# Opens the webbrowser 
fresh_tomatoes.open_movies_page(movies)

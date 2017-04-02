import fresh_tomatoes
import media

# Here is the instances for Movie Class
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyzH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                                 "Using Rock music to learn",
                                 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                                 "A rat is a chef in paris",
                                 "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                                 "https://www.youtube.com/watch?v=c3sBBRxDAqk")


kungfupanda = media.Movie("Kung Fu Panda",
                                 "The Furious Fight",
                                 "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                                 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")


hunger_games = media.Movie("Hunger Games",
                                 "A really real reality show",
                                 "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                                 "https://www.youtube.com/watch?v=4S9a5V9ODuY")


# Here is the list of moview to show on browser
movies = [toy_story, avatar, school_of_rock, ratatouille, kungfupanda, hunger_games]

# This function call uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)  



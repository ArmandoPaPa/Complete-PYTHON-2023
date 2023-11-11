movies = []


def add_a_movie():
    print("Please, add  a movie! Enter the following to add a movie:")
    title = input("Title:   ")
    director = input("Director:   ")
    year = input("Year:   ")
    movies.append({"title": title, "director": director, "year": year})
    print("Ty! Movie added!")


def print_movie(movie):
    print(f"Title: {movie['title']} | Director: {movie['director']} | Year: {movie['year']}")


def see_all_movies():
    for movie in movies:
        print_movie(movie)


def find_a_movie():
    movie_to_find = input("Enter movie title, you want to find:   ")
    for movie in movies:
        if movie_to_find.lower() == movie['title'].lower():
            print_movie(movie)


user_options = {
    "a": add_a_movie,
    "l": see_all_movies,
    "f": find_a_movie
}

def menu():
    selection = input("Hi! What would you like to do?"
                      "\nEnter"
                      "\n'a' - to add movie to"
                      "\n'l' - to see all movies"
                      "\n'f' - to find a movie"
                      "\n'q' - to quit"
                      "\n:   ").lower()
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()

        # if selection == "a":
        #     add_a_movie()
        # elif selection == "l":
        #     see_all_movies()
        # elif selection == "f":
        #     find_a_movie()

        else:
            print("Sorry, you entered something unexpected!")

        selection = input("Hi! What would you like to do?"
                          "\nEnter"
                          "\n'a' - to add movie to"
                          "\n'l' - to see all movies"
                          "\n'f' - to find a movie"
                          "\n'q' - to quit"
                          "\n:   ").lower()


menu()
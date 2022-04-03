def main():
    about_me = {
        "name": "Adelia",
        "student_id": 10259013,
        "pizza_toppings": [
            "Pepperoni",
            "Mushrooms",
            "Black Olives"
        ],
        "movies": [
            {"title": "American Psycho",
             "genre": "Thriller"
             },
            {"title": "Ferris Bueller's Day Off",
             "genre": "Comedy"
             }
        ]
    }


    #append new movie to end of list
    new_movie = {"title": "Monsters Inc.", "genre": "Animated"}
    about_me["movies"].append(new_movie)
    
    
    #add tuple of new pizza toppings
    new_toppings = ("Onions", "Cheese")
    add_pizza_toppings(about_me, new_toppings)

    #print information about me
    print_identity_info(about_me)

    #print ideal pizza toppings
    print_pizza_toppings(about_me)

    #print movies I like
    print_movie_genres(about_me)

    #print my favourite movies
    print_movie_titles(about_me)

def add_pizza_toppings(about_me, new_toppings):
    
    for p in new_toppings:
        about_me["pizza_toppings"].append(p)
        
        for t in new_toppings:
            about_me["pizza_toppings"].sort()
    
def print_identity_info(about_me):
    print("Hi Jeremy, my name is", about_me["name"] + ",", "and my student ID is", str(about_me["student_id"]) + ".")

def print_pizza_toppings(about_me):
    sentence = "My ideal pizza has "
    for t in range(len(about_me["pizza_toppings"])):
        sentence += about_me["pizza_toppings"][t]

        if t < len(about_me["pizza_toppings"]) - 1:
            sentence += ", "
        else:
            sentence += "."
    print(sentence)  
    
def print_movie_genres(about_me):
    sentence = "I like to watch "
    for t,g in enumerate(about_me["movies"]):
        sentence += g["genre"]

        if t < len(about_me["movies"]) - 1:
            sentence += ", "
        else:
            sentence += " "
    print(sentence + "movies.")

def print_movie_titles(about_me):
    sentence = "Some of my favourites are "
    for t,g in enumerate(about_me["movies"]):
        sentence += g["title"]

        if t < len(about_me["movies"]) - 1:
            sentence += ", "
        else:
            sentence += "!"
    print(sentence)
    
main()